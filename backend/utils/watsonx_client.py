import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_iam_token():
    """Fetch IAM token from IBM Cloud for watsonx.ai authentication"""
    url = "https://iam.cloud.ibm.com/identity/token"
    data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": os.getenv("WATSONX_API_KEY")
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

def call_granite(system_prompt: str, user_message: str) -> str:
    """
    Call watsonx.ai Granite model with system and user prompts.
    
    Args:
        system_prompt: System instructions for the agent
        user_message: User's ticket content
        
    Returns:
        str: JSON response from the model (pure JSON, no markdown)
    """
    token = get_iam_token()
    url = f"{os.getenv('WATSONX_URL')}/ml/v1/text/chat?version=2023-05-29"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "model_id": os.getenv("WATSONX_MODEL_ID"),
        "project_id": os.getenv("WATSONX_PROJECT_ID"),
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_message}
        ],
        "parameters": {
            "max_new_tokens": 1000,
            "temperature": 0.3
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']

# Made with Bob
