#Program to record a student's academic performance

def letter_grade(num_grade):
    if 100 >= num_grade >= 90:
        letter = 'A'
    elif 89 >= num_grade >= 80:
        letter = 'B'
    elif 79 >= num_grade >= 70:
        letter = 'C'
    elif 69 >= num_grade >= 60:
        letter = 'D'
    else:
        letter = 'F'

    return letter

print("Display student records from the user...\n")

student_name = input("Enter student name:")

student_address = input("Enter student address:")

student_grade = int(input("Enter student grade:"))

letter_returned= letter_grade(student_grade)

print('The student name is {}. They live at {}. They have a numeric grade of {} and a letter grade of {}.'
      .format(student_name, student_address, student_grade, letter_returned))
