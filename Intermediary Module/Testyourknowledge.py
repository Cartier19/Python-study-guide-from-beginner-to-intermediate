# What is the result of this code
nums = {1, 2, 3, 4, 5, 6}
nums = {1, 2, 3} & nums
nums = filter(lambda x : x>1, nums)
print(len(list(nums)))

# What is the result of this code
def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)
print(power(2, 3))

# What is the output of this code
def func(**kwargs):
    print(kwargs["zero"])
func(a=0, zero=8)

# What is A() ^ B() evaluated as, if A doesn't implement any magic methods?
# A().__xor(B())
#B().__rxor__(A())*
#B().xor(A())

#How is a property created?

#What is the difference between a class method and a static method?

# What are the usual name for calling the parameters for the calling instance and the calling class?

# Which method is called just before an object is instantiated?

