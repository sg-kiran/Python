#addition of two numbers
add = lambda x,y:x+y
print(add(2,3))

"""Sorting with a custom key, Sort by the second item in each tuple:"""

t= [("a",3),("c",2),("b",4),("e",1)]
t.sort(key=lambda item:item[1])
t.sort(key=lambda item:item[1], reverse=True)
print(t)

#write the program without using lambda or sort function
big=0
index = 0
new_t=[]
for i,element in enumerate(t):
    if big==0:
        big = element[1]
        index = i
        new_t.insert(index,(element))
    elif element[1]<big:
        big = element[1]
        index = 0
        new_t.insert(index,(element))
    else:
        new_t.append(element)

print(new_t)

#######filter######
ids=(1,2,3,4,5,6,7)
evenorodd_func=(lambda i:i%2==0)
print("3 is even",evenorodd_func(3))

res = list(filter(evenorodd_func,ids))
print("even numbers=", res)

"""Keep numbers divisible by 3 from range(1, 20)."""
divby3=(lambda i:i%3==0)
res1= list(filter((divby3), range(1,21)))
print(res1)

"""From ["apple", "kiwi", "banana", "fig"], keep words containing "a"""
words= ["apple", "kiwi", "banana", "fig"]
cont_a=list(filter((lambda w: "a" in w),words))
print(cont_a)

""" From [0, 1, 2, "", "x", [], [10], None], remove falsy values (no custom function)"""
lis=[0, 1, 2, "", "x", [], [10], None]
print(list(filter(None,lis)))

#####map function##########
num=[1,2,3,4,5,6]
print("square of ",list(map(lambda i: i*i, num)))


