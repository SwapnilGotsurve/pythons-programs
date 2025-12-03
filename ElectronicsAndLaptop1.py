class Electronic :
    def __init__(self, pow):
            self.pow = pow


class Laptop(Electronic):
    def __init__(self, pow, brand, model):
        super().__init__(pow)
        self.brand = brand
        self.model = model

    def show_details(self):
        print(f"Laptop Brand: {self.brand}, Model: {self.model}, Power: {self.pow}W")

l1 = Laptop(65, "Dell", "XPS 13")
l1.show_details()   
