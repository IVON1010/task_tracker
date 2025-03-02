import json
import uuid
import sys
from datetime import datetime
from pathlib import Path

TASK_FILE = Path("tasks.json")

def load_tasks():
    if not TASK_FILE.exists():
        print("File not found")
        return []
    try:
        with open(TASK_FILE, mode='r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
    
def save_tasks(tasks):
    with open(TASK_FILE, mode='w') as file:
        json.dump(tasks, file, indent=4)

def add_tasks(description):
    tasks = load_tasks()
    task = {
        "id": str(uuid.uuid4()),
        "description": description,
        "status": "pending",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": None
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"{task['description']} added successfully.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Tasks not found")
        return

    for i, task in enumerate(tasks, 1):
        status = "completed" if task['status'] == "completed" else("in progress" if task['status'] == "in progress" else "pending")
        updated_at = f" | updated at: {task['updated_at']}" if task["updated_at"] else ""
        print(f"{i}. {task['description']} (ID: {task['id']})\n Status: {status} | Created_at: {task['created_at']}{updated_at}\n")
        save_tasks(tasks)

def delete_tasks(task_id):
    tasks = load_tasks()
    filtered_tasks = [task for task in tasks if task['id'] != task_id]

    if len(filtered_tasks) == len(tasks):
        print("Tasks not found")
    else:
        save_tasks(filtered_tasks)
        print(f"Successfully deleted: {task_id}")

def completed_tasks(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = "completed"
            task['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_tasks(tasks)
            print(f"Task completed: {task['description']}")
            return
    print("Task not found")

def update_tasks(task_id, new_description, new_status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['status'] = new_status
            task['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_tasks(tasks)
            print(f"Task added: {task['description']} Status: {task['status']}")
            return
    print("Task not found.")

def mark_done():
    tasks = load_tasks()
    done_tasks = [task for task in tasks if task['status'] == "completed"]

    if not done_tasks:
        print("Tasks not found")
    
    for i , task in enumerate(done_tasks, 1):
        print(f"{i}. {task['description']} | Completed at: {task.get('updated_at', 'N/A')}")


def pending_tasks():
    tasks = load_tasks()
    tasks_pending = [task for task in tasks if task['status'].lower() == 'pending']

    if not tasks_pending:
        print("No pending tasks")
        return

    for i, task in enumerate(tasks_pending, 1):
        print(f"{i}. {task['description']} | Created_at: {task.get('created_at', 'N/A')}")


def in_progress():
    tasks = load_tasks()
    in_progress_tasks = [task for task in tasks if task['status'] == "in progress"]

    if not in_progress_tasks:
        print("No tasks in progress")

    for i , task in enumerate(in_progress_tasks, 1):
        print(f"{i}. {task['description']} | Created at: {task['created_at']} | Updated_at: {task['updated_at']}\n")

def mark_in_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task_id == task['id']:
            task['status'] = "in progress"
            task['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_tasks(tasks)
            print(f"Task: {task['description']} in progress")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        return
    
    command = sys.argv[1]

    if command == "add" and len(sys.argv) > 2:
        add_tasks("".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "mark-done":
        mark_done()
    elif command == "list-to-do":
        pending_tasks()
    elif command == "in-progress":
        in_progress()
    elif command == "delete" and len(sys.argv) > 2:
        delete_tasks(sys.argv[2])
    elif command == 'completed' and len(sys.argv) > 2:
        completed_tasks(sys.argv[2])
    elif command == "updated" and len(sys.argv) > 4:
        update_tasks(sys.argv[2], sys.argv[3], sys.argv[4])
    elif command == "mark-in-progress" and len(sys.argv) > 2:
        mark_in_progress(sys.argv[2])
    else:
        print("Command not found, commands include add, list, delete, update, in-progress, mark-done and completed")



if __name__ == '__main__':
    main()