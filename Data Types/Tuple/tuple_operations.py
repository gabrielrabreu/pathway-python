# Tuple Operations in Python

# Tuples are ordered collections of items in Python, and they are similar to lists. However, tuples are immutable, meaning their elements cannot be changed after creation. Here are some common tuple operations:

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing Elements

# Indexing: Access elements by their index (starting from 0)
first_element = my_tuple[0]
# Result: 1

# Slicing: Extract a portion of the tuple using slicing
slice_of_tuple = my_tuple[1:4]
# Result: (2, 3, 4)

# Tuple Methods

# Length: Get the number of elements in a tuple
length = len(my_tuple)
# Result: 5

# Count: Count the number of occurrences of an element in a tuple
count_of_element = my_tuple.count(3)
# Result: 1

# Index: Find the index of the first occurrence of an element in a tuple
index_of_element = my_tuple.index(4)
# Result: 3
