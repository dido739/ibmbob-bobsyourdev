import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.watsonx_client import call_granite
from utils.mock_data import get_mock_architecture
from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMPT = """You are a senior software architect.
Analyze this ticket and propose a concrete technical architecture.

Return:
- components: list of required components
- complexity: S / M / L / XL
- endpoints: API endpoints to create
- implementation_order: ordered steps to implement
- estimated_days: number of days to implement

Respond ONLY in valid JSON format (no markdown, no explanations):
{
  "architecture": {
    "components": ["..."],
    "complexity": "L",
    "endpoints": ["..."],
    "implementation_order": ["..."],
    "estimated_days": 5
  }
}"""

def run_architect_agent(ticket: str) -> dict:
    """
    Analyze ticket and propose technical architecture.
    
    Args:
        ticket: The development ticket text
        
    Returns:
        dict: JSON object with architecture details
    """
    # Check if we should use mock data
    use_mock = os.getenv("USE_MOCK_DATA", "false").lower() == "true"
    
    if use_mock:
        print("🔧 Using mock data for Architect Agent")
        return get_mock_architecture()
    
    try:
        response = call_granite(SYSTEM_PROMPT, ticket)
        # Parse JSON response
        result = json.loads(response)
        return result
    except json.JSONDecodeError as e:
        print(f"⚠️ JSON parse error, falling back to mock data: {str(e)}")
        return get_mock_architecture()
    except Exception as e:
        print(f"⚠️ Agent error, falling back to mock data: {str(e)}")
        return get_mock_architecture()

# Made with Bob
