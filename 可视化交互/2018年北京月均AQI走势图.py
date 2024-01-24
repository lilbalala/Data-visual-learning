import numpy as np
import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts

df = pd.read_csv('beijing_AQI_2018.csv')
dom = df[['Date', 'AQI']]
list1 = []
for j in dom['Date']:
    time = j.split('/')[1]
    list1.append(time)
df['month'] = list1

month_message = df.groupby(['month'])
month_com = month_message['AQI'].agg(['mean'])
month_com.reset_index(inplace=True)
month_com_last = month_com.sort_index()

attr = ["{}".format(str(i) + '月') for i in range(1, 13)]
v1 = np.array(month_com_last['mean'])
v1 = ["{}".format(int(i)) for i in v1]

line=Line(init_opts=opts.InitOpts(width='800px',height='400px'))
line.add_xaxis(attr)
line.add_yaxis('AQI月均值',v1,
              markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='max'),
                                                     opts.MarkPointItem(type_='min')]))
line.set_global_opts(title_opts=opts.TitleOpts(title='2018年北京月均AQI走势图',pos_left='center',pos_top='18'))
line.render("2018年北京月均AQI走势图.html")
