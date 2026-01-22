# Question : Write a program which accepts one number and check whether it is prime or not.
# Input : 11
# Output : Prime Number

def Prime(No1):
	for i in range(2, int((No1+1)/2)):
		if No1 % i == 0:
			return False
	return True


def main():
	No1 = int(input("Enter Number :"))
	Ret = False
	Ret = Prime(No1)
	if Ret == True:
		print("Prime Number")
	else:
		print("Not a Prime Number")


if __name__ == "__main__":
	main()
