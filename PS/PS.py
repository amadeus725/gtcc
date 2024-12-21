import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import math

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

    # Calculate deviations from Benford's Law
    deviation1 = 1/9 * sum([(observed_values[i]/benford_values[i]-1)**2 for i in range(9)])
    deviation2 = 1/9 * sum([(observed_values[i]-benford_values[i])**2 for i in range(9)])
    print(f"Chi-Square Deviation: {deviation1:.6f}, Sum of Squared Differences: {deviation2:.6f}")

    plt.figure(figsize=(10, 8))  # Increased figure height
    # Add text with more space from the plot
    plt.text(0.5, 1.15, f"Chi-Square Deviation: {deviation1:.6f}\nSum of Squared Differences: {deviation2:.6f}", 
             horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
    
    plt.bar(digits, observed_values, alpha=0.7, label="Observed", color="blue", width=0.4, align="center")
    plt.bar(digits, benford_values, alpha=0.7, label="Benford's Law", color="orange", width=0.4, align="edge")
    plt.xticks(digits)
    plt.xlabel("First Digit")
    plt.ylabel("Frequency")
    plt.title(title)
    plt.legend()
    # Add more space at the top
    plt.subplots_adjust(top=0.7)
    plt.savefig('Benford.pdf')
    plt.show()
# read data    
data = pd.read_csv("exoplanets.csv")
print(data.shape, "\n", data.dtypes)
# import data2string
period = data["Period (days)"]
# data washing
# @ calculate the number of NaN
print("NAN quantity:" , period.isnull().sum())
period = period.tolist()
period_new = [float(x) for x in period if "+" not in str(x) and "-" not in str(x) and "±" not in str(x) and ">" not in str(x) and "}" not in str(x) and not math.isnan(float(x))]
# @ calculate the number of 
print("duplicate quantity:", data.duplicated().sum())
#plot_leading_digit(period_new)


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

plot_histogram_with_moments(period_new)