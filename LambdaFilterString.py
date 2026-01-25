# Question : Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

from functools import reduce

Greater = lambda s : len(s) > 5


def main():
    Data = ["India", "Is", "My", "Country", "Pride", "Respect", "Mother"]
    print("Actual Data is : ",Data)

    FData = list(filter(Greater,Data))
    print("Data after filter is : ",FData)

if __name__ == "__main__":
    main()