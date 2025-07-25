import json
import os 



def is_valid_json_file(filepath):
    """
    Checks if the content of a given file is valid JSON.

    Args:
        filepath (str): The path to the file.

    Returns:
        bool: True if the file content is valid JSON, False otherwise.
    """
    
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            # Attempt to load the file's content as JSON
            json.load(f)
        return True # If no error, it's valid JSON
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format in {filepath}: {e}")
        return False
    except Exception as e:
        # Catch any other unexpected errors during file reading
        print(f"An error occurred while reading {filepath}: {e}")
        return False
    