import pytest
from app import app
from models import db
import os

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('TEST_DATABASE_URI', 'sqlite:///:memory:')
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_ask_endpoint(client, monkeypatch):
    def mock_openai_completion_create(*args, **kwargs):
        class MockResponse:
            choices = [type('obj', (object,), {'text': 'Mock answer'})]
        return MockResponse()

    monkeypatch.setattr('openai.Completion.create', mock_openai_completion_create)

    response = client.post('/ask', json={'question': 'What is the capital of France?'})

    assert response.status_code == 200
    data = response.get_json()
    assert 'answer' in data
 