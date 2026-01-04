# What is the difference between bytes and bytearray ?
# Mention mutability and use cases.

# Answer:
# Bytes and bytearray are both built-in data types in Python used to handle binary data, but they have a key difference in terms of mutability.
# Bytes are immutable, meaning once a bytes object is created, its contents cannot be changed. This immutability makes bytes suitable for representing fixed binary data, such as file headers or network packets.
# Bytearray, on the other hand, is mutable. This means you can modify the contents of a bytearray after it has been created. This mutability makes bytearray useful for scenarios where you need to modify binary data in place, such as when processing binary files or implementing custom protocols. 
