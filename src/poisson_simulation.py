import numpy as np  # 导入numpy库，用于数值计算
import matplotlib.pyplot as plt  # 导入matplotlib.pyplot库，用于绘图
from scipy.special import factorial  # 导入scipy.special.factorial函数，用于计算阶乘

def plot_poisson_pmf(lambda_param=8, max_l=20):
    """绘制泊松分布的概率质量函数"""
    # 生成l值序列，从0到max_l（包括max_l）
    l = np.arange(0, max_l + 1)
    
    # 计算泊松分布的概率质量函数值，公式为：p(l) = (λ^l * e^(-λ)) / l!
    pmf = (lambda_param**l * np.exp(-lambda_param)) / factorial(l)
    
    # 绘制概率质量函数曲线，使用蓝色圆点和线条，标签为'Poisson PMF'
    plt.plot(l, pmf, 'bo-', label='Poisson PMF')
    
    # 设置图形标题，显示泊松分布的参数λ
    plt.title(f'Poisson Distribution (λ={lambda_param})')
    
    # 设置x轴标签为'l'
    plt.xlabel('l')
    
    # 设置y轴标签为'Probability'
    plt.ylabel('Probability')
    
    # 显示图例，区分不同的曲线
    plt.legend()

def simulate_coin_flips(n_experiments=10000, n_flips=100, p_head=0.08):
    """模拟多组抛硬币实验"""
    # 使用np.random.choice模拟每次抛硬币的结果：
    # - [1, 0]表示硬币的正面和反面
    # - size=(n_experiments, n_flips)生成一个二维数组，行数为实验组数，列数为每组抛硬币次数
    # - p=[p_head, 1-p_head]指定正面和反面的概率
    flips = np.random.choice([1, 0], size=(n_experiments, n_flips), p=[p_head, 1-p_head])
    
    # 统计每组实验中正面朝上的次数，即每行的和。axis=1表示沿列方向求和
    heads_count = np.sum(flips, axis=1)
    
    # 返回每组实验中正面朝上的次数数组
    return heads_count

def compare_simulation_theory(n_experiments=10000, lambda_param=8):
    """比较实验结果与理论分布"""
    # 调用simulate_coin_flips函数，获取实验结果，即每组实验中正面朝上的次数
    heads_count = simulate_coin_flips(n_experiments)
    
    # 绘制实验结果的直方图：
    # - bins=np.arange(0, 21) - 0.5设置分组区间，确保每个整数都有一个独立的柱子
    # - density=True将直方图归一化为概率密度
    # - alpha=0.6设置透明度，方便叠加显示
    # - label='Simulation Results'设置标签
    plt.hist(heads_count, bins=np.arange(0, 21) - 0.5, density=True, alpha=0.6, label='Simulation Results')
    
    # 计算理论泊松分布的概率质量函数值：
    # - l=np.arange(0, 21)生成从0到20的整数序列
    # - pmf=(lambda_param**l * np.exp(-lambda_param)) / factorial(l)计算每个l对应的概率
    l = np.arange(0, 21)
    pmf = (lambda_param**l * np.exp(-lambda_param)) / factorial(l)
    
    # 绘制理论泊松分布曲线，使用红色圆点和线条，标签为'Theoretical Poisson Distribution'
    plt.plot(l, pmf, 'ro-', label='Theoretical Poisson Distribution')
    
    # 设置图形标题为'Comparison of Simulation and Theory'
    plt.title('Comparison of Simulation and Theory')
    
    # 设置x轴标签为'Number of Heads'
    plt.xlabel('Number of Heads')
    
    # 设置y轴标签为'Probability'
    plt.ylabel('Probability')
    
    # 显示图例，区分实验结果和理论分布
    plt.legend()

if __name__ == "__main__":
    # 设置随机种子，保证结果可重复。42是一个常用的随机种子值
    np.random.seed(42)
    
    # 1. 绘制理论泊松分布：
    # 调用plot_poisson_pmf函数，使用默认参数λ=8，max_l=20
    plot_poisson_pmf()
    
    # 2&3. 进行实验模拟并比较结果：
    # 调用compare_simulation_theory函数，使用默认参数n_experiments=10000，lambda_param=8
    compare_simulation_theory()
    
    # 显示绘制的图形
    plt.show()
