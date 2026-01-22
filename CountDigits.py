# Question : Write a program which accepts one number and print count of digits in that number.
# Input : 7521
# Output : 4

def CountDigit(No1):
	iCnt = 0
	temp = No1
	
	while temp:
		iCnt += 1
		temp = temp // 10
	return iCnt

def main():
	No1 = int(input("Enter Number : "))
	Ans = CountDigit(No1)
	print(f"Total digits of {No1} is : ", Ans) 


if __name__ == "__main__":
	main()