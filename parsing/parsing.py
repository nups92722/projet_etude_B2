import pandas as pd

from parsing_regionname import parsing_regionnname
from parsing_construction_year import parsing_construction_year

# Function to request the name of the JSON file to be loaded
def get_json_filename():
    filename = input("Enter the name of the JSON file to load (default: data.json): ").strip()
    return filename if filename else "data.json"

def load_data():
    # Get the filename of the JSON file to be parsed
    filename = get_json_filename()
    try:
        # Load data
        data = pd.read_json(filename)
        print("File loaded successfully!")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return (None)
    except ValueError:
        print(f"Error: The file '{filename}' is not a valid JSON file.")
        return (None)
    except Exception as e:
        print(f"Unexpected error: {e}")
    return (data)


def main(): 
    # Load data
    data = load_data()

    if data is None:
        return (False)

    # Remove rows with missing values in important columns
    data = data.dropna(subset=['Price'])
    data = data.dropna(subset=['Suburb'])

    data = parsing_regionnname(data)
    data = parsing_construction_year(data)
    
    

if __name__ == "__main__":
    main()
