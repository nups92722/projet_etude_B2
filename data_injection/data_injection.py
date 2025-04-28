from utils.bdd_management import Database
import mysql.connector

from utils.load_json_data import load_json_data

from data_injection.region import insert_data_into_region_table

def data_injection():
    try :
        bdd = Database()

        # Load data
        data = load_json_data("data.json")

        if data is None:
            return (False)

        insert_data_into_region_table(bdd, data)

    except mysql.connector.Error as err:
        print(f"Error : {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")