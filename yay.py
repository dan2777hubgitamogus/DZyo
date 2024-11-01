class Product:
    def __init__(self):
        self.price = 190
        self.name = "product"
        self.quantity = 30
        self.calculate_total_price = self.price * self.quantity
        self.display_info = "The computer game"
    def printer(self):
        print(f"The {self.name} is cost {self.price}, there are {self.quantity} items,total price is{self.calculate_total_price},{self.display_info}")

product1=()
product1.printer()