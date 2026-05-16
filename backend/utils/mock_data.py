"""
Mock data for testing BobSpec without watsonx.ai
"""

def get_mock_edge_cases():
    """Return mock edge cases response"""
    return {
        "edge_cases": [
            {
                "scenario": "Utilisateur tente de s'inscrire avec un email déjà existant",
                "criticality": "HIGH",
                "question_for_po": "Quel message d'erreur afficher ? Doit-on suggérer la récupération de mot de passe ?"
            },
            {
                "scenario": "Tentatives de connexion multiples échouées",
                "criticality": "CRITICAL",
                "question_for_po": "Après combien de tentatives bloquer le compte ? Quelle est la durée du blocage ?"
            },
            {
                "scenario": "Token de réinitialisation expiré",
                "criticality": "MEDIUM",
                "question_for_po": "Quelle est la durée de validité du token ? 15 min, 1h, 24h ?"
            },
            {
                "scenario": "Email temporaire ou jetable utilisé",
                "criticality": "MEDIUM",
                "question_for_po": "Doit-on bloquer les emails temporaires (10minutemail, etc.) ?"
            }
        ]
    }

def get_mock_security():
    """Return mock security risks response"""
    return {
        "security_risks": [
            {
                "vulnerability": "Stockage des mots de passe en clair",
                "risk_level": "CRITICAL",
                "standard": "OWASP A02:2021",
                "mitigation": "Utiliser bcrypt avec un salt de 12+ rounds pour hasher les mots de passe"
            },
            {
                "vulnerability": "Absence de protection contre les attaques par force brute",
                "risk_level": "HIGH",
                "standard": "OWASP A07:2021",
                "mitigation": "Implémenter un rate limiting (ex: 5 tentatives max par 15 min) et CAPTCHA après 3 échecs"
            },
            {
                "vulnerability": "Injection SQL potentielle sur les champs email/password",
                "risk_level": "CRITICAL",
                "standard": "OWASP A03:2021",
                "mitigation": "Utiliser des requêtes préparées (prepared statements) et valider/sanitiser toutes les entrées"
            },
            {
                "vulnerability": "Tokens de session non sécurisés",
                "risk_level": "HIGH",
                "standard": "OWASP A01:2021",
                "mitigation": "Utiliser JWT avec signature HMAC-SHA256, expiration courte (15min) et refresh tokens"
            },
            {
                "vulnerability": "Données personnelles non conformes RGPD",
                "risk_level": "HIGH",
                "standard": "GDPR",
                "mitigation": "Obtenir consentement explicite, permettre export/suppression des données, chiffrer les données sensibles"
            }
        ]
    }

def get_mock_architecture():
    """Return mock architecture response"""
    return {
        "architecture": {
            "components": [
                "API REST (Flask/FastAPI)",
                "Base de données PostgreSQL",
                "Service d'envoi d'emails (SendGrid/AWS SES)",
                "Cache Redis pour les sessions",
                "Service de validation d'emails"
            ],
            "complexity": "L",
            "endpoints": [
                "POST /api/auth/register - Inscription utilisateur",
                "POST /api/auth/login - Connexion utilisateur",
                "POST /api/auth/logout - Déconnexion",
                "POST /api/auth/forgot-password - Demande de réinitialisation",
                "POST /api/auth/reset-password - Réinitialisation avec token",
                "GET /api/auth/verify-email - Vérification email",
                "POST /api/auth/refresh-token - Renouvellement du token"
            ],
            "implementation_order": [
                "1. Créer le modèle User en base de données avec champs (id, email, password_hash, created_at, verified)",
                "2. Implémenter l'endpoint d'inscription avec validation email et hashing bcrypt",
                "3. Créer le système de tokens JWT (access + refresh tokens)",
                "4. Implémenter l'endpoint de connexion avec vérification du hash",
                "5. Ajouter le rate limiting sur les endpoints sensibles",
                "6. Implémenter le système de réinitialisation de mot de passe avec tokens temporaires",
                "7. Créer le service d'envoi d'emails pour les confirmations",
                "8. Ajouter la vérification d'email à l'inscription",
                "9. Implémenter la déconnexion avec invalidation des tokens",
                "10. Ajouter les tests unitaires et d'intégration"
            ],
            "estimated_days": 8
        }
    }

# Made with Bob
