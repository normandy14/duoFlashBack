# Third party modules
import pytest
import json
import os

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


def test_auth(client):
    rv = client.get('/auth/es')
    json_dict = json.loads(rv.data)
    assert 'two' in json_dict['dos'] # Enter known words and translations from your account
    assert 'brother' in json_dict['hermano']