#!/usr/bin/env python3
# Author ID: rfrancisco6

class Student:

    # Define the name and number when a student object is created, ex. student1 = Student('john', 025969102)
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.courses = {}

    # Return student name and number in a formatted string
    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + str(self.number)

    # Add course and grade to the student's record
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate the grade point average of all courses and return a string
    def displayGPA(self):
        gpa = 0.0   # set GPA to 0
        for course in self.courses.keys():  # Loop
            gpa = gpa + self.courses[course]    # Add grade
        
        # Prevent division by zero
        if len(self.courses) > 0:
            total_gpa = gpa / len(self.courses)     # Calculate
        else:
            total_gpa = 0.0     # Set GPA to 0
        
        return 'GPA of student ' + self.name + ' is ' + str(total_gpa)

    # Return a list of passed courses (non-0.0 grades)
    def displayCourses(self):
        passed_course_codes = []    # Initialize list
        
        for course_code in self.courses.keys(): # Loop course names
            if self.courses[course_code] > 0: # Check grade
                passed_course_codes.append(course_code) # Add to list
                
        return passed_course_codes

if __name__ == '__main__':
    # Create first student object and add grades for each class
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades for each class
    student2 = Student('Jessica', '123456')
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display information for student1 object
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display information for student2 object
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())