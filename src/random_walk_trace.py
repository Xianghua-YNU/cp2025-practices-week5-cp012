import numpy as np
import matplotlib.pyplot as plt


def random_walk_2d(steps):
    """生成二维随机行走轨迹

    参数:
        steps (int): 随机行走的步数

    返回:
        tuple: 包含x和y坐标序列的元组 (x_coords, y_coords)
    """
    x_steps = np.random.choice([-1, 1], size=steps)
    y_steps = np.random.choice([-1, 1], size=steps)
    x_coords = np.cumsum(x_steps)
    y_coords = np.cumsum(y_steps)
    return x_coords, y_coords


def plot_single_walk(path):
    """绘制单个随机行走轨迹

    参数:
        path (tuple): 包含x和y坐标序列的元组
    """
    x_coords, y_coords = path
    plt.plot(x_coords, y_coords, 'b-', alpha=0.7)
    plt.scatter(x_coords[0], y_coords[0], color='green', s=100, label='起点')
    plt.scatter(x_coords[-1], y_coords[-1], color='red', s=100, label='终点')
    plt.axis('equal')
    plt.legend()
    plt.title('单个随机行走轨迹')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    plt.show()


def plot_multiple_walks():
    """在2x2子图中绘制四个不同的随机行走轨迹"""
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    seeds = [42, 123, 456, 789]

    for i, seed in enumerate(seeds):
        np.random.seed(seed)
        path = random_walk_2d(1000)
        x_coords, y_coords = path
        row = i // 2
        col = i % 2

        axes[row, col].plot(x_coords, y_coords, 'b-', alpha=0.7)
        axes[row, col].scatter(x_coords[0], y_coords[0], color='green', s=100, label='起点')
        axes[row, col].scatter(x_coords[-1], y_coords[-1], color='red', s=100, label='终点')
        axes[row, col].axis('equal')
        axes[row, col].set_title(f'随机行走轨迹 {i + 1}')
        axes[row, col].set_xlabel('X轴')
        axes[row, col].set_ylabel('Y轴')
        axes[row, col].legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # 生成并绘制单个轨迹
    single_path = random_walk_2d(1000)
    plot_single_walk(single_path)

    # 生成并绘制多个轨迹
    plot_multiple_walks()
