
# #absolute of a value
# print(abs(-30))
#
# #power of a value
# print(pow(10,2))
#
# #rounding of the decimal number
# print(round(32.1234,2)) #if no value given in the ndigits, it will be considered 0

l=[1,2,28,4,32,6,7]
#minimum value
print(min(l))
#maximum number
print(max(l))

high_value=0
for i in l:
    if high_value==0:
        high_value = i
        continue
    if high_value< i:
        high_value =i
print("highest value",high_value)

#sum of elements in a list or tuple
l1=[1,2,3]
t1=(1,2,3)
print(sum(l1))
#write the code
total=0
for i in l1:
    total+= i
print("sum of values =",total)

print(sum(l1,10)) # it is considering 10 as another element of list
print(sum(t1))
print(sum(t1,10))
print(sum(t1, start=10))

#to check if the all the values in the list are true
l3 = [True, 1, 2]
res = all(l3)
print("all the values present in the list are true:", res)

# for i in l3:
#     if(i == False):
#         print("it has false")
#         break
# print("it has only true")

#to check if any one of the values in the list is true
l3 = [True, 1, False]
res1 = any(l3)
print("one of the values present in the list are true:", res1)

# How can I create a function which accepts dynamic number of integers and print them.

# def dynamic_int(*arguments):
#     print("the numbers entered \n",arguments)
# dynamic_int(1,2,3,4,5)

def n_num_values_without_collection(*argments):
    print("The Values are ==>", argments)
    print(type(argments))
n_num_values_without_collection("1", "2", 3, 4, 5)