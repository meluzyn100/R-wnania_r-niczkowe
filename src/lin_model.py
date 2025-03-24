import numpy as np
import matplotlib.pyplot as plt

# Function definition
def f(t, a, b, c, d, p0=2):
    """
    Computes the value of the function based on the given parameters.
    """
    if b + d == 0:
        raise ValueError("Parameters b and d cannot sum to zero.")
    px = (a + c) / (b + d)
    return (p0 - px) * np.exp(-(b + d) * t) + px

if __name__ == "__main__":
    # Generate x values
    x = np.arange(1, 10, 0.1)

    # Create subplots
    fig, axs = plt.subplots(2, 3, figsize=(10, 6))

    # Parameter sets and titles
    parameter_sets = [
        (0, 1, 0, 1),
        (1, 0, 0, 1),
        (0, 0, 0.2, 0.3),
        (4, 1, 1, 1),
        (4, 0.1, 0.5, 1),
        (4, 0.1, 2, 0.2),
    ]

    # Plot each parameter set
    for idx, (a, b, c, d) in enumerate(parameter_sets):
        row, col = divmod(idx, 3)
        y = [f(i, a, b, c, d) for i in x]
        axs[row, col].plot(x, y)
        axs[row, col].set_title(r"$\alpha$=%g, $\beta$=%g, $\gamma$=%g, $\delta$=%g" % (a, b, c, d))
        axs[row, col].set_xlabel("Time")
        axs[row, col].set_ylabel("Capital")
        axs[row, col].grid(True)

    # Adjust layout
    fig.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.35, wspace=0.35)

    # Save and show the plot
    plt.savefig("./img/lin_mod_gosp.png")
    plt.show()
