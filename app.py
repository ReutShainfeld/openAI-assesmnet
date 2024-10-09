from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, QA
from openai import OpemAi
import openai

from config import Config


app = Flask(__name__)
app.config.from_object(Config)



db.init_app(app)
with app.app_context():
    db.create_all()

openai.api_key = Config.OPENAI_API_KEY


app = Flask(__name__)


@app.route('/ask')

def hask():
    return 'Hello World'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5015)