# Question.7- Why does the input() function always return a string?
# How can you convert it to another data type?

# The input() function in Python always returns a string because it is designed to read user input as text. This allows for flexibility, as users can enter any type of data, and it is up to the programmer to interpret and convert that input into the desired data type.
# To convert the string returned by input() to another data type, you can use built-in functions such as int(), float(), or eval(). For example, to convert the input to an integer, you can use int(input("Enter a number: ")). Similarly, for a float, you can use float(input("Enter a number: ")).
user_input = input("Enter a number: ")
converted_input = int(user_input)  # Convert to integer
print("Converted input (int):", converted_input)    