import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts

df = pd.read_csv('beijing_AQI_2018.csv')

rank_message = df.groupby(['Quality_grade'])
rank_com = rank_message['Quality_grade'].agg(['count'])
rank_com.reset_index(inplace=True)
rank_com_last = rank_com.sort_values('count', ascending=False)

attr = rank_com_last['Quality_grade']
v1 = rank_com_last['count']

pie=Pie()
pie.add('',list(zip(attr,v1)))
pie.set_global_opts(title_opts=opts.TitleOpts(title='2018年北京全年空气质量情况',pos_left='center',pos_top='0'),
                   legend_opts=opts.LegendOpts(orient='vertical',pos_left='0 ',pos_top='10%'))

pie.render('2018年北京全年空气质量情况.html')