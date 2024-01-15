# String Operations in Python

# Strings are fundamental data types in Python used for text processing. Here are some common string operations:

# Creating a string
my_string = "Hello, Python!"

# Length: Get the length of the string
length = len(my_string)
# Result: 13

# Accessing Characters: Access individual characters in the string using indexing
first_char = my_string[0]
# Result: 'H'

# Slicing: Extract substrings using slicing
substring = my_string[7:13]
# Result: 'Python!'

# Concatenation: Combine two or more strings
new_string = my_string + " Welcome!"
# Result: 'Hello, Python! Welcome!'

# Repetition: Repeat a string
repeated_string = my_string * 3
# Result: 'Hello, Python!Hello, Python!Hello, Python!'

# String Methods

# Uppercase and Lowercase: Convert to uppercase or lowercase
uppercase_string = my_string.upper()
# Result: 'HELLO, PYTHON!'
lowercase_string = my_string.lower()
# Result: 'hello, python!'

# Replace: Replace a substring with another string
replaced_string = my_string.replace("Python", "Java")
# Result: 'Hello, Java!'

# Split: Split a string into a list of substrings
split_string = my_string.split(", ")
# Result: ['Hello', 'Python!']

# Join: Join a list of strings into a single string
joined_string = "-".join(["apple", "banana", "cherry"])
# Result: 'apple-banana-cherry'

# Stripping: Remove leading and trailing whitespace
strip_whitespace = "   Python   ".strip()
# Result: 'Python'

# String Formatting: Format strings using f-strings (Python 3.6+)
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
# Result: 'My name is Alice and I am 30 years old.'
