from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_api_key():
    response = client.get("/exchange/bybit/api_key")
    assert response.status_code == 200
    assert response.json() == {"api_key": "QWERTY12"}


def test_exchange_bybit():
    response = client.get("/exchange/bybit/")
    assert response.status_code == 200
    assert response.json() == {"info": "Основная платформа для следования за сделками"}
