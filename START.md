# 🚀 Guide de Démarrage BobSpec

## Prérequis
- Python 3.11 installé
- Node.js et npm installés
- Credentials IBM watsonx.ai (API Key, Project ID)

---

## 📋 Étape 1 : Configuration de l'environnement virtuel Python

### Créer l'environnement virtuel
```bash
# Créer un environnement virtuel avec Python 3.11
py -3.11 -m venv venv
```

### Activer l'environnement virtuel

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

Vous devriez voir `(venv)` apparaître au début de votre ligne de commande.

---

## 🔧 Étape 2 : Configuration des credentials

### Créer le fichier .env
```bash
# Copier le template
copy .env.example .env
```

### Éditer .env avec vos credentials watsonx
Ouvrir `.env` et remplir :
```env
WATSONX_API_KEY=votre_api_key_ici
WATSONX_PROJECT_ID=votre_project_id_ici
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-4-h-small
```

---

## 📦 Étape 3 : Installation des dépendances

### Backend (avec environnement virtuel activé)
```bash
# S'assurer que l'environnement virtuel est activé (venv)
# Vous devriez voir (venv) au début de votre ligne de commande

# Installer les dépendances Python depuis requirements.txt
pip install -r backend/requirements.txt
```

**⚠️ IMPORTANT:** Vous DEVEZ installer les dépendances depuis `backend/requirements.txt` qui contient :
- flask
- flask-cors
- requests
- python-dotenv

### Frontend
```bash
# Aller dans le dossier frontend
cd frontend

# Installer les dépendances npm
npm install

# Retourner à la racine
cd ..
```

---

## ▶️ Étape 4 : Démarrer le projet

### Terminal 1 - Backend (Flask)
```bash
# Activer l'environnement virtuel si pas déjà fait
.\venv\Scripts\Activate.ps1

# Lancer le serveur Flask sur le port 5000
python backend/app.py
```

Vous devriez voir :
```
 * Running on http://127.0.0.1:5000
```

### Terminal 2 - Frontend (React)
```bash
# Aller dans frontend
cd frontend

# Lancer le serveur de développement React
npm start
```

Le navigateur s'ouvrira automatiquement sur `http://localhost:3000`

---

## ✅ Vérification

1. **Backend** : Ouvrir `http://localhost:5000` dans le navigateur
   - Vous devriez voir un message JSON avec les endpoints disponibles

2. **Frontend** : Ouvrir `http://localhost:3000`
   - Vous devriez voir l'interface BobSpec avec le champ de saisie du ticket

---

## 🧪 Test rapide

1. Coller un ticket de test dans le textarea :
```
Créer un système d'authentification utilisateur avec email et mot de passe.
Les utilisateurs doivent pouvoir se connecter, se déconnecter et réinitialiser leur mot de passe.
```

2. Cliquer sur "Analyze with BobSpec"

3. Observer les 3 agents s'activer en parallèle

4. Consulter les résultats dans les onglets Edge Cases, Security, Architecture

---

## 🐛 Dépannage

### Erreur "venv not activated"
```bash
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Si erreur de politique d'exécution
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Erreur "Python not found"
- Vérifier que Python 3.11 est installé : `py -3.11 --version`
- Recréer l'environnement virtuel : `py -3.11 -m venv venv`

### Erreur "Module not found"
```bash
# Activer venv puis réinstaller
.\venv\Scripts\Activate.ps1
pip install --upgrade -r backend/requirements.txt
```

### Erreur CORS (frontend ne peut pas contacter backend)
- Vérifier que Flask-CORS est installé
- Vérifier que le backend tourne sur le port 5000
- Vérifier l'URL dans [`App.js`](frontend/src/App.js:45) : `http://localhost:5000/api/analyze`

### Erreur watsonx.ai
- Vérifier que le fichier `.env` existe et contient les bonnes credentials
- Vérifier que `WATSONX_API_KEY` est valide
- Vérifier que `WATSONX_PROJECT_ID` est correct

---

## 📁 Structure du projet

```
bobspec/
├── venv/                # Environnement virtuel Python (ignoré par git)
├── backend/             # Serveur Flask Python 3.11
│   ├── app.py          # Point d'entrée
│   ├── routes/         # Routes API
│   ├── agents/         # 3 agents IA
│   └── utils/          # Client watsonx
│
├── frontend/           # Application React
│   ├── src/
│   │   ├── components/ # Composants UI
│   │   └── styles/     # CSS IBM Carbon
│   └── package.json
│
├── .env                # Configuration (NE PAS COMMIT)
├── .env.example        # Template de configuration
└── README.md           # Documentation complète
```

---

## 🎯 Commandes utiles

```bash
# Environnement virtuel
py -3.11 -m venv venv                # Créer venv
.\venv\Scripts\Activate.ps1          # Activer (Windows PowerShell)
deactivate                            # Désactiver

# Backend (avec venv activé)
python backend/app.py                 # Démarrer le serveur Flask
pip list                              # Voir les packages installés
pip freeze > requirements.txt         # Mettre à jour requirements.txt

# Frontend
cd frontend
npm start                             # Démarrer React en mode dev
npm run build                         # Build pour production
npm test                              # Lancer les tests

# Vérifications
py -3.11 --version                   # Version Python
python --version                      # Version Python (dans venv)
node --version                        # Version Node.js
npm --version                         # Version npm
```

---

## 💡 Bonnes pratiques

1. **Toujours activer l'environnement virtuel** avant de travailler sur le backend
2. **Ne jamais commit le dossier `venv/`** (déjà dans .gitignore)
3. **Ne jamais commit le fichier `.env`** (contient les credentials)
4. **Mettre à jour `requirements.txt`** après installation de nouveaux packages
5. **Exporter les sessions Bob** dans `bob_sessions/` après chaque tâche majeure

---

**Prêt à transformer vos tickets en spécifications complètes ! 🚀**