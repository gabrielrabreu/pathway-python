# Encapsulation in Python

# Encapsulation is one of the fundamental principles of object-oriented programming (OOP). It involves restricting access to certain parts of an object and controlling how data is accessed and modified. Here's an example:

# Define a class called "Person"
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    # Getter methods to access private attributes
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Setter methods to modify private attributes
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age > 0:
            self.__age = age

# Create an instance of the "Person" class
person1 = Person("Alice", 30)

# Access private attributes using getter methods
print(person1.get_name())  # Output: "Alice"
print(person1.get_age())   # Output: 30

# Modify private attributes using setter methods
person1.set_name("Bob")
person1.set_age(25)

# Access modified attributes
print(person1.get_name())  # Output: "Bob"
print(person1.get_age())   # Output: 25
