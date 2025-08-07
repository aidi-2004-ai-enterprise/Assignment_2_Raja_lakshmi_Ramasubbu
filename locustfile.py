from locust import HttpUser, task, between

class PenguinPredictorUser(HttpUser):
    wait_time = between(1, 5)  # Simulates a user waiting between 1-5 seconds between requests

    @task
    def predict_species(self):
        self.client.post(
            "/predict",
            json={
                "island": "Torgersen",
                "bill_length_mm": 39.1,
                "bill_depth_mm": 18.7,
                "flipper_length_mm": 181,
                "body_mass_g": 3750,
                "sex": "male",
                "year": 2007
            },
            headers={"Content-Type": "application/json"}
        )
