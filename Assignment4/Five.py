# Predict the output:
s = "Python"
print(id(s))
s = s + "3"
print(id(s))
# Explain the reason for change/ no change in id().
# The output will show two different id values for the string variable 's'. 
# This is because strings in Python are immutable. When we concatenate "3" to the original string "Python", a new string object is created in memory,
# and the variable 's' is updated to reference this new object. Therefore, the id of 's' changes after the concatenation.
