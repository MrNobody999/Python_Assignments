# Question.2 - What is difference between : 
# a = 10
# b = 10
# and
# a = [10]
# b = [10]
# Explain usind id()

a = 10
b = 10
print("For integers:")
print("id(a):", id(a))
print("id(b):", id(b))  

a = [10]
b = [10]
print("\nFor lists:")
print("id(a):", id(a))
print("id(b):", id(b))  

# Explanation:
# a = 10, b = 10 (Integers):
# In Python, integers are immutable and small integers (typically -5 to 256) are often cached. So, a and b usually point to the same object in memory, meaning id(a) will equal id(b), and a is b will be True.

# a = [10], b = [10] (Lists):
# Lists are mutable. Each time you create a new list (even with the same content), Python allocates a new, distinct block of memory for it.
# Therefore, id(a_list) and id(b_list) will be different, and a_list is b_list will be False, indicating they are separate objects. 