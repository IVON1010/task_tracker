import json
import uuid
from pathlib import Path

TASK_FILE = Path("tasks.json")

def load_tasks():
    if not TASK_FILE.exists():
        return []
    try:
        with open(TASK_FILE, mode='r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, mode='w') as file:
        json.dumps(tasks, file, indent=4)

def add_tasks():
    tasks = load_tasks()
    task = {
        "id": str.
    }