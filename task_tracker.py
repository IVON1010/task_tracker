import json
import os

TASK_FILE = "tasks.json"

def initialize():
    os.path.exists(TASK_FILE)
    with open("TASK_FILE", mode="w") as file:
        json.dumps([], file)