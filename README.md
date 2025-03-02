Task Tracker CLI
A simple command-line task tracker written in Python to manage tasks with statuses such as pending, in progress, and completed.

Features
Add tasks with descriptions.
List all tasks with status and timestamps.
Mark tasks as completed or in progress.
View only pending, in progress, or completed tasks.
Update task descriptions and statuses.
Delete tasks by ID.

Installation
Clone this repository:

git clone https://github.com/IVON1010/task-tracker.git
cd task-tracker
Ensure you have Python installed (version 3.x recommended).

Usage
Run the script with various commands:

python task_tracker.py [command] [arguments]

Commands:
Command	Description
add "task description"	Adds a new task
list	Lists all tasks
delete <task_id>	Deletes a task by ID
completed <task_id>	Marks a task as completed
mark-in-progress <task_id>	Marks a task as in progress
updated <task_id> "new description" "new status"	Updates a task's description and status
list-to-do	Shows only pending tasks
in-progress	Shows only tasks in progress
mark-done	Lists completed tasks
Example Usage
Adding a task:

python task_tracker.py add "Finish project report"
Listing tasks:

python task_tracker.py list
Marking a task as completed:

python task_tracker.py completed <task_id>
Deleting a task:

python task_tracker.py delete <task_id>
Task Storage
Tasks are stored in tasks.json in JSON format.

License
This project is open-source and available under the MIT License.

⭐ Developed by IVON1010
