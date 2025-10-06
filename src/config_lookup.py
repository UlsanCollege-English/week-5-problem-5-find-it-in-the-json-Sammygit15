def find_key(data, key):
    """
    Depth-first left-to-right search for the first occurrence of key.
    Return value or None if not found.
    """
    if isinstance(data, dict):
        # Check current level first
        if key in data:
            return data[key]
        # Recurse into values
        for value in data.values():
            found = find_key(value, key)
            if found is not None:
                return found
    elif isinstance(data, (list, tuple)):
        for item in data:
            found = find_key(item, key)
            if found is not None:
                return found
    # Base case: non-collection or not found
    return None
