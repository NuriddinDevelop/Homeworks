class Class1:
    def __init__(self, name, age): 
        self.name = name
        self.age = age

class1= Class1("Anvar", 30)
print(f"Class1 age: {class1.age}")


class Class2:
    def __init__(self, name, surname): 
        self.name = name
        self.surname = surname
    
class2 = Class2("Bekzod", "Teshaboyev")
print(f"Class2 surname: {class2.surname}")

    
class Class3:
    def __init__(self, name, id): 
        self.name = name
        self.id = id

class3 = Class3("Diyor", "u123")
print(f"Class3 id: {class3.id}")


class Class4:
    def __init__(self, name, color): 
        self.name = name
        self.color = color

class4 = Class4("Islom", "Black")
print(f"Class4 color: {class4.color}")


class Class5:
    def __init__(self, name, speed): 
        self.name = name
        self.speed = speed  
        
class5 = Class5("Kamron", 14)
print(f"Class5 speed: {class5.speed}")


class Class6:
    def __init__(self, name, job): 
        self.name = name
        self.job = job

class6 = Class6("Bob", "Bekorchi")
print(f"Class6 job: {class6.job}")


class Class7:
    def __init__(self, name, adress): 
        self.name = name
        self.adress = adress

class7 = Class7("Nodir", "Tashkent")
print(f"Class7 adress: {class7.adress}")


class Class8:
    def __init__(self, name, phoneNumber): 
        self.name = name
        self.phoneNumber = phoneNumber

class8 = Class8("Ozod", "+998(99)999-99-99")
print(f"Class8 phoneNumber: {class8.phoneNumber}")


class Class9:
    def __init__(self, name, amount): 
        self.name = name
        self.amount = amount

class9 = Class9("Rustam", 83)
print(f"Class9 amount: {class9.amount}")


class Class10:
    def __init__(self, name, health): 
        self.name = name
        self.health = health

class10 = Class10("Shohrux", 17)
print(f"Class10 health: {class10.health}")


class Class11:
    def __init__(self, name, age): 
        self.name = name
        self._age = age
    
    @property
    def age(self):
        return self._age

class Class12:
    def __init__(self, name, surname): 
        self.name = name
        self._surname = surname
    
    @property
    def surname(self):
        return self._surname

class Class13:
    def __init__(self, name, id): 
        self.name = name
        self._id = id
    
    @property
    def id(self):
        return self._id

class Class14:
    def __init__(self, name, color): 
        self.name = name
        self._color = color
    
    @property
    def color(self):
        return self._color

class Class15:
    def __init__(self, name, speed): 
        self.name = name
        self._speed = speed
    
    @property
    def speed(self):
        return self._speed

class Class16:
    def __init__(self, name, job): 
        self.name = name
        self._job = job
    
    @property
    def job(self):
        return self._job

class Class17:
    def __init__(self, name, adress): 
        self.name = name
        self._adress = adress
    
    @property
    def adress(self):
        return self._adress

class Class18:
    def __init__(self, name, phoneNumber): 
        self.name = name
        self._phoneNumber = phoneNumber
    
    @property
    def phoneNumber(self):
        return self._phoneNumber

class Class19:
    def __init__(self, name, amount): 
        self.name = name
        self._amount = amount
    
    @property
    def amount(self):
        return self._amount

class Class20:
    def __init__(self, name, health): 
        self.name = name
        self._health = health
    
    @property
    def health(self):
        return self._health

class Class21:
    def __init__(self, name, age): 
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

private1 = Class21("Anvar", 30)
print(f"Private1 age: {private1.age}")

class Class22:
    def __init__(self, name, surname): 
        self.name = name
        self.__surname = surname

    @property
    def surname(self):
        return self.__surname

private2 = Class22("Bekzod", "Teshaboyev")
print(f"Private2 surname: {private2.surname}")
class Class23:
    def __init__(self, name, id): 
        self.name = name
        self.__id = id

    @property
    def id(self):
        return self.__id

private3 = Class23("Diyor", "u123")
print(f"Private3 id: {private3.id}")
class Class24:
    def __init__(self, name, color): 
        self.name = name
        self.__color = color

    @property
    def color(self):
        return self.__color

private4 = Class24("Islom", "Black")
print(f"Private4 color: {private4.color}")
class Class25:
    def __init__(self, name, speed): 
        self.name = name
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

private5 = Class25("Kamron", 14)
print(f"Private5 speed: {private5.speed}")
class Class26:
    def __init__(self, name, job): 
        self.name = name
        self.__job = job

    @property
    def job(self):
        return self.__job

private6 = Class26("Bob", "Bekorchi")
print(f"Private6 job: {private6.job}")
class Class27:
    def __init__(self, name, adress): 
        self.name = name
        self.__adress = adress

    @property
    def adress(self):
        return self.__adress

private7 = Class27("Nodir", "Tashkent")
print(f"Private7 adress: {private7.adress}")
class Class28:
    def __init__(self, name, phoneNumber): 
        self.name = name
        self.__phoneNumber = phoneNumber

    @property
    def phoneNumber(self):
        return self.__phoneNumber

private8 = Class28("Ozod", "+998(99)999-99-99")
print(f"Private8 phoneNumber: {private8.phoneNumber}")
class Class29:
    def __init__(self, name, amount): 
        self.name = name
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

private9 = Class29("Rustam", 83)
print(f"Private9 amount: {private9.amount}")
class Class30:
    def __init__(self, name, health): 
        self.name = name
        self.__health = health

    @property
    def health(self):
        return self.__health

private10 = Class30("Shohrux", 17)
print(f"Private10 health: {private10.health}")

class Class31:
    def __init__(self, name, age): 
        self.name = name
        self._age = age
    
    @property
    def age(self):
        return self._age

class Class32:
    def __init__(self, name, surname): 
        self.name = name
        self._surname = surname
    
    @property
    def surname(self):
        return self._surname

class Class33:
    def __init__(self, name, id): 
        self.name = name
        self._id = id
    
    @property
    def id(self):
        return self._id

class Class34:
    def __init__(self, name, color): 
        self.name = name
        self._color = color
    
    @property
    def color(self):
        return self._color

class Class35:
    def __init__(self, name, speed): 
        self.name = name
        self._speed = speed
    
    @property
    def speed(self):
        return self._speed

class Class36:
    def __init__(self, name, job): 
        self.name = name
        self._job = job
    
    @property
    def job(self):
        return self._job

class Class37:
    def __init__(self, name, adress): 
        self.name = name
        self._adress = adress
    
    @property
    def adress(self):
        return self._adress

class Class38:
    def __init__(self, name, phoneNumber): 
        self.name = name
        self._phoneNumber = phoneNumber
    
    @property
    def phoneNumber(self):
        return self._phoneNumber

class Class39:
    def __init__(self, name, amount): 
        self.name = name
        self._amount = amount
    
    @property
    def amount(self):
        return self._amount

class Class40:
    def __init__(self, name, health): 
        self.name = name
        self._health = health
    
    @property
    def health(self):
        return self._health

class Class41:
    def __init__(self, name): 
        self.name = name

class Class42:
    def __init__(self, name): 
        self.name = name

class Class43:
    def __init__(self, name): 
        self.name = name

class Class44:
    def __init__(self, name): 
        self.name = name

class Class45:
    def __init__(self, name): 
        self.name = name

class Class46:
    def __init__(self, name): 
        self.name = name

class Class47:
    def __init__(self, name): 
        self.name = name

class Class48:
    def __init__(self, name): 
        self.name = name

class Class49:
    def __init__(self, name): 
        self.name = name

class Class50:
    def __init__(self, name): 
        self.name = name

