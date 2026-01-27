# Write a program which accepts N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 62
# Element to search : 5
# Output : 3


def Frequency(list, Target):
    Count = 0

    for i in list:
        if i == Target:
            Count += 1

    return Count


def main():
    list1 = []
    Nos = int(input("Enter list elements: "))

    for i in range(Nos):
        num = int(input(f"Enter Number {i + 1} : "))
        list1.append(num)
    

    Target = int(input("Enter target number: "))
    
    Ret = Frequency(list1, Target)
    print(f"Total count of {Target} is : ", Ret)


if __name__ == "__main__":
    main()