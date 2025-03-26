import numpy as np  # 导入numpy库，用于数值计算
import matplotlib.pyplot as plt  # 导入matplotlib.pyplot库，用于绘图


def random_walk_finals(num_steps=1000, num_walks=1000):
    """生成多个二维随机游走的终点位置"""
    # 生成随机步长，每个方向独立选择±1
    dx = np.random.choice([-1, 1], size=(num_walks, num_steps))  # 为x方向生成随机步长，size参数指定数组形状
    dy = np.random.choice([-1, 1], size=(num_walks, num_steps))  # 为y方向生成随机步长

    # 计算总位移
    x_finals = np.sum(dx, axis=1)  # 沿着步数维度求和，得到每个游走的x方向总位移
    y_finals = np.sum(dy, axis=1)  # 沿着步数维度求和，得到每个游走的y方向总位移

    return x_finals, y_finals  # 返回所有游走的终点坐标


def calculate_mean_square_displacement():
    """计算不同步数下的均方位移"""
    steps = np.array([1000, 2000, 3000, 4000])  # 预设的步数列表
    msd = np.zeros_like(steps, dtype=float)  # 初始化均方位移数组，与steps形状相同

    for i, num_steps in enumerate(steps):  # 遍历每个步数
        x_finals, y_finals = random_walk_finals(num_steps=num_steps)  # 调用random_walk_finals函数，获取终点坐标

        # 计算每个终点的位移平方和
        r_squared = x_finals ** 2 + y_finals ** 2  # 位移平方和公式

        # 计算均值
        msd[i] = np.mean(r_squared)  # 使用np.mean计算平均值，得到均方位移

    return steps, msd  # 返回步数和对应的均方位移


def analyze_step_dependence():
    """分析均方位移与步数的关系，并进行最小二乘拟合"""
    steps, msd = calculate_mean_square_displacement()  # 调用calculate_mean_square_displacement函数，获取数据

    # 线性拟合：msd = k * steps
    numerator = np.sum(steps * msd)  # 计算分子部分：步数与均方位移的乘积之和
    denominator = np.sum(steps ** 2)  # 计算分母部分：步数的平方和
    k = numerator / denominator  # 计算比例系数k

    return steps, msd, k  # 返回步数、均方位移和比例系数


if __name__ == "__main__":
    # 获取数据和拟合结果
    steps, msd, k = analyze_step_dependence()  # 调用analyze_step_dependence函数，获取分析结果

    # 绘制实验数据点和理论曲线
    plt.figure(figsize=(8, 6))  # 设置图形大小
    plt.scatter(steps, msd, color='blue', label='实验数据')  # 绘制散点图，显示实验数据
    plt.plot(steps, k * steps, color='red', label=f'拟合曲线 (msd = {k:.4f} * steps)')  # 绘制拟合曲线

    # 设置图形属性
    plt.title('均方位移与步数的关系')  # 设置标题
    plt.xlabel('步数')  # 设置x轴标签
    plt.ylabel('均方位移 (msd)')  # 设置y轴标签
    plt.grid(True)  # 添加网格
    plt.legend()  # 添加图例

    # 打印数据分析结果
    print(f"拟合得到的比例系数 k = {k:.4f}")  # 打印比例系数，保留4位小数
    print("理论预期：在二维随机游走中，msd 应与步数成正比，比例系数接近 2")  # 打印理论预期

    # 显示图形
    plt.show()  # 显示绘制的图形
