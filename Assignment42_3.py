import matplotlib.pyplot as plt

Border = "-"*40

#########################################################
# Dataset
#########################################################

Experience = [1, 2, 3, 4, 5]
Salary     = [20000, 25000, 30000, 35000, 40000]

n = len(Experience)

#########################################################
# Step 1 : Calculate Mean of X and Y (X_bar, Y_bar)
#########################################################

print(Border)
print("Step 1 : Calculate Mean of X and Y")
print(Border)

# X_bar = sum of all Xi / n
# Y_bar = sum of all Yi / n

X_bar = sum(Experience) / n
Y_bar = sum(Salary) / n

print(f"Experience (X) : {Experience}")
print(f"Salary     (Y) : {Salary}")
print()
print(f"X_bar = {sum(Experience)} / {n} = {X_bar}")
print(f"Y_bar = {sum(Salary)} / {n} = {Y_bar}")

#########################################################
# Step 2 : Calculate Slope (m)
#########################################################

print(Border)
print("Step 2 : Calculate Slope (m)")
print(Border)

# Slope Formula :
#        sum( (Xi - X_bar)(Yi - Y_bar) )
# m  =  ---------------------------------
#              sum( (Xi - X_bar)^2 )

print("m = sum( (Xi - X_bar)(Yi - Y_bar) ) / sum( (Xi - X_bar)^2 )")
print()
print(f"{'i':<5} {'Xi':<6} {'Yi':<10} {'Xi-X_bar':<12} {'Yi-Y_bar':<12} {'(Xi-X_bar)(Yi-Y_bar)':<24} {'(Xi-X_bar)^2'}")
print("-" * 80)

numerator   = 0
denominator = 0

for i in range(n):
    xi_diff = Experience[i] - X_bar
    yi_diff = Salary[i] - Y_bar
    product = xi_diff * yi_diff
    sq      = xi_diff ** 2

    numerator   += product
    denominator += sq

    print(f"{i+1:<5} {Experience[i]:<6} {Salary[i]:<10} {xi_diff:<12} {yi_diff:<12} {product:<24} {sq}")

print("-" * 80)
print(f"{'':>50} sum = {numerator:<16} sum = {denominator}")
print()

slope = numerator / denominator

print(f"m = {numerator} / {denominator}")
print(f"m = {slope}")

#########################################################
# Step 3 : Calculate Intercept (c)
#########################################################

print(Border)
print("Step 3 : Calculate Intercept (c)")
print(Border)

# Intercept Formula :
# c = Y_bar - m * X_bar

intercept = Y_bar - (slope * X_bar)

print(f"c = Y_bar - m * X_bar")
print(f"c = {Y_bar} - ({slope} * {X_bar})")
print(f"c = {intercept}")

#########################################################
# Step 4 : Display Regression Equation
#########################################################

print(Border)
print("Step 4 : Display Regression Equation")
print(Border)

print(f"Regression Equation :")
print(f"  Y = {slope}X + {intercept}")

#########################################################
# Step 5 : Predict Salary for 6 Years Experience
#########################################################

print(Border)
print("Step 5 : Predict Salary for 6 Years Experience")
print(Border)

new_x           = 6
predicted_salary = (slope * new_x) + intercept

print(f"Prediction Calculation :")
print(f"  Y = m * X + c")
print(f"  Y = {slope} * {new_x} + {intercept}")
print(f"  Y = {predicted_salary}")

#########################################################
# Step 6 : Predict all Y values for plotting
#########################################################

print(Border)
print("Step 6 : Predict all Y values for regression line")
print(Border)

Y_pred = []

print(f"{'i':<5} {'Xi':<6} {'Yi (Actual)':<15} {'Y_pred = slope*Xi + intercept'}")
print("-" * 55)

for i in range(n):
    y_p = slope * Experience[i] + intercept
    Y_pred.append(y_p)
    print(f"{i+1:<5} {Experience[i]:<6} {Salary[i]:<15} {slope} * {Experience[i]} + {intercept} = {y_p}")

print()
print(f"Actual Y    : {Salary}")
print(f"Predicted Y : {Y_pred}")

#########################################################
# Step 7 : Plot regression line using matplotlib
#########################################################

print(Border)
print("Step 7 : Plot regression line using matplotlib")
print(Border)

plt.figure(figsize=(8, 5))

# Plot actual data points
plt.scatter(
    Experience,
    Salary,
    color="blue",
    marker="o",
    s=80,
    label="Actual Data Points",
    zorder=5
)

# Plot regression line
plt.plot(
    Experience,
    Y_pred,
    color="red",
    linewidth=2,
    label=f"Regression Line : Y = {slope}X + {intercept}"
)

# Mark the predicted point for X = 6
plt.scatter(
    [new_x],
    [predicted_salary],
    color="green",
    marker="*",
    s=200,
    label=f"Predicted (X=6) : {predicted_salary}",
    zorder=6
)

plt.title("Linear Regression : Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("Graph plotted successfully")

#########################################################
# Final Output
#########################################################

print(Border)
print("Final Output")
print(Border)

print(f"X_bar (Mean Experience) : {X_bar}")
print(f"Y_bar (Mean Salary)     : {Y_bar}")
print()
print(f"Slope (m)               : {slope}")
print(f"Intercept (c)           : {intercept}")
print()
print(f"Regression Equation     : Y = {slope}X + {intercept}")
print()
print(f"Predicted Salary for 6 Years Experience : {predicted_salary}")
print(Border)