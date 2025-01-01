from locust import HttpUser, TaskSet, task, between
import random
import string

# Helper function to generate random user data
def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

class UserBehavior(TaskSet):

    @task  # Load test the client_registeration endpoint
    def client_register(self):
        # Generate random user data for each request
        data = {
            "fullName": random_string(10),
            "userName": random_string(8),
            "email": f"{random_string(5)}@example.com",
            "password": random_string(10),
            "phone": str(random.randint(1000000000, 9999999999))
        }
        with self.client.post("/client_registeration", data=data, catch_response=True) as response:
            if response.status_code == 200 and "User Registered" in response.text:
                response.success()
            elif "Email already Exist" in response.text:
                response.failure("Duplicate email detected.")
            else:
                response.failure(f"Failed to register user: {response.text}")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 3)  # Simulate a wait time between 1 to 3 seconds between requests
