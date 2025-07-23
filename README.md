# QualGent Multi-Agent QA System

This project implements a multi-agent LLM-based QA pipeline using the Agent-S architecture. It currently uses a mock environment to simulate Android UI behavior.

## Agents

- **Planner Agent** – Parses high-level QA goals and decomposes them into subgoals. Currently supports Wi-Fi toggling via mock environment.
- **Executor Agent** – Executes subgoals by inspecting the UI hierarchy and simulating UI interactions (e.g., tapping, waiting). Screenshots are saved to `logs/mock/`.
- **Verifier Agent** – Determines whether the app behaves as expected after each step using string matching and state detection.

## Setup

This project uses a Python 3.12 virtual environment (`venv/`).

To install dependencies:

```bash
pip install -r agent_s/requirements.txt
pip install -e agent_s
```

>  Python 3.13 is not supported due to version constraints in dependencies.

## Logs

Screenshots and results are saved to:

```
logs/mock/
├── step_1.png
├── step_2.png
└── ...
```

## Project Requirements Checklist

- [x] Clone and extend the Agent-S architecture
- [x] Implement Planner Agent
- [x] Implement Executor Agent with mock environment
- [x] Implement Verifier Agent with UI validation and state tracking

---

Youssef Amin – 2025
