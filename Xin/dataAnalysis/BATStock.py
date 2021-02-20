import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['SimHei']

closing_bat = np.genfromtxt('收盘价.csv', delimiter=',')
vol_bat = np.genfromtxt('成交量.csv', delimiter=',')

labels = ['百度', '阿里巴巴', '腾讯']
dates = [
  '01月', '02月', '03月', '04月', '05月', '06月',
  '07月', '08月', '09月', '10月', '11月', '12月'
]

plt.suptitle('2019 BAT 股票分析')
ax1 = plt.subplot(2,2,1)
ax1.set_title('平均收盘价对比')
data1 = closing_bat.mean(axis=0)
ax1.bar(labels, data1)

ax2 = plt.subplot(2,2,2)
ax2.set_title('月平均成交量')
data2 = vol_bat.mean(axis=0)
ax2.pie(data2, labels=labels, autopct='%0.1f%%')

ax3 = plt.subplot(2,1,2)
ax3.set_title('股价趋势')
closing_baidu = closing_bat[:, 0]
closing_alibaba = closing_bat[:, 1]
closing_tencent = closing_bat[:, 2]
ax3.plot(dates, closing_baidu, 'ro-', label=labels[0])
ax3.plot(dates, closing_alibaba, 'bo-', label =labels[1])
ax3.plot(dates, closing_tencent, 'yo-', label = labels[2])
plt.show()
