num = 100
temp=num
binary_value = 0
value =''
while num >0:
    binary_value = num % 2
    num = num//2
    value=str(binary_value)+value
print(f"Binary result of {temp} is", value)


# def bin_con(given:int):
#     binary_value = 0
#     value = ''
#     while given > 0:
#         binary_value = given % 2
#         given = given // 2
#         value = str(binary_value) + value
#

