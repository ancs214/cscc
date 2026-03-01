
import csv

# # read csv file and output list of dictionaries containing 3rd column and values
# file = 'C:/Users/ancs2/PycharmProjects/cscc/scripting-with-python/WIIT-7740-01OA-9936-SP-2026/week-7-file-and-database-manipulation/homework/unit_7_restaurant_rating.csv'
#
# # open file for reading and writing to
# with open(file, 'r+') as f:
#     file_reader = csv.reader(f)
#
#     line_count = 1
#     ratings = []
#     for column in file_reader:
#         """Take a csv file and create a list of dictionaries containing user name, surname, and email"""
#         if line_count > 1:
#             worth_it = column[3]
#             ratings.append({'Worth_it' : worth_it})
#         line_count += 1
#
#     for rating in ratings:
#         print(rating)


with open('unit_7_restaurant_rating.csv') as csvfile:
    # use DictReader to create an object that reads and maps information in each row to a dict
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Worth_the_price'])


# Create the function with 5 parameters:
# (Input file, Output file, Column name, Bad value, Replacement value)
def new_csv(input_file, output_file, column_data, bad_data, replacement_value):
    print(input_file, output_file, column_data, bad_data, replacement_value)

