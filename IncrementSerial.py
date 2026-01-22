# Question : Write a program which accept one number and prints that many numbers starting from 1.
# Input : 5
# Output : 1 2 3 4 5

def PrintSerial(No1):
	serial = []
	for i in range(1, No1 + 1):
		serial.append(i)
	return serial

def main():
	No1 = int(input("Enter Number : "))
	Ret = []
	Ret = PrintSerial(No1)

	print(f"Incremental Serial Numbers until {No1} are : ")
	for i in Ret:
		print(i)

if __name__ == "__main__":
	main()
