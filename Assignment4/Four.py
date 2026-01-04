# Explain why strings are immutable in Python.
# What happens internally when you modify a string variable?

# Strings are immutable in Python to ensure data integrity and optimize performance. When a string is created, it is stored in a fixed memory location. 
# If you attempt to modify a string, Python does not change the original string; instead, it creates a new string with the desired modifications and assigns it to the variable. 
# This immutability allows Python to optimize memory usage and improve performance, as immutable objects can be cached and reused without the risk of unintended side effects from modifications. 
# Additionally, immutability helps maintain consistency in multi-threaded environments, as immutable objects cannot be altered by one thread while being accessed by another.
# Internally, when you modify a string variable, Python allocates new memory for the new string and updates the variable to reference this new memory location, leaving the original string unchanged.      
# This behavior ensures that strings remain consistent and reliable throughout their usage in a program.