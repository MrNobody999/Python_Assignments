Border = "-"*40

#########################################################
# Dataset & Regression Results (from Assignment 1)
#########################################################

X         = [1, 2, 3, 4, 5]
Y         = [3, 4, 2, 4, 5]

slope     = 0.4
intercept = 2.4

# Regression Equation : Y = 0.4X + 2.4

#########################################################
# Step 1 : Predict all Y values using Regression Equation
#########################################################

print(Border)
print("Step 1 : Predict all Y values using Regression Equation")
print(Border)

# Y_pred = m * X + c

Y_pred = []

print("Regression Equation : Y = 0.4 * X + 2.4")
print()
print(f"{'i':<5} {'Xi':<6} {'Yi (Actual)':<15} {'Y_pred = 0.4*Xi + 2.4':<28} {'Y_pred (Predicted)'}")
print("-" * 65)

for i in range(len(X)):
    y_p = slope * X[i] + intercept
    Y_pred.append(y_p)
    print(f"{i+1:<5} {X[i]:<6} {Y[i]:<15} {slope} * {X[i]} + {intercept} = {y_p:<12} {y_p}")

print()
print(f"Actual Y    : {Y}")
print(f"Predicted Y : {Y_pred}")

#########################################################
# Step 2 : Calculate Mean Squared Error (MSE)
#########################################################

print(Border)
print("Step 2 : Calculate Mean Squared Error (MSE)")
print(Border)

# MSE Formula :
# MSE = ( sum of (Yi - Y_pred_i) squared ) / n

print("MSE Formula :")
print("  MSE = sum( (Yi - Y_pred_i)^2 ) / n")
print()
print(f"{'i':<5} {'Yi':<8} {'Y_pred':<10} {'Yi - Y_pred':<15} {'(Yi - Y_pred)^2'}")
print("-" * 55)

mse_sum = 0

for i in range(len(Y)):
    diff    = Y[i] - Y_pred[i]
    sq_diff = diff ** 2
    mse_sum += sq_diff
    print(f"{i+1:<5} {Y[i]:<8} {Y_pred[i]:<10} {round(diff,4):<15} {round(sq_diff,4)}")

print("-" * 55)
print(f"{'':>38} sum = {round(mse_sum, 4)}")
print()

n   = len(Y)
mse = mse_sum / n

print(f"MSE = {round(mse_sum, 4)} / {n}")
print(f"MSE = {round(mse, 4)}")

#########################################################
# Step 3 : Calculate Mean of Actual Y (Y_bar)
#########################################################

print(Border)
print("Step 3 : Calculate Mean of Actual Y (Y_bar)")
print(Border)

# Y_bar = sum of all Yi / n

Y_bar = sum(Y) / len(Y)

print(f"Y_bar = sum(Y) / n")
print(f"Y_bar = {sum(Y)} / {len(Y)}")
print(f"Y_bar = {Y_bar}")

#########################################################
# Step 4 : Calculate SS_total and SS_residual
#########################################################

print(Border)
print("Step 4 : Calculate SS_total and SS_residual")
print(Border)

# SS_total    = sum of (Yi - Y_bar)^2
# SS_residual = sum of (Yi - Y_pred_i)^2

print("SS_total    = sum( (Yi - Y_bar)^2 )")
print("SS_residual = sum( (Yi - Y_pred_i)^2 )")
print()
print(f"{'i':<5} {'Yi':<6} {'Y_bar':<8} {'Yi-Y_bar':<12} {'(Yi-Y_bar)^2':<16} {'Yi-Y_pred':<12} {'(Yi-Y_pred)^2'}")
print("-" * 75)

ss_total    = 0
ss_residual = 0

for i in range(len(Y)):
    diff_total    = Y[i] - Y_bar
    diff_residual = Y[i] - Y_pred[i]
    sq_total      = diff_total ** 2
    sq_residual   = diff_residual ** 2

    ss_total    += sq_total
    ss_residual += sq_residual

    print(f"{i+1:<5} {Y[i]:<6} {Y_bar:<8} "
          f"{round(diff_total,4):<12} {round(sq_total,4):<16} "
          f"{round(diff_residual,4):<12} {round(sq_residual,4)}")

print("-" * 75)
print(f"{'':>38} SS_total = {round(ss_total,4):<8} "
      f"{'':>12} SS_residual = {round(ss_residual,4)}")

#########################################################
# Step 5 : Calculate R2 Score
#########################################################

print(Border)
print("Step 5 : Calculate R2 Score")
print(Border)

# R2 Formula :
# R2 = 1 - ( SS_residual / SS_total )

print("R2 Formula :")
print("  R2 = 1 - ( SS_residual / SS_total )")
print()
print(f"  SS_residual = {round(ss_residual, 4)}")
print(f"  SS_total    = {round(ss_total, 4)}")
print()

r2 = 1 - (ss_residual / ss_total)

print(f"  R2 = 1 - ( {round(ss_residual,4)} / {round(ss_total,4)} )")
print(f"  R2 = 1 - {round(ss_residual / ss_total, 4)}")
print(f"  R2 = {round(r2, 4)}")

#########################################################
# Final Output
#########################################################

print(Border)
print("Final Output")
print(Border)

print(f"Actual Y         : {Y}")
print(f"Predicted Y      : {Y_pred}")
print()
print(f"Y_bar            : {Y_bar}")
print(f"SS_total         : {round(ss_total, 4)}")
print(f"SS_residual      : {round(ss_residual, 4)}")
print()
print(f"MSE              : {round(mse, 4)}")
print(f"R2 Score         : {round(r2, 4)}")
print()

if r2 >= 0.8:
    remark = "Excellent fit"
elif r2 >= 0.6:
    remark = "Good fit"
elif r2 >= 0.4:
    remark = "Moderate fit"
else:
    remark = "Poor fit"

print(f"Model Remark     : {remark}")
print(Border)