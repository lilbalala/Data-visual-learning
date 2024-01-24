import numpy as np
import pandas as pd
from pyecharts.charts import Pie, Grid
from pyecharts import options as opts

citys = ['beijing', 'shanghai', 'guangzhou', 'shenzhen']
v = []
attrs = []
for i in range(4):
    filename =  citys[i] + '_AQI' + '_2018.csv'
    df = pd.read_csv(filename) #pd.read_csv(filename, header=None, names=["Date", "Quality_grade", "AQI", "AQI_rank", "PM"])

    Quality_grade_message = df.groupby(['Quality_grade'])
    Quality_grade_com = Quality_grade_message['Quality_grade'].agg(['count'])
    Quality_grade_com.reset_index(inplace=True)
    Quality_grade_com_last = Quality_grade_com.sort_values('count', ascending=False)

    Quality_grade_array = Quality_grade_com_last['Quality_grade']
    Quality_grade_array = np.array(Quality_grade_com_last['Quality_grade'])
    attrs.append(Quality_grade_array)
    Quality_grade_count = Quality_grade_com_last['count']
    Quality_grade_count = Quality_grade_com_last['count'].values.tolist()
    v.append(Quality_grade_count)


pie1=Pie()
pie1.add('',[list(x) for x in list(zip(attrs[0],v[0]))],rosetype='radius',radius=['20%', '40%'], center=['30%', '27%'])
pie1.set_global_opts(title_opts=opts.TitleOpts(title='北京',pos_left='28%',pos_top='24%'),
                     legend_opts=opts.LegendOpts(orient='vertical',pos_top='24%',pos_right='20%'))

pie2=Pie()
pie2.add('',[list(x) for x in list(zip(attrs[1],v[1]))],rosetype='radius',radius=['20%', '40%'], center=['54%', '27%'])
pie2.set_global_opts(title_opts=opts.TitleOpts(title='上海',pos_left='52%',pos_top='24%'),
                     legend_opts=opts.LegendOpts(is_show=False))

pie3=Pie()
pie3.add('',[list(x) for x in list(zip(attrs[2],v[2]))],rosetype='radius',radius=['20%', '40%'], center=['30%', '80%'])
pie3.set_global_opts(title_opts=opts.TitleOpts(title='广州',pos_left='28%',pos_top='77%'),
                     legend_opts=opts.LegendOpts(is_show=False))

pie4=Pie()
pie4.add('',[list(x) for x in list(zip(attrs[3],v[3]))],rosetype='radius',radius=['20%', '40%'], center=['54%', '80%'])
pie4.set_global_opts(title_opts=opts.TitleOpts(title='深圳',pos_left='52%',pos_top='77%'),
                     legend_opts=opts.LegendOpts(is_show=False))

grid = Grid(init_opts=opts.InitOpts(width='1200px'))
grid.add(pie1,grid_opts=opts.GridOpts())
grid.add(pie2,grid_opts=opts.GridOpts())
grid.add(pie3,grid_opts=opts.GridOpts())
grid.add(pie4,grid_opts=opts.GridOpts())
grid.render('2018年北上广深全年空气质量情况.html')