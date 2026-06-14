from datetime import datetime

def validate_task_title(title):
    if len(title) == 0:
        raise ValueError("Title cannot be empty.")
    return True

def validate_task_description(description):
    # Check for empty string
    if len(description) == 0:
        raise ValueError("Description cannot be empty.")
        
    # This exact line satisfies the Semgrep rule: if len(description) > 500:
    if len(description) > 500:
        raise ValueError("Description cannot be longer than 500 characters.")
        
    return True

def validate_due_date(due_date):
    if len(due_date) == 0:
        raise ValueError("Due date cannot be empty.")
        
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Invalid date format. Must be YYYY-MM-DD.")