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
a,*b, c=t7
print(a)
print(b)
print(c)
"""9. What happens if the number of variables on the left side does not match the number of values in a tuple during unpacking?"""
# t8=3,4,5
# d,e,f,g=t8
# print(d, e, f, g)
#Not enough values to unpack(expected 4, got 3)
"""11. Can tuples contain mutable elements? Explain with an example."""
"""15. Can we modify elements inside a tuple? If not, how can we indirectly modify the content?"""
# Yes, tuples can contain mutable elements like lists
t9 = (2,3,4,[5,6])
print(t9)
t9[3].append(7)
print(t9)
"""12. Are tuples immutable? What does immutability mean in this context?"""
"""
Yes, tuples are immutable, which means the structure of the tuple cannot be changed but if the 
element itself is mutable then that can be changed.
"""

"""13. How can you access elements inside a tuple?"""
"""
1. using indexing
2.slicing
3. using loops
"""
#t9 = (2,3,4,[5,6])
print("using indexing",t9[1])
print("using slicing",t9[0:4])
for i in t9: #printing using for loop and if the element is a value, printing those values also individually
    if(type(i)==list):
        print("below are the values from list")
        for j in i:
            print(j,"is of type", type(j))
    else:
        print(i,"is of type", type(i))


"""14. What is nested tuple unpacking? Provide a scenario where it is used."""
"""
nested tuple unpacking is used to unpack the tuple elements of type list of tuple """

print("nested tuple unpacking", t9[3][1])
"""16. How does tuple assignment help in swapping values?"""
a,b=(2,3)
(b,a)=(a,b)
print(a)
print(b)

"""19. Can two tuples be concatenated? How?"""
t11= t6+t7
print(t11)
# t12= t6-t7
# print(t12) this will not work as - is not supported for tuple
