
def __is_string(string):
    if (not isinstance(string, str)) or (not string.strip()):
        return False
    return True

def actor(obj):
    errors = []
    if not __is_string(obj.name):
        errors.append("name should be a string.")
    if not isinstance(obj.id, int):
        errors.append("id should be an integer.")
    if errors:
        return errors
    return True
