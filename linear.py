import numpy as np
import matplotlib.pyplot as plt

# Given data
x = np.array([30, 70, 110, 150, 180, 220, 260, 300, 350, 390])
y = np.array([0.18, 0.37, 0.35, 0.78, 0.56, 0.75, 1.18, 1.36, 1.17, 1.65])

# Calculate b1 and b0
x_mean, y_mean = np.mean(x), np.mean(y)
b1 = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
b0 = y_mean - b1 * x_mean

# Calculate R-squared value
y_hat = b0 + b1 * x
r_squared = 1 - np.sum((y - y_hat) ** 2) / np.sum((y - y_mean) ** 2)

# Find the evaporation coefficient for air velocity = 250
air_velocity_to_find = 250
evaporation_coefficient_250 = b0 + b1 * air_velocity_to_find

# Print the results
print(f"b1 (Slope): {b1:}")
print(f"b0 (Intercept): {b0:}")
print(f"R-squared Value: {r_squared:}")
print(f"ŷ = {b0:} + {b1:}x")
print(f"Evaporation Coefficient for Air Velocity 250: {evaporation_coefficient_250:}")

# Plot the regression line
plt.scatter(x, y, color="m", marker="o", s=30)
plt.plot(x, y_hat, color="g")
plt.xlabel('Air Velocity (cm/sec)')
plt.ylabel('Evaporation Coefficient (mm^2/sec)')
plt.show()
