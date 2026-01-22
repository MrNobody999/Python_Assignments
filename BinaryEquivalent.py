# Question : Write a program which accepts one number and prints binary equivalent.


def BinaryEquivalent(No1):
	binary_str = ""

	while No1 > 0:
		remainder = No1 % 2
		binary_str = str(remainder) + binary_str
		No1 = No1 // 2

	return binary_str


def main():
	No1 = int(input("Enter number : "))

	Ret = ""

	Ret = BinaryEquivalent(No1)
	print(f"Binary equivalent of {No1} is : ", Ret)

if __name__ == "__main__":
	main()