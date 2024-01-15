# Set Operations in Python

# Sets are versatile data structures in Python used to store unique and unordered elements. Here are some common set operations:

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding Elements

# Add: Add an element to the set
my_set.add(6)
# Result: {1, 2, 3, 4, 5, 6}

# Removing Elements

# Remove: Remove a specific element from the set
my_set.remove(3)
# Result: {1, 2, 4, 5, 6}

# Discard: Remove a specific element if it exists, without raising an error if it doesn't
my_set.discard(7)
# Result: {1, 2, 4, 5, 6}

# Set Methods

# Length: Get the number of elements in the set
length = len(my_set)
# Result: 5
