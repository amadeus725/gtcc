import matplotlib.pyplot as plt
import numpy as np

# 模拟数据
np.random.seed(42)
data = np.random.lognormal(mean=1, sigma=0.5, size=10000)

# 计算对数刻度的bin边缘
edges = np.geomspace(1, 100000, num=20)

# 绘制直方图
fig, ax = plt.subplots()

# 使用numpy的histogram函数计算频率
counts, _, patches = ax.hist(data, bins=edges, color='red', edgecolor='blue')

# 将x轴设置为对数刻度
ax.set_xscale("log")

# 设置标题和标签
ax.set_title('Log-Normal Distribution Histogram')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')

# 显示网格线
ax.grid(True, which="both", linestyle="--", linewidth=0.5)

# 显示图表
plt.show()
