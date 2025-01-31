# code to transform CSV into JSON

import pandas as pd
import os

# function to request the name of the csv file
def get_csv_filename():
    filename = input("Enter the name of the CSV file: ").strip()
    if not os.path.isfile(filename):
        print("Error: The file does not exist.")
        return None
    return filename

# function to request the name of the json file
def get_json_filename():
    filename = input("Enter the name of the output JSON file (default: data.json): ").strip()
    return filename if filename else "data.json"

# function to convert the csv file into a json file
def convert_csv_to_json():
    csv_file = get_csv_filename()
    if csv_file is None:
        return
    
    json_file = get_json_filename()

    try:
        df = pd.read_csv(csv_file)
        df.to_json(json_file, orient="records", indent=4)
        print(f"JSON file successfully created: {json_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    convert_csv_to_json()
