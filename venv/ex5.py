
"""
Assignment II

"""


def menu():
    print('Welcome to the CBS manage system for the Diploma (Minor) programme for Data Science, \n please choose number to continue: ')
    print('1 to Add a Course')
    print('2 to Delete a Course')
    print('3 to Add an Student')
    print('4 to Remove an Student')
    print('5 to Grade an assignment')
    print('6 to Check the status of your course')
    print('7 to Check students list with grades')
    print('8 to quit')

def choice():
    choice = int(input('Enter menu choice: '))
    return choice

def main():
    menu()
    t = choice()

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
        option8()
    main()


class DiplomaProgramme:
    VALID_COURSES = ["Python Programming", "Data Mining and Machine Learning", "Visual Analytics", "Text Analytics"]

    def __init__(self):
        self.courses = []

    def add_course(self, course):
        if course in self.VALID_COURSES:
            if course in self.courses:
                raise Exception('The course is already added')
            else:
                self.courses.append(course)
        else:
            raise Exception('The course is not part of the programme, select a valid one:', self.VALID_COURSES)

    def remove_course(self, course):
        if not self.courses:
            raise Exception('No more courses to remove')
        else:
            self.courses.remove(course)

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
        print(self.dob)

    def get_id(self):
        return self.id

    def create_id(self):
        full_name = self.name[:2].upper(), self.lastname[:2].upper()
        full_name_reduced = ''.join(full_name)
        return full_name_reduced + self.dob

    def courses_enrolled(self):
        pass

    def student_grades(self):
        pass

    def student_info(self):
        print(name + lastname)
        pass

class Course:
    def __init__(self):
        self.students_enrolled = []
        pass

    def add_student(self, student_id, diploma_student_list):

        id_list = [s.get_id() for s in diploma_student_list]

        if student_id in id_list:  # if student in masters programme
            for s in self.students_enrolled:  # check if student is already enrolled in course
                if student_id == s.get_id():
                    raise Exception ("The student is already assigned")
            else:

                self.students_enrolled.append()
        else:
            raise Exception("The student is not in programme")

    def remove_student(self, student_id):
        pass

    def grade_student(self, studend_id, assignment, grade):
        pass




# Testing section

def test_add_course(course_name):
    primerintento = DiplomaProgramme()
    primerintento.add_course(course_name)
    print(primerintento.courses)


def test_construct_student_id():
    student_dict = {"name": "Alolels",
                    "lastname": "lsadldl",
                    "dob": "10071995"}
    s = Student(**student_dict)
    s.create_id()
    #print(s.get_name())

if __name__ == '__main__':
    #test_add_course("Bla")
    num_students = 1000
    names = ["Alessandro", "Andrea", "Davide"]
    surnames = ["Catania", "Perez", "Catania"]
    dob = ["100795", "071290", "250886"]
    students = []
    for n in range(len(names)):
        students.append(Student(name=names[n],
                                lastname=surnames[n],
                                dob=dob[n]))
    print(f"My wonderful student {students[1].get_id()}")

    test_construct_student_id()
