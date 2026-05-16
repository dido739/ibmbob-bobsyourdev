# 🔧 BobSpec Troubleshooting Guide

## Problem: Application Returns No Results

### Diagnosis

If the application is not working properly, it may be due to:

1. **watsonx.ai Connection Issue** - Invalid credentials or API is unreachable
2. **Configuration Problem** - `.env` file is misconfigured
3. **Network Issue** - Unable to contact IBM API

### Solution: Test Mode with Mock Data

BobSpec includes a **test mode** that uses sample data instead of the watsonx.ai API. This allows testing the application even without valid credentials.

#### Enable Test Mode

Edit the `.env` file and change:

```env
USE_MOCK_DATA=true
```

Instead of:

```env
USE_MOCK_DATA=false
```

#### Restart Backend

```bash
# Stop the server (CTRL+C)
# Then restart
.\venv\Scripts\Activate.ps1
python backend/app.py
```

### Behavior in Test Mode

With `USE_MOCK_DATA=true`, the 3 agents return realistic sample data:

**Edge Case Agent** returns 4 edge cases:
- Email already exists
- Multiple failed login attempts
- Expired token
- Temporary email

**Security Agent** returns 5 risks:
- Plain text password storage
- Brute force attacks
- SQL injection
- Unsecured tokens
- GDPR non-compliance

**Architect Agent** returns:
- 5 technical components
- 7 API endpoints
- 10 implementation steps
- Complexity: L (Large)
- Estimation: 8 days

### Behavior in Production Mode

With `USE_MOCK_DATA=false`, agents use watsonx.ai:

- If API works → Real AI results
- If API fails → Automatic fallback to mock data

**Advantage**: Application always works, even with API issues!

---

## watsonx.ai Credentials Verification

### Required .env File

```env
WATSONX_API_KEY=your_api_key_here
WATSONX_PROJECT_ID=your_project_id_here
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-4-h-small
USE_MOCK_DATA=false
```

### Test Credentials

```bash
# Activate venv
.\venv\Scripts\Activate.ps1

# Test connection
python -c "from backend.utils.watsonx_client import get_iam_token; print(get_iam_token())"
```

If this displays a token, your credentials are valid.

---

## Common Issues

### 1. Backend Won't Start

**Error**: `ModuleNotFoundError: No module named 'flask'`

**Solution**:
```bash
.\venv\Scripts\Activate.ps1
pip install -r backend/requirements.txt
```

### 2. Frontend Cannot Connect to Backend

**Error**: `CORS error` or `Network error`

**Checks**:
- Backend running on http://localhost:5000
- Frontend running on http://localhost:3000
- Flask-CORS is installed

**Solution**:
```bash
pip install flask-cors
```

### 3. Agents Return Empty Errors

**Symptom**: Agent cards display but without results

**Solution**: Enable test mode
```env
USE_MOCK_DATA=true
```

### 4. Error "Python not found"

**Solution**: Use Python 3.11 explicitly
```bash
py -3.11 -m venv venv
```

---

## Debug Logs

Agents display messages in backend console:

```
🔧 Using mock data for Edge Case Agent
🔧 Using mock data for Security Agent  
🔧 Using mock data for Architect Agent
```

Or in case of error:

```
⚠️ JSON parse error, falling back to mock data: ...
⚠️ Agent error, falling back to mock data: ...
```

---

## Recommended Mode for Hackathon

For hackathon demo, we recommend:

```env
USE_MOCK_DATA=true
```

**Why?**
- ✅ Instant results (no API wait)
- ✅ No network dependency
- ✅ Consistent and impressive data
- ✅ Zero risk of API quota exceeded

You can still show watsonx.ai integration works by changing to `false` during demo.

---

## Support

If problem persists:

1. Check backend logs (terminal 1)
2. Check browser console (F12)
3. Test with `USE_MOCK_DATA=true`
4. Consult [`START.md`](START.md) for complete guide

---

**BobSpec - Team Bobsyourdev | IBM Bob Hackathon 2026**