import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import math
from scipy import stats

def first_significant_digit(num):
    num = abs(num)
    # Scale the number into the range [1, 10) and extract the first digit
    while num < 1:
        num *= 10
    while num >= 10:
        num //= 10
    
    return int(num)


def draw_histogram(data, bins=10):
    """
    绘制数据的频率分布直方图

    参数:
    data : list
        需要绘制直方图的数据列表
    bins : int
        直方图的区间数量，默认为10
    """
    # 计算直方图数据
    count, bin_edges = np.histogram(data, bins=bins)
    
    # 绘制直方图
    plt.bar(bin_edges[:-1], count, width=np.diff(bin_edges), edgecolor='black')
    
    # 设置图表标题和坐标轴标签
    plt.title('graph')
    plt.xlabel('data')
    plt.ylabel('frequency')
    
    # 显示图表
    plt.show()


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

# 研究如何变换均匀分布
data = np.random.uniform(0,1, 10000)
# 幂函数类
# data = np.power(data, 5)# 上界的改变没有任何区别, 5~10逐渐接近本福特定律
# data = np.power(data, 0.3)# power越小越往右偏, 0.3时倒置但不完全对称
# data = np.power(data, -30)# power越小越往接近本福特定律，越从负数方向接近0越偏离本福特定律
# 总结和猜测：将分布变为左偏分布(峰值靠左)会让它接近本福特定律, 但左偏过多会让数据过多集中于1开头；将分布变为右偏分布，会让他远离本福特定律，甚至于反向

# 指数变换
# data = np.exp(np.exp(np.exp(data)))# 上界过小会导致跨数量级过小, 但是如果集中在1开头附近，可以通过多重exp操作来解决
# data = np.exp(200*data)# 当上界扩大后，只要单重指数变换即可

# 对数变换
# data = np.log(data) # 当数据在0~1分布时，对数变换和指数变换其实都是左偏，因为负数实际上得加个符号

# 观察数据的分布
# draw_histogram(data, bins=50)

# 观察与本福特定律的相似性
# plot_leading_digit(data)
