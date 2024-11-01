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



class Rectangle:
    def __init__(self):
        self.width = 30
        self.height = 20
        self.calculate_perimeter = 2*self.width + 2*self.height
        self.calculate_area = self.height * self.width
    def printer(self):
        print(f"Rectangle has width {self.width} and height {self.height}.The area is {self.calculate_area} and perimeter {self.calculate_perimeter}")

rectangle1=()
rectangle1.printer()