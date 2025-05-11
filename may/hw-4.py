import random
import time
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
list_id = []
def generate_id():
    id = ""
    for i in range(random.randint(8, 16)):
        id += random.choice(letters)
    if id in list_id:
        return generate_id()
    list_id.append(id)
    return id

def get_int(type=True, min=1, max=10):
    if type:
        num = input(f"\nObjectlar sonini kiriting: ")
        if num.isdigit():
            num = int(num)
        else:
            print("Son kiriting!")
            return get_int()
        
        if num >= 1:
            pass
        else:
            print("1 dan katta bo'lsin!")
            return get_int()
        
        if num > 10:
            print("10 dan kichik bo'lsin!")
            return get_int()
        return num
    else:
        num = input(f"\nTanlang: ")
        if num.isdigit():
            num = int(num)
        else:
            print("Son kiriting!")
            return get_int(False, min, max)
        
        if num >= min and num <= max:
            return num
        else:
            print(f"{min} dan {max} gacha bo'lsin!")
            return get_int(False, min, max)

class Character:
    def __init__(self):
        self.__id = generate_id()
        self.level = random.randint(1, 10)
        self.health = 100
        self.mana = random.randint(50, 100)
        self.attack = random.randint(self.level * 3, self.level * 5)
        self.defense = random.randint(5, 15)
        self.speed = random.randint(5, 15)
        self.special_move_level = 1

    def __str__(self):
        raise NotImplementedError("str() metodini o'zgartirish kerak! ")
    
    def special_move(self):
        raise NotImplementedError("Klasslarda bu funksiyani o'zgartirish kerak! ")
    
    def damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.__id} o'ldirildi!")
            objects.remove(self)
            return True
        return False

class Boss(Character):
    def __init__(self):
        super().__init__()
        self.name = "Boss"
        self.type = "Boss"
        self.attack = random.randint(self.level * 5, self.level * 10)
        self.health = random.randint(self.level * 40, self.level * 90)

    def __str__(self):
        return f"\nBoss, Level: {self.level}, Health: {self.health}, Mana: {self.mana}, Attack: {self.attack}, Defense: {self.defense}, Speed: {self.speed}"
    
    def special_move(self):
        self.mana -= 5
        if self.mana < 0:
            return f"Mana yetarli emas! Mana: {self.mana} ta"
        else:
            choice = random.choice(objects[1:])
            if choice.health <= self.attack:
                choice.health = 0
                objects.remove(choice)
                return f"\nBossning {choice.name}ga zarbasi {choice.name}ni o'ldirdi!"
            else:
                choice.damage(self.attack)
                print(f"\nBossning {choice.name}ga zarbasi!")
                return f"{choice.name}ning joni {choice.health} ta qoldi!"

    def damage(self, damage):   
        self.health -= damage
        if self.health <= 0:
            print(f"Boss o'ldirildi!")
            objects.remove(self)
            return True
        return False

class Assassin(Character):
    def __init__(self):
        super().__init__()
        name = input("\nAssassin nomini kiriting: ")
        self.name = name
        self.type = "Assassin"

    def __str__(self):
        return f"\nAssassin: {self.name}, Level: {self.level}, Health: {self.health}, Mana: {self.mana}, Attack: {self.attack}, Defense: {self.defense}, Speed: {self.speed}"
    
    def special_move(self):
        if self.special_move_level == 1:
            self.special_move_level += 1
            if self.mana < 5:
                return f"\nMana yetarli emas!"
            self.mana -= 5
            self.health += 5
            if objects[0].health <= 0:
                objects[0].health = 0
                objects.remove(objects[0])
                return f"\nAssassin {self.name}ning zarbasi Bossni o'ldirdi!"
            else:
                objects[0].damage(self.attack)
                return f"\nAssassin {self.name}ning qilich bilan eng kuchli zarbasi!"
        elif self.special_move_level == 2:
            self.special_move_level += 1
            if self.mana < 10:
                return f"\nMana yetarli emas!"
            self.mana -= 10
            self.health += 10
            if objects[0].health <= 0:
                objects[0].health = 0
                objects.remove(objects[0])
                return f"\nAssassin {self.name}ning zarbasi Bossni o'ldirdi!"
            else:
                objects[0].damage(self.attack * 2)
                return f"\nAssassin {self.name}ning qilich bilan eng kuchli zarbasi!"
        elif self.special_move_level == 3:
            if self.mana < 15:
                return f"\nMana yetarli emas!"
            self.mana -= 15
            self.health += 15
            self.special_move_level = 1
            if objects[0].health <= 0:
                objects[0].health = 0
                objects.remove(objects[0])
                return f"\nAssassin {self.name}ning zarbasi Bossni o'ldirdi!"
            else:
                objects[0].damage(self.attack * 3)
                return f"\nAssassin {self.name}ning qilich bilan eng kuchli zarbasi!"
        

class Paladin(Character):
    def __init__(self):
        super().__init__()
        name = input("\nPaladin nomini kiriting: ")
        self.name = name
        self.type = "Paladin"

    def __str__(self):
        return f"\nPaladin: {self.name}, Level: {self.level}, Health: {self.health}, Mana: {self.mana}, Attack: {self.attack}, Defense: {self.defense}, Speed: {self.speed}"  
    
    def special_move(self):
        if self.special_move_level == 1:
            self.special_move_level += 1
            if self.mana < 10:
                return f"\nMana yetarli emas!"
            self.mana -= 10
            self.health += 10
            for obj in objects[1:]:
                if obj.type != "Paladin":
                    obj.health += self.level * 2
            return f"Paladin {self.name} o'yinchilarga jon berdi!"
        elif self.special_move_level == 2:
            self.special_move_level += 1
            if self.mana < 15:
                return f"\nMana yetarli emas!"
            self.mana -= 15
            self.health += 15
            for obj in objects[1:]:
                if obj.type != "Paladin":
                    obj.health += self.level * 3
            return f"Paladin {self.name} o'yinchilarga jon berdi!"
        elif self.special_move_level == 3:
            if self.mana < 20:
                return f"\nMana yetarli emas!"
            self.mana -= 20
            self.health += 20
            for obj in objects[1:]:
                if obj.type != "Paladin":
                    obj.health += self.level * 4
            return f"Paladin {self.name} o'yinchilarga jon berdi!"

class Necromancer(Character):
    def __init__(self):
        super().__init__()
        name = input("Necromancer nomini kiriting: ")
        self.name = name
        self.type = "Necromancer"

    def __str__(self):
        return f"\nNecromancer: {self.name}, Level: {self.level}, Health: {self.health}, Mana: {self.mana}, Attack: {self.attack}, Defense: {self.defense}, Speed: {self.speed}" 
    
    def special_move(self):
        if self.special_move_level == 1:
            self.special_move_level += 1
            if self.mana < 15:
                return f"Mana yetarli emas!"
            self.mana -= 15
            self.health += 15
            for obj in objects[1:]:
                if obj.type != "Necromancer":
                    obj.health += self.level * 3
            return f"\nNecromancer {self.name} o'yinchilarga mana berdi!"
        elif self.special_move_level == 2:
            self.special_move_level += 1
            if self.mana < 20:
                return f"Mana yetarli emas!"
            self.mana -= 20
            self.health += 20
            for obj in objects[1:]:
                if obj.type != "Necromancer":
                    obj.health += self.level * 4
            return f"\nNecromancer {self.name} o'yinchilarga mana berdi!"
        elif self.special_move_level == 3:
            if self.mana < 25:
                return f"Mana yetarli emas!"
            self.mana -= 25
            self.health += 25
            for obj in objects[1:]:
                if obj.type != "Necromancer":
                    obj.health += self.level * 5
            return f"\nNecromancer {self.name} o'yinchilarga mana berdi!"
    
def start_game(obj: Character):
    obj.mana += 3
    print(f"\n{obj.special_move()}")
    time.sleep(1.5)

objects = []
objects.append(Boss())
print(f"\n{objects[0]}")

print("\nQancha o'yinchilar yaratmoqchisiz?")
num_objects = get_int()

i = 0
def menu():
    print("1. Assassin")
    print("2. Paladin")
    print("3. Necromancer")
    print("4. Random tanlash")
    print("5. O'yinni boshlash")
    print("6. Chiqish")

    choice = get_int(False, 1, 6)
    return choice

assassins = 0
paladins = 0
necromancers = 0
for i in range(num_objects):
    choice = menu()

    if choice == 1:
        new_assasin = Assassin()
        print(f"Assassin yaratildi: {new_assasin}")
        objects.append(new_assasin)
        assassins += 1
    elif choice == 2:
        new_paladin = Paladin()
        print(f"Paladin yaratildi: {new_paladin}")
        objects.append(new_paladin)
        paladins += 1
    elif choice == 3:
        new_necromancer = Necromancer()
        print(f"Necromancer yaratildi: {new_necromancer}")
        objects.append(new_necromancer)
        necromancers += 1

    elif choice == 4:
        random_choice = random.choice(["Assassin", "Paladin", "Necromancer"])
        if random_choice == "Assassin":
            print(f"Random Assassin yaratildi!")
            new_assasin = Assassin()
            objects.append(new_assasin)
            assassins += 1
        elif random_choice == "Paladin":
            print(f"Random Paladin yaratildi!")
            new_paladin = Paladin()
            objects.append(new_paladin)
            paladins += 1
        elif random_choice == "Necromancer":
            print(f"Random Necromancer yaratildi!")
            new_necromancer = Necromancer()
            objects.append(new_necromancer)
            necromancers += 1
        else:
            print("Random tanlashda xatolik yuz berdi!")
            continue

    elif choice == 5:
        print("\nO'yin boshlanmoqda...")
        break
    elif choice == 6:
        print("\nO'yin tugadi!")
        break
    else:
        print("\nNoto'g'ri tanlov! Iltimos, qaytadan urinib ko'ring.")
        i = i - 1
        continue

    print(f"{i + 1}-ob'ekt yaratildi: {choice}")

    if i == num_objects - 1:
        print("\nO'yin boshlanmoqda...")
        print(f"Yaratilgan ob'ektlar soni: {num_objects}-ta")
        print(f"Assassinlar soni: {assassins}")
        print(f"Paladinlar soni: {paladins}")
        print(f"Necromancerlar soni: {necromancers}")
        print("")
while True:
    if len(objects) == 1 and objects[0].type == "Boss":
        print("\nBoss g'olib!")
        print("O'yin tugadi!")
        break
    if objects[0].type != "Boss":
        print(f"\nO'yinchilar g'olib!")
        print("O'yin tugadi!")
        break
    for obj in objects:
        start_game(obj)

        