from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, QA
from openai import OpenAI
import openai

from config import Config


app = Flask(__name__)
app.config.from_object(Config)



db.init_app(app)
with app.app_context():
    db.create_all()

openai.api_key = Config.OPENAI_API_KEY


app = Flask(__name__)



@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')

    if not question:
        return jsonify({'error': 'No question provided'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5015)