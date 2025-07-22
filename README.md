# QualGent Multi-Agent QA System

This project implements a multi-agent LLM-based QA pipeline using the Agent-S architecture on AndroidEnv.

## Agents
- **Planner Agent** – Translates user prompts into subgoals.
- **Executor Agent** – Executes UI actions based on subgoals.
- **Verifier Agent** – Checks app behavior after each step.
- **Supervisor Agent** – Reviews whole test episodes and suggests improvements.

## Running
```bash
python main.py

## Setup

This project uses a Python 3.12 virtual environment (`venv/`).

## Next Steps

1. Executor agent 
2. Creating test flow  Planner -> Executor -> Verifier
3. Log everything into 'logs/'
4. screenshots