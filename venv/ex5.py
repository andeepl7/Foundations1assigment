
"""
Assignment II

"""
valid_courses = ["Python Programming", "Data Mining and Machine Learning", "Visual Analytics",
                              "Text Analytics"]
class DiplomaProgramme:


    def __init__(self):

        self.courses = []

    def add_course(self, course):
        if course in valid_courses:
            self.courses.append(course)
        else:
            raise Exception('The course is not part of the programme, select a valid one:', valid_courses)

    def remove_course(self,course):
        self.courses.remove(course)



#class Courses(object):


primerintento = DiplomaProgramme()
primerintento.add_course("Python")
print(primerintento.courses)

#class Student(object):

