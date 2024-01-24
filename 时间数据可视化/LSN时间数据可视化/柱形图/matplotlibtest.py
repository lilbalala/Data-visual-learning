import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'E:\pycharmworkspace\数据可视化\时间数据可视化\data\hot-dog-contest-winners.csv')

plt.rcParams['font.family']=['sans-serif']
plt.rcParams['font.sans-serif']=['SimHei']

plt.bar(data.iloc[:,0],data.iloc[:,2])
plt.xlabel('时间')
plt.ylabel('人口总量（亿元）')
plt.title('全球历年人口总量')
plt.show()