def is_non_empty_string(s):
	"""Return True if `s` is a non-empty string after stripping whitespace."""
	return isinstance(s, str) and len(s.strip()) > 0


def is_valid_index(idx, tasks):
	"""Return True if `idx` can be converted to an int and is a valid index into `tasks`.

	`tasks` should be a sequence (like a list). Negative indices are not considered valid
	for this simple validation (require 0 <= idx < len(tasks)).
	"""
	try:
		i = int(idx)
	except (TypeError, ValueError):
		return False
	return 0 <= i < len(tasks)

