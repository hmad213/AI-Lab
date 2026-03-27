class Product:
    def __init__(self, n, p):
        self.name = n
        self.price = p

    def calculate_tax(self):
        return 0

class Electronics(Product):
    def __init__(self, n, p, wp):
        super().__init__(n, p)
        self.warranty_period = wp

    def calculate_tax(self):
        return self.price * 0.15

class Clothing(Product):
    def __init__(self, n, p, s, f):
        super().__init__(n, p)
        self.size = s
        self.fabric = f

    def calculate_tax(self):
        return self.price * 0.05

class Wallet:
    def __init__(self, b):
        self.__balance = b

    def get_balance(self):
        return self.__balance
    
    def update_balance(self, b):
        self.__balance = b