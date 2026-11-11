MAX_LEN = 25

# Check both strings before running algorithm
def validate(x, y):
    if not x or not y:
        return False, f"Both strings must be non-empty"
    if len(x) > MAX_LEN or len(y) > MAX_LEN:
        return False, f"Both strings must be at most {MAX_LEN} characters long"
    return True, "Valid"