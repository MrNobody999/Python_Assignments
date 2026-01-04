# Explain how Python manages memory automatically.
# Why does the Programmer not need to explicitly allocate or free memory.

# Ans: Python manages memory automatically through a built-in memory management system that includes a private heap containing all Python objects and data structures. 
# The Python memory manager handles the allocation of memory for new objects and the deallocation of memory for objects that are no longer in use. This is primarily achieved through a technique called reference counting, where each object keeps track of the number of references pointing to it. 
# When an object's reference count drops to zero, meaning no references point to it anymore, the memory occupied by that object is automatically freed. Additionally, Python employs a garbage collector to handle cyclic references that reference counting alone cannot resolve. 
# This automatic memory management allows programmers to focus on writing code without worrying about manual memory allocation and deallocation, reducing the chances of memory leaks and other related issues.

