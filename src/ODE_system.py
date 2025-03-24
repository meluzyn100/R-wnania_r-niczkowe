import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the system of ODEs
def system_of_equations(state, time):
    x, y = state  # Unpack the state vector
    dx_dt = -x
    dy_dt = -y
    return [dx_dt, dy_dt]

if __name__ == "__main__":
    # Initial conditions
    initial_state = [0.3, 0.5]

    # Time points for the solution
    time_points = np.linspace(0, 5, 100)  # Increased resolution for smoother plots

    # Solve the system of ODEs
    solution = odeint(system_of_equations, initial_state, time_points)

    # Plot the results
    plt.figure(figsize=(8, 6))
    plt.plot(time_points, solution[:, 0], 'b-', label='x(t)')  # x(t) in blue solid line
    plt.plot(time_points, solution[:, 1], 'r--', label='y(t)')  # y(t) in red dashed line
    plt.title('Solution of the System of ODEs')
    plt.xlabel('Time')
    plt.ylabel('Response')
    plt.legend(loc='best')
    plt.grid(True)
    plt.tight_layout()
    plt.show()