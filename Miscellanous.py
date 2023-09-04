x = 9
x %= 2
x += 3
print(x)

####
spam = "7"
spam = spam + "0"
eggs = int(spam) + 3
print(float(eggs))

####
print(17%3)

####
spam = 7
if spam > 5:
    print("five")
if spam > 8:
    print("eight")    

num = 7
if num > 3:
    print("3")
    if num < 5:
        print("5")
        if num == 7:
            print("7")


## continue statements
i = 0
while i < 5:
    i += 1
    if i == 3:
        print("Skipping 3")
        continue
    print(i)


i = 0
while True:
    i +=1
    if i == 2:
        continue
    if i == 5:
        break
    print(i)

## in operator usage
nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1]- 5
print(nums)
if 4 in nums:
    print(nums[3])
else:
    print(nums[4])

x = "hello world"
if "world" in x:
    print("Yes")\
    
## not operator usage
nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print( 3 not in nums)

## for loops
nums = [4, 7, 3, 1]
for x in nums:
    print(x*2)

# break and continue statements can also be used in the for loop: to stop the loop or jump over to the next iteration.
text = "some text"
for x in text:
    if x == "e":
        break
    print(x)

list = [2, 3, 4, 5, 6, 7]
for x in list:
    if(x%2 ==1 and x >4):
        print(x)
        break


nums = [1, 2, 3, 4]
res = 0
for x in nums:
    if x%2 ==0:
        continue
    else:
        res +=x
print(res)

list = [1,1,2,3,5,8,13]
print(list[list[4]])

txt = "hello"
print(max(txt))

def print_double(x):
    print(2 * x)
print_double(3)

def sum(x):
    res = 0
    for i in range(x):
        res += i
    return res
print(sum(4))

def print_nums(x):
    for i in range(x):
        print(i)
        return
print_nums(10)

def func(x):
    res = 0
    for i in range(x):
        res += i
    return res
print(func(3))

n = [2, 4, 6, 8]
res = 1
for x in n[1: 3]:
    res *= x
print(res)

nums = (55, 44, 33, 22)
print(max(min(nums[ : 2]), abs(-42)))

### Functional Programming
def test(func, arg):
    return func(func(arg))
def mult(x):
    return x * x
print(test(mult, 2))

# Recursion
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
print(fib(4))

# Inheritance(Practice)
class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print(self.width * self.height)
    
class Rectangle(Shape):
    def perimeter(self):
        print(2*(w + h))

w = int(input())
h = int(input())
r = Rectangle(w, h)
r.area()
r.perimeter()    

### Exceptions
x = 0
try:
    x+=1
    raise ValueError
except NameError:
    x+=1
except ValueError:
    x+=1
else:
    x+=1
finally:
    x+=1