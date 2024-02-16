import pandas as pd

def read_excel_file(excel_file_path, sheet_names):
    """
       Read specified sheets from an Excel file and store them in a dictionary.

       This function takes an Excel file path and a list of sheet names as input. It reads each
       specified sheet from the Excel file and stores the corresponding DataFrame in a dictionary.

       Parameters:
       - excel_file_path (str): The file path of the Excel file.
       - sheet_names (list): List of sheet names to read from the Excel file.

       Returns:
       - dict: A dictionary containing DataFrames for each specified sheet. Returns None if an error occurs.
       """
    try:
        # Initialize an empty dictionary to store DataFrames for each sheet
        sheet_data = {}

        # Read each sheet and store it in the dictionary
        for sheet_name in sheet_names:
            try:
                df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
                sheet_data[sheet_name] = df
            except FileNotFoundError:
                print(f"Sheet {sheet_name} not found in Excel file. Skipping.")

        return sheet_data

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
def perform_excel_read():
    """
      Perform the reading of an Excel file with specified sheets.

      This function sets the Excel file path, specifies the sheet names to read, and then calls
      the 'read_excel_file' function to read the Excel file and retrieve the sheet data.

      Returns:
      - dict: A dictionary containing DataFrames for each specified sheet. Returns None if an error occurs.
      """
    # Set the Excel file path directly
    excel_file_path = r'C:\cropyear\crop year.xlsx'

    # Specify the sheet names to read
    sheet_names = ['cropyear', 'configuration_mr_master', 'configuration_master']

    # Call the function to read the Excel file
    sheet_data = read_excel_file(excel_file_path, sheet_names)

    return sheet_data
