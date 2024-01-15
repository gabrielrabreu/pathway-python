# List Operations in Python

# Lists are versatile data structures in Python that allow various operations. Here are some common list operations:

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Adding Elements

# Append: Add an item to the end of the list
my_list.append(6)
# Result: [1, 2, 3, 4, 5, 6]

# Insert: Insert an item at a specific index
my_list.insert(2, 10)
# Result: [1, 2, 10, 3, 4, 5, 6]

# Extend: Add elements from an iterable to the list
my_list.extend([7, 8, 9])
# Result: [1, 2, 10, 3, 4, 5, 6, 7, 8, 9]

# Removing Elements

# Remove: Remove the first occurrence of an item
my_list.remove(3)
# Result: [1, 2, 10, 4, 5, 6, 7, 8, 9]

# Pop: Remove and return an item at a specific index
popped_item = my_list.pop(4)
# Result: Popped item = 5, my_list = [1, 2, 10, 4, 6, 7, 8, 9]

# Delete: Delete an item at a specific index
del my_list[1]
# Result: [1, 10, 4, 6, 7, 8, 9]

# Clear: Remove all items from the list
my_list.clear()
# Result: []

# Common List Operations

# Length: Get the number of items in the list
length = len(my_list)
# Result: 0

# Index: Get the index of the first occurrence of an item
index = my_list.index(6)
# Result: Raises ValueError since 6 is not in the empty list

# Count: Get the number of times an item appears in the list
count = my_list.count(10)
# Result: 0

# Sort: Sort the list in ascending order
my_list.sort()
# Result: []

# Reverse: Reverse the order of elements in the list
my_list.reverse()
# Result: []
