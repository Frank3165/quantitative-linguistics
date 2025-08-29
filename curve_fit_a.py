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
        a = i.strip().split('\t')
        g.append((float(a[0]), float(a[1])))
        n += 1

# 拆分自变量和因变量
x = np.array([item[0] for item in g])
y = np.array([item[1] for item in g])

# 定义拟合函数 y = 2.88 * x^(-b)
def func(x, b):
    return 2.6493902439 * x ** (-b)

# 只拟合b
popt, pcov = curve_fit(func, x, y, maxfev=10000)
b = popt[0]

# 计算理论值
y_theory = func(x, b)

# 卡方统计量
chi2_stat = np.sum((y - y_theory) ** 2 / (y_theory + 1e-10))
dof = len(x) - 1  # 只拟合1个参数
p_value = 1 - chi2.cdf(chi2_stat, dof)

# 计算决定系数R^2
ss_res = np.sum((y - y_theory) ** 2)
ss_tot = np.sum((y - np.mean(y)) ** 2)
r2 = 1 - ss_res / ss_tot

print(f"拟合参数: b={b}")
print(f"卡方统计量 C = {chi2_stat}")
print(f"P(X^2) = {p_value}")
print(f"决定系数 R^2 = {r2}")

# 绘图
plt.scatter(x, y, label='data')
x_smooth = np.linspace(min(x), max(x), 200)
plt.plot(x_smooth, func(x_smooth, b), 'r-', label=f'fit: y=2.649*x^(-{b:.2f})')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()