# Question.3 - What does the id() function return ?
# Is the value returned by id() same for two variables holding the same value?

# The id() function in Python returns the "identity" of an object. This identity is unique and constant for the object during its lifetime. It is typically represented as an integer, which corresponds to the memory address where the object is stored.  
# For two variables holding the same value, the value returned by id() may or may not be the same, depending on the type of the object and how Python manages memory for that type.
# For immutable types like small integers and strings, Python often reuses existing objects for the same value, so the id() may be the same. However, for mutable types like lists or dictionaries, even if they hold the same content, they are distinct objects in memory, and thus their id() values will be different.
# Example:
a = 1000
b = 1000
print("id(a):", id(a))
print("id(b):", id(b))
