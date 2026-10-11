# list of three students named Jon, Kim and Lee
students = ["Jon", "Kim", "Lee"]
students.append("Sara")
students.append("Miko")

# function to print ‘Hi name’ for each student in the list and show the total number of students
def greet_students(students):
    print(f"Total number of students: {len(students)}")
    for student in students:
        print(f"Hi {student}")

# call the function
greet_students(students)