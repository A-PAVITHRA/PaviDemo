from get_excel import process_sheet_data
from manage import req_crop_year
from readfile import read_excel_file, perform_excel_read


def runapp():
    """
       Main function to execute the application.

       This function reads an Excel file, processes the sheet data using process_sheet_data function,
       and then calls the req_crop_year function with the processed data.

       Raises:
       - Exception: An error message is displayed if any exception occurs during execution.
       """
    try:
        # Call the function to read the Excel file and get the DataFrame
        sheet_data = perform_excel_read()

        # Display the DataFrame to the console
        # print("df read here:", sheet_data)

        # Check if the DataFrame is not None
        if sheet_data is not None:
            # Call the process_sheet_data method
            processed_data = process_sheet_data(sheet_data)
            print('11', processed_data)
            req_crop_year(processed_data)


        else:
            # Display a message if the DataFrame is None
            print("DataFrame is None. Unable to proceed with the onboarding process.")
            print("Pavi")
            print("demo")
            print("testing")

    except Exception as e:
        # Display an error message if an exception occurs
        print(f"An error occurred: {e}")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    runapp()


