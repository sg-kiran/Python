# 1. What are loops in Python.
# A. Loops are used for performing repeated tasks in a easy way if you know how many times we have to perform
# 2. What is the syntax of for loop.
# for <variable> in (iterables):
#     {
#
#     }
# 3. What is the use of continue statement in Python. Where do you use it and write multiple examples for it.
"""continue keyword is used to let the python know when to skip the loop and continue executing the further code when a
certain condition is met"""
# 4. What is the use of break statement in Python. Where do you use it and write multiple examples for it.
"""break keyword is used to let the python know when to break the loop and stop executing the further code when a
certain condition is met"""
#
# Programs:
# 1. Print Numbers from 1 to 100 That Are Divisible by 3.
# for num in range(10):
#     if(num % 3 == 0):
#         print(num ,"is divisible by 3")
#     else:
#         print(num, "is not divisible by 3")

# 2. Print Prime Numbers from 1 to 100.
# 3. Print mathematical tables from 1 to 10.
# 4. Print 1 to current year that are leap years.
# 5. Sum of All Even Numbers from 1 to 100
# for table_num in range(11):
#     for table_num in range(11):
#         if (table_num == 0):
#             for i in range(10):
#                 if (i == 0):
#                     print(table_num, "*", i, "=", (table_num * i))
#         print("=========")
#
#
# # 6. Numbers from 1 to 100 That Are Both Divisible by 2 and 5

"""Write a code to reverse a string"""

# stat = []
# def name(value):
#     for i in value:
#         stat.insert(0, i)
#     print(stat)
# a = str(input("enter the string"))
# name(a)


def name(value):
    for i in value:
        stat1 = stat1 + i
    print(stat1)
a = str(input("enter the string"))
name(a)

