# Question : Write a programs which accepts two numbers and prints addition, substraction, multiplication and division.

def Addition(No1, No2):
	return No1 + No2


def Substraction(No1, No2):
	return No1 - No2


def Multiplication(No1, No2):
	return No1 * No2


def Division(No1, No2):
	return No1 / No2

def main():
	No1 = int(input("Enter first number : "))
	No2 = int(input("Enter second number : "))

	print(f"Addition of {No1} and {No2} is : ", Addition(No1, No2))
	print(f"Substraction of {No1} and {No2} is : ", Substraction(No1, No2))
	print(f"Multiplication of {No1} and {No2} is : ", Multiplication(No1, No2))
	print(f"Division of {No1} and {No2} is : ", Division(No1, No2))


if __name__ ==  "__main__":
	main()
