# Exception Handling in Python

# Exception handling allows you to handle errors gracefully during program execution.

try:
    # Code that may raise an exception
    x = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    # Handle the exception
    print("Error: Division by zero")
    x = 0  # Set x to a default value or perform recovery actions

try:
    # Code that may raise another exception
    file = open("nonexistent.txt", "r")  # This will raise a FileNotFoundError
except FileNotFoundError as e:
    # Handle the exception
    print(f"Error: {e}")
    file = None  # Set file to None or perform recovery actions

# You can also use 'else' to specify code that should run if no exceptions are raised:
try:
    y = 10 / 2
except ZeroDivisionError as e:
    print("Error: Division by zero")
else:
    print("No error occurred")
    # Continue with code execution

# Finally, you can use 'finally' to specify code that always runs, whether an exception is raised or not:
try:
    z = 10 / 5
except ZeroDivisionError as e:
    print("Error: Division by zero")
else:
    print("No error occurred")
finally:
    print("This code always runs")

# Exception handling helps in making your code more robust and prevents it from crashing due to errors.
