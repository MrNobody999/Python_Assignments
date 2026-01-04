# What is difference between:
#print() and return
#Explain with function example.

# Ans: The main difference between print() and return is that print() outputs a value to the console, while return sends a value back to the caller of the function.
# When a function uses print(), it displays the value but does not send it back to where the function was called. On the other hand, when a function uses return, it sends the value back to the caller, allowing it to be stored in a variable or used in further calculations.

def add_numbers(a, b):
    print("Adding numbers...")
    return a + b

result = add_numbers(5, 10)
print("The result is:", result)     

