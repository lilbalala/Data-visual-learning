import pandas as pd
import matplotlib.pylot as plt

data = pd.read_csv(r'E:\pycharmworkspace\数据可视化\时间数据可视化\data\hot-dog-places.csv').T
dataA = data.iloc[:,0]+data.iloc[:,1]
dataB = data.iloc[:,1]+data.iloc[:,2]
dataC = data.iloc[:,2]

plt.rcParams['font.family']=['sans-serif']
plt.rcParams['font.sans-serif']=['SimHei']

plt.bar(data.index,dataA,color='green')
plt.bar(data.index,dataB,color='red')
plt.bar(data.index,dataC,color='blue')
plt.xlabel('时间')
plt.title('大胃王比赛前三甲')
plt.show()