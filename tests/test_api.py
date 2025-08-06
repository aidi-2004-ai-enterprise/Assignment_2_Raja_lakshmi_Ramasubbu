# tests/test_api.py
from fastapi.testclient import TestClient
from app.main import app  # Adjust the import path if needed
import pytest
import warnings
warnings.filterwarnings("ignore")


client = TestClient(app)

def test_predict_endpoint_valid_input():
    """Test prediction with valid penguin data"""
    sample_data = {
        "bill_length_mm": 39.1,
        "bill_depth_mm": 18.7,
        "flipper_length_mm": 181,
        "body_mass_g": 3750,
        "year": 2008,
        "sex": "male",
        "island": "Biscoe"
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 200
    assert "species" in response.json()

def test_predict_missing_field():
    """Test input with a missing field"""
    sample_data = {
        "bill_length_mm": 39.1,
        "bill_depth_mm": 18.7,
        "flipper_length_mm": 181
        # body_mass_g missing
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 422  # Unprocessable Entity

def test_predict_invalid_data_type():
    """Test input with invalid data type"""
    sample_data = {
        "bill_length_mm": "invalid",
        "bill_depth_mm": 18.7,
        "flipper_length_mm": 181,
        "body_mass_g": 3750
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 422

def test_predict_out_of_range_value():
    """Test input with out-of-range value"""
    sample_data = {
        "bill_length_mm": 39.1,
        "bill_depth_mm": 18.7,
        "flipper_length_mm": 181,
        "body_mass_g": -100  # invalid negative value
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 422

def test_predict_empty_request():
    """Test completely empty request body"""
    response = client.post("/predict", json={})
    assert response.status_code == 422
