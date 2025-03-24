"""
equilibrium_point.py

The script calculates and visualizes equilibrium points for a mathematical model.
"""
import matplotlib.pyplot as plt


# Plot the supply and demand lines
plt.plot(((0, 0), (2, 2)), color="black", label="Supply (S)")
plt.plot(((0, 2), (2, 0)), color="black", label="Demand (D)")

# Add labels for axes
plt.xlabel("Price", fontsize=15)
plt.ylabel("Quantity", fontsize=15)

# Remove tick labels for a cleaner look
plt.tick_params(labelbottom=False)
plt.tick_params(labelleft=False)

# Add annotations for equilibrium point and curves
plt.text(0.5, 1.1, r"$P^*$", fontsize=15)  # Equilibrium price
plt.text(0.8, 0.45, "D", fontsize=15)      # Demand curve
plt.text(0.8, 1.7, "S", fontsize=15)       # Supply curve

# Save the plot to a file
plt.savefig("./img/punkt_równowagi.png", dpi=300)

# Display the plot
plt.show()
