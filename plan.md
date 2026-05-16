# BobSpec — Development Plan
### IBM Bob Hackathon 2026 | Team Bobsyourdev

---

## What is BobSpec?

BobSpec is a multi-agent system powered by IBM Bob and watsonx Orchestrate.
It transforms a vague development ticket into a complete technical specification
before any developer writes a single line of code.

> "Zero ambiguity. Zero surprises. Zero specification bugs."

---

## How it works

```
INPUT  → User pastes a vague ticket (plain text)
         ↓
PROCESS → 3 AI agents activate simultaneously via watsonx Orchestrate:
         → Agent 1 - Edge Case Detective : finds missing edge cases
         → Agent 2 - Security Analyst   : detects security risks
         → Agent 3 - Architect Blueprint: proposes technical architecture
         ↓
OUTPUT → Complete structured specification document
         → Edge cases list with questions for the PO
         → Security checklist
         → Architecture blueprint
         → Complexity estimate (S/M/L/XL)
         → Step-by-step implementation plan
```

---

## Architecture

```
┌─────────────────────────────────────────┐
│           USER (Dev / PO)               │
└──────────────────┬──────────────────────┘
                   │ ticket text
                   ▼
┌─────────────────────────────────────────┐
│         FRONTEND — React.js             │
│  • Ticket input field                   │
│  • Real-time agent status display       │
│  • Final specification dashboard        │
│  • Markdown export                      │
└──────────────────┬──────────────────────┘
                   │ POST /api/analyze
                   ▼
┌─────────────────────────────────────────┐
│         BACKEND — Flask (Python 3.11)   │
│  • POST /api/analyze route              │
│  • Calls 3 agents in parallel threads   │
│  • Aggregates results                   │
│  • Returns structured JSON              │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│        watsonx Orchestrate              │
│        (multi-agent orchestrator)       │
└──────┬───────────┬──────────────┬───────┘
       ▼           ▼              ▼
  [Agent 1]   [Agent 2]      [Agent 3]
  Edge Case   Security       Architect
       \           |              /
        └──────────┴──────────────┘
                   │
          watsonx.ai Granite
          ibm/granite-4-h-small
```

---

## Project Structure

```
bobspec/
│
├── README.md
├── PLAN.md
├── .env.example
├── .gitignore
│
├── bob_sessions/
│   ├── screenshots/
│   └── exports/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── routes/
│   │   └── analyze.py
│   ├── agents/
│   │   ├── edge_case_agent.py
│   │   ├── security_agent.py
│   │   └── architect_agent.py
│   └── utils/
│       ├── watsonx_client.py
│       └── response_formatter.py
│
└── frontend/
    ├── package.json
    └── src/
        ├── App.jsx
        ├── components/
        │   ├── TicketInput.jsx
        │   ├── AgentCard.jsx
        │   ├── SpecOutput.jsx
        │   └── ExportButton.jsx
        └── styles/
            └── main.css
```

---

## Tech Stack

### Backend
- **Python 3.11** (use py311 explicitly — other versions may be installed)
- Flask
- Flask-CORS
- Requests
- python-dotenv
- concurrent.futures (parallel agent calls)

### Frontend
- **React.js**
- CSS Animations / Keyframes
- Fetch API

### IBM Stack
- IBM Bob IDE (core — used to build this project)
- watsonx Orchestrate (agent orchestration)
- watsonx.ai — model: `ibm/granite-4-h-small`

---

## Environment Variables (.env)

```
WATSONX_API_KEY=your_api_key_here
WATSONX_PROJECT_ID=your_project_id_here
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-4-h-small
```

---

## Backend Implementation

### `backend/app.py`

```python
from flask import Flask
from flask_cors import CORS
from routes.analyze import analyze_bp

app = Flask(__name__)
CORS(app)
app.register_blueprint(analyze_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

### `backend/routes/analyze.py`

```python
from flask import Blueprint, request, jsonify
from agents.edge_case_agent import run_edge_case_agent
from agents.security_agent import run_security_agent
from agents.architect_agent import run_architect_agent
import concurrent.futures

analyze_bp = Blueprint('analyze', __name__)

@analyze_bp.route('/analyze', methods=['POST'])
def analyze_ticket():
    data = request.get_json()
    ticket = data.get('ticket', '')

    if not ticket:
        return jsonify({'error': 'Empty ticket'}), 400

    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(run_edge_case_agent, ticket)
        f2 = executor.submit(run_security_agent, ticket)
        f3 = executor.submit(run_architect_agent, ticket)

    results = {
        'edge_cases':   f1.result(),
        'security':     f2.result(),
        'architecture': f3.result()
    }

    return jsonify(results), 200
```

### `backend/utils/watsonx_client.py`

```python
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_iam_token():
    url = "https://iam.cloud.ibm.com/identity/token"
    data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": os.getenv("WATSONX_API_KEY")
    }
    response = requests.post(url, data=data)
    return response.json()["access_token"]

def call_granite(system_prompt: str, user_message: str) -> str:
    token = get_iam_token()
    url = f"{os.getenv('WATSONX_URL')}/ml/v1/text/chat?version=2023-05-29"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "model_id": os.getenv("WATSONX_MODEL_ID"),
        "project_id": os.getenv("WATSONX_PROJECT_ID"),
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_message}
        ],
        "parameters": {
            "max_new_tokens": 1000,
            "temperature": 0.3
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()['choices'][0]['message']['content']
```

---

## The 3 Agents

### Agent 1 — Edge Case Detective
**File:** `backend/agents/edge_case_agent.py`

**System prompt:**
```
You are a senior developer with 15 years of experience.
Your role is to identify ALL edge cases the Product Owner forgot to mention.

For each edge case found, return:
- scenario: description of the edge case
- criticality: LOW / MEDIUM / HIGH / CRITICAL
- question_for_po: the question to ask the PO

Respond ONLY in valid JSON format:
{
  "edge_cases": [
    {
      "scenario": "...",
      "criticality": "HIGH",
      "question_for_po": "..."
    }
  ]
}
```

### Agent 2 — Security Analyst
**File:** `backend/agents/security_agent.py`

**System prompt:**
```
You are a cybersecurity expert and compliance specialist.
Analyze this development ticket and identify all potential security risks.

For each risk, return:
- vulnerability: what the risk is
- risk_level: LOW / MEDIUM / HIGH / CRITICAL
- standard: applicable standard (OWASP, GDPR, PCI-DSS...)
- mitigation: how to fix it

Respond ONLY in valid JSON format:
{
  "security_risks": [
    {
      "vulnerability": "...",
      "risk_level": "CRITICAL",
      "standard": "PCI-DSS",
      "mitigation": "..."
    }
  ]
}
```

### Agent 3 — Architect Blueprint
**File:** `backend/agents/architect_agent.py`

**System prompt:**
```
You are a senior software architect.
Analyze this ticket and propose a concrete technical architecture.

Return:
- components: list of required components
- complexity: S / M / L / XL
- endpoints: API endpoints to create
- implementation_order: ordered steps to implement
- estimated_days: number of days to implement

Respond ONLY in valid JSON format:
{
  "architecture": {
    "components": ["..."],
    "complexity": "L",
    "endpoints": ["..."],
    "implementation_order": ["..."],
    "estimated_days": 5
  }
}
```

---

## Frontend — React Components

### `TicketInput.jsx`
- Textarea to paste the ticket
- "Analyze with BobSpec" button
- Loading spinner during analysis

### `AgentCard.jsx`
- Visual card per agent with pulse animation on activation
- Colors: Edge Case = Blue / Security = Red / Architect = Green
- Shows results when agent finishes

### `SpecOutput.jsx`
- Final complete specification
- Collapsible sections per category
- Complexity badge (S/M/L/XL)
- Interactive checklist

### `ExportButton.jsx`
- Export as Markdown
- Copy to clipboard

### Design Guidelines
- Dark theme, dark blue tones + cyan accents
- CSS keyframe animations for agent activation effect
- Animated gradient background + subtle grid overlay
- Fonts: JetBrains Mono (headings) + IBM Plex Sans (body)

---

## Python Version

> ⚠️ IMPORTANT: Always use **Python 3.11** explicitly.
> Multiple Python versions may be installed on the machine.

```bash
# Install dependencies with py311
py -3.11 -m pip install flask flask-cors requests python-dotenv

# Run the backend with py311
py -3.11 backend/app.py
```

---

## Install & Run

```bash
# 1. Clone the repo
git clone https://github.com/bobsyourdev/bobspec.git
cd bobspec

# 2. Backend setup (Python 3.11)
cd backend
py -3.11 -m pip install -r requirements.txt
copy .env.example .env
# Fill in your credentials in .env
py -3.11 app.py

# 3. Frontend setup
cd ../frontend
npm install
npm start
```

---

## Requirements (backend/requirements.txt)

```
flask
flask-cors
requests
python-dotenv
```

---

## Key Rules for Development

1. Use **Python 3.11** for all backend code
2. Use **React** for all frontend code
3. Never hardcode API keys — always use `.env`
4. All 3 agents must return **valid JSON only**
5. Use **concurrent.futures** for parallel agent calls
6. Use the `/ml/v1/text/chat` API endpoint (not deprecated `/text/generation`)
7. Model: `ibm/granite-4-h-small`
8. Export Bob IDE sessions to `bob_sessions/` after every major task

---

*BobSpec — Team Bobsyourdev | IBM Bob Hackathon 2026*
