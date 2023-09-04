### Collection Types
# Dictionaries
ages = {"Dave": 24,
        "Mary": 42,
        "John": 58
        }
print(ages["Dave"])
print(ages["Mary"])

# Dictionary Functions
nums = {1: "one",
        2: "two",
        3: "three"}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

# get function
pairs = {
    1: "apple",
    "orange": [2, 3, 4],
    True: False,
    12: True
}
print(pairs.get("orange"))
print(pairs.get(7, 42))
print(pairs.get(12345, "not found"))

# Tuples
my_tuple = "one", "two", "three"
print(my_tuple[0])
# Tuple unpacking
numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)
# This can also be used to swap variables by doing a, b = b, a
# A variable that is prefaced with an asterisk takes all values from the collection that are left over from the other variables.
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

# Set
num_set = {1, 2, 3, 4, 5}
print(3 in  num_set)
# add() & remove() function
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(1)
print(nums)
# Duplicate elements will automatically get removed from the set.
# Combination of sets
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

# List comprehension
cubes = [i**3 for i in range(5)]
print(cubes)