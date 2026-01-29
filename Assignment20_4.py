# Design a Python application that creates three threads named Small, Capital, and Digits.
# All threads should accept a string as input.
# The Small thread should count and display the number of lowercase characters.
# The Capital thread should count and display the number of uppercase characters.
# The Digits thread should count and display the number of numeric digits.
# Each thread must also display
   # Thread ID
   # Thread Name

import threading

def CountSmall(input_string):
    Count = 0
    for char in input_string:
        if char.islower():
            Count += 1

    thread_id = threading.current_thread().ident
    thread_name = threading.current_thread().name

    print(f"Thread : {thread_name} (ID : {thread_id})")
    print("Number of lowercase characters is : ", Count)

def CountCapital(input_string):
    Count = 0
    for char in input_string:
        if char.isupper():
            Count += 1

    thread_id = threading.current_thread().ident
    thread_name = threading.current_thread().name

    print(f"Thread : {thread_name} (ID : {thread_id})")
    print("Number of uppercase characters is : ", Count)

def CountDigits(input_string):
    Count = 0
    for char in input_string:
        if char.isdigit():
            Count += 1

    thread_id = threading.current_thread().ident
    thread_name = threading.current_thread().name

    print(f"Thread : {thread_name} (ID : {thread_id})")
    print("Number of digits : ", Count)



def main():

    input_string = input("Enter input : ")

    Small_thread = threading.Thread(target= CountSmall, args = (input_string, ), name = "Small")
    Capital_thread = threading.Thread(target= CountCapital, args = (input_string, ), name = "Capital")
    Digits_thread = threading.Thread(target= CountDigits, args = (input_string, ), name = "Digits")

    Small_thread.start()
    Capital_thread.start()
    Digits_thread.start()

    Small_thread.join()
    Capital_thread.join()
    Digits_thread.join()

    print("Main thread completed")

if __name__ == "__main__":
    main()