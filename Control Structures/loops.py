# Loops (for and while)

# Loops are used to repeatedly execute a block of code. In Python, you have two primary loop types:

# 1. 'for' loop: Used for iterating over a sequence (e.g., list, tuple, string).
sequence = []
for element in sequence:
  print(element)
  # Code to execute for each element in the sequence

# Example:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)

# 2. 'while' loop: Continues to execute a block of code as long as a condition is True.
while_condition = False
while condition:
  print("executing")
  # Code to execute while the condition is True

# Example:
count = 0
while count < 5:
    print(count)
    count += 1
