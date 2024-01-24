import datetime
import random
import numpy as np
import pandas as pd
from pyecharts.charts import Calendar
from pyecharts import options as opts

df = pd.read_csv('beijing_AQI_2018.csv')

dom = df[['Date', 'PM']]
list1 = []
for i, j in zip(dom['Date'], dom['PM']):
    time_list = i.split('/')
    time = datetime.date(int(time_list[0]),int(time_list[1]),int(time_list[2]))
    PM = int(j)
    list1.append([time,str(PM)])

# 创建 Calendar 对象
calendar = Calendar(init_opts=opts.InitOpts(width='800px',height='400px'))
calendar.add('',list1,calendar_opts=opts.CalendarOpts(range_='2018'))
calendar.set_global_opts(title_opts=opts.TitleOpts(title='2018年北京PM2.5指数日历图',pos_left='40%',pos_top='10'),
                        visualmap_opts=opts.VisualMapOpts(
                            textstyle_opts=opts.TextStyleOpts(color='#000'),
                            range_text=['较大','较小'],
                            max_=300,min_=0,orient='horizontal',pos_left='20%',pos_top='70%',is_piecewise=True,split_number=6))
# 调用 render 方法保存为 HTML
calendar.render('2018年北京PM2.5指数日历图.html')
