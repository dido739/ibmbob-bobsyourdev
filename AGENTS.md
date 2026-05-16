# AGENTS.md

This file provides guidance to agents when working with code in this repository.

## Critical Python Version Requirement
- **ALWAYS use Python 3.11 explicitly** with `py -3.11` command
- Multiple Python versions may be installed - never use generic `python` or `py` commands
- Backend dependencies: `py -3.11 -m pip install flask flask-cors requests python-dotenv`
- Run backend: `py -3.11 backend/app.py`

## watsonx.ai API Specifics
- Use `/ml/v1/text/chat` endpoint (NOT deprecated `/text/generation`)
- Model ID: `ibm/granite-4-h-small`
- IAM token authentication required (fetch from `https://iam.cloud.ibm.com/identity/token`)
- All agent responses MUST be valid JSON only (no markdown, no explanations)

## Agent Architecture Pattern
- 3 agents run in parallel using `concurrent.futures.ThreadPoolExecutor`
- Each agent has strict JSON response schema (see [`plan.md`](plan.md:254-328))
- Agent files: [`edge_case_agent.py`](backend/agents/edge_case_agent.py), [`security_agent.py`](backend/agents/security_agent.py), [`architect_agent.py`](backend/agents/architect_agent.py)

## IBM Carbon Design System Rules
- **Border radius: 0px** (sharp corners, no rounded edges)
- IBM Plex fonts required (Sans, Mono, Serif from Google Fonts)
- Agent colors: Purple (#BE95FF), Red (#FF8389), Green (#42BE65)
- 8px spacing base unit

## Project Structure Convention
- Backend in `backend/` directory (Flask Python)
- Frontend in `frontend/` directory (React)
- Bob IDE session exports go to `bob_sessions/` directory
- Environment variables in `.env` (never commit API keys)

## Non-Standard Patterns
- Ticket analysis returns 3 separate JSON objects (not unified response)
- Frontend displays real-time agent status with pulse animations during processing
- Complexity estimation uses S/M/L/XL scale (not numeric)

## After each major task
- Export Bob session to bob_sessions/
- Take screenshot of task summary
- Commit with Bob-generated message