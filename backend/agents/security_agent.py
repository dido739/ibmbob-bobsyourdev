import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.watsonx_client import call_granite
from utils.mock_data import get_mock_security
from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMPT = """You are a cybersecurity expert and compliance specialist.
Analyze this development ticket and identify all potential security risks.

For each risk, return:
- vulnerability: what the risk is
- risk_level: LOW / MEDIUM / HIGH / CRITICAL
- standard: applicable standard (OWASP, GDPR, PCI-DSS...)
- mitigation: how to fix it

Respond ONLY in valid JSON format (no markdown, no explanations):
{
  "security_risks": [
    {
      "vulnerability": "...",
      "risk_level": "CRITICAL",
      "standard": "PCI-DSS",
      "mitigation": "..."
    }
  ]
}"""

def run_security_agent(ticket: str) -> dict:
    """
    Analyze ticket for security risks.
    
    Args:
        ticket: The development ticket text
        
    Returns:
        dict: JSON object with security_risks array
    """
    # Check if we should use mock data
    use_mock = os.getenv("USE_MOCK_DATA", "false").lower() == "true"
    
    if use_mock:
        print("🔧 Using mock data for Security Agent")
        return get_mock_security()
    
    try:
        response = call_granite(SYSTEM_PROMPT, ticket)
        # Parse JSON response
        result = json.loads(response)
        return result
    except json.JSONDecodeError as e:
        print(f"⚠️ JSON parse error, falling back to mock data: {str(e)}")
        return get_mock_security()
    except Exception as e:
        print(f"⚠️ Agent error, falling back to mock data: {str(e)}")
        return get_mock_security()

# Made with Bob
