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
        print(f"playing music on {self.color} and {self.model} {self.company}phone")

nokiamobile = mobile("red","Nokia")
print(nokiamobile.Year)
print(nokiamobile.music("India"))

# class tv:
#     def __init__(self):
#         self.model = 2023
# lg_tv=tv()
# print(lg_tv.model)