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
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found")
        return
    
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task["status"] == "completed" else "Pending"
        print(f"{i} {task['description']} (ID: {task['id']}\n) status: {status} | created_at: {task['created_at']}\n  updated_at: {task['updated_at']}\n")

def delete_tasks(task_id):
    tasks = load_tasks()
    filtered_tasks = [task for task in tasks if task['id'] != task_id]
    
    if len(filtered_tasks) == len(tasks):
        print("Task not found")
    else:
        save_tasks(filtered_tasks)
        print(f"Taks with ID {task_id} removed.")

def complete_tasks(task_id):
    
