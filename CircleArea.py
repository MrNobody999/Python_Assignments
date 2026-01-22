# Question : Write a program which accepts radius of circle and prints area of circle.

def CircleArea(radius, pie = 3.14):
	return pie * (radius ** 2)

def main():
	radius = int(input("Enter radius of circle : "))

	print("Area of rectangle is : ", CircleArea(radius))

if __name__ == "__main__":
	main()