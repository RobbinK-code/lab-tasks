from datetime import datetime
# Import validation functions
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    if validate_task_title(title) and validate_task_description(description) and validate_due_date(due_date):
        new_task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False
        }
        tasks.append(new_task)
        print("Task added successfully!")
    else:
        print("Error: Invalid task details.")

# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    try:
        # Convert user 1-based indexing to python 0-based indexing
        actual_index = index - 1
        
        if actual_index < 0:
            raise IndexError
            
        if not tasks[actual_index]["completed"]:
            tasks[actual_index]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Task is already complete.")
    except IndexError:
        print("Error: Task index does not exist.")

# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending = [task for task in tasks if not task["completed"]]
    if not pending:
        print("No pending tasks currently.")
        return
        
    for i, task in enumerate(tasks):
        if not task["completed"]:
            # Displaying as 1-based index for the user
            print(f"[{i + 1}] {task['title']} (Due: {task['due_date']}) - {task['description']}")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0.0
    
    completed_count = sum(1 for task in tasks if task["completed"])
    progress = (completed_count / len(tasks)) * 100
    
    return round(progress, 2)