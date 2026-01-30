#Creating a program with default parameters

#Function to display a student's detail information
#default parameter must be the last parameter stated when defining the function
def student_details(name, rank=10, score=60.50):
    print("\nStudent Name = ", name)
    print("Student Rank =", rank)
    print("Student Score =", score)

student_details(name="Jack", rank=5, score=50.50)
student_details(name="Tim")
student_details(name="Corelone", rank=1001)