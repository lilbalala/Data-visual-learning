import pandas as pd
from pyecharts.charts import Line
from pyecharts import options
data = pd.read_csv(r'E:\pycharmworkspace\数据可视化\时间数据可视化\data\world-population.csv')
line = Line()
line.add_xaxis([str(x) for x in data['Year'].values.tolist()])
line.add_yaxis('人口',data['Population'].values.tolist(),label_opts=options.LabelOpts(is_show=True))
line.set_global_opts(title_opts=options.TitleOpts(title='历年人口总量折线图'))
line.render('折线图.html')