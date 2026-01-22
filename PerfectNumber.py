# Question : Write a program which accepts one number and check whether it is perfect number or not.
# Input : 6
# Output : Perfect Number

def PerfectNumber(No1):
	DivisorSum = 0
	for i in range(1, No1):
		if No1 % i == 0:
			DivisorSum += i

	if No1 == DivisorSum:
		return True
	

def main():
	No1 = int(input("Enter number : "))

	Ret = False

	Ret = PerfectNumber(No1)
	if Ret == True:
		print(f"{No1} is perfect number.")
	else:
		print(f"{No1} is not perfect number.")

if __name__ == "__main__":
	main()