import pandas as pd

from parsing.parsing_regionname import parsing_regionnname
from parsing.parsing_construction_year import parsing_construction_year
from utils.file_input_functions import get_file_to_load
from utils.file_input_functions import request_output_filename
from utils.load_json_data import load_json_data

def parsing(): 
    # Load data
    data = load_json_data("data.json")

    if data is None:
        return (False)
    
    output_filename = request_output_filename("json", "data.json")

    # Remove rows with missing values in important columns
    data = data.dropna(subset=['Price'])
    data = data.dropna(subset=['Suburb'])

    data = parsing_regionnname(data)
    data = parsing_construction_year(data)
    
    data.to_json(output_filename, orient="records", indent=4)