# Design a Python application that creates two threads named EvenFactor and OddFactor.
# Both threads should accept one integer number as a parameter,
# The EvenFactor thread Should:
     # Identify all even factors of the given number.
     # Calculate and display the sum of even factors.
# The OddFactor thread should :
     # Identify all odd factors of the given number.
     # Calculate and display the sum of odd factors.

# After both threads complete execution, the main thread should display the message:
# "Exit from main"

import threading

def EvenFactor(No):
    Sum = 0
    for i in range(1,No+1):
        if No % i == 0:
            if i % 2 == 0:
                Sum += i
    
    print(f"Sum of even factors of {No} is : ", Sum)

def OddFactor(No):
    Sum = 0
    for i in range(1,No+1):
        if No % i == 0:
            if i % 2 == 1:
                Sum += i
    
    print(f"Sum of odd factors of {No} is : ", Sum)


def main():
    No1 = 30
    Even_factor_thread = threading.Thread(target= EvenFactor, args = (No1, ))
    Odd_factor_thread = threading.Thread(target= OddFactor, args = (No1, ))

    Even_factor_thread.start()
    Odd_factor_thread.start()

    Even_factor_thread.join()
    Odd_factor_thread.join()

    print("Exit from main.")

if __name__ == "__main__":
    main()