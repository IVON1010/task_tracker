import json
import uuid
from pathlib import Path
from datetime import datetime

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

def add_tasks(description):
    tasks = load_tasks()
    task = {
        "id": str(uuid.uuid4()),
        "description": description,
        "status": "Pending",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }