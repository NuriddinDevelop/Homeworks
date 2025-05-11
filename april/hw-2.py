import random
id_list = []
student_courses = {}
professor_courses = {}
class Person:
    def __init__(self, name,surname, age):
        self.name = name.lower()
        self.surname = surname.lower()
        self.age = age


class Student(Person):
    def __init__(self, name, surname, age, courses_stu):
        super().__init__(name, surname, age)
        j = 1
        while j: 
            self.__student_id = random.randint(100, 1000)
            if self.__student_id not in id_list:
                j = 0
        self.courses_stu = []
        a = courses_stu.split(",")
        for itm in a:
            self.courses_stu.append(itm.lower())
        student_courses[self.name] = self.courses_stu
        id_list.append(self.__student_id)

    def enrol(self, course_name):
        print(self.courses_stu)
        a = self.courses_stu
        if course_name.lower() in self.courses_stu:
            a.remove(course_name.lower())
            self.courses_stu = a
        else:
            print("Course not found")

        return self.courses_stu
    def get_stu_courses(self):
        return self.courses_stu
    

class Professor(Person):
    def __init__(self, name, surname, age, courses_prof):
        super().__init__(name, surname, age)
        j = 1
        while j: 
            self.__student_id = random.randint(100, 1000)
            if self.__student_id not in id_list:
                j = 0
        self.courses_prof = []
        a = courses_prof.split(",")
        for itm in a:
            self.courses_prof.append(itm.lower())
        professor_courses[self.name] = self.courses_prof
        id_list.append(self.__student_id)

    def add_course(self, course_name):
        course_name = course_name.lower()
        a = self.courses_prof
        a.append(course_name)
        self.courses_prof = a

    def get_prof_courses(self):
        return self.courses_prof
    
class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        students = []
        professors = []
        for stu_cour in student_courses:
            if self.course_name.lower() in student_courses[stu_cour]:
                students.append(stu_cour)
        self.students = students

        for prof_cour in professor_courses:
            if self.course_name.lower() in professor_courses[prof_cour]:
                professors.append(prof_cour)
        self.professors = professors

    def add_student(self, name):
        name = name.lower()
        if name in student_courses.keys():
            a = self.students
            a.append(name)
            self.students = a
        else:
            print("Student not found!")
    def get_info(self):
        print(f"\nCourse-name: {self.course_name}")
        print(f"Professors: {self.professors}({len(self.professors)})")
        print(f"Students: {self.students}({len(self.students)})")
        print("")

stu1 = Student("Bob","Teshaboyev",20,"Python,JS,HTML,Css,expressJS")
stu2 = Student("Anvar","Boltaboyev",60,"HTML,Css")
stu3 = Student("Tyson","Saturn",60,"HTML,Css,JS,ReactNative")
stu1.enrol("HTML")
stu1.get_stu_courses()

prof1 = Professor("Avazbek","Do'stmuhammedov",25,"HTML,Css,JS,Python")
prof2 = Professor("Humoyun","Yarashev",25,"HTML,Css,JS,expressJS")
prof3 = Professor("Bomj","Azimov",99,"HTML,Css,JS,ReactNative")
prof1.get_prof_courses()
prof2.add_course("Python")

course1 = Course("HTML")
course2 = Course("Css")
course3 = Course("JS")
course4 = Course("Python")
course5 = Course("ReactNative")
course6 = Course("expressJS")
course5.add_student("Bob")
course1.get_info()
course2.get_info()
course3.get_info()
course4.get_info()
course5.get_info()
course6.get_info()

print(student_courses)
print(professor_courses)