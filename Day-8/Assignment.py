"""
Q. What is reassignment? How do you do this.
A. reassignment means overriding the existing value of a variable and giving it a new value
a=2
print(a)
a=3
print(a)
Python reassigns the name to a new object (rebinding), rather than “overriding the value.”
"""

"""
Q. What do you mean by `Python is a dynamic typing language`. Can you please give a brief explaination with some examples. 
A. It means there is no need define the data type along with the variable and python will automatically identifies which data type you have entered.
examples:
a =3 # it is of data type int
name = "Kiran" # it is of data type str
"""

# a= int(input("enter your age"))
# if(a>=18):
#     print("Eligible to Vote")
# else:
#     print("Not eligible to vote")


# a = 15
# b = 9
#
# if (a>b):
#     print(a,"is larger")
# else:
#     print(b, "is larger")


"""
Write a program that takes marks (0–100) and prints:

A if marks ≥ 90
B if marks ≥ 80
C if marks ≥ 70
D if marks ≥ 60
F if marks < 60
"""

# a=int(input("enter the marks"))
# if(a>=90):
#     print("Grade: A")
# elif(a<90 and a>=80):
#     print("Grade: B")
# elif(a<80 and a>=70):
#     print("Grade: C")
# elif(a<70 and a>=60):
#     print("Grade: D")
# else:
#     print("Grade: F")
try:
    a = int(input("enter the number"))
    if a == 0:
        print("Zero")
    elif a > 0:
        print("Positive number")
    else:
        print("Negative number")
except ValueError:
    print("please enter numeric value")
