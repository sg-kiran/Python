""" 1. Write a program to add, subtract, multiply, and divide two numbers."""
a = 10
b = 2

print("a+b =", a+b)
print("a-b =", a-b)
print("a*b =", a*b)
print("a/b =", a/b)
print("a%b =", a%b)
print("a**b =", a**b)

"""    2. Write a program to check whether a number is even or odd."""

a = 22
if a%2 == 0:
    print(a,"is an even number")
else:
    print(a, "is an odd number")

"""    3. Write a program to find the largest of three numbers."""
a = 10
b = 10
c = 10
if (a>b) & (a>c):
    print("Bigger value is ", a)
elif(b>a) & (b>c):
    print("bigger value is ", b)
else:
    print("bigger value is ", c)

"""4. Write a function to calculate the square of a number."""
a = 3
print("square of",a, "is",a**2)

"""5. Write a program to check whether a number is positive, negative, or zero."""


a = -1
if(a>0):
    print(a, "is a positive number")
elif(a==0):
    print(a, "is a zero")
else:
    print(a, "is a negative number")

"""6. Write a program that takes a username and prints a greeting message using a function."""

def greet(name:str):
    print(name)
greet("Kiran")
"""    7. Write a program to calculate the simple interest."""
P=100
T=1
R=5
I= (P*T*R)/100
print(I)

"""    8. Write a program to check if a given year is a leap year."""

Y=1900
if ((Y%4==0)or(Y%400==0)):
    if(Y%100==0):
        print("Not a Leap year")
    else:
        print("leap year")

"""9. Write a program to find the greatest of two numbers using a function."""

# def gr_two(a:int, b:int):
#     if(a>b):
#         print(a, "is greater value")
#     else:
#         print(b, "is greater value")
# a=(input('enter value of a \n'))
# b=(input('enter value of b \n'))
# gr_two(a,b)

"""10. Write a program that reads a number and print whether it is divisible by both 3 and 5."""
a = int(input('enter the value for a \n'))
if(a%3==0)and(a%5==0):
    print(a, "is divisible by by 3 and 5")
else:
    print(a, "is not divisible by by 3 and 5")