from pyecharts.charts import Bar,Page
from pyecharts import options as opts
import pandas as pd

page = Page()
data = pd.read_csv(r'E:\pycharmworkspace\数据可视化\时间数据可视化\data\hot-dog-contest-winners.csv')
bar = Bar()
bar.add_xaxis(data.iloc[:,2].values.tolist())
bar.add_yaxis("A",data.iloc[:,2].values.tolist())
bar.set_global_opts(title_opts=opts.TitleOpts(title="柱状图数据显示"))
page.add(bar)
page.render('柱状图.html')
