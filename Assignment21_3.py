# Design a Python application where multiple threads update a shared variable.
# Use a Lock to avoid race conditions.
# Each thread should increment the shared counter multiple times.
# Display the final value of the counter after all threads complete execution.

import threading
import time

shared_counter = 0
counter_lock = threading.Lock()

def increment_counter(iterations, thread_id):
    global shared_counter
    print(f"Thread {thread_id} starting...")
    
    for _ in range(iterations):
        counter_lock.acquire()
        try:
            current_value = shared_counter
            time.sleep(0.0001) 
            shared_counter = current_value + 1
        finally:
            counter_lock.release()
            
    print(f"Thread {thread_id} finished after {iterations} increments.")



def main():

    NumThreads = 5
    threads = []
    iteration_per_thread = 100

    print(f"Starting {NumThreads} threads, each incrementing {iteration_per_thread} times.")

    for i in range(NumThreads):
        thread = threading.Thread(target= increment_counter, args = (iteration_per_thread, i + 1))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

        expected_value = NumThreads * iteration_per_thread

    print("-" * 30)
    print(f"Expected final value: {expected_value}")
    print(f"Actual final value:   {shared_counter}")

    if shared_counter == expected_value:
        print("Success: Race condition avoided using threading.Lock!")
    else:
        print("Error: Counter value is incorrect. A race condition may still exist.")

    print("Main thread completed")

if __name__ == "__main__":
    main()