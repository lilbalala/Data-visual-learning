import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as pit
import pandas as pd

data = pd.read_csv(r'E:\pycharmworkspace\数据可视化\时间数据可视化\data\unemployment-rate-1948-2010.csv')
plt.figure()
plt.scatter(data['Year'],data['Value'],s=10,c='g',marker='o',alpha=0.5)
ploy = np.polyfit(data['Year'],data['Value'],deg = 3)
plt.plot(data['Year'],np.polyval(ploy,data['Year']))
plt.show()