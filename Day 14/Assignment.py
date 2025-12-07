"""1. Write a program to create a function that takes two numbers as mandatory arguments and returns their sum."""

def sum_of_two(a=2,b=3):
    print(a+b)
sum_of_two()
"""
2. Write a function that accepts a number and returns whether it is even or odd.

3. Write a function that takes two numbers and returns the largest one.

4. Write a function that accepts a number and returns whether it is positive, negative, or zero.

5. Write a function that takes a year and returns whether it is a leap year or not.

"""
"""
B. Functions with Optional (Default) Arguments. 

1. Write a function to calculate simple interest where the rate has a default value.
"""
def SI(P,T,R=5):
    I= (P*T*R)/100
    print(I)
SI(100,1)

"""2. Write a function that prints a greeting message. If no name is passed, it should greet as "Hello, Guest"."""

def greet(name="Guest"):
    print("Hello", name)
greet("Kiran")

"""3. Write a function to calculate the area of a rectangle where width is optional (if width is missing, treat it as a square)."""

def area(L,W=None):
    if W is None:
        print(L*L)
    else:
        print(L*W)
area(2,3)
