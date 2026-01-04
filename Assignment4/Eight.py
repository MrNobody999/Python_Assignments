# What is the range data type in Python?
# How is it different from a list of numbers?

# The range data type in Python represents an immutable sequence of numbers and is commonly used for looping a specific number of times in for loops.
# It is defined by the range() function, which can take one, two, or three arguments: start, stop, and step.
# The key differences between range and a list of numbers are:
# 1. Memory Efficiency: A range object does not store all the numbers in memory; it generates them on the fly, making it more memory efficient than a list.
# 2. Immutability: A range is immutable, meaning it cannot be changed after creation, while a list is mutable and can be modified.
# 3. Performance: Iterating over a range is generally faster than iterating over a list, especially for large sequences.
# 4. Usage: Ranges are typically used for iteration in loops, while lists are used for storing collections of items that may need to be modified.
# Example:
# range_obj = range(1, 10, 2)  # Creates a range object for numbers 1, 3, 5, 7, 9
# list_obj = [1, 3, 5, 7, 9]  # Creates a list with the same numbers   