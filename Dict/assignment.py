"""3. What types of values can a dictionary store? Can values be mutable? Show with an example program."""
from copyreg import constructor

# d1={"name":"Kiran","age":33,}
# print(d1)
# d1["age"]=34
# print(d1)
"""4. What are different ways to create a dictionary in Python? Write example programs for each method."""
"""5. How do you create an empty dictionary?"""
# empty dictionary
d2={}
# using curly braces
# d3={"name":"Kiran","age":33,}
# using dict constructor()
# d4=dict(name="Kiran",age=33)
# print(d4)
"""6. How do you access dictionary values safely? Explain direct access vs .get() with examples."""
"""to get the values safely we shoud use .get() method, if that key is not present, the output will be displayed as None 
or the value that we want"""
# print(d1.get("34", "not found"))

"""7. How do you add new items and update existing items in a dictionary? Explain = assignment and .update() with examples."""
""".update will update value of a key if that key is present, if not add, it will add new key value pair 
whereas = assignment operator will add new key value pair to the dictionary, main diff is, we can add mutiple key value pairs using update
but we cannot add it using assignment operator"""
d5={"name":"Kiran","age":33,}
d5.update(age=35)
print(d5)#{'name': 'Kiran', 'age': 35}
d5.update(name="Sravan")
print(d5) #{'name': 'Sravan', 'age': 35}
d5.update(sm="Sravan",age_sm=38)
print(d5) #{'name': 'Sravan', 'age': 35, 'sm': 'Sravan', 'age_sm': 38}
d5["sm"]= "Sravan1"
print(d5) #{'name': 'Sravan', 'age': 35, 'sm': 'Sravan1', 'age_sm': 38}
d6={"name":"Kiran","age":33}
d6=d5.update(d6)
print(d5) #updated values using another dict --> {'name': 'Kiran', 'age': 33, 'sm': 'Sravan1', 'age_sm': 38}
"""8. How do you remove items from a dictionary? Explain del, .pop(), and .popitem() with example programs."""