# What are bytes in Python?
# Why are they immutable?

# Bytes in Python are a built-in data type that represents a sequence of immutable bytes. They are used to handle binary data, such as files, network protocols, and other low-level data manipulations. Bytes are similar to strings, but while strings are sequences of Unicode characters, bytes are sequences of raw 8-bit values (0-255).  
# Bytes are immutable, meaning that once a bytes object is created, its contents cannot be changed. This immutability is important for several reasons:
# 1. Performance: Immutable objects can be optimized by the Python interpreter, leading to better performance in certain scenarios.
# 2. Hashability: Immutable objects can be used as keys in dictionaries and elements in sets, which require hashable types.
# 3. Safety: Immutability helps prevent accidental modifications to data, which can lead to bugs and unexpected behavior in programs.
