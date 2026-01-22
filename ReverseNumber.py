# Question : Write a program which accepts one number and prints reverse of that number.
# Input : 123
# Output : 321


def ReverseNumber(No1):
	temp = No1
	Ans = 0
	while temp:
		iDigit = temp % 10
		Ans = Ans * 10 + iDigit
		temp //= 10

	return Ans


def main():
	No1 = int(input("Enter Number : "))
	print(f"Reverse number of {No1} is : ", ReverseNumber(No1))



if __name__ == "__main__":
	main()