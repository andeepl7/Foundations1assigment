"""
Assignment II
"""
import random

class UniqueId:
    unique_id = 100000

    def get_next_id(self):
        UniqueId.unique_id += 1
        return UniqueId.unique_id

class DiplomaProgramme:
    def __init__(self):
        self.courses = {"Python Programming": Course("Python Programming"),
                        "Data Mining and Machine Learning": Course("Data Mining and Machine Learning"),
                        "Visual Analytics": Course("Visual Analytics"),
                        "Text Analytics": Course("Text Analytics")
                        }
        self.students = {}
        self.pass_limit = 12
        self.pass_distinction_limit = 16

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

    def print_courses(self):
        print(self.courses.keys())

    def list_courses(self):
        return self.courses

    def register_students(self, students):
        for student in students:
            self.students[student.get_id()] = student
            # Automatically add student to diploma´s courses
            for course in self.courses.keys():
                self.courses[course].add_student(student)

    def list_students(self):
        print("Diploma Students")
        for student_id in self.students.keys():
            print(student_id,
                  self.students[student_id].name,
                  self.students[student_id].lastname)

    def diploma_scores(self):
        students_scores = {}
        for student_id, student in self.students.items():
            assignment_score = 0
            # Calculating student score by iterating through each course
            for course in student.courses_enrolled():
                # Get Grades for student, per course enrolled
                assignment_score += student.student_grades(course).count("PASS")
            students_scores[student.get_id()] = self.score_description(assignment_score)
        print("Assignment Score")
        print(students_scores)

    def score_description(self,score):
        if score > self.pass_distinction_limit:
            return 'PASS with distinction'
        if score > self.pass_limit:
            return 'PASS'
        return 'FAIL'



class Student:
    def __init__(self, name, lastname, dob):
        self.name = name
        self.lastname = lastname
        self.dob = dob
        self.id = self.create_id()
        # {"Course1": [PASS, FAIL, PASS, PASS],
        #  "Course2": [PASS, PASS, PASS]}
        self.courses_grades = {}

    def enroll_to_course(self, course_name):
        self.courses_grades[course_name] = ["UNGRADED", "UNGRADED", "UNGRADED", "UNGRADED", "UNGRADED"]

    def get_id(self):
        return self.id

    def create_id(self):
        u = UniqueId()
        full_name = self.name[:2].upper(), self.lastname[:2].upper()
        full_name_reduced = ''.join(full_name)
        return full_name_reduced + str(u.get_next_id())

    def courses_enrolled(self):
        return list(self.courses_grades.keys())

    def print_student_grades(self):
        for course in self.courses_grades.keys():
            print(f"Course {course}: {self.courses_grades[course]}")

    def student_grades(self, course_name):
        return self.courses_grades[course_name]

    def student_info(self):
        print("-"*20)
        print('Student info: ')
        print(self.name, self.lastname, self.id)
        print('The student is enrolled in this courses: ')
        for enrolled_course in self.courses_enrolled():
            print(f'Assignment grades/{enrolled_course}')
            print(self.student_grades(enrolled_course))
        print("-"*16)


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students_enrolled = []

    def get_student(self, student_id):
        for course_student in self.students_enrolled:
            if student_id == course_student.get_id():
                return course_student
        print(f"Student with student_id {student_id} not found")
        return None

    def add_student(self, student):
        if student in self.students_enrolled:
            raise Exception('The student is already assigned')
        else:
            self.students_enrolled.append(student)
            student.enroll_to_course(self.course_name)

    def remove_student(self, student_id):
        for student in self.students_enrolled:
            if student.get_id() == student_id:
                self.students_enrolled.remove(student)

    def all_students(self):
        for a in self.students_enrolled:
            a.student_info()
        # print(self.students_enrolled)

    def grade_student(self, student_id):
        student = self.get_student(student_id)
        if student is not None:
            student_grades = student.courses[self.course_name]
            assignment_score = 0
            for grade in student_grades:
                if grade == "PASS":
                    assignment_score += 1
            return assignment_score, self.pass_course(assignment_score)

    def pass_course(self, assignment_score):
        if assignment_score >= 3:
            return True
        return False


    def grade_assignments(self, student_id, grades):
        student = self.get_student(student_id)
        if student is not None:
            student.courses_grades[self.course_name] = grades

    def get_student_grades(self, student_id):
        student = self.get_student(student_id)
        if student is not None:
            return student.courses_grades[self.course_name]

# Testing section
grades_test_pass = ["PASS", "FAIL", "PASS", "PASS", "PASS"]
grades_test_fail = ["PASS", "FAIL", "FAIL", "FAIL", "PASS"]
grades_test_pass_distinction = ["PASS", "PASS", "PASS", "PASS", "PASS"]

def test_diploma():
    diploma = DiplomaProgramme()
    diploma.print_courses()
    diploma.add_course("Big Data")
    diploma.add_course("Cybersecurity")
    diploma.print_courses()
    diploma.remove_course("Big Data")
    diploma.print_courses()
    diploma.add_course("Cybersecurity")
    diploma.remove_course("Storytelling")
    diploma.print_courses()

def test_diploma_student(students):
    diploma = DiplomaProgramme()
    diploma.register_students(students)
    diploma.list_students()
    print("Courses per Student")
    for s in students:
        print(s.get_id(), s.courses_enrolled())
    for course_name, course in diploma.list_courses().items():
        course.grade_assignments('ANPE100002', grades_test_fail)
        course.grade_assignments('ANGO100003', grades_test_pass_distinction)
        course.grade_assignments('ROPE100001', grades_test_pass)
    diploma.diploma_scores()

def test_course_class(course_students):
    python_programming = Course(course_name="Python Programming")
    for student in course_students:
        python_programming.add_student(student)
    python_programming.grade_assignments('ANPE100002', grades_test_fail)
    python_programming.grade_assignments('ANGO100003', grades_test_pass_distinction)
    python_programming.grade_assignments('ROPE100001', grades_test_pass)

    data_mining = Course(course_name="Data Mining and Machine Learning")
    for student in course_students:
        data_mining.add_student(student)
    data_mining.grade_assignments('ANPE100002', grades_test_fail)
    data_mining.grade_assignments('ANGO100003', grades_test_pass_distinction)
    data_mining.grade_assignments('ROPE100001', grades_test_pass)

    visual_analytics = Course(course_name="Visual Analytics")
    for student in course_students:
        visual_analytics.add_student(student)
    visual_analytics.grade_assignments('ANPE100002', grades_test_fail)
    visual_analytics.grade_assignments('ANGO100003', grades_test_pass_distinction)
    visual_analytics.grade_assignments('ROPE100001', grades_test_pass)

    text_analytics = Course(course_name="Text Analytics")
    for student in course_students:
        text_analytics.add_student(student)
    text_analytics.grade_assignments('ANPE100002', grades_test_fail)
    text_analytics.grade_assignments('ANGO100003', grades_test_pass_distinction)
    text_analytics.grade_assignments('ROPE100001', grades_test_pass)
    #course_students[0].student_info()


if __name__ == '__main__':
    student_info = [
        {"name": "Rocio", "surname": "Pereyra", "dob": "100795"},
        {"name": "Andrea", "surname": "Perez", "dob": "071290"},
        {"name": "Andres", "surname": "Gonzalez", "dob": "250886"},
    ]

    students = []
    for student in student_info:
        s = Student(name=student["name"],
                    lastname=student["surname"],
                    dob=student["dob"])
        #s.student_info()
        students.append(s)

    test_diploma_student(students)
    #test_course_class(students)

    for s in students:
        s.student_info()
