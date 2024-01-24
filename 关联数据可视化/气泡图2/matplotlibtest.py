import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei'] # 解决中文不能正常显示的问题
crime=pd.read_csv("../data/crimeRatesByState2005.csv")
print (list(crime.murder)) # murder是列名
crime2 = crime[crime.state != "United States"] # # 排除排除state state为为United States United States的这一行 的这一行
crime2 = crime2[crime2.state != "District of Columbia"] # 排除state为District of Col
z = list(crime2.population/10000)
colors = np.random.rand(len(list(crime2.murder)))
colors = np.random.rand(len(list(crime2.murder)))
cm = plt.cm.get_cmap('RdYlBu')
fig,ax=plt.subplots(figsize=(10,5))
ax.scatter(list(crime2.murder), list(crime2.burglary), s=z,c=z,cmap=cm, linewidth=0.5, alpha=0.5)

# 图形不支持中文显示
ax.set(xlim=(0,11),ylim=(200,1300),\
    xlabel="谋杀（每10W人口）",\
    ylabel="入室盗窃（每10W人口）",\
    title="美国谋杀率和入室盗窃率")

# 特殊处理state，只显示部分地方
state_show = []
for sta in list(crime2.state):
    print(sta)
    if(sta == 'California'or
    sta == 'Florida' or
    sta == 'Texas' or
    sta == 'New York' or
    sta == 'Pennsylvania' or
    sta == 'Louisiana' or
    sta == 'Maryland'):
        state_show.append(sta)
    else:
        state_show.append('')
print(state_show)

# 显示所有气泡的state名称
for i,j,k in zip(crime2.murder,crime2.burglary, state_show):
    plt.text(x=i-0.3,y=j-0.1,s=k,fontsize=7)
ax.spines["top"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.show()