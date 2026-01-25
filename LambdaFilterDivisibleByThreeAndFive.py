# Question : Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

from functools import reduce

DivisibleByThreeAndFive = lambda No : No % 3 == 0 and No % 5 == 0


def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is : ",Data)

    FData = list(filter(DivisibleByThreeAndFive,Data))
    print("Data after filter is : ",FData)

if __name__ == "__main__":
    main()