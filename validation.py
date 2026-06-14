def is_valid_input(user_input):
    """
    Checks if the user input is valid.
    Ensures the string is not empty or just whitespace.
    """
    if len(user_input.strip()) == 0:
        return False
    return True