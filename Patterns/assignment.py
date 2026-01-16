
# #square fill pattern
# for i in range(6):
#     print('* '* 6)
# print("============================================================")

# #Right half pyramid
#
# for i in range(1, 6):
#     print('* ' *i)
# print("============================================================")

# #Reverse Right half pyramid
#
# for i in range(5, 0, -1):
#     print('* ' * i)
# print("============================================================")

# #Left half pyramid
n = 5
for i in range(1,n+1):
    spaces = "  "* (n-i)
    stars = " *"* i
    print(spaces,stars)
print("============================================================")

# # reverse Left half pyramid
# # n = 5
# # for i in range(n,0,-1):
# #     spaces = "  "* (n-i)
# #     stars = " *"* i
# #     print(spaces + stars)
#
# m =5
# for i in range(m+1,0,-1):
#     spaces1 = " "*(m-(i-1))
#     stars1 = " *"*(6-i)
#     print(spaces1+stars1)
#
#
