from locust import HttpUser, TaskSet, task, between
import random
import string

import requests

# Utility functions
def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_email():
    return f"{random_string(5)}@{random_string(3)}.com"


# Define the Locust task set for /client_registeration and /client_login
class UserBehavior(TaskSet):
    @task(1)
    def register(self):
        # Perform load testing on /client_registeration
        requests.post(
            "/client_registeration",
            data={
                "fullName": random_string(),
                "userName": random_string(),
                "email": random_email(),
                "password": "password123",
                "phone": "1234567890"
            }
        )

    @task(1)
    def login(self):
        # Perform stress testing on /client_login
        self.client.post(
            "/client_login",
            data={
                "email": random_email(),  # Random data simulating invalid logins
                "userName": "",
                "password": "password123"
            }
        )


# Define the Locust User class
class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 3)  # Users wait between 1-3 seconds between tasks
