# BobSpec — IBM Bob Hackathon 2026

Multi-agent system powered by IBM watsonx.ai that transforms vague development tickets into complete technical specifications.

## Team Bobsyourdev

---

## 📖 Qu'est-ce que BobSpec ?

BobSpec est un système intelligent qui analyse automatiquement vos tickets de développement et génère une spécification technique complète **avant même d'écrire une seule ligne de code**.

### 🎯 Le Problème

Les tickets de développement sont souvent :
- ❌ Vagues et incomplets
- ❌ Manquent de cas limites critiques
- ❌ Ignorent les risques de sécurité
- ❌ N'ont pas d'architecture définie
- ❌ Causent des allers-retours entre dev et PO

### ✨ La Solution BobSpec

BobSpec utilise **3 agents IA spécialisés** qui travaillent en parallèle pour analyser votre ticket :

1. **🔍 Edge Case Detective** - Identifie tous les cas limites oubliés
2. **🛡️ Security Analyst** - Détecte les vulnérabilités potentielles
3. **🏗️ Architect Blueprint** - Propose une architecture technique complète

### 📥 Entrée (Input)

Un ticket de développement simple, même vague :

```
Créer un système d'authentification utilisateur avec email et mot de passe.
Les utilisateurs doivent pouvoir se connecter, se déconnecter et réinitialiser leur mot de passe.
```

### 📤 Sortie (Output)

Une spécification technique complète avec :

**Edge Cases identifiés :**
- Que se passe-t-il si l'email existe déjà ?
- Comment gérer les tentatives de connexion multiples échouées ?
- Quelle est la politique d'expiration des tokens de réinitialisation ?
- Comment traiter les emails invalides ou temporaires ?

**Risques de sécurité détectés :**
- Stockage des mots de passe (hashing bcrypt requis)
- Protection contre les attaques par force brute
- Validation et sanitisation des entrées
- Conformité RGPD pour les données personnelles
- Sécurisation des tokens de réinitialisation

**Architecture proposée :**
- Composants nécessaires (API, base de données, service email)
- Endpoints API à créer (`POST /auth/login`, `POST /auth/register`, etc.)
- Ordre d'implémentation étape par étape
- Estimation de complexité (S/M/L/XL)
- Nombre de jours estimés

### 🎁 Ce que BobSpec vous permet

✅ **Zéro ambiguïté** - Tous les cas limites sont identifiés
✅ **Zéro surprise** - Les risques de sécurité sont anticipés
✅ **Zéro bug de spec** - L'architecture est définie avant le code
✅ **Gain de temps** - Moins d'allers-retours avec le PO
✅ **Qualité accrue** - Spécifications complètes et professionnelles

### ⚡ Comment ça fonctionne

```
1. Vous collez votre ticket → Interface web simple
2. BobSpec analyse → 3 agents IA en parallèle (watsonx.ai Granite)
3. Vous obtenez la spec → Résultats en temps réel avec animations
4. Vous exportez → Format Markdown prêt à partager
```

**Temps d'analyse moyen :** 10-30 secondes
**Technologie :** IBM watsonx.ai (modèle Granite 4H Small)
**Agents parallèles :** Exécution simultanée pour rapidité maximale

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