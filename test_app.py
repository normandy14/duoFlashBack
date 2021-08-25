# Third party modules
import pytest
import json

# First party modules
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    rv = client.get("/hello")
    assert b"<p>Hello, World!<p>" == rv.data

'''
def test_session(client):
    rv = client.get("/user")
    assert 1 == 1
'''
    
def test_chopstick(client):
    rv = client.get("/chopstick/")
    json_dict = json.loads(rv.data)
    assert "bamboo" == json_dict['color']