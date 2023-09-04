### OOP(Object Oriented Programming)
# Classes
class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.lrgs = legs
felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)
# This code defines a class named Cat, which has two attributes: color & legs
# Then the class is used to create 3 separate objects of that class

# Inheritance
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Purr...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()
# The function super is a useful inheritance-related function that refers to the parent class. 
# It can be used to find the method with a certain name in an object's superclass.
class A:
    def spam(self):
        print(1)
class B(A):
    def spam(self):
        print(2)
        super().spam()
B().spam()

# Magic methods & Operator overloading
# An example of magic method is __add__ for +
class Vector2D:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def __add__(self, other):
            return Vector2D(self.x + other.x, self.y + other.y)
        
first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

# Another example
class Specialstring:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont) + 1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

spam = Specialstring("spam")
eggs = Specialstring("eggs")
spam > eggs
# You can define any custom behaviour for the overloaded operators.
# Making classes act like containers
import random
class Vaguelist:
    def __init__(self, cont):
        self.cont = cont
    
    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]
    
    def __len__(self):
        return random.randint(0, len(self.cont)*2)
    
vague_list = Vaguelist(["A", "B", "c", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
# We have overridden the len() function for the Vaguelist to return a random number.
# The indexing function also returns a random item in a range from the list, based on the expression.

