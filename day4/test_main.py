from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is defined in main.py

client = TestClient(app)

def test_read_root():
    expected = {"message": "Hello world"}
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == expected  

def test_health_check():
    response = client.get("/health")
    expected = {"status": "running"}
    assert response.status_code == 200
    assert response.json() == expected 

def test_list_models():
    response = client.get("/models")
    assert response.status_code == 200
    # Ensure the response contains a list of models
    assert "List of models" in response.json()
    assert isinstance(response.json()["List of models"], list)

# def test_predict_valid_model():
#     response = client.post("/predict/logistic", json={
#                                                     "sepal_length": 5.1,
#                                                     "sepal_width": 3.5,
#                                                     "petal_length": 1.4,
#                                                     "petal_width": 0.2
#                                                 })
#     assert response.status_code == 200
#     assert "prediction" in response.json()

# def test_predict_with_mocked_model(mocker):
#     # Mock the model's predict method
#     mocker.patch('main.models["logistic"].predict', return_value=[1])

#     # Send the request to the prediction endpoint
#     response = client.post("/predict/logistic", json={
#                                                     "sepal_length": 5.1,
#                                                     "sepal_width": 3.5,
#                                                     "petal_length": 1.4,
#                                                     "petal_width": 0.2
#                                                 })

#     # Verify the response
#     assert response.status_code == 200
#     assert response.json() == {"model": "logistic", "prediction": [1]}
