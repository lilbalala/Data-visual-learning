import pandas as pd
from pyecharts.charts import Scatter
from pyecharts import options as opts

data = pd.read_csv(r'E:\pycharmworkspace\数据可视化\时间数据可视化\data\flowingdata_subscribers.csv')
scatter = Scatter()
scatter.add_xaxis(data.iloc[:,0].values.tolist())
scatter.add_yaxis('订阅量',data.iloc[:,1].values.tolist(),label_opts=opts.LabelOpts(is_show=False))
scatter.set_global_opts(title_opts=opts.TitleOpts(title='杂志订阅量'))
scatter.render('散点图.html')