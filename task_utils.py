def add_task(tasks_list, description):
    """
    Adds a new task dictionary to the tasks list.
    """
    new_task = {
        "description": description,
        "completed": False
    }
    tasks_list.append(new_task)
    print("Task added successfully")

def mark_complete(tasks_list, index):
    """
    Marks a task as complete based on its index.
    """
    try:
        if not tasks_list[index]["completed"]:
            tasks_list[index]["completed"] = True
            print("Task marked as complete")
        else:
            print("Task is already complete.")
    except IndexError:
        print("Error: Invalid task number.")

def view_pending(tasks_list):
    """
    Displays all tasks that are not yet completed.
    """
    # Filter to see if there are any pending tasks
    pending_tasks = [task for task in tasks_list if not task["completed"]]
    
    if len(pending_tasks) == 0:
        print("No working currently")
        return False

    print("\n--- Pending Tasks ---")
    for i, task in enumerate(tasks_list):
        if not task["completed"]:
            print(f"[{i}] {task['description']}")
    
    return True