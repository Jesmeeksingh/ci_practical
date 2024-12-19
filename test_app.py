import app
def test_home():
    client = app.app.test_client()
    response = client.get("/")
    assert response.data == b"Hell, Continuous integration and deployment!"
