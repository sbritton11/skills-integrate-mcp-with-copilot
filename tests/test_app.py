from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_github_skills_activity_exists():
    response = client.get("/activities")

    assert response.status_code == 200
    activities = response.json()
    assert "GitHub Skills" in activities
    assert activities["GitHub Skills"]["description"]
