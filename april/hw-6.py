from abc import ABC, abstractmethod

# 1. Vehicle
# Abstract class Vehicle
class Vehicle(ABC):
    def __init__(self, brand):
        self._brand = brand  # Brand nomi encapsulation bilan saqlanadi

    @property
    def brand(self):
        return self._brand  # Getter: brand qiymatini olish

    @brand.setter
    def brand(self, value):
        self._brand = value  # Setter: brand qiymatini o‘zgartirish

    @abstractmethod
    def start(self):
        pass  # Har bir transport turi o‘z usulida ishga tushadi

# Car klassi Vehicle'dan meros oladi va start funksiyasini aniqlaydi
class Car(Vehicle):
    def start(self):
        print(f"{self.brand} mashinasi ishga tushdi.")

car1 = Car("BMW")
car1.start()
new_brand = input("Yangi brend nomini kiriting: ")
car1.brand = new_brand  # Setter orqali brandni o‘zgartiryapti
car1.start()

# 2. Animal
# Abstract class Animal
class Animal(ABC):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name  # Getter

    @name.setter
    def name(self, value):
        self._name = value  # Setter

    @abstractmethod
    def my_name(self):
        pass  # Har bir hayvon o‘zini qanday tanishtiradi

# Dog klassi Animal'dan meros oladi
class Dog(Animal):
    def my_name(self):
        print(f"Bu hayvon {self.name}.")

dog1 = Dog("Bezbet")
dog1.my_name()
new_name = input("Isimni kiriting: ")
dog1.name = new_name  # Setter orqali ismni yangilayapti
dog1.my_name()

# 3. Person
# Abstract class Person
class Person(ABC):
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age  # Getter

    @age.setter
    def age(self, value):
        self._age = value  # Setter

    @abstractmethod
    def role(self):
        pass  # Har bir insonning roli turlicha bo'lishi mumkin

# Student klassi Person'dan meros oladi
class Student(Person):
    def role(self):
        print(f"O'quvchi, yoshi: {self.age}")

student1 = Student(20)
student1.role()
new_age = int(input("Yoshni kiriting: "))
student1.age = new_age  # Setter orqali yoshni o‘zgartirish
student1.role()

# 4. BankAccount
# Abstract class BankAccount
class BankAccount(ABC):
    def __init__(self, balance):
        self._balance = balance  # Hisobdagi balans (private)

    @property
    def balance(self):
        return self._balance  # Getter

    def add_balance(self, amount):
        self._balance += amount  # Hisobga pul qo‘shish

    def chiqarish(self, amount):
        self._balance -= amount  # Hisobdan pul olish

    @abstractmethod
    def account_type(self):
        pass  # Har xil turdagi hisoblar bo'lishi mumkin

# SavingsAccount klassi - jamg‘arma hisob turi
class SavingsAccount(BankAccount):
    def account_type(self):
        print(f"Jamg'arma hisobida: ${self.balance}")

acc = SavingsAccount(200000)
acc.account_type()
add_balance = int(input("Qancha pul kiritmoqchisiz: "))
acc.add_balance(add_balance)  # Hisobga pul kiritish
acc.account_type()
chiqarish = int(input("Qancha pul chiqarmoqchisiz: "))
acc.chiqarish(chiqarish)  # Pul chiqarish
acc.account_type()

# 5. Employee
# Abstract class Employee
class Employee(ABC):
    def __init__(self, salary):
        self._salary = salary  # Ish haqi

    @property
    def salary(self):
        return self._salary  # Getter

    @salary.setter
    def salary(self, value):
        self._salary = value  # Setter

    @abstractmethod
    def work(self):
        pass  # Har bir xodim har xil ish qiladi

# Developer klassi - xodimning dasturchi turi
class Developer(Employee):
    def work(self):
        print(f"Dasturchining maoshi: {self.salary} so'm.")

dev1 = Developer(200000)
dev1.work()
dev1.salary = 210000  # Maoshni yangilash
dev1.work()
