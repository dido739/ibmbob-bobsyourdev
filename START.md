# 🚀 BobSpec Getting Started Guide

## Prerequisites
- Python 3.11 installed
- Node.js and npm installed
- IBM watsonx.ai credentials (API Key, Project ID)

---

## 📋 Step 1: Python Virtual Environment Setup

### Create Virtual Environment
```bash
# Create a virtual environment with Python 3.11
py -3.11 -m venv venv
```

### Activate Virtual Environment

**Windows (PowerShell):**
```bash
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```bash
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

You should see `(venv)` appear at the beginning of your command line.

---

## 🔧 Step 2: Credentials Configuration

### Create .env File
```bash
# Copy the template
copy .env.example .env
```

### Edit .env with Your watsonx Credentials
Open `.env` and fill in:
```env
WATSONX_API_KEY=your_api_key_here
WATSONX_PROJECT_ID=your_project_id_here
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-4-h-small
```

---

## 📦 Step 3: Dependencies Installation

### Backend (with activated virtual environment)
```bash
# Make sure virtual environment is activated (venv)
# You should see (venv) at the beginning of your command line

# Install Python dependencies from requirements.txt
pip install -r backend/requirements.txt
```

**⚠️ IMPORTANT:** You MUST install dependencies from `backend/requirements.txt` which contains:
- flask
- flask-cors
- requests
- python-dotenv

### Frontend
```bash
# Navigate to frontend directory
cd frontend

# Install npm dependencies
npm install

# Return to root
cd ..
```

---

## ▶️ Step 4: Start the Project

### Terminal 1 - Backend (Flask)
```bash
# Activate virtual environment if not already done
.\venv\Scripts\Activate.ps1

# Start Flask server on port 5000
python backend/app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

### Terminal 2 - Frontend (React)
```bash
# Navigate to frontend
cd frontend

# Start React development server
npm start
```

Browser will automatically open at `http://localhost:3000`

---

## ✅ Verification

1. **Backend**: Open `http://localhost:5000` in browser
   - You should see a JSON message with available endpoints

2. **Frontend**: Open `http://localhost:3000`
   - You should see the BobSpec interface with ticket input field

---

## 🧪 Quick Test

1. Paste a test ticket in the textarea:
```
Create a user authentication system with email and password.
Users should be able to login, logout, and reset their password.
```

2. Click "Analyze with BobSpec"

3. Watch the 3 agents activate in parallel

4. View results in Edge Cases, Security, Architecture tabs

---

## 🐛 Troubleshooting

### Error "venv not activated"
```bash
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# If execution policy error
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Error "Python not found"
- Check Python 3.11 is installed: `py -3.11 --version`
- Recreate virtual environment: `py -3.11 -m venv venv`

### Error "Module not found"
```bash
# Activate venv then reinstall
.\venv\Scripts\Activate.ps1
pip install --upgrade -r backend/requirements.txt
```

### CORS Error (frontend cannot contact backend)
- Verify Flask-CORS is installed
- Verify backend is running on port 5000
- Check URL in [`App.js`](frontend/src/App.js:45): `http://localhost:5000/api/analyze`

### watsonx.ai Error
- Verify `.env` file exists and contains correct credentials
- Verify `WATSONX_API_KEY` is valid
- Verify `WATSONX_PROJECT_ID` is correct

---

## 📁 Project Structure

```
bobspec/
├── venv/                # Python virtual environment (ignored by git)
├── backend/             # Flask Python 3.11 server
│   ├── app.py          # Entry point
│   ├── routes/         # API routes
│   ├── agents/         # 3 AI agents
│   └── utils/          # watsonx client
│
├── frontend/           # React application
│   ├── src/
│   │   ├── components/ # UI components
│   │   └── styles/     # IBM Carbon CSS
│   └── package.json
│
├── .env                # Configuration (DO NOT COMMIT)
├── .env.example        # Configuration template
└── README.md           # Complete documentation
```

---

## 🎯 Useful Commands

```bash
# Virtual environment
py -3.11 -m venv venv                # Create venv
.\venv\Scripts\Activate.ps1          # Activate (Windows PowerShell)
deactivate                            # Deactivate

# Backend (with venv activated)
python backend/app.py                 # Start Flask server
pip list                              # View installed packages
pip freeze > requirements.txt         # Update requirements.txt

# Frontend
cd frontend
npm start                             # Start React in dev mode
npm run build                         # Build for production
npm test                              # Run tests

# Verifications
py -3.11 --version                   # Python version
python --version                      # Python version (in venv)
node --version                        # Node.js version
npm --version                         # npm version
```

---

## 💡 Best Practices

1. **Always activate virtual environment** before working on backend
2. **Never commit `venv/` directory** (already in .gitignore)
3. **Never commit `.env` file** (contains credentials)
4. **Update `requirements.txt`** after installing new packages
5. **Export Bob sessions** to `bob_sessions/` after each major task

---

**Ready to transform your tickets into complete specifications! 🚀**