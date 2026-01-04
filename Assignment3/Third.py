# Question: Predict the output:

def fun():
    x = 10
    print(x)

fun()   
print(x)
#Explain the reason.

#Ans: The output of the code will be:
# 10
# Followed by an error message: NameError: name 'x' is not defined  
# This is because the variable 'x' is defined within the local scope of the function 'fun()'. When 'fun()' is called, it prints the value of 'x' which is 10. However, when we try to print 'x' outside of the function, it results in a NameError because 'x' is not defined in the global scope.