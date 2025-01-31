import pandas as pd

def create_suburb_regionname_mapping(data):
    # Remove rows with no region name
    regional_data = data.dropna(subset=['Regionname'])
    
    # Find combinations between regions and suburbs with occurrence count
    suburb_region_mapping = regional_data.groupby(['Suburb', 'Regionname']).size().reset_index(name='count')
    
    # Count how many times each suburb appears with different regions
    suburb_region_count = suburb_region_mapping.groupby('Suburb').size().reset_index(name='count')
    
    # Ensure each suburb is associated with only one region
    for _, row in suburb_region_count.iterrows():
        if row['count'] != 1: 
            multiple_region_suburb = suburb_region_mapping[suburb_region_mapping['Suburb'] == row['Suburb']]
            total_suburb_count = multiple_region_suburb.groupby('Suburb', as_index=False).sum()
            
            suburb_region_mapping = suburb_region_mapping.drop(
                suburb_region_mapping[
                    (suburb_region_mapping['Suburb'] == row['Suburb']) & 
                    (suburb_region_mapping['count'] < total_suburb_count.iloc[0]['count'] * 0.90)
                ].index
            )
    return suburb_region_mapping

# Function to request the name of the JSON file to be loaded
def get_json_filename():
    filename = input("Enter the name of the JSON file to load (default: data.json): ").strip()
    return filename if filename else "data.json"

def main(): 
    indexes_to_remove = []
    
    # Get the filename of the JSON file to be parsed
    filename = get_json_filename()

    # Load data
    data = pd.read_json(filename)

    # Remove rows with missing values in important columns
    data = data.dropna(subset=['Price'])
    data = data.dropna(subset=['Suburb'])
    
    # Create mapping of suburbs to regions
    suburb_region_mapping = create_suburb_regionname_mapping(data)
    
    # Correct invalid data and mark incorrect rows for deletion
    for index, row in data.iterrows():
        matching_region = suburb_region_mapping[suburb_region_mapping['Suburb'] == row['Suburb']]
        
        if matching_region.empty:
            indexes_to_remove.append(index)
        elif row['Regionname'] != matching_region.iloc[0]['Regionname']:
            data.at[index, 'Regionname'] = matching_region.iloc[0]['Regionname']
    
    # Drop incorrect rows
    data = data.drop(indexes_to_remove)

if __name__ == "__main__":
    main()
