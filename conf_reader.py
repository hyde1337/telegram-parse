import json

def read_conf_setting(file_path, setting):
    """
    The function will read the configuration file and load up required parameters:
    Args:
        file_path (str): The path to the configuration file
    Returns: data
    """
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
            loaded = config[setting]
        return loaded
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: JSON file '{file_path}' is invalid.")
    except Exception as e:
        print(f"Error: {e}")