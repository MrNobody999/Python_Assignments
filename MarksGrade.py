# Question : Write a program which accepts marks and displays grade.
# Condtion Example : 
# Marks >= 75 -> Distinction
# Marks >= 60 -> First Class
# Marks >= 50 -> Second Class
# Marks < 50 -> Fail.


# def MarksGrade(Marks):
# 	#str = ""

# 	if Marks >= 75:
# 		return "Distinction"
# 	elif Marks >= 60 and Marks < 75:
# 		return "First Class"
# 	elif Marks >= 50 and Marks < 60:
# 		return "Second Class"
# 	else:
# 		return "Fail"

def MarksGrade(Marks):
	str = ""

	if Marks >= 75:
		str = "Distinction"
	elif Marks >= 60 and Marks < 75:
		str = "First Class"
	elif Marks >= 50 and Marks < 60:
		str = "Second Class"
	else:
		str = "Fail"

	return str


def main():
	Marks = int(input("Enter marks : "))

	Ret = ""

	Ret = MarksGrade(Marks)
	print(Ret)

if __name__ == "__main__":
	main()