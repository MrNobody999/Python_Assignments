# Predict the output:
d = {1: "One", 1: "ONE", 2: "Two"}
print(d)
# Why does this happen?

# The output will be: {1: 'ONE', 2: 'Two'}
# This happens because dictionary keys in Python must be unique. When the dictionary is created, the second occurrence of the key '1' overwrites the first one. 
# As a result, the final dictionary contains only one entry for the key '1', which maps to the value 'ONE'. 
# The key '2' remains unchanged, mapping to the value 'Two'.