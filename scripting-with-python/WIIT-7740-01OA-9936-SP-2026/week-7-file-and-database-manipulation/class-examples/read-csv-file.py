import csv

file = 'C:/Users/ancs2/PycharmProjects/cscc/scripting-with-python/WIIT-7740-01OA-9936-SP-2026/week-7-file-and-database-manipulation/class-examples/MOCK_DATA.csv'
# open file for reading and writing to
with open(file, 'r+') as f:
    mock_data_reader = csv.reader(f)

    line_count = 1
    users = []
    for row in mock_data_reader:
        """Take a csv file and create a list of dictionaries containing user name, surname, and email"""
        if line_count > 1:
            name = row[1]
            surname = row[2]
            email = row[3]
            users.append({'name':name, 'surname':surname, 'email':email})
        line_count += 1

    for user in users:
        print(user)