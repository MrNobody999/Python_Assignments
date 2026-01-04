# Predict the output:
lst = [10, 20, 30]
tpl = (10, 20, 30)

lst[0] = 100
tpl[0] = 100
# Which line will raise an error and why?


# The line "tpl[0] = 100" will raise an error because tuples are immutable, meaning their elements cannot be changed after creation.        
# The line "lst[0] = 100" will execute successfully because lists are mutable, allowing their elements to be modified.


