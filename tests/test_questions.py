import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_question():
    response = client.post("/questions/", json={"text": "Test question"})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["text"] == "Test question"
    assert "created_at" in data
