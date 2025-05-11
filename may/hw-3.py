from abc import ABC, abstractmethod  # Abstrakt sinflar uchun modul
import random  # Tasodifiy ID yaratish uchun

# Raqamlar va harflar ro'yxatlari
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
harf = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
harf_upper = [i.upper() for i in harf]  # Harflarning katta harf ko'rinishi

# Umumiy belgilar ro'yxati (raqam + kichik harf + katta harf)
all = []
all.extend(num)
all.extend(harf)
all.extend(harf_upper)

all_id = []  # Yaratilgan ID'lar ro'yxati (dublikatdan qochish uchun)

# Unikal ID yaratish funksiyasi
def create_id():
    while True:
        id = ""
        for i in range(random.randint(3, 30)):  # 3 dan 30 gacha uzunlikdagi ID
            id += random.choice(all)
        if id in all_id:  # Avval yaratilgan bo'lsa, qaytadan yarat
            continue
        else:
            all_id.append(id)  # Yangi ID'ni ro'yxatga qo'sh
            break
    return id

# Int qiymat olish uchun universal funksiya
def get_int(name="Object", type=True):
    if type:  # Obyektlar sonini olish uchun
        num = input(f"Objectlar sonini kiriting: ")
    else:  # Yoshi yoki boshqa raqamli ma'lumot uchun
        num = input(f"{name}ni kiriting: ")

    if num.isdigit():  # Faqat son kiritilganini tekshiradi
        num = int(num)
    else:
        print("Son kiriting!")
        return get_int(name, type)

    if num >= 1:
        return num
    else:
        print("1 dan katta bo'lsin!")
        return get_int(name, type)

# Abstrakt sinf - inson haqida asosiy ma'lumot
class Human(ABC):
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Protected atribut

    @abstractmethod
    def info(self):  # Har bir subklassda aniqlanishi kerak
        pass

# Manager sinfi
class Manenger(Human):
    job = "Manenger"

    def __init__(self, name, age):
        super().__init__(name, age)
        self.__id = create_id()  # Maxfiy ID

    def info(self):
        return f"I am {self.job}. My name is {self.name}, i am {self._age} years old"

# Developer sinfi
class Developer(Human):
    job = "Developer"

    def __init__(self, name, age):
        super().__init__(name, age)
        self.__id = create_id()

    def info(self):
        return f"I am {self.job}. My name is {self.name}, i am {self._age} years old"

# Employee sinfi, qo'shimcha `position` (lavozim) atributiga ega
class Employee(Human):
    job = "Employee"

    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.__id = create_id()
        self.position = position

    def info(self):
        return f"I am {self.job}. My name is {self.name}, i am {self._age} years old, my position {self.position}"

# Obyekt haqida ma'lumot chiqaruvchi funksiya
def give_info(obj):
    print(obj.info())

# Ishchilar turini ro'yxatga kiritamiz
lst = ["Manenger", "Developer", "Employee"]
lst_obj = []  # Barcha obyektlar shu ro'yxatda saqlanadi

# Har bir turdagi ishchidan nechtadan kiritilishini so'raymiz
for id, value in enumerate(lst, start=0):
    number = get_int()  # Nechta obyekt yaratilsin?
    for num in range(1, number + 1):
        name = input(f"{value} ismini kiriting: ")
        age = get_int(f"{value} yoshi", False)

        # Har bir turga mos obyekt yaratamiz
        if id == 0:
            obj = Manenger(name, age)
        elif id == 1:
            obj = Developer(name, age)
        elif id == 2:
            position = input(f"{value} joylashuvini kiriting: ")
            obj = Employee(name, age, position)

        # Obyektga global nom beramiz (ixtiyoriy), va ro'yxatga qo'shamiz
        globals()[f"{value.lower()}{num}"] = obj
        lst_obj.append(obj)

# Barcha yaratilgan obyektlar haqida ma'lumot chiqaramiz
for obj in lst_obj:
    give_info(obj)

    
class Class4(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class4_1(Class4):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class4_2(Class4):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class4_3(Class4):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_4 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class4{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_4.append(obj)

for __ in obj_lst_4:
    give_info(__)


class Class5(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class5_1(Class5):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class5_2(Class5):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class5_3(Class5):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_5 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class5{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_5.append(obj)

for __ in obj_lst_5:
    give_info(__)


class Class6(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class6_1(Class6):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class6_2(Class6):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class6_3(Class6):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_6 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class6{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_6.append(obj)

for __ in obj_lst_6:
    give_info(__)


class Class7(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class7_1(Class7):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class7_2(Class7):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class7_3(Class7):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_7 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class7{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_7.append(obj)

for __ in obj_lst_7:
    give_info(__)


class Class8(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class8_1(Class8):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class8_2(Class8):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class8_3(Class8):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_8 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class8{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_8.append(obj)

for __ in obj_lst_8:
    give_info(__)


class Class9(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class9_1(Class9):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class9_2(Class9):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class9_3(Class9):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_9 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class9{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_9.append(obj)

for __ in obj_lst_9:
    give_info(__)


class Class10(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class10_1(Class10):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class10_2(Class10):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class10_3(Class10):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_10 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class10{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_10.append(obj)

for __ in obj_lst_10:
    give_info(__)


class Class11(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class11_1(Class11):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class11_2(Class11):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class11_3(Class11):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_11 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class11{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_11.append(obj)

for __ in obj_lst_11:
    give_info(__)


class Class12(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class12_1(Class12):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class12_2(Class12):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class12_3(Class12):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_12 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class12{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_12.append(obj)

for __ in obj_lst_12:
    give_info(__)


class Class13(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class13_1(Class13):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class13_2(Class13):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class13_3(Class13):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_13 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class13{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_13.append(obj)

for __ in obj_lst_13:
    give_info(__)


class Class14(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class14_1(Class14):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class14_2(Class14):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class14_3(Class14):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_14 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class14{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_14.append(obj)

for __ in obj_lst_14:
    give_info(__)


class Class15(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class15_1(Class15):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class15_2(Class15):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class15_3(Class15):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_15 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class15{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_15.append(obj)

for __ in obj_lst_15:
    give_info(__)


class Class16(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class16_1(Class16):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class16_2(Class16):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class16_3(Class16):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_16 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class16{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_16.append(obj)

for __ in obj_lst_16:
    give_info(__)


class Class17(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class17_1(Class17):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class17_2(Class17):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class17_3(Class17):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_17 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class17{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_17.append(obj)

for __ in obj_lst_17:
    give_info(__)


class Class18(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class18_1(Class18):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class18_2(Class18):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class18_3(Class18):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_18 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class18{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_18.append(obj)

for __ in obj_lst_18:
    give_info(__)


class Class19(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class19_1(Class19):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class19_2(Class19):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class19_3(Class19):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_19 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class19{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_19.append(obj)

for __ in obj_lst_19:
    give_info(__)


class Class20(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class20_1(Class20):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class20_2(Class20):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class20_3(Class20):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_20 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class20{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_20.append(obj)

for __ in obj_lst_20:
    give_info(__)


class Class21(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class21_1(Class21):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class21_2(Class21):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class21_3(Class21):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_21 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class21{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_21.append(obj)

for __ in obj_lst_21:
    give_info(__)


class Class22(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class22_1(Class22):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class22_2(Class22):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class22_3(Class22):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_22 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class22{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_22.append(obj)

for __ in obj_lst_22:
    give_info(__)


class Class23(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class23_1(Class23):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class23_2(Class23):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class23_3(Class23):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_23 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class23{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_23.append(obj)

for __ in obj_lst_23:
    give_info(__)


class Class24(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class24_1(Class24):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class24_2(Class24):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class24_3(Class24):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_24 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class24{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_24.append(obj)

for __ in obj_lst_24:
    give_info(__)


class Class25(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class25_1(Class25):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class25_2(Class25):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class25_3(Class25):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_25 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class25{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_25.append(obj)

for __ in obj_lst_25:
    give_info(__)


class Class26(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class26_1(Class26):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class26_2(Class26):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class26_3(Class26):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_26 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class26{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_26.append(obj)

for __ in obj_lst_26:
    give_info(__)


class Class27(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class27_1(Class27):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class27_2(Class27):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class27_3(Class27):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_27 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class27{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_27.append(obj)

for __ in obj_lst_27:
    give_info(__)


class Class28(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class28_1(Class28):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class28_2(Class28):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class28_3(Class28):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_28 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class28{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_28.append(obj)

for __ in obj_lst_28:
    give_info(__)


class Class29(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class29_1(Class29):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class29_2(Class29):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class29_3(Class29):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_29 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class29{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_29.append(obj)

for __ in obj_lst_29:
    give_info(__)


class Class30(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class30_1(Class30):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class30_2(Class30):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class30_3(Class30):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_30 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class30{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_30.append(obj)

for __ in obj_lst_30:
    give_info(__)


class Class31(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class31_1(Class31):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class31_2(Class31):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class31_3(Class31):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_31 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class31{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_31.append(obj)

for __ in obj_lst_31:
    give_info(__)


class Class32(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class32_1(Class32):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class32_2(Class32):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class32_3(Class32):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_32 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class32{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_32.append(obj)

for __ in obj_lst_32:
    give_info(__)


class Class33(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class33_1(Class33):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class33_2(Class33):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class33_3(Class33):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_33 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class33{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_33.append(obj)

for __ in obj_lst_33:
    give_info(__)


class Class34(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class34_1(Class34):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class34_2(Class34):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class34_3(Class34):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_34 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class34{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_34.append(obj)

for __ in obj_lst_34:
    give_info(__)


class Class35(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class35_1(Class35):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class35_2(Class35):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class35_3(Class35):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_35 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class35{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_35.append(obj)

for __ in obj_lst_35:
    give_info(__)


class Class36(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class36_1(Class36):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class36_2(Class36):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class36_3(Class36):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_36 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class36{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_36.append(obj)

for __ in obj_lst_36:
    give_info(__)


class Class37(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class37_1(Class37):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class37_2(Class37):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class37_3(Class37):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_37 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class37{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_37.append(obj)

for __ in obj_lst_37:
    give_info(__)


class Class38(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class38_1(Class38):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class38_2(Class38):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class38_3(Class38):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_38 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class38{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_38.append(obj)

for __ in obj_lst_38:
    give_info(__)


class Class39(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class39_1(Class39):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class39_2(Class39):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class39_3(Class39):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_39 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class39{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_39.append(obj)

for __ in obj_lst_39:
    give_info(__)


class Class40(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class40_1(Class40):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class40_2(Class40):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class40_3(Class40):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_40 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class40{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_40.append(obj)

for __ in obj_lst_40:
    give_info(__)


class Class41(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class41_1(Class41):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class41_2(Class41):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class41_3(Class41):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_41 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class41{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_41.append(obj)

for __ in obj_lst_41:
    give_info(__)


class Class42(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class42_1(Class42):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class42_2(Class42):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class42_3(Class42):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_42 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class42{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_42.append(obj)

for __ in obj_lst_42:
    give_info(__)


class Class43(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class43_1(Class43):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class43_2(Class43):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class43_3(Class43):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_43 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class43{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_43.append(obj)

for __ in obj_lst_43:
    give_info(__)


class Class44(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class44_1(Class44):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class44_2(Class44):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class44_3(Class44):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_44 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class44{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_44.append(obj)

for __ in obj_lst_44:
    give_info(__)


class Class45(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class45_1(Class45):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class45_2(Class45):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class45_3(Class45):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_45 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class45{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_45.append(obj)

for __ in obj_lst_45:
    give_info(__)


class Class46(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class46_1(Class46):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class46_2(Class46):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class46_3(Class46):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_46 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class46{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_46.append(obj)

for __ in obj_lst_46:
    give_info(__)


class Class47(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class47_1(Class47):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class47_2(Class47):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class47_3(Class47):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_47 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class47{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_47.append(obj)

for __ in obj_lst_47:
    give_info(__)


class Class48(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class48_1(Class48):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class48_2(Class48):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class48_3(Class48):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_48 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class48{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_48.append(obj)

for __ in obj_lst_48:
    give_info(__)


class Class49(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class49_1(Class49):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class49_2(Class49):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class49_3(Class49):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_49 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class49{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_49.append(obj)

for __ in obj_lst_49:
    give_info(__)


class Class50(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Class50_1(Class50):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class50_2(Class50):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


class Class50_3(Class50):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        return f"My name is {self.name}, I am {self.age} years"


def give_info(obj):
    print(obj.get_info())

obj_lst_50 = []
for _ in range(3):
    name = input("Enter name: ")
    age = int(input("Yosh: "))
    class_name = f"Class50{_+1}"
    obj = globals()[class_name](name, age)
    obj_lst_50.append(obj)

for __ in obj_lst_50:
    give_info(__)