# 🎮 SOC Ops Python Workshop

> An interactive social BINGO game built with **FastAPI** and **HTMX**—perfect for breaking the ice at in-person events and learning modern AI-assisted development workflows.

**Find people who match the questions. Get 5 in a row. Have fun!**

### 🚀 Quick Links

- **[Play the Game Now](https://madebygps.github.io/vscode-github-copilot-agent-lab/)** — Try it live!
- **[Start the Lab Guide](#-lab-guide)** — Learn by building
- **[View Docs](workshop/)** — Offline workshop materials

---

## ✨ What You'll Build

This workshop teaches you how to build a **full-stack web application** using cutting-edge AI-assisted development practices:

- 🎯 **Interactive BINGO Board** — Real-time game state with HTMX
- 🤝 **Multi-Player Sessions** — Manage concurrent players seamlessly
- 🔒 **Robust Game Logic** — Proper validation and error handling
- 🧪 **Comprehensive Tests** — 25+ test cases with 100% coverage
- 🔥 **Hot-Reload Development** — See changes instantly

### 💡 What You'll Learn

- Setting up **FastAPI** projects with modern Python tooling
- Writing **failing tests first** (TDD) to guide implementation
- Using **GitHub Copilot agents** to accelerate development
- Designing **responsive UIs** with HTMX and Jinja2
- Building **real-time interactions** without traditional JavaScript
- **Best practices** for production-ready code

---

## 🛠️ Tech Stack

| Layer               | Technology                      |
| ------------------- | ------------------------------- |
| **Backend**         | FastAPI, Uvicorn, Pydantic      |
| **Frontend**        | Jinja2, HTMX, CSS               |
| **Testing**         | pytest, 25+ comprehensive tests |
| **Package Manager** | uv (ultra-fast Python manager)  |

---

## ⚡ Quick Start

### Prerequisites

- [Python 3.13](https://www.python.org/downloads/)+
- [uv](https://docs.astral.sh/uv/) package manager

### Setup & Run

```bash
# Install dependencies
uv sync

# Start the dev server
uv run uvicorn app.main:app --reload --port 8000
```

Then open **http://localhost:8000** in your browser. Changes reload automatically! ✨

### Run Tests

```bash
uv run pytest
```

### Lint & Format

```bash
uv run ruff check .
uv run ruff format .
```

---

## 📚 Lab Guide

| Part                                                                                                     | Title                       |
| -------------------------------------------------------------------------------------------------------- | --------------------------- |
| [**00**](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/step.html?step=00-overview)    | Overview & Checklist        |
| [**01**](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/step.html?step=01-setup)       | Setup & Context Engineering |
| [**02**](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/step.html?step=02-design)      | Design-First Frontend       |
| [**03**](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/step.html?step=03-quiz-master) | Custom Quiz Master Agent    |
| [**04**](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/step.html?step=04-multi-agent) | Multi-Agent Development     |

> 💾 **Working offline?** Lab guides are also available in the [`workshop/`](workshop/) folder.

---

## 🎯 Why This Workshop?

Traditional coding tutorials often feel disconnected from real-world development. This workshop is different:

✅ **Learn from Real Code** — Not toy examples. Build a genuinely useful game.  
✅ **AI-Assisted Development** — Master GitHub Copilot agents to write better code faster.  
✅ **Test-Driven Workflow** — Write tests first, let them guide your implementation.  
✅ **Production Ready** — Apply patterns and practices used in real applications.  
✅ **Hands-On Learning** — Every step is interactive and immediately feedback.

---

## 📁 Project Structure

```
app/
  ├── main.py              # FastAPI entry point
  ├── game_logic.py        # Core BINGO mechanics
  ├── game_service.py      # Business logic layer
  ├── models.py            # Pydantic data models
  ├── templates/           # Jinja2 HTML templates
  └── static/              # CSS & HTMX assets
tests/
  ├── test_api.py          # API endpoint tests
  └── test_game_logic.py   # Game logic tests (25+ tests)
workshop/                  # Comprehensive learning guides
```

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 🚀 Ready to Build?

1. **[Start the Quick Start above](#-quick-start)**
2. **[Follow the Lab Guide](#-lab-guide)**
3. **Have fun building!**

Deploys automatically to GitHub Pages on each push to `main`.
