import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts
df = pd.read_csv('beijing_AQI_2018.csv')
attr = df['Date']
v1 = df['AQI']

line=Line(init_opts=opts.InitOpts(width='800px',height='400px',
                                  animation_opts=opts.AnimationOpts(animation_duration=800)))
line.add_xaxis([str(x) for x in attr])
line.add_yaxis('AQI值',v1,markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_='average')]),
              areastyle_opts=opts.AreaStyleOpts(opacity=0.3,color='#000'),
              markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='max'),
                                                     opts.MarkPointItem(type_='min')],symbol='circle',symbol_size=25))
line.set_global_opts(title_opts=opts.TitleOpts(title='2018年北京AQI全年走势图',pos_left='center',pos_top='18'))

line.render('2018年北京AQI全年走势图.html')