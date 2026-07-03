from app import app

def test_add():
    client = app.test_client()
    response = client.get('/add?a=5&b=3')
    assert response.data.decode() == "Result: 8"

def test_subtract():
    client = app.test_client()
    response = client.get('/subtract?a=5&b=3')
    assert response.data.decode() == "Result: 2"
