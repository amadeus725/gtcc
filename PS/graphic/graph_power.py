import numpy as np
import matplotlib.pyplot as plt

# Create new x values (avoiding x=0)
x_new = np.logspace(0, 1, 1000)

# Calculate Fr(x;f) for power law
def fr_power_law(x, alpha=2, n_terms=100):
    result = 0
    for n in range(n_terms):
        result += 1/10**(n*alpha)
    return (1/x**alpha - 1/(x+1)**alpha) * result

# Calculate y values
y3 = [fr_power_law(xi) for xi in x_new]
y4 = np.log10(1 + 1/x_new) 

# Create new plot
plt.figure(figsize=(10, 6))
plt.plot(x_new, y3, label=r'$(\frac{1}{x^\alpha} - \frac{1}{(x+1)^\alpha})\sum_{n=0}^{\infty}\frac{1}{10^{n\alpha}}$')
plt.plot(x_new, y4, label='log10(1+1/x)')

plt.xscale('log')
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Comparison of Power Distribution and Log10 Logarithm', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, which="both", ls="-", alpha=0.2)

plt.show()