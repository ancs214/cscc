"""
FILE_NAME: csv-homework.py
AUTHOR: Ashley-Noel Swarn
DATE: 3/8/2026
PURPOSE: Create a program that accepts a csv file, replaces bad data from a specific column name
and replaces with good data. Outputs a new csv file with corrected information.
"""

import csv


def csv_correction(
        input_file,
        column_name,
        bad_data_value,
        replacement_value,
        output_file_name
    ):
    """
    Function to correct bad data from a specific column in a csv file.
    Args: csv file, column with bad data, bad data value, replacement value, and
    desired output file name.
    """
    # empty starter list that will contain dictionaries (or rows)
    all_data = []

    # open input file
    with open(input_file, newline='') as csv_file_in:
        # use DictReader to create an object that reads and maps information in each row to a dict
        reader = csv.DictReader(csv_file_in)

        for row in reader:
            # if row has bad data, change bad data to replacement value
            if row[column_name] == bad_data_value:
                row[column_name] = replacement_value
            # add all rows to our empty string
            all_data.append(row)

    # open new file for writing
    with open(output_file_name, 'w', newline='') as csv_file_out:
        # get headers from first dictionary in list (column names)
        headers = all_data[0].keys()

        # create writer to include headers
        writer = csv.DictWriter(csv_file_out, fieldnames=headers)

        # write header and all dictionaries from all_data list to csv file
        writer.writeheader()
        writer.writerows(all_data)

    return all_data


csv_correction(
    'unit_7_restaurant_rating.csv',
    'Worth_the_price',
    '45',
    'no',
    'corrected_file.csv'
    )