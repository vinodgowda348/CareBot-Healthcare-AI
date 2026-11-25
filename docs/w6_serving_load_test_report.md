# CareBot Healthcare AI
## Model Serving and Load Testing Report

### 1. Objective
Integrate the trained Random Forest model into a FastAPI serving layer, perform integration testing, and evaluate performance under 50 concurrent requests.

### 2. Model Details
- Model: Random Forest Classifier
- Number of trees: 100
- Maximum depth: None
- Input features: 15
- Diagnosis classes: 8
- Model artifact: models/carebot_model.joblib

### 3. API Endpoints
- GET / : API welcome message
- GET /health : API health check
- POST /predict : Model prediction endpoint

### 4. Integration Testing
Framework: Pytest and FastAPI TestClient

Results:
- Home endpoint: PASS
- Health endpoint: PASS
- Prediction endpoint: PASS
- Invalid input validation: PASS

Total tests: 4
Passed: 4
Failed: 0
Test execution time: 1.04 seconds

### 5. Load Testing
Tool: Python asyncio and HTTPX
Total requests: 200
Maximum concurrent requests: 50

Results:
- Successful requests: 200
- Failed requests: 0
- Total test time: 2.327 seconds
- Average latency: 555.16 ms
- Median latency: 514.21 ms
- 95th percentile latency: 823.82 ms
- Maximum latency: 895.22 ms
- Throughput: 85.96 requests/second

### 6. Conclusion
The CareBot FastAPI serving layer successfully loaded the trained Random Forest model and handled all 200 requests in the local load test, with a maximum concurrency of 50 requests.

All four integration tests passed. No failed requests were observed during the load test.

These measurements represent a local development environment using Uvicorn with reload enabled. They are not production capacity guarantees.

This project uses a synthetic educational dataset. Predictions are for demonstration only and must not be used as medical diagnoses.
