# Write a program which display first 10 even numbers on screen.
# Output : 2 4 6 8 10 12 14 16 18 20

def PrintEven(No1):
    for i in range(2, No1*2+1, 2):
        print(i, end=" ")
    print()

def main():
    No1 = 10
    PrintEven(No1)

if __name__ == "__main__":
    main()