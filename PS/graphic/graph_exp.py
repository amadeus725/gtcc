import numpy as np
import matplotlib.pyplot as plt

def integral_sum(x, n_terms=200):
    """Calculate the sum of integrals for finite terms"""
    result = 0
    for n in range(-n_terms, n_terms + 1):
        result += np.exp(-x * 10**n) - np.exp(-(x+1) * 10**n)
    return result

# Create x values (avoiding x=0)
x = np.logspace(-2, 2, 1000)

# Calculate y values for both functions
y1 = [integral_sum(xi) for xi in x]
y2 = np.log10(1 + 1/x)  # Changed from np.log to np.log10

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=r'$\sum_{n=-\infty}^{+\infty} \int_{x \cdot 10^n}^{(x+1) \cdot 10^n} e^{-t}dt$')
plt.plot(x, y2, label=r'$\log_{10}(1+\frac{1}{x})$')  # Changed label to reflect log10

# Set scale to logarithmic for x-axis
plt.xscale('log')

# Add labels and title with larger font size
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Comparison of Expotional Distribution and Log Base 10', fontsize=14)  # Updated title
plt.legend(fontsize=12)
plt.grid(True)

# Show the plot
plt.grid(True, which="both", ls="-", alpha=0.2)
plt.show()
