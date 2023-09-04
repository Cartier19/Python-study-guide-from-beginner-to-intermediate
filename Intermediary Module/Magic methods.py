class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        raise TypeError("Unsupported operand type for +: 'Point' and '{}'".format(type(other)))

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        raise TypeError("Unsupported operand type for -: 'Point' and '{}'".format(type(other)))

    def __len__(self):
        return 2

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Index out of range")

    def __iter__(self):
        yield self.x
        yield self.y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __getattr__(self, name):
        if name == "distance_from_origin":
            return (self.x ** 2 + self.y ** 2) ** 0.5
        raise AttributeError(f"'Point' object has no attribute '{name}'")

    def __setattr__(self, name, value):
        if name == "x" or name == "y":
            self.__dict__[name] = value
        else:
            raise AttributeError("Attribute assignment not allowed")

    def __enter__(self):
        print("Entering the Point context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the Point context")

# Test the Point class with various magic methods
if __name__ == "__main__":
    p1 = Point(2, 3)
    p2 = Point(1, 1)

    print(p1)  # Output: Point(2, 3)
    print(str(p1))  # Output: Point(2, 3)
    print(repr(p1))  # Output: Point(2, 3)

    p3 = p1 + p2
    print(p3)  # Output: Point(3, 4)

    p4 = p1 - p2
    print(p4)  # Output: Point(1, 2)

    print(len(p1))  # Output: 2

    print(p1[0])  # Output: 2
    print(p1[1])  # Output: 3

    for coord in p1:
        print(coord)  # Output: 2, then 3

    print(p1 == p2)  # Output: False
    print(p1 != p2)  # Output: True

    print(p1.distance_from_origin)  # Output: 3.605551275463989

    with Point(0, 0) as p:
        print("Inside the Point context")  # Output: "Entering the Point context" and then "Inside the Point context"

# In this example, we defined various magic methods for the Point class, such as __add__, __sub__, __len__, __getitem__, __iter__, __eq__, __ne__, __getattr__, __setattr__, __enter__, and __exit__. 
# Each of these methods allows us to customize the behavior of the Point instances and make them work intuitively with Python's built-in operations and constructs.