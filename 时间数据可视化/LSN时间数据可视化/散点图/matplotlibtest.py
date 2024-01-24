import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r'E:\pycharmworkspace\数据可视化\时间数据可视化\data\flowingdata_subscribers.csv')
plt.scatter(data.iloc[:,0],data.iloc[:,1],s=50,c='r',marker='o',alpha=0.5)
plt.xticks(rotation=90)
plt.show()