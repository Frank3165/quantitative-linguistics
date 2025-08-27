import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from scipy.stats import chi2

with open('syllable_phone_HSK.txt','r') as sp:
    g = []
    n = 0
    for i in sp.readlines():
        if n == 4:
            break
        a_ = i.strip().split('\t')
        g.append((float(a_[0]), float(a_[1])))
        n += 1

# 拆分自变量和因变量
x = np.array([item[0] for item in g])
y = np.array([item[1] for item in g])

# 定义拟合函数 y = a * x^(-b) * exp(-c*x)
def func(x, a, b, c):
    return a * x ** (-b) * np.exp(-c * x)

# 拟合，给定初始参数猜测
popt, pcov = curve_fit(func, x, y, p0=[1, 1, 0.01], maxfev=10000)
a, b, c = popt

# 计算理论值
y_theory = func(x, *popt)

# 卡方统计量
chi2_stat = np.sum((y - y_theory) ** 2 / (y_theory + 1e-10))  # 防止除零
dof = len(x) - 3  # 参数数变为3
p_value = 1 - chi2.cdf(chi2_stat, dof)

# 计算决定系数R^2
ss_res = np.sum((y - y_theory) ** 2)
ss_tot = np.sum((y - np.mean(y)) ** 2)
r2 = 1 - ss_res / ss_tot

print(f"拟合参数: a={a}, b={b}, c={c}")
print(f"卡方统计量 C = {chi2_stat}")
print(f"P(X^2) = {p_value}")
print(f"决定系数 R^2 = {r2}")

# 绘图
plt.scatter(x, y, label='data')
x_smooth = np.linspace(min(x), max(x), 200)
plt.plot(x_smooth, func(x_smooth, *popt), 'r-', label=f'fit: y={a:.2f}*x^(-{b:.2f})*e^(-{c:.4f}x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()