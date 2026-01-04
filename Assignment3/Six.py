# Write a program to display:
#Data type, Memory address, Sizes in bytes of a variable entered by the user.

user_input = input("Enter something: ")

print("Data type:", type(user_input))
print("Memory address:", id(user_input))
print("Size in bytes:", user_input.__sizeof__())    