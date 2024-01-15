# Classes and Objects in Python

# In Python, classes are used to define objects and their behavior. Here's a basic example of creating and using a class:

# Define a class called "Person"
class Person:
    # Constructor to initialize the object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to introduce the person
    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Create an instance of the "Person" class
person1 = Person("Alice", 30)

# Access object attributes and call methods
print(person1.name)  # Output: "Alice"
print(person1.age)   # Output: 30
print(person1.introduce())  # Output: "Hello, my name is Alice and I am 30 years old."
