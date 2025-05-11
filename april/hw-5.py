class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display_info(self, one=False, two=False, three=False):
        if one == False:
            print(f"My name: {self.__name}")
            print(f"My age: {self.__age}")
        elif one != False and three == False:
            print(f"\nMy id: {one}")
            print(f"My position: {two}")
        else:
            print(f"\nMy name: {self.__name}")
            print(f"My position: {two}")
            print(f"My id: {one}")
            print(f"My team size: {three}")

    @property 
    def get_name(self):
        return self.__name

    @get_name.setter
    def set_name(self, value):
        self.__name = value

    @property 
    def get_age(self):
        return self.__age

    @get_age.setter
    def set_age(self, value):
        self.__age = value

class Employee(Person):
    def __init__(self, name, age, employee_id, position):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__position = position

    def display_employee_info(self):
        super().display_info(self.__employee_id, self.__position)

    @property 
    def get_employee_id(self):
        return self.__employee_id

    @get_employee_id.setter
    def set_employee_id(self, value):
        self.__employee_id = value

    @property 
    def get_position(self):
        return self.__position

    @get_position.setter
    def set_position(self, value):
        self.__position = value

class Manager(Employee):
    def __init__(self, name, age, employee_id, position, team_size):
        super().__init__(name, age, employee_id, position)
        self.__team_size = team_size

    def display_manager_info(self):
        super().display_info(self.get_employee_id, self.get_position, self.__team_size)

    @property 
    def get_team_size(self):
        return self.__team_size

    @get_team_size.setter
    def set_team_size(self, value):
        self.__team_size = value

def func(val):
    if val == 1:
        choice = input("Enter person (a or b or c): ")
        if choice == 'a':
            print("Name:", a.get_name)
            print("Age:", a.get_age)
        elif choice == 'b':
            print("Name:", b.get_name)
            print("Age:", b.get_age)
            print("ID:", b.get_employee_id)
            print("Position:", b.get_position)
        elif choice == 'c':
            print("Name:", c.get_name)
            print("Age:", c.get_age)
            print("ID:", c.get_employee_id)
            print("Position:", c.get_position)
            print("Team Size:", c.get_team_size)
        else:
            print("Invalid person.")
    elif val == 2:
        choice = input("Choose person to update (a or b or c): ")
        if choice == 'a':
            new_name = input("Enter new name for a: ")
            a.set_name = new_name
            new_age = int(input("Enter new age for a: "))
            a.set_age = new_age
        elif choice == 'b':
            new_id = input("Enter new ID for b: ")
            b.set_employee_id = new_id
            new_pos = input("Enter new position for b: ")
            b.set_position = new_pos
        elif choice == 'c':
            new_team_size = int(input("Enter new team size for c: "))
            c.set_team_size = new_team_size
        else:
            print("Invalid person.")
    elif val == 3:
        print("\nInfo of a (Person):")
        a.display_info()
        print("\nInfo of b (Employee):")
        b.display_employee_info()
        print("\nInfo of c (Manager):")
        c.display_manager_info()
    else:
        print("Error: Invalid value!")
        menu()

def menu():
    print("\nMenu: ")
    print("1: Get")
    print("2: Set")
    print("3: Info")
    val = int(input("Enter the value: "))
    func(val)


while True:
    a_name = input("Please enter name(a): ")
    b_name = input("Please enter name(b): ")
    c_name = input("Please enter name(c): ")
    a_age = int(input("Please enter age(a): "))
    b_age = int(input("Please enter age(b): "))
    c_age = int(input("Please enter age(c): "))
    b_id = input("Please enter id(b): ")
    c_id = input("Please enter id(c): ")
    b_position = input("Please enter position(b): ")
    c_position = input("Please enter position(c): ")
    c_team_size = int(input("Please enter team size(c): "))

    a = Person(a_name, a_age)
    b = Employee(b_name, b_age, b_id, b_position)
    c = Manager(c_name, c_age, c_id, c_position, c_team_size)

    while True:
        menu()
        cont = input("\nDavom etmoqchimisiz? (yes/no): ")
        if cont.lower() != 'yes':
            break
    again = input("\n Odam ismini almashtirmoqchimisiz? (yes/no): ")
    if again.lower() != 'yes':
        break
