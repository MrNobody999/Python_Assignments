# Predict the output:
ba = bytearray([65,66,67])
ba [0] = 97
print(ba)
# Why is this allowed?
# Answer:
# This is allowed because bytearray is mutable, meaning its contents can be changed after creation. In contrast, bytes objects are immutable, so attempting to change a byte in a bytes object would raise an error.

# Output :
# bytearray(b'aBC')