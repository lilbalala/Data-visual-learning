from pyecharts.charts import Bar,Page
from pyecharts import options as opts
import pandas as pd

data = pd.read_csv(r'E:\pycharmworkspace\数据可视化\时间数据可视化\data\hot-dog-places.csv').T
page = Page()
bar = Bar()

bar.add_xaxis([str(x) for x in data.values.tolist()])
bar.add_yaxis('A',data.iloc[:,0].values.tolist(),stack=True)
bar.add_yaxis('B',data.iloc[:,1].values.tolist(),stack=True)
bar.add_yaxis('C',data.iloc[:,2].values.tolist(),stack=True)
bar.set_global_opts(title_opts=opts.TitleOpts(title='堆叠柱形图数据示例'))
page.add(bar)
page.render('堆叠柱形图.html')