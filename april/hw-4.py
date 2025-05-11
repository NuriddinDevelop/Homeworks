# Oila a'zolari uchun klasslar

# Bobo klassi
class Bobo:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

# Buvi klassi
class Buvi:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

# Ota klassi, Bobodan va Buvdan meros oladi (multiple inheritance)
class Ota(Bobo, Buvi):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def father(self):
        print(f"I am father")

# Ona klassi, faqat o'ziga xos xususiyat — kasbi bor
class Ona:
    def __init__(self, job):
        self.job = job

    def my_job(self):
        print(f"My job is {self.job}")

# Bola klassi, Ota va Onadan meros oladi
class Bola(Ota, Ona):
    def __init__(self, name, surname, age, job, game):
        # super().__init__ chaqirishda faqat name, surname, age yuboriladi
        Ota.__init__(self, name, surname, age)
        Ona.__init__(self, job)
        self.game = game

    def my_game(self):
        print(f"I can play {self.game}")

# Nevara klassi, Boladan meros oladi, o'ziga xos hususiyati — sevimli rangi
class Nevara(Bola):
    def __init__(self, name, surname, age, job, game, color):
        super().__init__(name, surname, age, job, game)
        self.color = color

    def my_color(self):
        print(f"My favorite color is {self.color}")


# Ushbu funksiya obyekt haqida ma'lumot chiqaradi, nechta metod chaqirilishini num belgilaydi
def qw(num, obj):
    print(f"1: {obj.name}.")
    print(f"2: {obj.surname}.")
    print(f"3: {obj.age}.")

    if num == 1:
        return

    obj.father()
    if num == 2:
        return

    obj.my_job()
    if num == 3:
        return

    obj.father()
    obj.my_job()
    obj.my_game()
    if num == 4:
        return

    obj.father()
    obj.my_job()
    obj.my_game()
    obj.my_color()

    if num == 5:
        return


# Nechta oila a'zosi kiritilishini so'raymiz
count = int(input("Nechta object: "))

for i in range(count):
    # Foydalanuvchidan kimligini so'raymiz
    quest = input("Kimsiz (Bobo, buvi, ota, ona, bola, nevara): ").lower()
    name = input("Name: ")
    surname = input("Surname: ")
    age = input("Age: ")

    # Turiga qarab tegishli obyekt yaratamiz
    if quest == "bobo":
        num = 1
        obj = Bobo(name, surname, age)
        qw(num, obj)

    elif quest == "buvi":
        num = 1
        obj = Buvi(name, surname, age)
        qw(num, obj)

    elif quest == "ota":
        num = 2
        obj = Ota(name, surname, age)
        qw(num, obj)

    elif quest == "ona":
        num = 3
        job = input("Job: ")
        # Ona klassi faqat job oladi, ammo `qw` funksiyasi name va age ham kerak qiladi
        obj = Ona(job)
        # Biroz mos kelmaydi, lekin shunchaki metodlarini chaqiramiz
        print(f"1: {name}.")
        print(f"2: {surname}.")
        print(f"3: {age}.")
        obj.my_job()

    elif quest == "bola":
        num = 4
        job = input("Job: ")
        game = input("Game: ")
        obj = Bola(name, surname, age, job, game)
        qw(num, obj)

    elif quest == "nevara":
        job = input("Job: ")
        game = input("Game: ")
        color = input("Color: ")
        num = 5
        obj = Nevara(name, surname, age, job, game, color)
        qw(num, obj)

# ==== Quyida hayvonlar boyicha kod ====

# Hayvonlar uchun klasslar

# Animal klassi — asosiy
class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def my_type(self):
        print(f"My type is {self.type}.")

# Bird klassi — rangga ega va ucha oladi
class Bird(Animal):
    def __init__(self, name, type, color):
        super().__init__(name, type)
        self.color = color

    def fly(self):
        print(f"I can fly! My color is: {self.color}")

# Fish klassi — suza oladi
class Fish(Animal):
    def __init__(self, name, type):
        super().__init__(name, type)

    def swim(self):
        print("I can swim!")

# Duck klassi — Animal, Bird va Fishdan meros oladi
class duck(Animal, Bird, Fish):
    def __init__(self, name, type, color):
        super().__init__(name, type)
        self.color = color

    def sound(self):
        print("Kvak, Kvak")

    def i_can(self):
        self.my_type()
        self.fly()
        self.swim()

# Hayvon haqida ma'lumot chiqaruvchi funksiya
def describe(animal_type, obj):
    print(f"Name: {obj.name}")
    print(f"Type: {obj.type}")

    if animal_type == "animal":
        return

    obj.my_type()

    if animal_type == "bird":
        obj.fly()
        return

    if animal_type == "fish":
        obj.swim()
        return

    if animal_type == "duck":
        obj.my_type()
        obj.fly()
        obj.swim()
        obj.sound()

# Foydalanuvchidan nechta hayvon yaratishini so'raymiz
animal_count = int(input("Nechta object: "))

for i in range(animal_count):
    animal_type = input("Hayvon turini kiriting (animal, bird, fish, duck): ").lower()
    name = input("Name: ")
    type_ = input("Type: ")

    if animal_type == "animal":
        obj = Animal(name, type_)
    elif animal_type == "bird":
        color = input("Color: ")
        obj = Bird(name, type_, color)
    elif animal_type == "fish":
        obj = Fish(name, type_)
    elif animal_type == "duck":
        color = input("Color: ")
        obj = duck(name, type_, color)
    else:
        print("Notogri hayvon turi!")
        continue

    describe(animal_type, obj)
