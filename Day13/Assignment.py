""" Note: Try to re write all these programs with return statements.


    1. Write a program to add, subtract, multiply, and divide two numbers."""

def cal_num(a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    return [c,d,e,f]
results=cal_num(10,5)
print("addition =", results[0])
print("sub",results[1])

"""    2. Write a program to check whether a number is even or odd."""

def evenorodd(a):
    return a%2==0
b=evenorodd(7)
if b==True:
    print("even")
else:
    print("odd")

"""    3. Write a program to find the largest of three numbers."""

def larofnum(a,b,c):
    if(a>b)&(a>c):
        d=a
    elif(b>a)and(b>c):
        d=b
    else:d=c
    return [a,b,c,d]
e = larofnum(2,3,4)
print("largest of below three numbers\n", e[0], e[1], e[2], "\n is\n", e[3])