import app
def test_home():
    client = app.app.test_client()
    response = client.get("/")
    assert response.data == b"Hello, Continuous integration and deployment!"
