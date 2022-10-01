"""
Assignment II
"""
import random


class UniqueId:
    unique_id = 100000

    def get_next_id(self):
        UniqueId.unique_id += 1
        return UniqueId.unique_id


def menu():
    print('Welcome to the CBS manage system for the Diploma (Minor) programme for Data Science, '
          '\n please choose number to continue: ')
    print('1 to Add a Course')
    print('2 to Delete a Course')
    print('3 to Create a student')
    print('4 to Add an Student to a course')
    print('5 to Remove an Student from a course')
    print('6 to Grade an assignment')
    print('7 to Check the status of your course')
    print('8 to Check students list with grades')
    print('9 to quit')


def main():
    menu()
    t = int(input('Enter menu choice: '))

    if t == 1:
        add_course()
    elif t == 2:
        remove_course()
    elif t == 3:
        option3()
    elif t == 4:
        option4()
    elif t == 5:
        option5()
    elif t == 6:
        option6()
    elif t == 7:
        option7()
    else:
        pass
    main()


class DiplomaProgramme:
    def __init__(self):
        self.courses = {"Python Programming": Course("Python Programming"),
                        "Data Mining and Machine Learning": Course("Data Mining and Machine Learning"),
                        "Visual Analytics": Course("Visual Analytics"),
                        "Text Analytics": Course("Text Analytics")
                        }

    def add_course(self, course_name):
        if course_name in self.courses.keys():
            print("Course already exists, will not add it")
        else:
            self.courses[course_name] = Course(course_name)

    def remove_course(self, course_name):
        if course_name not in self.courses.keys():
            print('Course does not exist, will not remove it')
        else:
            self.courses.pop(course_name)

    def list_courses(self):
        print (self.courses.keys())

    def list_students_passed(self):
        pass

    def list_students_distinction(self):
        pass


class Student:
    def __init__(self, name, lastname, dob):
        self.name = name
        self.lastname = lastname
        self.dob = dob
        self.id = self.create_id()
        # {"Course1": [PASS, FAIL, PASS, PASS],
        #  "Course2": [PASS, PASS, PASS]}
        self.courses = {}

    def enroll_to_course(self, course):
        self.courses[course.name] = course.assignments

    def get_id(self):
        return self.id

    def create_id(self):
        u = UniqueId()
        full_name = self.name[:2].upper(), self.lastname[:2].upper()
        full_name_reduced = ''.join(full_name)
        return full_name_reduced + str(u.get_next_id())

    def courses_enrolled(self):
        print ( )

    def student_grades(self):
        pass

    def student_info(self):
        print('Student info: ')
        print(self.name, self.lastname, self.id)
        # print('The student is enrol in this courses: ', courses)
        # print('The grades of its assignments are:')


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students_enrolled = []

    def add_student(self, student_id, diploma_student_list):

        # List of Dictionary of students:
        # Key : Value
        # student_id: student_object
        diploma_students = [dict({s.get_id(): s}) for s in diploma_student_list]

        for diploma_student in diploma_students:
            if student_id in diploma_student.keys():
                if diploma_student[student_id] in self.students_enrolled:
                    raise Exception('The student is already assigned')
                else:
                    self.students_enrolled.append(diploma_student[student_id])

    def remove_student(self, student_id):
        for student in self.students_enrolled:
            if student.get_id() == student_id:
                self.students_enrolled.remove(student)

    def all_students(self):
        for a in self.students_enrolled:
            a.student_info()
        # print(self.students_enrolled)

    def grade_student(self, student_id, assignment_number, grade):
        if type(grade) is not string:
            raise Exception("The grade could only be Pass or Fail")
        if assignment_number > 5:
            raise Exception('The course cannot has more than 5 assignments')
        if student_id in diploma_student_list:
            self.assigment_number = assignment_number
            self.grade = grade
        else:
            raise Exception('The student is not enrol in this course')


# Testing section

def test_diploma():
    diploma = DiplomaProgramme()
    diploma.list_courses()
    diploma.add_course("Big Data")
    diploma.add_course("Cybersecurity")
    diploma.list_courses()
    diploma.remove_course("Big Data")
    diploma.list_courses()
    diploma.add_course("Cybersecurity")
    diploma.remove_course("Storytelling")
    diploma.list_courses()


def test_course_class(course_students):
    course_name = "Maths"
    my_course = Course(course_name=course_name)
    my_course.add_student('ANPE071290', course_students)
    my_course.add_student('ALCA100795', course_students)
    my_course.remove_student('ALCA100795')
    my_course.all_students()



if __name__ == '__main__':
    num_students = 1000
    student_info = [
        {"name": "Alessandro", "surname": "Catania", "dob": "100795"},
        {"name": "Andrea", "surname": "Perez", "dob": "071290"},
        {"name": "Davide", "surname": "Catania", "dob": "250886"},
    ]

    students = []
    for student in student_info:
        s = Student(name=student["name"],
                    lastname=student["surname"],
                    dob=student["dob"])
        s.student_info()
        students.append(s)

    test_course_class(students)
    test_diploma()
