

def fun1(a,b):   #2,3
    n=a**2+b     #4+3
    return n     #7

def fun2(x,y):   #2,3
    z=fun1(x,y)  #7
    return z+y   #7+3

def fun3(p,q):
    r=fun2(p,q)  #10
    u=fun1(p,q)  #7
    return r+u   #10+7

print(fun3(2,3))

#1. Positional Arguments

def greet_user(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet_user("Alice", 25)

# 2. Default Arguments

def greet(name='User'):
    print(f"Hello", name)
greet ()

# 3. Keyword Arguments

def display_info(name, city):
    print(f"{name}, Lives in {city}.")

display_info(city="Bhilai", name="Ashish")