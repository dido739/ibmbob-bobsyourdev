from flask import Blueprint, request, jsonify
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.edge_case_agent import run_edge_case_agent
from agents.security_agent import run_security_agent
from agents.architect_agent import run_architect_agent
import concurrent.futures

analyze_bp = Blueprint('analyze', __name__)

@analyze_bp.route('/analyze', methods=['POST'])
def analyze_ticket():
    """
    Analyze a development ticket using 3 parallel agents.
    
    Request body:
        {
            "ticket": "ticket text here"
        }
        
    Returns:
        {
            "edge_cases": {...},
            "security": {...},
            "architecture": {...}
        }
    """
    data = request.get_json()
    ticket = data.get('ticket', '')

    if not ticket:
        return jsonify({'error': 'Empty ticket'}), 400

    # Run all 3 agents in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(run_edge_case_agent, ticket)
        f2 = executor.submit(run_security_agent, ticket)
        f3 = executor.submit(run_architect_agent, ticket)

    # Collect results
    results = {
        'edge_cases':   f1.result(),
        'security':     f2.result(),
        'architecture': f3.result()
    }

    return jsonify(results), 200

# Made with Bob
