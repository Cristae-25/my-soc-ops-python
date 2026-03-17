from dataclasses import dataclass, field

from app.game_logic import (
    check_bingo,
    check_hunt_complete,
    generate_board,
    get_winning_square_ids,
    toggle_square,
)
from app.models import BingoLine, BingoSquareData, GameMode, GameState


@dataclass
class GameSession:
    """Holds the state for a single game session."""

    game_state: GameState = GameState.START
    board: list[BingoSquareData] = field(default_factory=list)
    winning_line: BingoLine | None = None
    show_bingo_modal: bool = False
    mode: GameMode = GameMode.BINGO
    checked_items: set[int] = field(default_factory=set)

    @property
    def winning_square_ids(self) -> set[int]:
        return get_winning_square_ids(self.winning_line)

    @property
    def has_bingo(self) -> bool:
        return self.game_state == GameState.BINGO

    @property
    def hunt_progress(self) -> float:
        """Return hunt progress as a percentage (0-100)."""
        return (len(self.checked_items) / 24) * 100

    def start_game(self, mode: GameMode = GameMode.BINGO) -> None:
        self.mode = mode
        self.board = generate_board()
        self.winning_line = None
        self.game_state = GameState.PLAYING
        self.show_bingo_modal = False
        self.checked_items = set()

    def handle_square_click(self, square_id: int) -> None:
        if self.game_state != GameState.PLAYING:
            return

        if self.mode == GameMode.BINGO:
            self._handle_bingo_click(square_id)
        elif self.mode == GameMode.SCAVENGER_HUNT:
            self._handle_hunt_click(square_id)

    def _handle_bingo_click(self, square_id: int) -> None:
        """Handle a square click in BINGO mode."""
        self.board = toggle_square(self.board, square_id)

        if self.winning_line is None:
            bingo = check_bingo(self.board)
            if bingo is not None:
                self.winning_line = bingo
                self.game_state = GameState.BINGO
                self.show_bingo_modal = True

    def _handle_hunt_click(self, square_id: int) -> None:
        """Handle an item toggle in Scavenger Hunt mode."""
        # Toggle the item in checked_items
        if square_id in self.checked_items:
            self.checked_items.remove(square_id)
        else:
            self.checked_items.add(square_id)

        # Check if hunt is complete
        if check_hunt_complete(self.checked_items):
            self.game_state = GameState.BINGO
            self.show_bingo_modal = True

    def reset_game(self) -> None:
        self.game_state = GameState.START
        self.board = []
        self.winning_line = None
        self.show_bingo_modal = False
        self.mode = GameMode.BINGO
        self.checked_items = set()

    def dismiss_modal(self) -> None:
        self.show_bingo_modal = False
        self.game_state = GameState.PLAYING


# In-memory session store keyed by session ID
_sessions: dict[str, GameSession] = {}


def get_session(session_id: str) -> GameSession:
    """Get or create a game session for the given session ID."""
    if session_id not in _sessions:
        _sessions[session_id] = GameSession()
    return _sessions[session_id]
