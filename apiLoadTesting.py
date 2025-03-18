from locust import HttpUser, task, between
import random

class FastAPITestUser(HttpUser):
    wait_time = between(1, 3)  # Users wait 1-3 sec between requests

    @task
    def test_similarity(self):
        """Sends random name pairs to test similarity API"""
        name_pairs = [
            {"name1": "Alice", "name2": "Alicia"},
            {"name1": "Robert", "name2": "Bob"},
            {"name1": "Jonathan", "name2": "John"},
            {"name1": "Michael", "name2": "Mike"},
            {"name1": "Elizabeth", "name2": "Beth"}
        ]
        payload = random.choice(name_pairs)
        self.client.post("/similarity", json=payload)

