import numpy as np
import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts

citys = ['beijing', 'shanghai', 'guangzhou', 'shenzhen']
cityes_AQI = []
for i in range(4):
    filename =  citys[i] + '_AQI' + '_2018.csv' # 文件内容："日期","质量等级","AQI指数","当天AQI排名","PM2.5"
    aqi_data = pd.read_csv(filename)

    get_data = aqi_data[['Date', 'AQI']] # 提取 "日期","AQI指数"两列内容进行分析
    month_for_data = []
    for j in get_data['Date']:
        time = j.split('/')[1]
        month_for_data.append(time)
    aqi_data['Month'] = month_for_data # 获取每行数据的月份

    # 求每个月AQI平均值
    month_data = aqi_data.groupby(['Month'])
    month_AQI = month_data['AQI'].agg(['mean'])
    month_AQI.reset_index(inplace=True)
    month_AQI_average = month_AQI.sort_index()

    # 获取每个城市月均AQI的数据，转化为int数据类型
    month_AQI_data = np.array(month_AQI_average['mean'])
    month_AQI_data_int = ["{}".format(int(i)) for i in month_AQI_data]
    cityes_AQI.append(month_AQI_data_int)

months = ["{}".format(str(i) + '月') for i in range(1, 13)]

line=Line()
line.add_xaxis(months)
line.add_yaxis("北京", cityes_AQI[0], color='red')
line.add_yaxis("上海", cityes_AQI[1], color='purple')
line.add_yaxis("广州", cityes_AQI[2], color='blue')
line.add_yaxis("深圳", cityes_AQI[3], color='orange')
line.set_global_opts(title_opts=opts.TitleOpts(title='2018年北上广深AQI全年走势图',pos_left='center',pos_top='0'),
                    legend_opts=opts.LegendOpts(pos_top='8%'))
line.render("2018年北上广深AQI全年走势图.html")