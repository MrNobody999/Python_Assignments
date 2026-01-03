# Question.5 - Predict the output:
 
# a = 10
# b = 10
# print(id(a) == id(b))
# Explain why this happens.

a = 10
b = 10
print(id(a) == id(b))
# Output: True
# Explanation: In Python, small integers (typically from -5 to 256) are cached and reused for performance optimization. When both 'a' and 'b' are assigned the value 10, they reference the same memory location for that integer value. Therefore, the id() function returns the same identity for both variables, resulting in the comparison id(a) == id(b) being True.
