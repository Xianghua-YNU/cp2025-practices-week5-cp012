import numpy as np
import matplotlib.pyplot as plt
# 模拟1000步的随机行走
steps = 1000
x = np.cumsum(np.random.randn(steps))
y = np.cumsum(np.random.randn(steps))

# 绘制完整轨迹图
plt.figure(figsize=(8, 8))
plt.plot(x, y, 'b-', alpha=0.7)

# 标记起点和终点
plt.scatter(x[0], y[0], color='green', s=100, label='起点')
plt.scatter(x[-1], y[-1], color='red', s=100, label='终点')

# 设置图形比例正确
plt.axis('equal')

# 添加标题和图例
plt.title('1000步随机行走轨迹')
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.legend()

# 显示图形
plt.show()
seeds = [42, 123, 456, 789]
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

for i, seed in enumerate(seeds):
    np.random.seed(seed)
    steps = 1000
    x = np.cumsum(np.random.randn(steps))
    y = np.cumsum(np.random.randn(steps))

    # 计算当前子图的行和列索引
    row = i // 2
    col = i % 2

    # 在子图中绘制轨迹
    axes[row, col].plot(x, y, 'b-', alpha=0.7)

    # 标记起点和终点
    axes[row, col].scatter(x[0], y[0], color='green', s=100, label='起点')
    axes[row, col].scatter(x[-1], y[-1], color='red', s=100, label='终点')

    # 设置图形比例正确
    axes[row, col].axis('equal')

    # 添加标题和图例
    axes[row, col].set_title(f'随机行走轨迹 {i + 1}')
    axes[row, col].set_xlabel('X轴')
    axes[row, col].set_ylabel('Y轴')
    axes[row, col].legend()

plt.tight_layout()
plt.show()
