import requests

def test_public_api():
    """Test d'une API publique"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    assert "userId" in response.json()