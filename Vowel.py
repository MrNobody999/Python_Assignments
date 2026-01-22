# Question : Write a program which accepts one character and check whether it is vowel or consonant
# Input : a
# Output : Vowel


# First Approach
# def CheckVowel(char):
# 	if char == "A" or char == "a" or char == "E" or char == "e" or char == "I" or char == "i" or char == "O" or char == "o" or char == "U" or char == "u":
# 		return True
# 	else :
# 		return False


# Second Approach
def CheckVowel(char):

	vowels = ["a", "e", "i", "o", "u"]

	char_lower = char.lower()

	if char_lower in vowels:
		return True


def main():
	char = input("Enter character : ")
	Ret = False
	Ret = CheckVowel(char)

	if Ret == True:
		print("It is vowel.")
	else:
		print("It is consonant") 



if __name__ == "__main__":
	main()

