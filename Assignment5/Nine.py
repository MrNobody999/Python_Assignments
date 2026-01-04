# Predict the output:
s = {10, 20,30,10,20}
print(s)
# Why are some values are missing?

# The output of the code will be:
# {10, 20, 30}
# In Python, a set is an unordered collection of unique elements. When we create a set with duplicate values, such as {10, 20, 30, 10, 20}, Python automatically removes the duplicates and retains only one instance of each unique value.
# Therefore, the resulting set contains only the unique values {10, 20, 30}, and the duplicate values are omitted. This behavior is a fundamental property of sets in Python, which ensures that all elements in a set are unique.
