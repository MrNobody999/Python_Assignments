
def PrintOdd(No1):
    for i in range(1, No1+1):
        if (i % 2 == 1):
            print(i)


def main():
    print("Enter Number: ")
    No1 = int(input())
    PrintOdd(No1)

if __name__ == "__main__":
    main()