# Inheritance in Python

# Inheritance is a fundamental concept in object-oriented programming (OOP). It allows a class to inherit properties and methods from another class. Here's an example:

# Base class (parent class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # Placeholder for the speak method

# Derived class (child class)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Create instances of the classes
animal1 = Animal("Generic Animal")
dog1 = Dog("Buddy")

# Call the speak method on instances
print(animal1.speak())  # Output: "Generic Animal says <nothing>"
print(dog1.speak())     # Output: "Buddy says Woof!"
