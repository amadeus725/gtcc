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

# read data    
data = pd.read_csv("概统大作业\文件夹2\Salary_Data.csv")
print(data.shape, "\n", data.dtypes)
# import data2string
salary = data["Salary"]
# data washing
# @ calculate the number of NaN
print("NAN quantity:" , salary.isnull().sum())
salary = salary.tolist()
salary_new = [float(x) for x in salary if "+" not in str(x) and "-" not in str(x) and "±" not in str(x) and ">" not in str(x) and "}" not in str(x) and not math.isnan(float(x))]
# @ calculate the number of 
print("duplicate quantity:", data.duplicated().sum())
plot_leading_digit(np.exp(np.exp(np.power(salary_new, 0.1145141919810))))
