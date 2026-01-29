# 5: Design a Python application that creates two threads named Thread1 and Thread2.
# Thread1 should display numbers from 1 to 50.
# Thredd2 should display numbers from 50 to 1 reverse order.
# Ensure that
   # Thread2 starts execution only after Thread1 has completed.
# Use appropriate thread synchronization.


import threading

def print_1_to_50():
    for i in range(1,51):
        print(i)

def print_50_to_1():
    for i in range(50,0,-1):
        print(i)

def main():

    first_thread = threading.Thread(target= print_1_to_50, name = "Thread1")
    second_thread = threading.Thread(target= print_50_to_1, name = "Thread2")

    first_thread.start()
    first_thread.join()

    second_thread.start()
    second_thread.join()

    print("Main thread completed")

if __name__ == "__main__":
    main()