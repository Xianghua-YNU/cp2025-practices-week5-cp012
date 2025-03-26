import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

def plot_poisson_pmf(lambda_param=8, max_l=20):
    """绘制泊松分布的概率质量函数
    
    参数:
        lambda_param (float): 泊松分布参数λ
        max_l (int): 最大的l值
    """
    # 生成从0到max_l-1的整数序列，表示可能的事件发生次数
    l_values = np.arange(max_l)
    # 根据泊松分布公式计算每个l对应的概率
    pmf = (lambda_param**l_values * np.exp(-lambda_param)) / factorial(l_values)
    
    # 创建一个图形，设置大小为10x6英寸
    plt.figure(figsize=(10, 6))
    # 绘制理论泊松分布曲线，使用蓝色圆点和实线
    plt.plot(l_values, pmf, 'bo-', label='Theoretical Distribution')
    # 设置图形标题，包含参数λ的信息
    plt.title(f'Poisson Probability Mass Function (λ={lambda_param})')
    # 设置x轴标签为'l'，表示事件发生次数
    plt.xlabel('l')
    # 设置y轴标签为'p(l)'，表示概率
    plt.ylabel('p(l)')
    # 添加网格线，使图形更易读
    plt.grid(True)
    # 显示图例，区分不同曲线
    plt.legend()
    # 返回计算得到的概率质量函数值
    return pmf

def simulate_coin_flips(n_experiments=10000, n_flips=100, p_head=0.08):
    """模拟多组抛硬币实验
    
    参数:
        n_experiments (int): 实验组数N
        n_flips (int): 每组抛硬币次数
        p_head (float): 正面朝上的概率
        
    返回:
        ndarray: 每组实验中正面朝上的次数
    """
    results = []  # 用于存储每组实验中正面朝上的次数
    # 进行n_experiments次实验
    for i in range(n_experiments):
        # 模拟一次抛硬币实验，抛n_flips次，1表示正面，0表示反面
        coins = np.random.choice([0, 1], n_flips, p=[1-p_head, p_head])
        # 统计本次实验中正面朝上的次数，并添加到结果列表中
        results.append(coins.sum())
    # 将结果列表转换为NumPy数组并返回
    return np.array(results)

def compare_simulation_theory(n_experiments=10000, lambda_param=8):
    """比较实验结果与理论分布
    
    参数:
        n_experiments (int): 实验组数
        lambda_param (float): 泊松分布参数λ
    """
    # 进行实验模拟，获取每组实验中正面朝上的次数
    results = simulate_coin_flips(n_experiments)
    
    # 确定理论分布的计算范围，确保覆盖实验结果的最大值
    max_l = max(int(lambda_param * 2), max(results) + 1)
    # 生成从0到max_l-1的整数序列
    l_values = np.arange(max_l)
    # 计算理论泊松分布的概率质量函数值
    pmf = (lambda_param**l_values * np.exp(-lambda_param)) / factorial(l_values)
    
    # 创建一个图形，设置大小为12x7英寸
    plt.figure(figsize=(12, 7))
    # 绘制实验结果的直方图：
    # - bins指定分组区间，range(max_l+1)生成从0到max_l的整数分组
    # - density=True将直方图归一化为概率密度
    # - alpha=0.7设置透明度
    # - color='skyblue'设置直方图颜色
    # - label='Simulation Results'设置标签
    plt.hist(results, bins=range(max_l+1), density=True, alpha=0.7, 
             label='Simulation Results', color='skyblue')
    # 绘制理论泊松分布曲线，使用红色实线，线宽为2
    plt.plot(l_values, pmf, 'r-', label='Theoretical Distribution', linewidth=2)
    
    # 设置图形标题，包含实验组数和参数λ的信息
    plt.title(f'Poisson Distribution Comparison (N={n_experiments}, λ={lambda_param})')
    # 设置x轴标签为'Number of Heads'，表示正面朝上的次数
    plt.xlabel('Number of Heads')
    # 设置y轴标签为'Frequency/Probability'，表示频率或概率
    plt.ylabel('Frequency/Probability')
    # 添加网格线，透明度为0.3
    plt.grid(True, alpha=0.3)
    # 显示图例，区分实验结果和理论分布
    plt.legend()
    
    # 打印实验结果的统计信息：
    # - 实验均值和理论均值（泊松分布的均值等于λ）
    # - 实验方差和理论方差（泊松分布的方差也等于λ）
    print(f"实验均值: {np.mean(results):.2f} (理论值: {lambda_param})")
    print(f"实验方差: {np.var(results):.2f} (理论值: {lambda_param})")

if __name__ == "__main__":
    # 设置随机种子，保证结果可重复
    np.random.seed(42)
    
    # 1. 绘制理论泊松分布
    plot_poisson_pmf()
    
    # 2&3. 进行实验模拟并比较结果
    compare_simulation_theory()
    
    # 显示所有绘制的图形
    plt.show()
