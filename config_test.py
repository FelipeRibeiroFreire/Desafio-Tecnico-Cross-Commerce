import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()

def test_request_example(client):
    response = client.get("/ordered-number")
    assert response.data