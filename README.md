# BobSpec — IBM Bob Hackathon 2026

Multi-agent system powered by IBM watsonx.ai that transforms vague development tickets into complete technical specifications.

## Team Bobsyourdev

---

## 📖 What is BobSpec?

BobSpec is an intelligent system that automatically analyzes your development tickets and generates a complete technical specification **before writing a single line of code**.

### 🎯 The Problem

Development tickets are often:
- ❌ Vague and incomplete
- ❌ Missing critical edge cases
- ❌ Ignoring security risks
- ❌ Without defined architecture
- ❌ Causing back-and-forth between dev and PO

### ✨ The BobSpec Solution

BobSpec uses **3 specialized AI agents** working in parallel to analyze your ticket:

1. **🔍 Edge Case Detective** - Identifies all forgotten edge cases
2. **🛡️ Security Analyst** - Detects potential vulnerabilities
3. **🏗️ Architect Blueprint** - Proposes complete technical architecture

### 📥 Input

A simple development ticket, even vague:

```
Create a user authentication system with email and password.
Users should be able to login, logout, and reset their password.
```

### 📤 Output

A complete technical specification with:

**Identified Edge Cases:**
- What happens if the email already exists?
- How to handle multiple failed login attempts?
- What is the reset token expiration policy?
- How to handle invalid or temporary emails?

**Detected Security Risks:**
- Password storage (bcrypt hashing required)
- Protection against brute force attacks
- Input validation and sanitization
- GDPR compliance for personal data
- Reset token security

**Proposed Architecture:**
- Required components (API, database, email service)
- API endpoints to create (`POST /auth/login`, `POST /auth/register`, etc.)
- Step-by-step implementation order
- Complexity estimation (S/M/L/XL)
- Estimated days

### 🎁 What BobSpec Enables

✅ **Zero ambiguity** - All edge cases identified
✅ **Zero surprises** - Security risks anticipated
✅ **Zero spec bugs** - Architecture defined before code
✅ **Time savings** - Fewer back-and-forth with PO
✅ **Increased quality** - Complete and professional specifications

### ⚡ How It Works

```
1. Paste your ticket → Simple web interface
2. BobSpec analyzes → 3 AI agents in parallel (watsonx.ai Granite)
3. Get the spec → Real-time results with animations
4. Export → Markdown format ready to share
```

**Average analysis time:** 10-30 seconds
**Technology:** IBM watsonx.ai (Granite 4H Small model)
**Parallel agents:** Simultaneous execution for maximum speed

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11
- Node.js & npm
- IBM watsonx.ai API credentials

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install dependencies (MUST use Python 3.11)
py -3.11 -m pip install -r requirements.txt

# Configure environment variables
copy .env.example .env
# Edit .env and add your watsonx credentials

# Run backend server
py -3.11 app.py
```

Backend will run on `http://localhost:5000`

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

Frontend will run on `http://localhost:3000`

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│           USER (Dev / PO)               │
└──────────────────┬──────────────────────┘
                   │ ticket text
                   ▼
┌─────────────────────────────────────────┐
│         FRONTEND — React.js             │
│  • IBM Carbon Design System             │
│  • Real-time agent status display       │
└──────────────────┬──────────────────────┘
                   │ POST /api/analyze
                   ▼
┌─────────────────────────────────────────┐
│         BACKEND — Flask (Python 3.11)   │
│  • 3 parallel agents via ThreadPool     │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│        watsonx.ai Granite               │
│        ibm/granite-4-h-small            │
└─────────────────────────────────────────┘
```

---

## 🤖 The 3 Agents

### 1. Edge Case Detective 🔍
- Identifies missing edge cases
- Generates questions for Product Owner
- Criticality levels: LOW / MEDIUM / HIGH / CRITICAL

### 2. Security Analyst 🛡️
- Detects security vulnerabilities
- Maps to compliance standards (OWASP, GDPR, PCI-DSS)
- Provides mitigation strategies

### 3. Architect Blueprint 🏗️
- Proposes technical architecture
- Estimates complexity (S/M/L/XL)
- Creates implementation roadmap

---

## 📁 Project Structure

```
bobspec/
├── backend/
│   ├── app.py                 # Flask application
│   ├── requirements.txt       # Python dependencies
│   ├── routes/
│   │   └── analyze.py        # API endpoint
│   ├── agents/
│   │   ├── edge_case_agent.py
│   │   ├── security_agent.py
│   │   └── architect_agent.py
│   └── utils/
│       └── watsonx_client.py # watsonx.ai integration
│
├── frontend/
│   ├── package.json
│   └── src/
│       ├── App.jsx
│       └── components/
│
├── bob_sessions/             # Bob IDE exports
│   ├── screenshots/
│   └── exports/
│
├── .env.example              # Environment template
└── AGENTS.md                 # AI assistant rules
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
WATSONX_API_KEY=your_api_key_here
WATSONX_PROJECT_ID=your_project_id_here
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-4-h-small
```

---

## 🎨 Design System

- **IBM Carbon Design System**
- **Border radius:** 0px (sharp corners)
- **Fonts:** IBM Plex Sans, Mono, Serif
- **Agent colors:**
  - Edge Case: Purple (#BE95FF)
  - Security: Red (#FF8389)
  - Architect: Green (#42BE65)

---

## 📡 API Endpoints

### POST `/api/analyze`

Analyze a development ticket with 3 parallel agents.

**Request:**
```json
{
  "ticket": "Create a user authentication system..."
}
```

**Response:**
```json
{
  "edge_cases": {
    "edge_cases": [...]
  },
  "security": {
    "security_risks": [...]
  },
  "architecture": {
    "architecture": {...}
  }
}
```

---

## ⚠️ Important Notes

1. **Always use Python 3.11 explicitly:** `py -3.11`
2. **Never commit `.env` file** (contains API keys)
3. **Agent responses are pure JSON** (no markdown)
4. **Export Bob sessions** after major tasks to `bob_sessions/`

---

## 🛠️ Development

### Running Tests
```bash
# Backend tests (when implemented)
cd backend
py -3.11 -m pytest

# Frontend tests
cd frontend
npm test
```

### Building for Production
```bash
# Frontend build
cd frontend
npm run build
```

---

## 📝 License

IBM Bob Hackathon 2026 Project

---

**Built with ❤️ by Team Bobsyourdev**