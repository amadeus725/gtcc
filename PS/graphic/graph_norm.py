import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def integral_sum(x, n_terms=200, scale=10):
    """Calculate the sum of integrals using absolute value of normal distribution"""
    result = 0
    for n in range(-n_terms, n_terms + 1):
        # 使用正态分布的CDF，并考虑绝对值
        upper = x * 10**n + 10**n
        lower = x * 10**n
        # 对于绝对值的积分，需要考虑正负两部分
        result += (norm.cdf(upper, scale=scale) - norm.cdf(lower, scale=scale) +
                  norm.cdf(-lower, scale=scale) - norm.cdf(-upper, scale=scale))
    return result

# Create x values (avoiding x=0)
x = np.logspace(0, 1, 1000)

# Calculate y values using the absolute value of normal distribution
y1 = []
scale = 10  # 设置标准差
for xi in x:
    y1.append(integral_sum(xi, scale=scale))

# Calculate log function
y2 = np.log10(1 + 1/x)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=r'$\sum_{n=-\infty}^{+\infty} \int_{x \cdot 10^n}^{(x+1) \cdot 10^n} \frac{1}{\sqrt{2\pi}}e^{-\frac{t^2}{2\sigma^2}}dt$')
plt.plot(x, y2, label=r'$\log_{10}(1+\frac{1}{x})$')

# Set scale to logarithmic for x-axis
plt.xscale('log')

# Add labels and title with larger font size
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Comparison of Absolute Normal Distribution and Log Base 10', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, which="both", ls="-", alpha=0.2)
plt.show()
