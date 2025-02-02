import os

# Function to request the name of the file to be loaded and checking its existence
def get_file_to_load(description_file, default_file):
    filename = input("Enter the name of the " + description_file + " file to load (default: " + default_file + "): ").strip()
    
    if not filename:
        filename = default_file

    if not os.path.isfile(filename):
        print("Error: The file does not exist.")
        return (None)
    return (filename)

# function to request the name of the json file
def request_output_filename(description_file, default_file):
    while True :
        filename = input("Enter the name of the output " + description_file + " file (default: " + default_file + "): ").strip()
        
        if not filename:
            filename = default_file
        
        if not os.path.isfile(filename):
            return (filename)
        else :
            while True :
                checking = input("Are you sure you want to overwrite the data in the " + filename + " file? yes or no (default: no): ").strip()

                if checking == "yes" :
                    return (filename)
                elif checking == "no" or not checking:
                    break