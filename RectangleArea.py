# Question : Write a program which accepts length and width of rectangle and prints area.

def RectangleArea(length, width):
	return length * width

def main():
	length = int(input("Enter length of rectangle : "))
	width = int(input("Enter width of rectangle : "))

	print("Area of rectangle is : ", RectangleArea(length, width))

if __name__ == "__main__":
	main()