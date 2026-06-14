def check_length(user_input):
    """
    Satisfies: Check validation - Check for if len()
    """
    if len(user_input.strip()) == 0:
        return False
    return True

def check_number(user_input):
    """
    Satisfies: Check validation - Check for ValueError
    """
    try:
        val = int(user_input)
        return val
    except ValueError:
        return -1