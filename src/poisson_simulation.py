import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

def plot_poisson_pmf(lambda_param=8, max_l=20):
    """绘制泊松分布的概率质量函数"""
    # 生成l值序列，从0到max_l
    l = np.arange(0, max_l + 1)
    # 计算泊松分布的概率质量函数值
    pmf = (lambda_param**l * np.exp(-lambda_param)) / factorial(l)
    # 绘制概率质量函数曲线
    plt.plot(l, pmf, 'bo-', label='Poisson PMF')
    # 设置图形标题和轴标签
    plt.title(f'Poisson Distribution (λ={lambda_param})')
    plt.xlabel('l')
    plt.ylabel('Probability')
    # 显示图例
    plt.legend()

def simulate_coin_flips(n_experiments=10000, n_flips=100, p_head=0.08):
    """模拟多组抛硬币实验"""
    # 使用np.random.choice模拟每次抛硬币的结果，生成n_experiments组，每组n_flips次抛硬币
    # 参数p=[p_head, 1-p_head]指定正面和反面的概率
    flips = np.random.choice([1, 0], size=(n_experiments, n_flips), p=[p_head, 1-p_head])
    # 统计每组实验中正面朝上的次数，即每行的和
    heads_count = np.sum(flips, axis=1)
    return heads_count

def compare_simulation_theory(n_experiments=10000, lambda_param=8):
    """比较实验结果与理论分布"""
    # 调用simulate_coin_flips函数，获取实验结果
    heads_count = simulate_coin_flips(n_experiments)
    
    # 绘制实验结果的直方图
    plt.hist(heads_count, bins=np.arange(0, 21) - 0.5, density=True, alpha=0.6, label='Simulation Results')
    
    # 计算理论泊松分布的概率质量函数值，并乘以n_experiments以与直方图比较
    l = np.arange(0, 21)
    pmf = (lambda_param**l * np.exp(-lambda_param)) / factorial(l)
    plt.plot(l, pmf, 'ro-', label='Theoretical Poisson Distribution')
    
    # 设置图形属性
    plt.title('Comparison of Simulation and Theory')
    plt.xlabel('Number of Heads')
    plt.ylabel('Probability')
    plt.legend()

if __name__ == "__main__":
    # 设置随机种子，保证结果可重复
    np.random.seed(42)
    
    # 1. 绘制理论泊松分布
    plot_poisson_pmf()
    
    # 2&3. 进行实验模拟并比较结果
    compare_simulation_theory()
    
    # 显示图形
    plt.show()
