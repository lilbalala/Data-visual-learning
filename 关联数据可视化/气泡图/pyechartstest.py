from pyecharts.charts import Scatter
from pyecharts import options as opts
import pandas as pd

crime=pd.read_csv("../data/crimeRatesByState2005.csv")
crime2 = crime[crime.state != "United States"]
crime2 = crime2[crime2.state != "District of Columbia"]
data=[list(z) for z in zip(crime2['murder'].values.tolist(),crime2['burglary'].values.tolist())]
data.sort(key=lambda x:x[0])
datax=[d[0] for d in data]
datay=[d[1] for d in data]
scatter=Scatter()
scatter.add_xaxis(datax)
scatter.add_yaxis('气泡散点图',datay,label_opts={'is_show':False})
scatter.set_global_opts( title_opts=opts.TitleOpts(title='2005年美国各州的犯罪情况'),
                         visualmap_opts=opts.VisualMapOpts(type_='size',dimension=0,max_=11),
                         xaxis_opts=opts.AxisOpts(type_='value'),
                         yaxis_opts=opts.AxisOpts(type_='value'))

scatter.render('气泡散点图.html')
