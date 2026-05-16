# Project Architecture Rules (Non-Obvious Only)

## Multi-Agent Orchestration Pattern
- 3 agents execute in parallel (NOT sequential) via `concurrent.futures.ThreadPoolExecutor`
- Each agent returns independent JSON object - no unified response aggregation
- Agent responses MUST be pure JSON (watsonx.ai requirement - no markdown allowed)
- Response schemas are strictly defined in [`plan.md`](../../plan.md:254-328)

## watsonx.ai Integration Constraints
- IAM token must be fetched fresh before EACH API call (no token caching)
- Endpoint is `/ml/v1/text/chat` (deprecated `/text/generation` will fail)
- Model `ibm/granite-4-h-small` is fixed (not configurable per agent)
- Token fetch URL: `https://iam.cloud.ibm.com/identity/token`

## Backend Architecture
- Flask routes in `backend/routes/` subdirectory (not root-level)
- Agent logic isolated in separate files: `backend/agents/{edge_case,security,architect}_agent.py`
- watsonx client utilities centralized in `backend/utils/watsonx_client.py`
- Each agent implements `run_*_agent(ticket: str) -> dict` signature

## Frontend Architecture
- Real-time agent status display with pulse animations during processing
- Agent-specific color coding: Purple (Edge Case), Red (Security), Green (Architect)
- IBM Carbon Design System: 0px border-radius, 8px spacing base unit
- Complexity displayed as S/M/L/XL badges (not numeric estimates)

## Critical Python Version Constraint
- Python 3.11 MUST be invoked as `py -3.11` (multiple versions installed)
- Generic `python` or `py` commands will use wrong version and fail