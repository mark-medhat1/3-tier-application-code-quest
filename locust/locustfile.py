from locust import HttpUser, task, between
import os, random

TARGET = os.getenv("LOCUST_HOST", "http://localhost:30080")
class TaskUser(HttpUser):
    host = TARGET
    wait_time = between(1,3)
    @task(5)
    def list_tasks(self):
        self.client.get("/listTasks")
    @task(2)
    def add_task(self):
        payload = {"title": f"task-{random.randint(1,100000)}"}
        self.client.post("/addTask", json=payload)
    @task(1)
    def delete_task(self):
        task_id = random.randint(1,50)
        self.client.delete(f"/deleteTask/{task_id}")
