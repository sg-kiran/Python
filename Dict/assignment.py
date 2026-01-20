# """3. What types of values can a dictionary store? Can values be mutable? Show with an example program."""
# from copyreg import constructor
#
# d1={"name":"Kiran","age":33,}
# print(d1)
# d1["age"]=34
# print(d1)
# """4. What are different ways to create a dictionary in Python? Write example programs for each method."""
# """5. How do you create an empty dictionary?"""
# # empty dictionary
# d2={}
# # using curly braces
# # d3={"name":"Kiran","age":33,}
# # using dict constructor()
# # d4=dict(name="Kiran",age=33)
# # print(d4)
# """6. How do you access dictionary values safely? Explain direct access vs .get() with examples."""
# """to get the values safely we should use .get() method, if that key is not present, the output will be displayed as None
# or the value that we want"""
# print(d1.get("34", "not found"))
#
# """7. How do you add new items and update existing items in a dictionary? Explain = assignment and .update() with examples."""
# """.update will update value of a key if that key is present, if not, it will add new key value pair
# whereas = assignment operator will add new key value pair to the dictionary, main diff is, we can add mutiple key value pairs using update
# but we cannot add it using assignment operator"""
# d5={"name":"Kiran","age":33,}
# d5.update(age=35)
# print(d5)#{'name': 'Kiran', 'age': 35}
# d5.update(name="Sravan")
# print(d5) #{'name': 'Sravan', 'age': 35}
# d5.update(sm="Sravan",age_sm=38)
# print(d5) #{'name': 'Sravan', 'age': 35, 'sm': 'Sravan', 'age_sm': 38}
# d5["sm"]= "Sravan1"
# print(d5) #{'name': 'Sravan', 'age': 35, 'sm': 'Sravan1', 'age_sm': 38}
# d6={"name":"Kiran","age":33}
# d6=d5.update(d6)
# print(d5) #updated values using another dict --> {'name': 'Kiran', 'age': 33, 'sm': 'Sravan1', 'age_sm': 38}
# """8. How do you remove items from a dictionary? Explain del, .pop(), and .popitem() with example programs."""
#
# # Using del to remove a specific key
# person = {"name": "Kiran", "age": 30, "city": "Gothenburg"}
# del person["age"]
# print(person)  # {'name': 'Kiran', 'city': 'Gothenburg'}
# # Trying to delete a missing key -> KeyError
# # del person["karma"] #KeyError: 'karma'
# print("before deleting")
# del person
# # print(person) # deletes the complete variable itself not just an item
#
# #using .pop to remove a specific key and it returns the removed key
# setting = {"theme": 'dark', "timeout": 30}
# popvalue = setting.pop("timeout")
# print(setting)
# print("removed value", popvalue)
#
# #trying to delete missing key with and without default provided
# setting1 = {"theme": 'dark', "timeout": 30}
# popvalue1=setting1.pop("name", "notfound")
# print(popvalue1)
# # popvalue2=setting1.pop("name")
# # print(popvalue2) #KeyError: 'name'
#
#
# inventory = {"apples": 10, "bananas": 5, "oranges": 8}
# kv = inventory.popitem()
# print("popped:", kv)     # e.g., ('oranges', 8)
# print(inventory)         # {'apples': 10, 'bananas': 5}
# # popitem on empty -> KeyError
# empty = {}
# try:
#     empty.popitem()
# except KeyError:
#     print("Cannot popitem() from an empty dict")
# # examples of usage of .pop/.del/.popitem
#
# d = {"a":1,"b":2,"c":3,"d":4}
# print(d)
# tobedeleted={"a","b","x"}
# for i in tobedeleted:
#     d.pop(i, "missing") #even though the key 'x' is missing it will not through any keyError as we are using .pop along with default value
# print(d)
#
# scores = {"alice": 91, "bob": 58, "carol": 77, "dave": 42}
# #delete the keys whose score is less than 60
# names= list(scores.keys())
#
# for i in names:
#     if scores[i] <60:
#         del scores[i]
# print(scores)
#
#
# def remove_with_del(d, key):
#     try:
#         del d[key]
#         return True, d
#     except KeyError:
#         return False, d
#
# data = {"id": 101, "status": "open", "owner": "Kiran"}
# ok, after = remove_with_del(data, "status")
# print(type(after))
# print(ok, after)  # True {'id': 101, 'owner': 'Kiran'}
# ok, after = remove_with_del(data, "missing")
# print(ok, after)  # False {'id': 101, 'owner': 'Kiran'}
#
######################################################################

"""1. Count the occurrences of each character in a string
Input: "hello world"
Output:
{'h':1, 'e':1, 'l':3, 'o':2, ' ':1, 'w':1, 'r':1, 'd':1}
``
"""

# def ele_count(word:str):
#     d = {}
#     str_list = list(word)
#     for j, k in enumerate(str_list):
#         count = 0
#         for i in str_list:
#             if i == str_list[j]:
#                 count += 1
#                 pass
#         d.update({str_list[j]: count})
#     return d
#
# print(ele_count("hello world"))

# def ele_count(word: str):
#     return {ch: word.count(ch) for ch in word}
#
# print(ele_count("hello world"))
#
# def ele_count(word1:str):
#     return {ch: word1.count(ch) for ch in word1}
# print(ele_count("hello world"))

# def stri_true(word2:str):
#     return { ch: True for ch in word2}
# print(stri_true('python'))

def list_squ(l:list):
    return { (lambda a: a*a) (i)for i in l}
print(list_squ([1,2,3]))
