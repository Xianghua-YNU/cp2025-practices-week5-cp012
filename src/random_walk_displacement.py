import numpy as np
import matplotlib.pyplot as plt

# 模拟二维随机行走
def random_walk_displacement(num_steps,num_simulations):
    # 初始化位置数组 (x, y)
    steps=np.random.choice([-1,1],size=(2,num_simulations,num_steps))
    final_displacements=np.sum(steps,axis=2)
    return final_displacements

def plot_displacement_distribution(final_displacements, bins=30):
    displacements=np.sqrt(final_displacements[0]**2+final_displacements[1]**2)
    plt.figure(figsize=(10,6))
    plt.hist(displacements, bins=bins,density=True,alpha=0.7,color='r')
    plt.title('Distribution of displacements')
    plt.xlabel('displacement')
    plt.ylabel('probability')
    plt.legend()
    plt.show()

def plot_displacement_square_distribution(final_displacements, bins=30):
    """
    绘制位移平方分布直方图

    参数:
    final_displacements (list): 包含每次模拟最终位移的列表
    bins (int): 直方图的组数
    """
    # TODO: 实现位移平方分布的直方图绘制
    # 1. 计算位移平方
    # 2. 使用plt.hist绘制直方图
    # 3. 添加标题和标签

    displacement_squared=final_displacements[0]**2+final_displacements[1]**2
    plt.hist(displacement_squared, bins=bins,density=True,alpha=0.7,color='g')
    plt.title('Distribution of displacement squared')
    plt.xlabel('displacement')
    plt.ylabel('probability')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # 可调整的参数
    num_steps = 1000  # 随机行走的步数
    num_simulations = 1000  # 模拟的次数
    bins = 30  # 直方图的组数
    final_displacements=random_walk_displacement(num_steps, num_simulations)
    plot_displacement_distribution(final_displacements, bins=30)
    plot_displacement_square_distribution(final_displacements, bins=30)
