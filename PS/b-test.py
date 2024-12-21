import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import math
from scipy.stats import moment


def first_significant_digit(num):
    num = abs(num)
    # Scale the number into the range [1, 10) and extract the first digit
    while num < 1:
        num *= 10
    while num >= 10:
        num //= 10
    
    return int(num)


def plot_leading_digit(numbers, title = "First Digit Frequency vs Benford's Law"):
    def get_first_digits(numbers):
        first_digits = list(map(first_significant_digit , numbers))
        return first_digits

    # Calculate the first digit frequencies
    first_digits = get_first_digits(numbers)
    digit_counts = Counter(first_digits)

    # Normalize to get proportions
    total_counts = sum(digit_counts.values())
    observed_frequencies = {digit: count / total_counts for digit, count in digit_counts.items()}

    # Benford's Law predictions
    benford_frequencies = {d: np.log10(1 + 1/d) for d in range(1, 10)}

    # Plotting
    digits = range(1, 10)
    observed_values = [observed_frequencies.get(d, 0) for d in digits]
    benford_values = [benford_frequencies[d] for d in digits]

    # 找到数据对本福特定律的偏离程度
    deviation1 = 1/9 * sum([(observed_values[i]/benford_values[i]-1)**2 for i in range(9)])
    deviation2 = 1/9 * sum([(observed_values[i]-benford_values[i])**2 for i in range(9)])
    print(f"Chi-Square Deviation: {deviation1:.6f}, Sum of Squared Differences: {deviation2:.6f}")

    plt.figure(figsize=(10, 6))
    plt.bar(digits, observed_values, alpha=0.7, label="Observed", color="blue", width=0.4, align="center")
    plt.bar(digits, benford_values, alpha=0.7, label="Benford's Law", color="orange", width=0.4, align="edge")
    plt.xticks(digits)
    plt.xlabel("First Digit")
    plt.ylabel("Frequency")
    plt.title(title)
    plt.legend()
    plt.savefig('Benford.pdf')
    plt.show()

def central_moment(data, k):
    mean = np.mean(data)
    var = np.var(data)
    std_dev = np.sqrt(var)
    print(mean)
    return np.mean(((data - mean)/std_dev) ** k)


def plot_histogram_with_moments(data, bins=100, title="Data Distribution"):
    
    third_central_moment = central_moment(data, 3)
    third_moment_magnitude = math.log10(abs(third_central_moment))
    fourth_central_moment = central_moment(data, 4)
    fourth_moment_magnitude = math.log10(abs(fourth_central_moment))
    
    # 打印偏度、峰度及其数量级
    print(f"Third Moment (Skewness): {third_central_moment}, Magnitude: {third_moment_magnitude}")
    print(f"Fourth Moment (Kurtosis): {fourth_central_moment}, Magnitude: {fourth_moment_magnitude}")
    # 绘制直方图
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, alpha=0.7, color="blue", edgecolor="black")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title(f"{title}\nThird Moment: {third_central_moment:.2f}, Fourth Moment: {fourth_central_moment:.2f}")
    plt.grid(True)
    plt.show()
'''
# 幂函数峰度的上下界（大于2.6）
data = np.random.uniform(0 ,10 ,100000)
data = np.power(1.3, data)# 本福特定律初见端倪 - 峰度～2.6；偏度～0.87
'''

# 生成服从对数正态分布的数据（大于16）
#data = np.random.lognormal(0, 0.5, 100000)#峰值为9.69的时候difference为0.004147
#data = np.random.lognormal(0, 0.7, 100000)#峰值为16的时候difference为0.000743
data = np.random.lognormal(0, 0.8, 100000)
'''
data = np.random.normal(0, 1, 100000)
data = np.abs(data)
'''
#data = np.random.chisquare(df=0.05, size=100000)#卡方分布可以非常接近
#data = np.random.f(dfnum=1, dfden=1, size=100000)

'''#峰度和difference的关系
# Generate data with different exponents and calculate kurtosis and sum of squared differences
# Define a range of exponents to test
exponents = np.linspace(1, 1.8, 100)
kurtosis_values = []
sum_of_squared_differences = []

# Loop through each exponent to generate data and calculate kurtosis and sum of squared differences
for exp in exponents:
    # Generate uniform random data and transform it using the current exponent
    data = np.random.uniform(0, 10, 100000)
    data = np.power(exp, data)
    
    # Calculate the fourth central moment (kurtosis) of the transformed data
    fourth_central_moment = central_moment(data, 4)
    kurtosis_values.append(fourth_central_moment)
    
    # Calculate the sum of squared differences from Benford's Law
    first_digits = [first_significant_digit(num) for num in data]
    digit_counts = Counter(first_digits)
    total_counts = sum(digit_counts.values())
    observed_frequencies = {digit: count / total_counts for digit, count in digit_counts.items()}
    benford_frequencies = {d: np.log10(1 + 1/d) for d in range(1, 10)}
    digits = range(1, 10)
    observed_values = [observed_frequencies.get(d, 0) for d in digits]
    benford_values = [benford_frequencies[d] for d in digits]
    sum_of_squared_diff = 1/9 * sum([(observed_values[i] - benford_values[i])**2 for i in range(9)])
    sum_of_squared_differences.append(sum_of_squared_diff)

# Plot kurtosis vs sum of squared differences
plt.figure(figsize=(10, 6))
plt.plot(kurtosis_values, sum_of_squared_differences, marker='o', linestyle='-', color='b')
plt.xlabel('Kurtosis')
plt.ylabel('Sum of Squared Differences')
plt.title('Kurtosis vs Sum of Squared Differences from Benford\'s Law')
plt.grid(True)
plt.show()
'''


plot_leading_digit(data)
plot_histogram_with_moments(data)