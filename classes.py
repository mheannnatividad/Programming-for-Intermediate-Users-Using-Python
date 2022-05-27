class Customers:
    greeting = "Welcome to the Cofee Palace!"
    
    def __init__(self, name, beverage, food, total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total
        
c_1 = Customers("Elaine", "Strawberry Frappuccino", "Tuna Wrap", 270)
c_2 = Customers("Jerry", "Caramel Macchiato", "Glazed Doughnut", 230)
#Customer Elaine
print(c_1.greeting)
print(c_1.name)
print(c_1.beverage)
print(c_1.food)
print(c_1.total)
#Customer Jerry
print(c_2.name)
print(c_2.beverage)
print(c_2.food)
print(c_2.total)
        
    