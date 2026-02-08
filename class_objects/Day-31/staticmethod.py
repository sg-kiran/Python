
class Student:
    SchoolName = "Balayesu"
    def __init__(self, name:str, age:int, marks:str):
        self.name = name
        self.age = age
        self.marks = Student.str_to_int(marks)



    @classmethod
    def modifyschoolname(cls, name:str):
        cls.SchoolName = name

    @staticmethod
    def str_to_int(marks:str):
        return int(marks)

S1 = Student("Kiran",22, "234")
print(S1.marks)

"""staticmethod does not depend on any object or class and can act on its own and returns the values
is not necessarily required, but it improves readability"""