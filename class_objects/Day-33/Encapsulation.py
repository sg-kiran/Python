class Employee:
    def __init__(self, name:str, age:int, password:str) -> None:
        self.name = name
        self.age = age
        self.__password = password

    def get_password(self):
        return self.__password

    def set_password(self, newpassword:str):
        self.__password = newpassword
E1 = Employee("Honda", 42, "rt@erev")
print(E1.get_password())
E1.set_password("kk@wewrr3")
print(E1.get_password())

""" encapsulation is a process of hiding internal data and allowing access through well defined methods"""
class Student(Employee):
class Student:
    def __init__(self): # init..
        pass


    def initialize(self, id: int, name: str): # Will it be executed? Not yet executed
        self.id = id
        self.name = name


student = Student()
student.initialize(12, "ABC")
print(student.id)