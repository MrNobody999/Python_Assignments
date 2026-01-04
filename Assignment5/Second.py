# Predict the output:
b = bytes([65,66,67]) 
print(b)
# Explain how numbers are converted internally.

# The output of the code will be:
# b'ABC'    
# In Python, the bytes() function creates an immutable sequence of bytes. When we pass a list of integers to the bytes() function, each integer is treated as an 8-bit value (ranging from 0 to 255) that corresponds to a specific byte.
# Each integer in the list is converted to its corresponding ASCII character based on the ASCII table.
# In this case, the integers 65, 66, and 67 correspond to the ASCII characters 'A', 'B', and 'C', respectively. Therefore, when we print the bytes object, it displays the byte representation of the string 'ABC', which is shown as b'ABC'.   
