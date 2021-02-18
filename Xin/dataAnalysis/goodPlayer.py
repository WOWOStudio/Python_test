import numpy as np


player1 = np.array([4, 16, 5, 8, 11, 40, 4, 12, 23, 13])
player2 = np.array([9, 8, 12, 11, 9, 10, 13, 10, 11, 13])
player3 = np.array([4, 6, 8, 5, 6, 7, 6, 5, 8, 6])

print('球员1的平均成绩是', player1.mean())
print('球员2的平均成绩是', player2.mean())
print('球员3的平均成绩是', player3.mean())

print('球员1成绩的中位数是', np.median(player1))
print('球员2成绩的中位数是', np.median(player2))
print('球员3成绩的中位数是', np.median(player3))

print('球员1成绩的标准差是', player1.std())
print('球员2成绩的标准差是', player2.std())
print('球员3成绩的标准差是', player3.std())
