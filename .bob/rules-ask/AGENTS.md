# Project Documentation Rules (Non-Obvious Only)

## Project Structure Context
- Planning documents in root: [`plan.md`](../../plan.md) (technical spec), [`visuel_plan.md`](../../visuel_plan.md) (design spec)
- Backend code will be in `backend/` directory (Flask Python 3.11)
- Frontend code will be in `frontend/` directory (React)
- Bob IDE session exports stored in `bob_sessions/` directory

## Architecture Understanding
- 3-agent system: Edge Case Detective, Security Analyst, Architect Blueprint
- Agents run in parallel using `concurrent.futures.ThreadPoolExecutor`
- Each agent returns separate JSON object (not unified response)
- watsonx.ai Granite model (`ibm/granite-4-h-small`) powers all agents

## Non-Standard Patterns
- Python 3.11 MUST be invoked explicitly as `py -3.11` (not `python` or `py`)
- watsonx API uses `/ml/v1/text/chat` endpoint (NOT deprecated `/text/generation`)
- Agent responses are pure JSON only (no markdown formatting allowed)
- Complexity estimation uses S/M/L/XL scale (not numeric days/hours)

## IBM Carbon Design System
- Border radius is 0px (sharp corners, no rounded edges)
- IBM Plex fonts required (Sans, Mono, Serif)
- Agent-specific colors: Purple (#BE95FF), Red (#FF8389), Green (#42BE65)
- 8px spacing base unit throughout UI