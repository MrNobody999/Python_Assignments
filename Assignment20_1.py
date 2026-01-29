# Design a Python application that creates two separate threads named Even and Odd.
# The Even thread should display the first 10 even numbers.
# The Odd thread should display the first 10 odd numbers.
# Both threads should execute independently using the threading module.
# Ensure proper thread creation and execution.

import threading

def PrintEven():
    for i in range(2,21,2):
        print(i)

        


def PrintOdd():
    for i in range(1,20,2):
        print(i)




def main():
    Even_thread = threading.Thread(target= PrintEven, name = "Even")
    Odd_thread = threading.Thread(target= PrintOdd, name = "Odd")

    Even_thread.start()
    Odd_thread.start()

    Even_thread.join()
    Odd_thread.join()

    print("Main thread completed")

if __name__ == "__main__":
    main()