class Product:
    def __init__(self):
        self.price = 190
        self.name = "product"
        self.quantity = 30
    def printer(self):
        print(f"The {self.name} is cost {self.price}, there are {self.quantity} items")

product1=()
product1.printer()