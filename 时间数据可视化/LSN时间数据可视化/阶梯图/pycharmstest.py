from pyecharts.charts import Line
from pyecharts import options as opts
line = Line()
datax = ['1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009']
datay = [0.32,0.32,0.32,0.32,0.33,0.33,0.34,0.37,0.37,0.37,0.37,0.39,0.41,0.42,0.44]
line.add_xaxis([str(x) for x in datax])
line.add_yaxis('Price',datay,is_step=True,label_opts=opts.LegendOpts(is_show=True))
line.set_global_opts(title_opts=opts.TitleOpts(title='美国邮票阶梯图'),yaxis_opts=opts.AxisOpts(max_=0.44,min_=0.3))
line.render('阶梯图.html')