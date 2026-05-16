import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.watsonx_client import call_granite
from utils.mock_data import get_mock_edge_cases
from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMPT = """You are a senior developer with 15 years of experience.
Your role is to identify ALL edge cases the Product Owner forgot to mention.

For each edge case found, return:
- scenario: description of the edge case
- criticality: LOW / MEDIUM / HIGH / CRITICAL
- question_for_po: the question to ask the PO

Respond ONLY in valid JSON format (no markdown, no explanations):
{
  "edge_cases": [
    {
      "scenario": "...",
      "criticality": "HIGH",
      "question_for_po": "..."
    }
  ]
}"""

def run_edge_case_agent(ticket: str) -> dict:
    """
    Analyze ticket for edge cases.
    
    Args:
        ticket: The development ticket text
        
    Returns:
        dict: JSON object with edge_cases array
    """
    # Check if we should use mock data
    use_mock = os.getenv("USE_MOCK_DATA", "false").lower() == "true"
    
    if use_mock:
        print("🔧 Using mock data for Edge Case Agent")
        return get_mock_edge_cases()
    
    try:
        response = call_granite(SYSTEM_PROMPT, ticket)
        # Parse JSON response
        result = json.loads(response)
        return result
    except json.JSONDecodeError as e:
        print(f"⚠️ JSON parse error, falling back to mock data: {str(e)}")
        return get_mock_edge_cases()
    except Exception as e:
        print(f"⚠️ Agent error, falling back to mock data: {str(e)}")
        return get_mock_edge_cases()

# Made with Bob
