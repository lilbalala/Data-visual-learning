import numpy as np
import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts

citys = ['beijing', 'shanghai', 'guangzhou', 'shenzhen']
cityes_PM = []
for i in range(4):
    filename =citys[i] + '_AQI' + '_2018.csv'  # 文件内容："日期","质量等级","AQI指数","当天AQI排名","PM2.5"
    aqi_data = pd.read_csv(filename)

    get_data = aqi_data[['Date', 'PM']] # 提取 "日期","PM2.5"两列内容进行分析
    month_for_data = []
    for j in get_data['Date']:
        time = j.split('/')[1]
        month_for_data.append(time)
    aqi_data['Month'] = month_for_data # 获取每行数据的月份

    # 求每个月PM2.5平均值
    month_data = aqi_data.groupby(['Month'])
    month_PM = month_data['PM'].agg(['mean'])
    month_PM.reset_index(inplace=True)
    month_PM_average = month_PM.sort_index()

    # 获取每个城市每个月AQI的数据，转化为int数据类型
    month_PM_data = np.array(month_PM_average['mean'])
    month_PM_data_int = ["{}".format(int(i)) for i in month_PM_data]
    cityes_PM.append(month_PM_data_int)

months = ["{}".format(str(i) + '月') for i in range(1, 13)]


line=Line()
line.add_xaxis(months)
line.add_yaxis("北京", cityes_PM[0], color='red')
line.add_yaxis("上海", cityes_PM[1], color='purple')
line.add_yaxis("广州", cityes_PM[2], color='blue')
line.add_yaxis("深圳", cityes_PM[3], color='orange')
line.set_global_opts(title_opts=opts.TitleOpts(title='2018年北上广深PM2.5全年走势图',pos_left='center',pos_top='0'),
                    legend_opts=opts.LegendOpts(pos_top='8%'))
line.render("2018年北上广深PM2.5全年走势图.html")