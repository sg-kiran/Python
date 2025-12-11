"""4. What are the different ways to create a tuple? Write an example program."""
"""5. How can you create an empty tuple? Write an example program."""
#1.empty tumple
t1 = ()
print(type(t1), t1)
#2.tuple with elements
t2 = (1,2,3,4,5,2)
print(t2)
#3. tuple with elements, no brackets
t3= 1,2,3,4,5
print(t3)
"""6. How do you create a tuple with a single element? Why is a comma required? Write an example program."""
t4 = (1,)
t5 = (1) # without comma, the value or element will not be considered as tuple it will be as per the value(like int, float etc)
print(t4)
print(type(t5))
"""7. What is tuple packing? Write an example program."""
# assigning multiple values to the same variable
t6 = 12,13,14
"""8. What is tuple unpacking? Write an example program."""
t7 = 1,2,3,4,5,6,7,8,9
a,b,*c=t7
print(a)
print(b)
print(c)