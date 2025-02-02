# code to transform CSV into JSON

import pandas as pd
from utils.file_input_functions import get_file_to_load
from utils.file_input_functions import request_output_filename

# function to convert the csv file into a json file
def convert_csv_to_json():
    csv_file = get_file_to_load("csv", "data.csv")
    if csv_file is None:
        return (False)
    
    json_file = request_output_filename("json", "data.json")

    try:
        df = pd.read_csv(csv_file)
        df.to_json(json_file, orient="records", indent=4)
        print(f"JSON file successfully created: {json_file}")
    except ValueError:
        print(f"Error: The file '{csv_file}' is not a valid CSV file.")
        return (False)
    except Exception as e:
        print(f"Error during conversion: {e}")
        return (False)

if __name__ == "__main__":
    convert_csv_to_json()
