# Data Hiding
# Enscapulation means only sharing the information you need to.
# Weakly private methods and attributes
class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)
    def push(self, value):
        self._hiddenlist.insert(0, value)
    def pop(self):
        return self._hiddenlist.pop(-1)
def __repr__(self):
    return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)
# In the code above, the attribute _hiddenlist is private but it can still be accessed in the outside code.
# The __repr__ magic method is used for string representation of this instance.

# Strongly private methods and attributes
class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
print(s.__egg)
# Basically, python protects those members by interally changing the name to include the class name.

# Setter/getter function
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self.pineapple_allowed = False
    @property
    def pineapple_allowed(self):
        return self.pineapple_allowed
    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "Swordfish!":
                self.pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")
            
pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)