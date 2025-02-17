import pytest
from app import app


@pytest.fixture()
def test_app():
   app.config.update({
       "TESTING": True,
   })
   yield app


@pytest.fixture()
def client(test_app):
   return test_app.test_client()


def test_index_page(client):
   res = client.get("/")
   assert 'Добро пожаловать' in res.text