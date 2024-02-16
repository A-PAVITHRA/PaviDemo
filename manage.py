from methods import crop_year, configuration_mr_master, configuration_master


def req_crop_year(data):
    """
       Perform the required operations based on the input data.

       This function extracts relevant information from the input dictionary and calls
       methods from the 'methods' module to process crop year, configuration master,
       and configuration master data.

       Parameters:
       - data (dict): A dictionary containing processed data, including 'year_value', 'config_value',
         and 'configuration_mr_master_data'.

       Prints:
       - Output messages and results of the called methods.

       Returns:
       - None
       """
    year_value = data.get('year_value')
    print('yv', year_value)
    config_value = data.get('config_value')
    print('ii', config_value)
    # Extract data from the input dictionary
    master_data = data['configuration_mr_master_data']
    print('mst', master_data)
    years_list = master_data.get('year')

    category_list = master_data.get('category')
    mr_min_list = master_data.get('mr_min')
    mr_max_list = master_data.get('mr_max')

    # Call the crop_year method
    crop_year(year_value)
    configuration_mr_master_result = configuration_mr_master(years_list, category_list, mr_min_list, mr_max_list)
    print(configuration_mr_master_result)
    configuration_master(config_value)
    print("test")
    print("demo")
    print("to do")

