class Laptop:
    storage_type = "ssd"
    
    def __init__(self, RAM, Storage):
        self.RAM = RAM
        self.storage = Storage
        
    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")
        
    def get_info(self):
        print(f"Laptop has {self.RAM} RAM & {self.storage} storage ({self.storage_type})")
    
    @staticmethod
    def discount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"final price = {final_price}")

l1 = Laptop("32gb", "1024gb")
l2 = Laptop("16gb", "512gb")

l1.get_info()
l2.get_info()

l1.get_storage_type()

Laptop.discount(40_000, 10)  # or l1.discount(40_000, 10)
