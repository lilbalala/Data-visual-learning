import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r'E:\pycharmworkspace\数据可视化\时间数据可视化\data\world-population.csv')
plt.plot(data['Year'],data['Population'])
plt.show()
