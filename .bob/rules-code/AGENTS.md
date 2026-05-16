# Project Coding Rules (Non-Obvious Only)

## Critical Python Version
- MUST use `py -3.11` explicitly (never `python` or `py` alone)
- Multiple Python versions installed - generic commands will fail

## watsonx.ai Integration
- Agent responses MUST be pure JSON (no markdown wrappers, no explanations)
- Use `/ml/v1/text/chat` endpoint (NOT `/text/generation`)
- IAM token must be fetched before each API call from `https://iam.cloud.ibm.com/identity/token`
- Model ID is `ibm/granite-4-h-small` (not configurable per agent)

## Agent Implementation Pattern
- All 3 agents run in parallel via `concurrent.futures.ThreadPoolExecutor`
- Each agent file must implement `run_*_agent(ticket: str) -> dict` function
- Response schema is strict - see [`plan.md`](../../plan.md:254-328) for exact JSON structure
- No unified response object - 3 separate JSON objects returned

## Backend Structure
- Flask routes in `backend/routes/` (not root-level routes)
- watsonx client utilities in `backend/utils/watsonx_client.py`
- Agent logic separated into individual files in `backend/agents/`

## Environment Variables
- `.env` file required (never commit)
- Must include: `WATSONX_API_KEY`, `WATSONX_PROJECT_ID`, `WATSONX_URL`, `WATSONX_MODEL_ID`

## No Access to MCP and Browser Tools
- Code mode cannot use MCP servers or browser automation
- Use standard file operations and command execution only