# Question : Write a program which accepts one number and print sum of digits.
# Input : 123
# Output : 6

def SumDigits(No1):
	Sum = 0
	while No1 :
		iDigit = No1 % 10
		Sum += iDigit
		No1 //= 10
	return Sum


def main():
	No1 = int(input("Enter Number : "))
	print(f"Sum of digits of {No1} is : ", SumDigits(No1))



if __name__ == "__main__":
	main()