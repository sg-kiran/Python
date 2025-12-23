
""" print the numbers from 0 to 9 in sequence"""
# for num in range(10):
#     print(num)

"""print the even and odd numbers between 0 to 9. Skipping to check the number 0"""
# for num in range(10):
#     if (num!=0):
#
#         if (num % 2 == 0):
#             print(num ,"is even")
#         else:
#             print(num, "is odd")

"""do the same code in different way"""
# for num in range(10):
#     if (num == 8):
#         print("continue 8") """this block of code will be skipped executes the rest of the loop"""
#         continue
#         # print("continue")
#     if (num %2 == 0):
#         print(num, "is even")
#     else:
#         print(num, "is odd")

"""Break the execution loop if the number hits 5"""
for num in range(10):
    if (num == 8):
        print("break 8") #break the loop when the loop if this condition is met
        break
        # print("continue")
    if (num %2 == 0):
        print(num, "is even")
    else:
        print(num, "is odd")