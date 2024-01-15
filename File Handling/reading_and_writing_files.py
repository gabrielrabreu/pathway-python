# File Handling in Python

# File handling is a crucial aspect of programming. Python provides built-in functions for reading and writing files. Let's explore some common file operations:

# Reading from a File

# Open a file in read-only mode ('r')
with open('example.txt', 'r') as file:
    content = file.read()
    print("Reading from the file:")
    print(content)

# Writing to a File

# Open a file in write mode ('w')
with open('output.txt', 'w') as file:
    text_to_write = "This is a sample text.\n"
    file.write(text_to_write)
    print("Writing to the file:")
    print(text_to_write)

# Appending to a File

# Open a file in append mode ('a')
with open('output.txt', 'a') as file:
    text_to_append = "Appending more text to the file.\n"
    file.write(text_to_append)
    print("Appending to the file:")
    print(text_to_append)

# Reading Lines from a File

# Open a file in read-only mode ('r')
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print("Reading lines from the file:")
    for line in lines:
        print(line.strip())  # Remove trailing newline characters

# Handling Errors

try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print(f"Error: {e}")
