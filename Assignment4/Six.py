# What is dectionary in python ?
# Explain: Key value pair, Why keys must be immutable, Why duplicate keys are not allowed

# A dictionary in Python is a built-in data type that stores data in key-value pairs. Each key is unique and is used to access its corresponding value. 
# Dictionaries are mutable, meaning that they can be changed after their creation by adding, removing, or modifying key-value pairs.  
# Keys in a dictionary must be immutable types, such as strings, numbers, or tuples. 
# This is because immutable objects have a fixed hash value that does not change over time, allowing Python to efficiently locate the corresponding value in memory. 
# If mutable objects were allowed as keys, their hash values could change, leading to inconsistencies and making it impossible to reliably retrieve the associated values.
# Duplicate keys are not allowed in dictionaries because each key must uniquely identify a value. 
# If duplicate keys were permitted, it would create ambiguity when trying to access values, as there would be no clear way to determine which value to return for a given key. 
# When a duplicate key is added to a dictionary, the new value overwrites the existing value associated with that key, ensuring that each key maps to a single, unique value.