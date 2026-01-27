# Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
# Input : Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output : 56

def MaximumNo(list):
    Maxi = 0

    for i in list:
        if i > Maxi:
            Maxi = i

    return Maxi


def main():
    list1 = []
    Nos = int(input("Enter list elements: "))

    for i in range(Nos):
        num = int(input(f"Enter Number {i + 1} : "))
        list1.append(num)
    
    Ret = MaximumNo(list1)
    print("Maximum Number is : ", Ret)


if __name__ == "__main__":
    main()