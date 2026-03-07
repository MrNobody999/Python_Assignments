Border = "-"*40

# Dataset

X = [1, 2, 3, 4, 5]
Y = [3, 4, 2, 4, 5]

# Step 1 : Calculate Mean of X and Y

print(Border)
print("Step 1 : Calculate Mean of X and Y")
print(Border)

# Mean Formula :
# Mean = Sum of all values / Total number of values

mean_x = sum(X) / len(X)
mean_y = sum(Y) / len(Y)

print(f"X values : {X}")
print(f"Y values : {Y}")
print(f"Sum of X : {sum(X)}")
print(f"Sum of Y : {sum(Y)}")
print(f"Mean of X (X_bar) = {sum(X)} / {len(X)} = {mean_x}")
print(f"Mean of Y (Y_bar) = {sum(Y)} / {len(Y)} = {mean_y}")

# Step 2 : Calculate Slope (m)

print(Border)
print("Step 2 : Calculate Slope (m)")
print(Border)


numerator   = 0
denominator = 0

print(f"{'i':<5} {'Xi':<6} {'Yi':<6} {'Xi-X_bar':<10} {'Yi-Y_bar':<10} {'(Xi-X_bar)(Yi-Y_bar)':<16} {'(Xi-X_bar)**2'}")
print("-" * 70)

for i in range(len(X)):
    xi_diff = X[i] - mean_x
    yi_diff = Y[i] - mean_y
    product = xi_diff * yi_diff
    sq      = xi_diff ** 2

    numerator   += product
    denominator += sq

    print(f"{i+1:<5} {X[i]:<6} {Y[i]:<6} {xi_diff:<10} {yi_diff:<10} {product:<16} {sq}")

print("-" * 70)
print(f"{'':>45} Σ = {numerator:<12} Σ = {denominator}")

slope = numerator / denominator

print(f"\nSlope (m) = {numerator} / {denominator} = {slope}")

# Step 3 : Calculate Intercept (c)

print(Border)
print("Step 3 : Calculate Intercept (c)")
print(Border)

# Intercept Formula :
# c = Y_bar - m * X_bar

intercept = mean_y - (slope * mean_x)

print(f"Intercept (c) = Y_bar - m * X_bar")
print(f"Intercept (c) = {mean_y} - ({slope} * {mean_x})")
print(f"Intercept (c) = {intercept}")

# Step 4 : Display Regression Equation

print(Border)
print("Step 4 : Display Regression Equation")
print(Border)

# Linear Regression Equation :
# Y = mX + c

print(f"Regression Equation :")
print(f"  Y = {slope}X + {intercept}")

# Step 5 : Predict Y for a new X value

print(Border)
print("Step 5 : Predict Y for a new X value")
print(Border)

new_x     = float(input("Enter X value to predict Y : "))
predicted = (slope * new_x) + intercept

print(f"Prediction Calculation :")
print(f"  Y = {slope} * {new_x} + {intercept}")
print(f"  Y = {predicted}")

# Final Output

print(Border)
print("Final Output")
print(Border)

print(f"Mean of X = {mean_x}")
print(f"Mean of Y = {mean_y}")
print(f"Slope (m)     = {slope}")
print(f"Intercept (c) = {intercept}")
print(f"Regression Equation :")
print(f"Y = {slope}X + {intercept}")
print(f"Predicted Y for X = {new_x} : {predicted}")
print(Border)