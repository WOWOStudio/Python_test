# 数据可视化

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

'''
t = np.arange(-6, 6, 0.1)
x = np.power(np.sin(t), 3) * 16
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
plt.plot(x, y, 'r')
plt.show()

for font in fm.fontManager.ttflist:
    print(font.name)

# 堆叠柱状图

plt.rcParams['font.family'] = ['SimHei']
names = ['篮球', '羽毛球', '乒乓球']
nums_boy = [16, 5, 11]
nums_girl = [10, 15, 8]

plt.bar(names, nums_boy, width=0.5, color='skyblue', label='男')
plt.bar(names, nums_girl, bottom=nums_boy, width=0.5, color='pink', label='女')
plt.legend()
plt.show()


'''
# 分组柱状图
plt.rcParams['font.family'] = ['SimHei']
times = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
# 蒸发量
data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
# 降水量
data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]

x = np.arange(12)
width = 0.2

plt.bar(x - width/2, data1, width=width, color='skyblue', label='蒸发量')
plt.bar(x + width/2, data2, width=width, color='pink', label='降水量')

plt.xticks(x, times)

plt.legend()
plt.show()

