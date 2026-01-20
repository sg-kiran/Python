emp_id = [1, 2, 3, 4, 5]
employee_ids_names = [1,2, 'A', "X", False, 23.67, 67]
# new_emp_id=employee_ids_names[0:5:2]
# print(new_emp_id)
# print(employee_ids_names[::2])
# print(employee_ids_names[3::])
emp_id.append(5)
# print(emp_id)
# emp_id.insert(2,99)
# print(emp_id)
emp_id.extend([6,7])
# print(emp_id)
# emp_id.remove(99)
# print(emp_id)
# emp_id.pop()
# print(emp_id)
# # emp_id.clear()
# # print(emp_id)
# emp_id.reverse()
# print(emp_id)
# emp_id.sort()
print(emp_id)
# print(emp_id.index(3))

print(emp_id[1])
print(emp_id.index(5))

"""2. Write down the program on finding the index of some element in the list."""
# emp_list=[22,33,44,55,66,77]
# # element=88
# def find(element):
#     ind = 0
#     for i in emp_list:
#         if i != element:
#             ind += 1
#         elif i == element:
#             break
#     return ind
# print(len(emp_list))
# a = find(99)
# if a < len(emp_list):
#     print("element is found at", a)
# else:
#     print("not found")

# print(emp_list.index(22))
"""3. Write down the program on finding count of occurances of the element in the list."""
#
# ind =0
# occ =0
# emp_list1=[22,33,44,55,66,77,33]
# def find(element):
#     # ind = 0
#     # occ = 0
#     for i in emp_list1:
#         if i != element:
#             ind += 1
#         elif i == element:
#             occ += 1
#     return [ind, occ]
# print(len(emp_list1))
# a = find(33)
# print(a)
# if a[0] < len(emp_list1):
#     print("element is found at", a[0])
# else:
#     print("not found")
#
# print("num of occurrences ", a[1])

# print(emp_list1.count(28))  #simple way to do it

# """4. Write down the program to add one list to other list."""
# emp_list2 = [22,33,44,55]
# emp_list3 = [66,77,88,99]
# for i in emp_list3:
#     emp_list2.append(i)
# print(emp_list2)
# print(emp_list2[-4::-2])
# print(emp_list2[-4::2])
# print(emp_list2[::2])

# print(emp_list2+emp_list3)
# print(emp_list2.count(22))

