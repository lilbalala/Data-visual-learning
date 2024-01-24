import pandas as pd
from pyecharts.charts import Boxplot
from pyecharts import options as opts

df = pd.read_csv('beijing_AQI_2018.csv')

dom = df[['Date', 'PM']]
data = [[], [], [], []]
dom1, dom2, dom3, dom4 = data
for i, j in zip(dom['Date'], dom['PM']):
    time = i.split('/')[1]
    if time in ['1', '2', '3']:
        dom1.append(j)
    elif time in ['4', '5', '6']:
        dom2.append(j)
    elif time in ['7', '8', '9']:
        dom3.append(j)
    else:
        dom4.append(j)

x_axis = ['第一季度', '第二季度', '第三季度', '第四季度']
y_axis = [dom1, dom2, dom3, dom4]
boxplot=Boxplot(init_opts=opts.InitOpts(width='800px',height='400px'))
boxplot.add_xaxis(x_axis)
boxplot.add_yaxis('',boxplot.prepare_data(y_axis))
boxplot.set_global_opts(title_opts=opts.TitleOpts(title='2018年北京季度PM2.5箱形图'))
boxplot.render("2018年北京季度PM2.5箱形图.html")
