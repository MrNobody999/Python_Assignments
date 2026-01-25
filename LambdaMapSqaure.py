# Question : Write a lambda function using map() which accepts a list of numbers and returns a list of square of each other.

Square = lambda No1 : No1 * No1


def main():
    Data = [1,2,3,4,5,6,7,8,9,10]
    print("Actual Data is : ",Data)

    MData = list(map(Square,Data))
    print("Data after Square is : ",MData)

if __name__ == "__main__":
    main()