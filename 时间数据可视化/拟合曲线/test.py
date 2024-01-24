from pyecharts.charts import Line
from pyecharts.options import VisualMapOpts, LabelOpts
from pyecharts import options as opts
import pandas as pd

# 从本地CSV文件加载数据
data = pd.read_csv(r'E:\课程\数据可视化\data\unemployment-rate-1948-2010.csv')  # 替换 'your_csv_file.csv' 为实际的文件路径

# 提取需要的列作为 x 和 y 数据
x_data = data['Year'].tolist()
y_data = data['Value'].tolist()

line = Line()
line.add_xaxis(x_data)
line.add_yaxis("模拟", y_data, label_opts=LabelOpts(is_show=False), is_smooth=True)
line.set_global_opts(
    visualmap_opts=VisualMapOpts(is_show=True),
    xaxis_opts=opts.AxisOpts(
        type_="value",
        name="x",
        is_show=True,
        is_scale=True,
        name_location='middle',
        min_=min(x_data),  # 使用数据中的最小值作为 x 轴的最小值
        max_=max(x_data),  # 使用数据中的最大值作为 x 轴的最大值
    ))

line.render('line_chart.html')  # 渲染图表到 HTML 文件