# 1

class Vehicle: # Vehicle nomli class ochildi.
    def __init__(self, color, year): # color va year parametrlarini qabul qiladi.
        self.color = color # color public xususiyat sifatida saqlanadi.
        self.year = year # year ham public xususiyat sifatida saqlanadi.

    def start_engine(self): # start_engine funksiyasi - motorni ishga tushirishga oid.
        print("Dvigitel ishga tushdi!") # Terminalga "Dvigitel ishga tushdi!" chiqadi.

class Bike(Vehicle): # Vehicle klassidan meros olgan Bike klassi.
    def __init__(self, color, year, model): # Yangi parametr: model.
        super().__init__(color, year) # color va year ni Vehicle ga uzatadi.
        self.model = model # model ham xususiyat sifatida saqlanadi.

    def ring_bell(self): # ring_bell funksiyasi - signal chalish uchun.
        print("Jiring Jring") # Terminalga "Jiring Jring" chiqadi.

# 2ta motosikl obyektlari yaratilmoqda.
bike1 = Bike("White", 2024, "m5")
bike2 = Bike("Black", 2025, "m4")
bike1.start_engine() # bike1 uchun dvigitelni ishga tushiradi.
bike2.ring_bell() # bike2 uchun signal chalinadi.

# 2

employes = [] # Xodimlar ro'yxati

class Employee: # Employee klassi - oddiy xodimlar uchun.
    def __init__(self, name, surname, age): # Parametrlar: ism, familiya, yosh.
        self.name = name # name public xususiyat sifatida saqlanadi.
        self.surname = surname # surname public xususiyat sifatida saqlanadi.
        self.age = age # age public xususiyat sifatida saqlanadi.

    def add_emp(self): # Xodim ma'lumotlarini ro'yxatga o'giradi.
        return [self.name, self.surname, self.age]

class Menenjer(Employee): # Manager klassi - Employee dan meros oladi.
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age) # Super orqali meros olingan qiymatlar.
        self.team = [] # Jamoa uchun bo'sh ro'yxat.

    def addEmployee(self, employee): # Jamoaga xodim(lar) qo'shish funksiyasi.
        self.team.extend(employee) # .extend() - ro'yxatni kengaytiradi.

    def info(self): # Jamoa haqida ma'lumot chiqaradi.
        print(f"\nMy employes:")
        for i in range(len(self.team)): # Har bir xodimni tartib raqami bilan chiqaradi.
            print(f"{i + 1}: {self.team[i]}")

# 10 ta bir xil xodim yaratilmoqda.
for emp in range(10):
    emp1 = Employee("Bob", "Teshaboyev", 99)
    employes.append(emp1.add_emp()) # Har bir xodim ro'yxatga qo'shilmoqda.

menenj1 = Menenjer("Tyson", "Saturn", 99) # Bitta menenjer yaratilmoqda.
menenj1.addEmployee(employes) # Menenjerga xodimlar qo'shilmoqda.
menenj1.info() # Menenjer jamoasi chiqariladi.

# 3

student_courses = {} # Talabalar kurslari uchun lug'at.
teacher_courses = {} # O'qituvchilar kurslari uchun lug'at.

class People: # Ota class - umumiy insonlar uchun.
    def __init__(self, name, surname, age): # Parametrlar: ism, familiya, yosh.
        self.name = name
        self.surname = surname
        self.age = age

class Student(People): # Student klassi - People dan meros oladi.
    def __init__(self, name, surname, age, courses): # Qo'shimcha: kurslar.
        super().__init__(name, surname, age)
        a = courses.split(",") # Kurslar vergul bilan ajratilgan bo'lsa, ro'yxatga ajratiladi.
        self.courses = []
        for i in a:
            self.courses.append(i.lower()) # Har bir kurs nomi kichik harflarda saqlanadi.
        student_courses[self.name] = self.courses # Global student_courses ga qo'shiladi.

    def introduce(self): # O'zini tanishtiradi.
        print(f"\nMen talabaman. \nMening ismim - {self.name} \nFamilyam - {self.surname} \nYoshim - {self.age} \nMen o'qiydigan kurslar - {self.courses}")
        
    def my_teachers(self): # Studentni o'qitadigan o'qituvchilar ro'yxatini topadi.
        lst = set() # Natijani to'plamda saqlaydi.
        for i in self.courses:
            for name in teacher_courses:
                if i.lower() in teacher_courses[name]: # Agar mos kelsa...
                    lst.add(name) # O'qituvchi nomini qo'shadi.

        print(f"\nStudent {self.name} teachers - {lst}") # Natija chiqariladi.

class Teacher(People): # Teacher klassi - People dan meros oladi.
    def __init__(self, name, surname, age, courses): # Qo'shimcha: kurslar.
        super().__init__(name, surname, age)
        a = courses.split(",")
        self.courses = []
        for i in a:
            self.courses.append(i.lower()) # Kichik harflarga aylantirib saqlanadi.
        teacher_courses[name] = self.courses # Global teacher_courses ga qo'shiladi.

    def introduce(self): # O'zini tanishtiradi.
        print(f"\nMen o'qituvchiman. \nMening ismim - {self.name} \nFamilyam - {self.surname} \nYoshim - {self.age} \nMen o'qitadigan kurslar - {self.courses}")

    def my_students(self): # O'qituvchi kimlarga dars berishini aniqlaydi.
        lst = set()
        for i in self.courses:
            for name in student_courses:
                if i.lower() in student_courses[name]:
                    lst.add(name)

        print(f"\nTeacher {self.name} students - {lst}") # Natija chiqariladi.

# Talaba va o'qituvchi yaratilmoqda.
st1 = Student("Bob", "Azimov", 10, "Pyton, Html, Css")
teach1 = Teacher("Avaz", "Do'stmuhammedov", 25, "Python, Html, Css, JS")

st1.introduce() # Talaba o'zini tanishtiradi.
teach1.introduce() # O'qituvchi o'zini tanishtiradi.

st1.my_teachers() # Talabani o'qitadigan o'qituvchilarni chiqaradi.
teach1.my_students() # O'qituvchining talabalarini chiqaradi.