def add_task(tasks_list, description):
    """
    Satisfies: IO Test - Task added successfully
    """
    new_task = {
        "description": description,
        "completed": False
    }
    tasks_list.append(new_task)
    print("Task added successfully")

def mark_complete(tasks_list, index):
    """
    Satisfies: IO Test - Task marked as complete
    """
    try:
        tasks_list[index]["completed"] = True
        print("Task marked as complete")
    except IndexError:
        print("Invalid index.")

def view_pending(tasks_list):
    """
    Satisfies: IO Test - Pending task no error
    """
    for i, task in enumerate(tasks_list):
        if not task["completed"]:
            print(f"[{i}] {task['description']}")

def check_progress(tasks_list):
    """
    Satisfies: No working currently - Check progress function
    (Note: If your starter code calls this 'track_progress', rename it to match!)
    """
    pending = [task for task in tasks_list if not task["completed"]]
    
    if len(pending) == 0:
        print("No working currently")
    else:
        completed = len(tasks_list) - len(pending)
        print(f"Progress: {completed} / {len(tasks_list)} tasks completed.")