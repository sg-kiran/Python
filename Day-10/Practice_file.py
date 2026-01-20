#
# def sum_of_list(nums:list) -> int:
#     count=0
#     for i in nums:
#         if type(i)!=int:
#             (print(f"non numeric value '{i}' skipped"))
#             pass
#         else:
#             count += i
#     return count
#
# value = sum_of_list([2,3, "b",6])

# def sum_avg_num(a:int,b:int,c:int) -> dict:
#     add = (a+b+c)
#     average = add/3
#     return{"sum of elements ":add , "average of elements ": average}
# print(sum_avg_num(2,3,4))




# def calc(a: int, b: int, op: str):
#     operations = {
#         "+": a + b,
#         "-": a - b,
#         "*": a * b,
#     }
#
#     if op == "/":
#         if b == 0:
#             return "Error: Division by zero"
#         return a / b
#
#     return operations.get(op, "Invalid operator")
#
# print(calc(10, 2, "*"))

#
# def prime_num(num: int) -> int:
#     factors = 0
#     for i in range(1, num + 1):
#         if (num % i == 0):
#             factors = factors + 1
#     return factors
# for j in range(100):
#     if prime_num(j)==2:
#         print(f"{j} is prime")

# for j in range(1,3):
#     for i in range(1, 11):
#         print(f"{j} *{i} =", j * i)
#     print("******************")
# mul_num = 1
# while mul_num<=3:
#     num = 1
#     while num <= 10:
#         print( mul_num, "* ", num, " = ", mul_num * num)
#         num += 1
#     print("++++++++++++++++")
#     mul_num +=1

#
#
# def reverse(num:int):
#     if num <0:
#         sign = -1
#     else:
#         sign = 1
#     num = abs(num)
#     rev = 0
#     while num > 0:
#         mid_rev = num % 10
#         num = num // 10
#         rev = rev * 10 + mid_rev
#     return rev * sign
# rev_num=reverse(-4321)
# print(rev_num)
#
#
# letters = list("abc")
#
#
# print(type(letters))
# print(letters)

# add_single_line= lambda a,b:a+b
# print("result of addition", add_single_line(2,3))
#
# singel_line_greet= lambda name: print("greet", name)
# singel_line_greet("Kiran")

flags_list = [1, 2, "Kiran"]

res = all(flags_list)
print("All the values present in the list are True : ", res)
flags_list = [False, False, True]
res = any(flags_list)
print("One of the values present in the list are True : ", res)