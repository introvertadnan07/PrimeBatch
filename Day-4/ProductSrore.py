class Product:
    count = 0
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1   # FIX
    
    def get_info(self):
        print(f"price of {self.name} is Rs.{self.price}")
    
    @classmethod  
    def get_count(cls):
        print(f"total product in store = {cls.count}") 
        
    @staticmethod
    def calc_discount(price, discount):
        print(f"discounted price = {price - (price * discount / 100)}")

# create objects
p1 = Product("Phone", 10_000)
p2 = Product("laptop", 50_000)
p3 = Product("Pen", 10)

p1.get_info()
p2.get_info()

Product.get_count()
p2.calc_discount(p1.price, 12)