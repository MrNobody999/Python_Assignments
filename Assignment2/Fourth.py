# Question.4 - What is the purpose of getsizeof() ?
# Why is memory size different for different data types ?

# The getsizeof() function in Python, which is part of the sys module, is used to determine the memory size (in bytes) of an object. It returns the size of the object itself, not including the sizes of objects it may reference.
# Different data types have different memory sizes because they have different structures and requirements for storing data. For example:
# 1. Primitive Data Types: Simple data types like integers and floats have a fixed size because they store a single value.
# 2. Complex Data Types: Data types like lists, dictionaries, and sets can store multiple values and have additional overhead for managing these collections, leading to larger memory sizes.
# 3. Immutable vs Mutable: Immutable types (like strings and tuples) may have different memory management strategies compared to mutable types (like lists and dictionaries), affecting their memory size.
# 4. Internal Representation: Different data types may have different internal representations and optimizations that affect their memory usage.

import sys
a = 10
b = [1, 2, 3]
print("Size of a:", sys.getsizeof(a))
print("Size of b:", sys.getsizeof(b))   