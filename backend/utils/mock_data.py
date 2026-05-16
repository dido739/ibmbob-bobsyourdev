"""
Mock data for testing BobSpec without watsonx.ai
"""

def get_mock_edge_cases():
    """Return mock edge cases response"""
    return {
        "edge_cases": [
            {
                "scenario": "User attempts to register with an existing email",
                "criticality": "HIGH",
                "question_for_po": "What error message should be displayed? Should we suggest password recovery?"
            },
            {
                "scenario": "Multiple failed login attempts",
                "criticality": "CRITICAL",
                "question_for_po": "After how many attempts should the account be locked? What is the lockout duration?"
            },
            {
                "scenario": "Expired password reset token",
                "criticality": "MEDIUM",
                "question_for_po": "What is the token validity duration? 15 min, 1h, 24h?"
            },
            {
                "scenario": "Temporary or disposable email used",
                "criticality": "MEDIUM",
                "question_for_po": "Should we block temporary emails (10minutemail, etc.)?"
            }
        ]
    }

def get_mock_security():
    """Return mock security risks response"""
    return {
        "security_risks": [
            {
                "vulnerability": "Plain text password storage",
                "risk_level": "CRITICAL",
                "standard": "OWASP A02:2021",
                "mitigation": "Use bcrypt with a salt of 12+ rounds to hash passwords"
            },
            {
                "vulnerability": "No protection against brute force attacks",
                "risk_level": "HIGH",
                "standard": "OWASP A07:2021",
                "mitigation": "Implement rate limiting (e.g., 5 attempts max per 15 min) and CAPTCHA after 3 failures"
            },
            {
                "vulnerability": "Potential SQL injection on email/password fields",
                "risk_level": "CRITICAL",
                "standard": "OWASP A03:2021",
                "mitigation": "Use prepared statements and validate/sanitize all inputs"
            },
            {
                "vulnerability": "Unsecured session tokens",
                "risk_level": "HIGH",
                "standard": "OWASP A01:2021",
                "mitigation": "Use JWT with HMAC-SHA256 signature, short expiration (15min) and refresh tokens"
            },
            {
                "vulnerability": "Personal data not GDPR compliant",
                "risk_level": "HIGH",
                "standard": "GDPR",
                "mitigation": "Obtain explicit consent, allow data export/deletion, encrypt sensitive data"
            }
        ]
    }

def get_mock_architecture():
    """Return mock architecture response"""
    return {
        "architecture": {
            "components": [
                "REST API (Flask/FastAPI)",
                "PostgreSQL database",
                "Email service (SendGrid/AWS SES)",
                "Redis cache for sessions",
                "Email validation service"
            ],
            "complexity": "L",
            "endpoints": [
                "POST /api/auth/register - User registration",
                "POST /api/auth/login - User login",
                "POST /api/auth/logout - Logout",
                "POST /api/auth/forgot-password - Password reset request",
                "POST /api/auth/reset-password - Password reset with token",
                "GET /api/auth/verify-email - Email verification",
                "POST /api/auth/refresh-token - Token refresh"
            ],
            "implementation_order": [
                "1. Create User model in database with fields (id, email, password_hash, created_at, verified)",
                "2. Implement registration endpoint with email validation and bcrypt hashing",
                "3. Create JWT token system (access + refresh tokens)",
                "4. Implement login endpoint with hash verification",
                "5. Add rate limiting on sensitive endpoints",
                "6. Implement password reset system with temporary tokens",
                "7. Create email service for confirmations",
                "8. Add email verification to registration",
                "9. Implement logout with token invalidation",
                "10. Add unit and integration tests"
            ],
            "estimated_days": 8
        }
    }

# Made with Bob
