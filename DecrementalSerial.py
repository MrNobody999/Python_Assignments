# Question : Write a program which accept one number and prints that many numbers in reverse order.
# Input : 5
# Output : 5 4 3 2 1 

def PrintSerial(No1):
	serial = []
	for i in range(No1, 0, -1):
		serial.append(i)
	return serial

def main():
	No1 = int(input("Enter Number : "))
	Ret = []
	Ret = PrintSerial(No1)

	print(f"Decremental serial numbers from {No1} to 0 are : ")
	for i in Ret:
		print(i)

if __name__ == "__main__":
	main()