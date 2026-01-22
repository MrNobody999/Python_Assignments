# Question : Write a program which accepts one number and prints its factors.
# Input : 12
# Output : 1 2 3 4 6 12

def CheckFactors(No1):
	Factors = []
	for i in range(1, No1 + 1):
		if No1 % i == 0:
			Factors.append(i)

	return Factors

	# print(f"Factors of {No1} are : ")
	# for i in Factors:
	# 	print(i)


def main():
	No1 =  int(input("Enter Number : "))
	Ret = []
	Ret = CheckFactors(No1)

	print(f"Factors of {No1} are : ")
	for i in Ret:
	 	print(i)



if __name__ == "__main__":
	main()
