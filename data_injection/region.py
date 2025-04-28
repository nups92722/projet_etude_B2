def insert_data_into_region_table(bdd, data) :
    data = data['Regionname'].dropna().unique()
    print("données:")
    print(data)
    data_tuples = [(region,) for region in data]
    bdd.multiple_injections("INSERT INTO region (label) VALUES (%s)", data_tuples)