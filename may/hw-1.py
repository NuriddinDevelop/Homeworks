from abc import ABC, abstractmethod
import random

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

class Account(ABC):
    def __init__(self, owner, initial_balance):
        self.__account_number = self._generate_account_number()
        self._balance = initial_balance
        self.owner = owner

    def __str__(self):
        return f"Account No: {self.__account_number}, Owner: {self.owner}, Balance: {self._balance}"

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Qiymat 0 dan katta bo'lishi kerak!")

    @abstractmethod
    def withdraw(self, amount):
        pass

    def transfer(self, to_account, amount):
        if amount > 0 and self.withdraw(amount):
            to_account.deposit(amount)
            return True
        return False

    @property
    def account_number(self):
        return self.__account_number

    @staticmethod
    def _generate_account_number():
        acc_number = ""
        acc_number += str(random.choice(nums[1:]))

        for i in range(16):
            acc_number += str(random.choice(nums))
        return acc_number

class SavingsAccount(Account):
    def __init__(self, owner, initial_balance, interest_rate):
        super().__init__(owner, initial_balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def add_interest(self):
        self._balance += self._balance * self.interest_rate

class CreditAccount(Account):
    def __init__(self, owner, initial_balance, credit_limit):
        super().__init__(owner, initial_balance)
        self.credit_limit = credit_limit

    def withdraw(self, amount):
        if self._balance - amount >= -self.credit_limit:
            self._balance -= amount
            return True
        return False

class Bank:
    def __init__(self):
        self.accounts = []

    def open_account(self, owner, account_type, **kwargs):
        if account_type == 'savings':
            account = SavingsAccount(owner, kwargs.get('initial_balance', 0), kwargs.get('interest_rate', 0.01))
        elif account_type == 'credit':
            account = CreditAccount(owner, kwargs.get('initial_balance', 0), kwargs.get('credit_limit', 1000))
        else:
            raise ValueError("Unknown account type")
        self.accounts.append(account)
        return account

    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def total_balance(self):
        balances = [acc._balance for acc in self.accounts]
        total = 0
        for i in balances:
            total += i
        return total

    def __str__(self):
        return "\n".join(str(acc) for acc in self.accounts)

# Bank obyektini yaratamiz
bank = Bank()

while True:
    print("\n--- BANK TIZIMI ---")
    print("1. Hisob ochish")
    print("2. Pul qo'shish (deposit)")
    print("3. Pul yechish (withdraw)")
    print("4. Hisoblar orasida pul o'tkazish (transfer)")
    print("5. Foiz qo'shish (faqat omonat hisoblar uchun)")
    print("6. Umumiy balansni ko'rish")
    print("7. Barcha hisoblarni ko'rish")
    print("0. Chiqish")

    tanlov = input("Tanlovni kiriting: ")

    if tanlov == '1':
        ism = input("Egasi ismini kiriting: ")
        tur = input("Hisob turi (savings/credit): ").lower()
        boshlangich = float(input("Boshlang'ich balans: "))
        if tur == 'savings':
            foiz = float(input("Foiz stavkasi (masalan, 0.05): "))
            acc = bank.open_account(ism, tur, initial_balance=boshlangich, interest_rate=foiz)
        elif tur == 'credit':
            limit = float(input("Kredit limiti: "))
            acc = bank.open_account(ism, tur, initial_balance=boshlangich, credit_limit=limit)
        print(f"Hisob ochildi. Hisob raqami: {acc.account_number}")

    elif tanlov == '2':
        acc_num = input("Hisob raqamini kiriting: ")
        acc = bank.find_account(acc_num)
        if acc:
            amount = float(input("Qo'shiladigan summa: "))
            acc.deposit(amount)
            print("Pul qo'shildi.")
        else:
            print("Hisob topilmadi.")

    elif tanlov == '3':
        acc_num = input("Hisob raqamini kiriting: ")
        acc = bank.find_account(acc_num)
        if acc:
            amount = float(input("Yechiladigan summa: "))
            if acc.withdraw(amount):
                print("Pul yechildi.")
            else:
                print("Yetarli mablag' mavjud emas.")
        else:
            print("Hisob topilmadi.")

    elif tanlov == '4':
        from_acc_num = input("Jo'natuvchi hisob raqami: ")
        to_acc_num = input("Qabul qiluvchi hisob raqami: ")
        amount = float(input("O'tkaziladigan summa: "))
        from_acc = bank.find_account(from_acc_num)
        to_acc = bank.find_account(to_acc_num)
        if from_acc and to_acc:
            if from_acc.transfer(to_acc, amount):
                print("Pul muvaffaqiyatli o'tkazildi.")
            else:
                print("Pul o'tkazib bo'lmadi.")
        else:
            print("Hisoblardan biri topilmadi.")

    elif tanlov == '5':
        acc_num = input("Omonat hisob raqamini kiriting: ")
        acc = bank.find_account(acc_num)
        if isinstance(acc, SavingsAccount):
            acc.add_interest()
            print("Foiz qo'shildi.")
        else:
            print("Bu hisob omonat hisobi emas.")

    elif tanlov == '6':
        print(f"Bankdagi umumiy balans: {bank.total_balance()}")

    elif tanlov == '7':
        print("--- Hisoblar ---")
        print(bank)

    elif tanlov == '0':
        print("Dastur yakunlandi.")
        break

    else:
        print("Noto'g'ri tanlov.")

