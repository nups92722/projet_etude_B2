import pandas as pd

from utils.file_input_functions import get_file_to_load

def load_json_data(default_file):
    # Get the filename of the JSON file
    filename = get_file_to_load("json", default_file)
    try:
        # Load data
        data = pd.read_json(filename)
        print("File loaded successfully!")
    except ValueError:
        print(f"Error: The file '{filename}' is not a valid JSON file.")
        return (None)
    except Exception as e:
        print(f"Unexpected error: {e}")
    return (data)