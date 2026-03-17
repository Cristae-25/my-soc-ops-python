---
applyTo: "**"
---

# Workspace Instructions

## ✅ Mandatory Development Checklist

Before committing or requesting review, complete these steps in order:

```bash
uv run ruff check .      # Lint code (fix issues: ruff check . --fix)
uv run pytest            # Run tests (must pass 100%)
uv run uvicorn app.main:app --reload --port 8000  # Verify build runs
```

---

## Project Overview

**SOC Ops Python Workshop** — An interactive BINGO game built with FastAPI and HTMX.

### Tech Stack

- **Backend:** FastAPI, Uvicorn, Pydantic
- **Frontend:** Jinja2, HTMX, CSS
- **Testing:** pytest
- **Package Manager:** uv

### Directory Structure

```
app/
  ├── main.py           # FastAPI entry point
  ├── game_logic.py     # Core bingo mechanics
  ├── game_service.py   # Game service layer
  ├── models.py         # Pydantic models
  ├── templates/        # Jinja2 templates
  └── static/           # CSS, JS assets
tests/                  # Test suite (25 tests)
workshop/              # Learning guides
```

## Development Workflow

**Start Dev Server:**

```bash
uv run uvicorn app.main:app --reload --port 8000
```

Access at http://localhost:8000

**Run Tests:**

```bash
uv run pytest                    # Run all tests
uv run pytest tests/test_api.py  # Run specific test file
```

**Lint & Format:**

```bash
uv run ruff check .        # Check code
uv run ruff check . --fix  # Auto-fix issues
```

## Key Features

- Interactive BINGO board with HTMX real-time updates
- Multi-player game session management
- Robust game state handling with proper validation
- Comprehensive test suite (api + game logic)
- Hot-reload development server

## Important Notes

- Do NOT use VS Code Simple Browser—requires a full browser for HTMX
- Hot-reload enabled: changes auto-reflect without restart
- Use `open http://localhost:8000` to launch in default browser
