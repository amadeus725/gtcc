
import matplotlib.pyplot as plt

import numpy as np



# 生成自然数序列

n = 1000000000

numbers = np.arange(1, n+1)



# 计算自然数的对数尾数

log_mantissas = np.mod(np.log10(numbers), 1)



# 统计尾数频率

bins = np.linspace(0, 1, 10)

counts, _ = np.histogram(log_mantissas, bins)

frequencies = counts / n



# 绘制直方图

plt.bar(bins[:-1], frequencies, width=0.1, align='edge', ec='black')

plt.xlabel('尾数')

plt.ylabel('频率')

plt.title('自然数对数尾数的分布')

plt.xticks(bins)

plt.show()

