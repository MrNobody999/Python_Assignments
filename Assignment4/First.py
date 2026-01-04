# What is difference between List and Tuple in Python?

# Explain in terms of: Mutability, Memory, Performance, Use Cases

# 1. Mutability:
# - Lists are mutable, meaning they can be changed after their creation. You can add, remove, or modify elements.
# - Tuples are immutable, meaning once they are created, their elements cannot be changed.

# 2. Memory:
# - Lists consume more memory than tuples because of their dynamic nature and the overhead of maintaining the list structure.
# - Tuples are more memory-efficient as they have a smaller memory footprint due to their immutability.

# 3. Performance:
# - Lists have a slight performance overhead for operations like appending or removing elements due to their dynamic nature.
# - Tuples are generally faster than lists for iteration and access because of their fixed size and immutability.

# 4. Use Cases:
# - Lists are used when you need a collection of items that may change over time, such as a list of user inputs.
# - Tuples are used when you need a fixed collection of items, such as coordinates (x, y) or RGB color values.
