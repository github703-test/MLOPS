import pytest
import json
from app import app

def test_prediction():
    tester = app.test_client()
    response = tester.post('/predict',
                           data=json.dumps({"features": [5.1, 3.5, 1.4, 0.2]}),
                           content_type='application/json')
    assert response.status_code == 200
    assert 'prediction' in response.get_json()
Run tests locally:
pytest test_app.py

