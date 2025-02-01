def get_average_construction_year_by_suburb(data):
    # Remove rows with no region name
    data_with_construction_year = data.dropna(subset=['YearBuilt'])
    
    # group the lines by suburbs, count their number and average their year of construction
    average_construction_year_by_suburb = data_with_construction_year.groupby('Suburb').agg(
        average_construction_year=('YearBuilt', 'mean'),
        count=('YearBuilt', 'count')
    ).reset_index()
    
    # deletes lines containing an average based on too few values
    average_construction_year_by_suburb = average_construction_year_by_suburb[average_construction_year_by_suburb['count'] >= 1]
    
    return (average_construction_year_by_suburb)


def parsing_construction_year(data) :
    # List to store the indexes of rows that should be removed from the dataset
    indexes_to_remove = []

    # creates the table showing the average years of construction per suburb
    average_construction_year_by_suburb = get_average_construction_year_by_suburb(data)

    # Correct invalid data and mark incorrect rows for deletion
    for index, row in data.iterrows():
        matching_region = average_construction_year_by_suburb[average_construction_year_by_suburb['Suburb'] == row['Suburb']]
        
        if matching_region.empty:
            indexes_to_remove.append(index)
        elif row['YearBuilt'] != matching_region.iloc[0]['average_construction_year']:
            data.at[index, 'YearBuilt'] = matching_region.iloc[0]['average_construction_year']
    
    # Drop incorrect rows
    data = data.drop(indexes_to_remove)

    print ("End function : get_average_construction_year_by_suburb")
    
    return (data)