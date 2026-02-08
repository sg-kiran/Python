class Bike:
    Name = "TVS"
    def __init__(self, branch:str, price:int):
        self.branch = branch
        self.price = price
    @classmethod
    def name(cls, Name):
        cls.Name = Name

starcity = Bike("Hindupur", 20000)
print(starcity.Name)
starcity.Name = "Yamaha" #instance level modification is done
print(starcity.Name) #out will be Yamaha
starcity.name("Bajaj") #modifying the class level variable using class level method
""" but the output will be still Yamaha because the lookup order will be instance level --> class level --> parent classm here instance level is available which is Yamaha"""
print("it should print Bajaj but it will print 'Yamaha':",starcity.Name)
print(Bike.Name) # output will be Bajaj as you are directly accessing the class level variable not through object instance
Bike.Name = "Honda" #class level variables can also be modified using class name
print(Bike.Name)

""" Instance variables override class variables during attribute lookup, 
so even if a class variable is modified, 
an existing instance variable with the same name will be accessed first."""
