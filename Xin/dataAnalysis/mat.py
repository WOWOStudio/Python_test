# 数据可视化

import matplotlib.pyplot as plt
import numpy as np
t = np.arange(-6, 6, 0.1)
x = np.power(np.sin(t), 3) * 16
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
plt.plot(x, y, 'r')
plt.show()
