### Functional Programming
def apply_twice(func, arg):
    return func(func(arg))
def add_five(x):
    return x+ 5
print(apply_twice(add_five, 10))
# The functionn apply_twice takes another function as its argument, and it calls it twice inside its body.

## Pure functions
def pure_functions(x, y):
    temp = x + 2*y
    return temp / (2*x + y) 

# Impure functions
some_list = []
def impure(arg):
    some_list.append(arg)

# Lambdas
def my_func(f, arg):
    return f(arg)
my_func(lambda x: 2*x*x, 5)

# named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4)(-4))

# Map & Filter
def add_five(x):
    return x + 5
nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(nums)

# Generators
def countdown():
    i=5
    while i > 0:
        yield i 
        i -= 1
for i in countdown():
    print(i)

# Decorators
def decor(func):
    def wrap():
        print("==========")
        func()
        print("==========")
    return wrap
def print_text():
    print("Hello World!")

decorated = decor(print_text)
decorated()
# We defined a function decor that has a single parameter func. Inside decor, we defined a nested function
# named wrap. The wrap function will print a string, then call func(), and print another string. The decor
# function returns the wrap function as its result. The variable decorated is a decorated version of 
# print_text -- it's print_text plus something
# Using the @ symbol
def decor(func):
    def wrap():
        print("==========")
        func()
        print("==========")
    return wrap
@decor
def print_text():
    print("Hello World!")

print_text()

# Recursion
# Factorial case(n! = n * (n-1)!)
# where 1! = 1, which is the base case
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
print(factorial(0))
# Indirect Recursion
def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)
def is_odd(x):
    return not is_even(x)
print(is_odd(17))
print(is_even(23))

# *args & **kwargs
def function(named_arg, *args):
    print(named_arg)
    print(args)
function(1, 2, 3, 4, 5)
# The parameter *args must come after the named parameters to a function
def my_func(x, y=7, *args, **kwargs):
    print(kwargs)
my_func(2, 3, 4, 5, 6, a=7, b=8)
# a & b are the names of the arguments we passed to the function call
# **kwargs are not included in *args