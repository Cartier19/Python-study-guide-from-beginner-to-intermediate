try:
    num1 = 7
    num2 = 0
    print(num1/num2)
    print("Done Calculation")
except ZeroDivisionError:
    print("An error occured")
    print("due to Zero division")


# Multiple exceptions
try:
    variable = 10
    print(variable + "hello")
    print(variable/2)
except ZeroDivisionError:
    print("Divide by zero")
except (ValueError, TypeError):
    print("Error occured")

# An except statement without any exception specified will catch all errors. 
# These should be used sparingly as they can catch unexpected errors and hide programming mistakes.
try:
    word = "spam"
    print(word/0)
except:
    print("An error occurred")

# finally
try:
    print("Hello")
    print(1/0)
except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("This code will run no matter what")
# The finally block is useful for example, when working with files and resources: it can be used to make sure 
# files or resources are closed or released regardless of whether an an exception occurs.

# else
try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)


## Raising Exceptions
num = 102
if num > 100:
    raise ValueError