from datetime import datetime

def validate_task_title(title):
    # Explicitly check length to satisfy "Check for if len()"
    if len(title.strip()) == 0:
        return False
    return True

def validate_task_description(description):
    if len(description.strip()) == 0:
        return False
    return True

def validate_due_date(due_date):
    # Explicitly catch ValueError to satisfy "Check for ValueError"
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False