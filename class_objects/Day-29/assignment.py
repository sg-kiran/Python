# class CarWithAttributes:
#     def __init__(self):
#         self.color = "white"
#         self.price = "22222"
#     def drive(self, a):
#         print("Driving", self.color, "car",a)
#         return 0
#
# carwithattributes= CarWithAttributes()
#
# print(carwithattributes.price)
# print(carwithattributes.drive(12))

class mobile:
    def __init__(self, color:str, model:str, Year:int=2026):
        self.color=color
        self.model=model
        self.Year=Year
    def music(self, company:str):
        self.company=company
        print(f"playing music on {self.color} and {self.model} {self.company}phone")

    def call(self):  # Method
         return "Calling"

    def music_player(self):
        print("Playing Music.")

    def video_player(self):
        print("Playing a Movie.")

nokiamobile = mobile("red","Nokia")
print(nokiamobile.Year)
print(nokiamobile.call())


# class car:
#     def __init__(self,colour:str, price:float, made:int):
#         self.colour = colour
#         self.price = price
#         self.made = made
#     def music(self):
#         print(f"listening music in {self.colour} car ")
#
# white_car = car("white", 20000, 2023)
# print(white_car.colour)
# print(white_car.price)
# print(white_car.music())
#
#
