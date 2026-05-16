# 🔧 Guide de Dépannage BobSpec

## Problème : L'application ne retourne pas de résultats

### Diagnostic

Si l'application ne fonctionne pas correctement, cela peut être dû à :

1. **Problème de connexion watsonx.ai** - Les credentials sont invalides ou l'API est inaccessible
2. **Problème de configuration** - Le fichier `.env` est mal configuré
3. **Problème réseau** - Impossible de contacter l'API IBM

### Solution : Mode Test avec Données Mockées

BobSpec inclut un **mode de test** qui utilise des données d'exemple au lieu de l'API watsonx.ai. Cela permet de tester l'application même sans credentials valides.

#### Activer le Mode Test

Éditez le fichier `.env` et changez :

```env
USE_MOCK_DATA=true
```

Au lieu de :

```env
USE_MOCK_DATA=false
```

#### Redémarrer le Backend

```bash
# Arrêter le serveur (CTRL+C)
# Puis relancer
.\venv\Scripts\Activate.ps1
python backend/app.py
```

### Comportement en Mode Test

Avec `USE_MOCK_DATA=true`, les 3 agents retournent des données d'exemple réalistes :

**Edge Case Agent** retourne 4 cas limites :
- Email déjà existant
- Tentatives de connexion multiples
- Token expiré
- Email temporaire

**Security Agent** retourne 5 risques :
- Stockage mot de passe en clair
- Attaques par force brute
- Injection SQL
- Tokens non sécurisés
- Non-conformité RGPD

**Architect Agent** retourne :
- 5 composants techniques
- 7 endpoints API
- 10 étapes d'implémentation
- Complexité : L (Large)
- Estimation : 8 jours

### Comportement en Mode Production

Avec `USE_MOCK_DATA=false`, les agents utilisent watsonx.ai :

- Si l'API fonctionne → Résultats réels de l'IA
- Si l'API échoue → Fallback automatique sur les données mockées

**Avantage** : L'application fonctionne toujours, même en cas de problème API !

---

## Vérification des Credentials watsonx.ai

### Fichier .env Requis

```env
WATSONX_API_KEY=votre_clé_api_ici
WATSONX_PROJECT_ID=votre_project_id_ici
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-4-h-small
USE_MOCK_DATA=false
```

### Tester les Credentials

```bash
# Activer venv
.\venv\Scripts\Activate.ps1

# Tester la connexion
python -c "from backend.utils.watsonx_client import get_iam_token; print(get_iam_token())"
```

Si cela affiche un token, vos credentials sont valides.

---

## Problèmes Courants

### 1. Backend ne démarre pas

**Erreur** : `ModuleNotFoundError: No module named 'flask'`

**Solution** :
```bash
.\venv\Scripts\Activate.ps1
pip install -r backend/requirements.txt
```

### 2. Frontend ne se connecte pas au backend

**Erreur** : `CORS error` ou `Network error`

**Vérifications** :
- Backend tourne sur http://localhost:5000
- Frontend tourne sur http://localhost:3000
- Flask-CORS est installé

**Solution** :
```bash
pip install flask-cors
```

### 3. Agents retournent des erreurs vides

**Symptôme** : Les cartes d'agents s'affichent mais sans résultats

**Solution** : Activer le mode test
```env
USE_MOCK_DATA=true
```

### 4. Erreur "Python not found"

**Solution** : Utiliser Python 3.11 explicitement
```bash
py -3.11 -m venv venv
```

---

## Logs de Débogage

Les agents affichent des messages dans la console backend :

```
🔧 Using mock data for Edge Case Agent
🔧 Using mock data for Security Agent  
🔧 Using mock data for Architect Agent
```

Ou en cas d'erreur :

```
⚠️ JSON parse error, falling back to mock data: ...
⚠️ Agent error, falling back to mock data: ...
```

---

## Mode Recommandé pour le Hackathon

Pour la démo du hackathon, nous recommandons :

```env
USE_MOCK_DATA=true
```

**Pourquoi ?**
- ✅ Résultats instantanés (pas d'attente API)
- ✅ Pas de dépendance réseau
- ✅ Données cohérentes et impressionnantes
- ✅ Zéro risque de quota API dépassé

Vous pouvez toujours montrer que l'intégration watsonx.ai fonctionne en changeant à `false` pendant la démo.

---

## Support

Si le problème persiste :

1. Vérifier les logs du backend (terminal 1)
2. Vérifier la console du navigateur (F12)
3. Tester avec `USE_MOCK_DATA=true`
4. Consulter [`START.md`](START.md) pour le guide complet

---

**BobSpec - Team Bobsyourdev | IBM Bob Hackathon 2026**