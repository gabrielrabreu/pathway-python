# Dictionary Operations in Python

# Dictionaries are versatile data structures in Python used to store key-value pairs. Here are some common dictionary operations:

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing Elements

# Accessing Values: Get the value associated with a key
name_value = my_dict["name"]
# Result: "Alice"

# Dictionary Methods

# Keys: Get a list of all keys in the dictionary
keys_list = list(my_dict.keys())
# Result: ['name', 'age', 'city']

# Values: Get a list of all values in the dictionary
values_list = list(my_dict.values())
# Result: ['Alice', 30, 'New York']

# Items: Get a list of key-value pairs (as tuples)
items_list = list(my_dict.items())
# Result: [('name', 'Alice'), ('age', 30), ('city', 'New York')]
