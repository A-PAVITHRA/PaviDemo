
def process_sheet_data(sheet_data):
    """
       Process the given sheet data and extract relevant information.

       Parameters:
       - sheet_data (dict): A dictionary containing DataFrames for different sheets.

       Returns:
       - data (dict): A dictionary containing processed data from different sheets.
       """
    data = {}

    # Process 'cropyear' sheet data
    cropyear_df = sheet_data.get('cropyear')
    if cropyear_df is not None:
        # year_value = cropyear_df['year'].iloc[0]
        year_value = int(cropyear_df['year'].iloc[0])

        print(f'Value for year in "cropyear" sheet: {year_value}')
        data['year_value'] = year_value
    else:
        print("DataFrame for 'cropyear' sheet is None. Unable to proceed with the onboarding process.")

    # Process 'configuration_mr_master' sheet data
    configuration_mr_master_df = sheet_data.get('configuration_mr_master')
    if configuration_mr_master_df is not None:
        # Add your logic for processing 'configuration_mr_master' DataFrame if needed
        column_data = {'year': [], 'category': [], 'mr_min': [], 'mr_max': []}

        for index, row in configuration_mr_master_df.iterrows():
            for column_name in column_data.keys():
                column_value = row[column_name]
                column_data[column_name].append(column_value)

        # Now you have a dictionary with lists for each column
        print(column_data['year'])
        print(column_data['category'])
        print(column_data['mr_min'])
        print(column_data['mr_max'])

        # Add processing logic and append data to configuration_mr_master_data
        # For example: configuration_mr_master_data.append(process_row(row))

        data['configuration_mr_master_data'] = column_data
    else:
        print("DataFrame for 'configuration_mr_master' sheet is None. Skipping.")

    # Process 'configuration_master' sheet data
    configuration_master_df = sheet_data.get('configuration_master')
    if configuration_master_df is not None:
        # Assuming you want to take the 'config_value' from the first row of the DataFrame
        config_value = configuration_master_df['config_value'].iloc[0]

        # Add your logic for processing 'configuration_master' DataFrame if needed
        print(f'DataFrame for "configuration_master" sheet:', config_value)
        # For example: configuration_master_data = process_dataframe(configuration_master_df)
        data['config_value'] = config_value
    else:
        print("DataFrame for 'configuration_master' sheet is None. Skipping.")

    return data


