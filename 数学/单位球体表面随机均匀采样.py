import numpy as np
from sympy.abc import theta


# 极坐标转换
def func():
    # numpy.random.rand(): 以给定的形状创建一个数组，数组元素为在[0,1]之间均匀分布的随机数。
    u, v = np.random.rand(2)
    phi = 2 * np.pi * u
    theta = np.arccos(2 * v - 1)
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)

    return x, y, z


# Muller 法
def func():
    # numpy.random.randn(): 以给定的形状创建一个数组，数组元素为服从标准正态分布N(0,1)的随机数。
    u, v, w = np.random.randn(3)

    norm = (u ** 2 + v ** 2 + w ** 2) ** 0.5

    x, y, z = (u, v, w) / norm

    return x, y, z


_ = func()

pass