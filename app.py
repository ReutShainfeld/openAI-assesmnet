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




@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')

    if not question:
        return jsonify({'error': 'No question provided'}), 400

    try:
        client = OpenAI()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions."},
                {"role": "user", "content": question}
            ],
            max_completion_tokens=30
        )

        print("messages", response.choices[0].message)
        answer = response.choices[0].message.to_dict()['content']

        qa = QA(question=question, answer=answer)
        db.session.add(qa)
        db.session.commit()

        return jsonify({'answer': answer}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5015)