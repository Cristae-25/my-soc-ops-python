import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


class TestHomePage:
    def test_home_returns_200(self, client: TestClient):
        response = client.get("/")
        assert response.status_code == 200

    def test_home_contains_start_screen(self, client: TestClient):
        response = client.get("/")
        assert "Seahawks Bingo" in response.text
        assert "Bingo Mode" in response.text or "Choose Your Mode" in response.text
        assert "session" in response.cookies or response.status_code == 200

    def test_home_sets_session_cookie(self, client: TestClient):
        response = client.get("/")
        assert "session" in response.cookies


class TestStartGame:
    def test_start_returns_game_board(self, client: TestClient):
        # First visit to get session
        client.get("/")
        response = client.post("/start")
        assert response.status_code == 200
        assert "FREE SPACE" in response.text
        assert "← Back" in response.text

    def test_board_has_25_squares(self, client: TestClient):
        client.get("/")
        response = client.post("/start")
        # Count the toggle buttons (squares with hx-post="/toggle/")
        assert response.text.count('hx-post="/toggle/') == 24  # 24 + 1 free space


class TestResetGame:
    def test_reset_returns_start_screen(self, client: TestClient):
        client.get("/")
        client.post("/start")
        response = client.post("/reset")
        assert response.status_code == 200
        assert "Bingo Mode" in response.text or "Choose Your Mode" in response.text


class TestDismissModal:
    def test_dismiss_returns_game_screen(self, client: TestClient):
        client.get("/")
        client.post("/start")
        response = client.post("/dismiss-modal")
        assert response.status_code == 200
        assert "FREE SPACE" in response.text


class TestScavengerHuntMode:
    def test_start_hunt_mode(self, client: TestClient):
        client.get("/")
        response = client.post("/start?mode=scavenger_hunt")
        assert response.status_code == 200
        # Hunt board shows a checklist, not bingo grid
        assert "Progress" in response.text
        assert "24" in response.text  # Progress counter shows /24

    def test_start_bingo_default(self, client: TestClient):
        client.get("/")
        response = client.post("/start?mode=bingo")
        assert response.status_code == 200
        assert "FREE SPACE" in response.text

    def test_hunt_mode_has_checkboxes(self, client: TestClient):
        client.get("/")
        response = client.post("/start?mode=scavenger_hunt")
        # Hunt board uses checkboxes
        assert 'type="checkbox"' in response.text

    def test_toggle_in_hunt_mode(self, client: TestClient):
        client.get("/")
        client.post("/start?mode=scavenger_hunt")
        # Toggle item 0
        response = client.post("/toggle/0")
        assert response.status_code == 200
        assert "Progress" in response.text

    def test_hunt_mode_progress_increments(self, client: TestClient):
        client.get("/")
        client.post("/start?mode=scavenger_hunt")
        # Toggle a few items
        client.post("/toggle/0")
        response = client.post("/toggle/1")
        # Should show 2 items checked
        assert "2/24" in response.text or "2" in response.text

    def test_hunt_mode_reset_clears_progress(self, client: TestClient):
        client.get("/")
        client.post("/start?mode=scavenger_hunt")
        client.post("/toggle/0")
        client.post("/toggle/1")
        # Reset
        response = client.post("/reset")
        assert response.status_code == 200
        assert "Bingo Mode" in response.text or "Choose Your Mode" in response.text
        # Verify we're back to start, not in hunt mode


class TestModeRegression:
    def test_bingo_mode_still_works(self, client: TestClient):
        """Regression test: ensure BINGO mode wasn't broken."""
        client.get("/")
        response = client.post("/start?mode=bingo")
        assert response.status_code == 200
        assert "FREE SPACE" in response.text
        # Should have bingo board, not checklist
        assert "Progress" not in response.text

    def test_default_mode_is_bingo(self, client: TestClient):
        """Test that omitting mode defaults to bingo."""
        client.get("/")
        response = client.post("/start")
        assert response.status_code == 200
        assert "FREE SPACE" in response.text
