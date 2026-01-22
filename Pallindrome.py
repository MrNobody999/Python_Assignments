# Question : Write a program which accepts one number and checks whether it is pallindrome or not.
# Input : 121
# Output : Pallindrome

def Pallindrome(No1):
	temp = No1
	Ans = 0
	while temp:
		iDigit = temp % 10
		Ans = Ans * 10 + iDigit
		temp //= 10

	if No1 == Ans:
		return True


def main():
	No1 = int(input("Enter Number : "))
	Ret = False
	Ret = Pallindrome(No1)
	if Ret == True:
		print(f"{No1} is Pallindrome")
	else:
		print(f"{No1} is Not Pallindrome")


if __name__ == "__main__":
	main()