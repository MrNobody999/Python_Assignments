# Question.8- predict the output:
# x = input("Enter number: ")
# print(type(x))
# Explain the reason.

# When you use the input() function in Python, it always returns the user input as a string, regardless of what the user enters. Therefore, when you print the type of the variable x, it will always be <class 'str'>.
x = input("Enter number: ")
print(type(x))
# Explanation: The input() function is designed to read input as text, so even if the user enters a number, it is treated as a string. To convert it to another data type, you would need to explicitly cast it using functions like int() or float().
