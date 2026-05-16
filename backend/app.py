from flask import Flask
from flask_cors import CORS
from routes.analyze import analyze_bp

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(analyze_bp, url_prefix='/api')

@app.route('/')
def home():
    return {
        "message": "BobSpec API - IBM Bob Hackathon 2026",
        "endpoints": {
            "POST /api/analyze": "Analyze ticket with 3 AI agents"
        }
    }

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# Made with Bob
