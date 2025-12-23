
print('*' * 10)
#range
for i in range(10):
    print(i, end=' ')

list_ids = [1, 2, 3, 4, 5, 6]
for index,element in enumerate(list_ids):
    print("index =", index, "element =", element)

print("reversed list is", list(reversed(list_ids)))
print("reversing the string", list(reversed("Kiran")))

unsorted_list = [45, 76, 89, 34, 83]
print("sorted list", list(sorted(unsorted_list)))

names = ["a", "b", "c", "d"]  # names list

attendance = [91, 56, 76]  # attendance of the students
print("zip result is", list(zip(names, attendance, strict=False)))
# print("zip result is", list(zip(names, attendance, strict=True)))
#####################################################




        