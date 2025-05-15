from abc import ABC, abstractmethod

# 1

def get_int(type=True, min=1, max=100):
    max = max + 1
    if type:
        num = input(f"\nObjectlar sonini kiriting: ")
        if num.isdigit():
            num = int(num)
        else:
            print("Son kiriting!")
            return get_int()
        
        if num >= min and num <= max:
            pass
        else:
            print(f"{min} dan katta va {max} dan kichkina bo'lsin!")
            return get_int(min=min, max=max)
        return num
    else:
        num = input(f"\Sonni kiriting: ")
        if num.isdigit():
            num = int(num)
        else:
            print("Son kiriting!")
            return get_int(False, min, max)
        
        if num >= min and num <= max:
            pass
        else:
            print(f"Son {min} dan katta va {max} dan kichikina bo'lsin!")
            return get_int(False, min, max)
        return num

def get_float(min=1.0, max=100.0):
    num = input(f"\Float sonni kiriting: ")
    if num.isdigit():
        num = float(num)
    else:
        print("Son kiriting!")
        return get_float(False, min, max)
    
    if num >= min and num <= max:
        pass
    else:
        print(f"{min} dan katta va {max} dan kichikina bo'lsin!")
        return get_float(False, min, max)
    return num    

class DeliveryCostStrategy(ABC):
    @abstractmethod
    def calculate(self, distance: float):
        pass

class StandardDelivery(DeliveryCostStrategy):
    def calculate(self, distance: float):
        return distance * 1

class VipDelivery(DeliveryCostStrategy):
    def calculate(self, distance: float):
        return distance * 0.8

class StudentDelivery(DeliveryCostStrategy):
    def calculate(self, distance: float):
        return distance * 0.75

class DeliveryCalculator:
    def __init__(self, strategy: DeliveryCostStrategy):
        self.strategy = strategy

    def calculate_cost(self, distance: float):
        return self.strategy.calculate(distance)
    
num_of_objects = get_int()
for i in range(num_of_objects):
    print(f"\n{i+1}-ob'ekt uchun masofani kiriting: ")
    distance = get_int(False, 1, 30)
    print("\nYetkazib berish turini tanlang (1: standart, 2: vip, 3: student): ")
    delivery_type = get_int(False, 1, 3)
    if delivery_type == "standart":
        strategy = StandardDelivery()
    elif delivery_type == "vip":
        strategy = VipDelivery()
    elif delivery_type == "student":
        strategy = StudentDelivery()

    calculator = DeliveryCalculator(strategy)
    cost = calculator.calculate_cost(distance)
    print(f"Yetkazib berish narxi: {cost * 1000} so'm")

#2

class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class EmailNotification(Notification):
    def send(self, message: str):
        print(f"Sending Email: {message}")

class SMSNotification(Notification):
    def send(self, message: str):
        print(f"Sending SMS: {message}")

class TelegramNotification(Notification):
    def send(self, message: str):
        print(f"Sending Telegram message: {message}")

class NotificationSender:
    def __init__(self, channels: list):
        self.channels = channels

    def send_notifications(self, message: str):
        for channel in self.channels:
            channel.send(message)

obj_count = get_int()
for i in range(obj_count):
    print(f"\n{i+1}-ob'ekt uchun xabarni kiriting: ")
    message = input("Xabarni kiriting: ")
    print("\nXabarni yuborish turini tanlang (1: email, 2: sms, 3: telegram): ")
    notification_type = get_int(False, 1, 3)
    if notification_type == "email":
        channel = EmailNotification()
    elif notification_type == "sms":
        channel = SMSNotification()
    elif notification_type == "telegram":
        channel = TelegramNotification()

    sender = NotificationSender([channel])
    sender.send_notifications(message)

# 3
class TaxStrategy(ABC):
    @abstractmethod
    def calculate_tax(self, income: float):
        pass

class USTax(TaxStrategy):
    def calculate_tax(self, income: float):
        return income * 0.30

class EUTax(TaxStrategy):
    def calculate_tax(self, income: float):
        return income * 0.25

class UATax(TaxStrategy):
    def calculate_tax(self, income: float):
        return income * 0.20

class TaxCalculator:
    def __init__(self, strategy: TaxStrategy):
        self.strategy = strategy

    def calculate(self, income: float):
        return self.strategy.calculate_tax(income)

obgect_count = get_int()
for i in range(obgect_count):
    print(f"\n{i+1}-ob'ekt uchun daromadni kiriting: ")
    income = get_float(0, 100000)
    print("\nSolig' turini tanlang (1: US, 2: EU, 3: UA): ")
    tax_type = get_int(False, 1, 3)
    if tax_type == "US":
        strategy = USTax()
    elif tax_type == "EU":
        strategy = EUTax()
    elif tax_type == "UA":
        strategy = UATax()

    calculator = TaxCalculator(strategy)
    tax = calculator.calculate(income)
    print(f"Solig' summasi: {tax} so'm")

