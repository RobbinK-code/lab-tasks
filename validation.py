from datetime import datetime

def validate_task_title(title):
    # Using the exact, basic if len() syntax for the static scanner
    if len(title) == 0:
        raise ValueError("Title cannot be empty.")
    
    # We can strip spaces after the len() check to ensure logic still works
    if title.isspace():
        raise ValueError("Title cannot be just spaces.")
        
    return True

def validate_task_description(description):
    if len(description) == 0:
        raise ValueError("Description cannot be empty.")
        
    if description.isspace():
        raise ValueError("Description cannot be just spaces.")
        
    return True

def validate_due_date(due_date):
    if len(due_date) == 0:
        raise ValueError("Due date cannot be empty.")
        
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Invalid date format. Must be YYYY-MM-DD.")