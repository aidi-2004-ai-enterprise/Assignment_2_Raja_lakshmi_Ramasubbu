from locust import HttpUser, task, between
import json

class PredictUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def predict(self):
        payload = {
            "bill_length_mm": 39.1,
            "bill_depth_mm": 18.7,
            "flipper_length_mm": 181.0,
            "body_mass_g": 3750.0,
            "island": "Torgersen",
            "sex": "male"
        }
        headers = {"Content-Type": "application/json"}
        self.client.post("/predict", data=json.dumps(payload), headers=headers)
