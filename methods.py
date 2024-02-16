from utils.utils import my_custom_sql
from mysql.connector import Error

def crop_year(year_value):
    """
       Insert a new record into the 'cropyear' table.

       This function constructs an SQL query to insert a new record with the provided year value
       into the 'cropyear' table. It uses the 'my_custom_sql' function for SQL execution.

       Parameters:
       - year_value (int): The year value to be inserted.

       Returns:
       - str: A message indicating the success of the SQL execution.
       """
    try:
        sql = '''
       INSERT INTO `visualizer2`.`cropyear` (`year`, `status`, `createdBy`, `createdAt`)
        VALUES ('%s', '1', 'Admin', now());
        '''

        args = [int(year_value)]
        print(f"SQL Query 1: {sql}")
        print(f"SQL Arguments 1: {args}")

        # Execute the INSERT query
        crop_year = my_custom_sql(sql, args)
        print("crop_year", crop_year)
        return crop_year


    except Error as e:
        print(f"Error in SQL execution: {e}")
        # Handle the error as needed, e.g., log the error, raise an exception, etc.
        # You may choose to return a specific value or raise a custom exception here.

def configuration_mr_master(year, category, mr_min, mr_max):
    """
       Insert new records into the 'configuration_mr_master' table.

       This function constructs an SQL query to insert new records with the provided lists of
       'year', 'category', 'mr_min', and 'mr_max' values into the 'configuration_mr_master' table.
       It uses the 'my_custom_sql' function for SQL execution.

       Parameters:
       - year (list): List of years.
       - category (list): List of categories.
       - mr_min (list): List of minimum values.
       - mr_max (list): List of maximum values.

       Returns:
       - str: A message indicating the success of the SQL execution.
       """
    try:
        sql = '''
         INSERT INTO `visualizer2`.`configuration_mr_master` 
              (`year`, `category`, `mr_min`, `mr_max`, `createdBy`, `createdAt`) 
              VALUES
        '''

        # Create a list of value tuples
        values_tuples = []
        for i in range(len(year)):
            values_tuples.append(
                f"('{year[i]}', '{category[i]}', '{mr_min[i]}', '{mr_max[i]}', 'Admin', NOW())"
            )

        # Concatenate the tuples and add them to the SQL query
        sql += ', '.join(values_tuples)
        args = []
        print(f"SQL Query: {sql}")

        # Execute the INSERT query
        configuration_mr_master_result = my_custom_sql(sql, args)
        print(f"Configuration_MR_Master Result: {configuration_mr_master_result}")

        return "Successfully inserted data into configuration_mr_master table"

    except Error as e:
        print(f"Error in SQL execution: {e}")
        # Handle the error as needed, e.g., log the error, raise an exception, etc.
        # You may choose to return a specific value or raise a custom exception here.


def configuration_master(config_value):
    """
       Update a record in the 'configuration_master' table.

       This function constructs an SQL query to update the 'config_value' of the record with ID 1
       in the 'configuration_master' table. It uses the 'my_custom_sql' function for SQL execution.

       Parameters:
       - config_value: The new value to be set for 'config_value'.

       Returns:
       - str: A message indicating the success of the SQL execution.
       """
    try:
        sql = '''
    UPDATE `visualizer2`.`configuration_master` SET `config_value` = %s WHERE (`id` = '1');
        '''

        args = [config_value]
        print(f"SQL Query 1: {sql}")
        print(f"SQL Arguments 1: {args}")

        # Execute the INSERT query
        configuration_master = my_custom_sql(sql, args)
        print("configuration_master", configuration_master)
        return configuration_master


    except Error as e:
        print(f"Error in SQL execution: {e}")
        # Handle the error as needed, e.g., log the error, raise an exception, etc.
        # You may choose to return a specific value or raise a custom exception here.

