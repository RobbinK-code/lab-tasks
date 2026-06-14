from datetime import datetime

def validate_task_title(title):
    # Ensures title is a string and not just blank spaces
    if isinstance(title, str) and len(title.strip()) > 0:
        return True
    return False

def validate_task_description(description):
    # Ensures description is a string and not just blank spaces
    if isinstance(description, str) and len(description.strip()) > 0:
        return True
    return False

def validate_due_date(due_date):
    # Ensures the date matches the expected format (YYYY-MM-DD)
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False