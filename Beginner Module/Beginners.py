## Maths Operation ##

#Addition & Subtraction
print(9+4-7)

#Multiplication
print(12*12)

#Division
print(8/2)

## Data Types
#String
print("Water" + "Park")

#Output Separator
print("Iron", "Man", sep="-")

# In-Place Operators
y = 4
y *= 3
print(y)

## Control Flow
# Booleans
my_boolean = True
print(my_boolean)

print(2 == 3)

print("hello" == "hello")

# Comparison operators(Relational Operators)
x = 7
print(x != 8)
print(x > 5)
print(x < 2)
print(x >= 7)
print(x <= 7)

# if statement
x = 42
if x > 5:
    print("x is greater than 5")

# Loops
i = 1
while i <= 5:
    print(i)
    i = i + 1
print ("Finished!")


x = 10
while x >= 0:
    print(x)
    x -= 10


###  Lists
words = ["Hello", "world", "!"]
print(words[0])

# reasssigning items in a list
nums = [1,2,3,4,5]
nums[3] = nums[1]
print(nums[3])

# Adding lists
x = [2, 4]
x += [6, 8]
print(x[2]//x[0])

#Multiplying lists by  an Integer
x = [2, 4]
x = x * 3
print(x[3])


### for loops
words = ["hello", "world", "spam", "egg"]
for word in words:
    print(word + "!")

str = "testing for loops"
count = 0
for x in str:
    if x == "t":
        count += 1
print(count)
# The above code defines a count variable, iterates over the string and calculates the count of "t" letters in it.


### Range function
numbers = list(range(10))
print(numbers)

# Range with step
numbers = list(range(5, 20, 2))
print(numbers)

## List Functions
# len()
nums = [1, 3, 5, 2, 4]
print(len(nums))

# append()
nums = [1, 2, 3, 4]
nums.append(4)
print(nums)

# insert()
words = ["Python", "fun"]
words.insert(1, "is")
print(words)

# index()
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))

# min&max(list)
x = [1, 8, 42, 3]
print(min(x))
print(max(x))

# list.count(item), list.remove(item), list.reverse()
x = [2, 4, 6, 2, 7, 2, 9]
print(x.count(2))
x.remove(4)
print(x)
x.reverse
print(x)

## String Functions
# String Formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

# join()
x = ", ".join(["spam", "eggs", "ham"])
print(x)

# split()
str = "some text goes here"
x = str.split(' ')
print(x)

# replace()
x = "Hello ME"
print(x.replace("ME", "world"))

## Function arguments
def exclamation(word):
    print(word + "!")
exclamation("spam")

def double(a, b):
    return [a*2, b*2]
x = double(6, 9)
print(x)