# Question : Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers .

CheckOdd = lambda No1 : No1 % 2 == 1


def main():
    Data = [1,2,3,4,5,6,7,8,9,10]
    print("Actual Data is : ",Data)

    MData = list(filter(CheckOdd,Data))
    print("Data after CheckOdd is : ",MData)

if __name__ == "__main__":
    main()