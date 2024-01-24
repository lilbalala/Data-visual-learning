import json
import pandas as pd
from flask import Flask,render_template,request,jsonify

from dataclass import setdata

app=Flask(__name__)

data=pd.read_csv('../data.csv')
data=setdata(data)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/test')
def iframe():
    return render_template('iframe.html')
@app.route('/data')
def givedata():
    category=data.category()
    category_1_2=data.category_1_2()
    gender_c1=data.gender_c1()
    category_2_mount=data.category_2_mount()
    t_y_m_mount = data.t_y_m_mount()
    category_1_mount = data.category_1_mount()
    gdata={'category':category,
          'category_1_2':category_1_2,
           'gender_c1':gender_c1,
           'category_2_mount':category_2_mount,
           't_y_m_mount':t_y_m_mount,
           'category_1_mount':category_1_mount}
    return json.dumps(gdata)


# @app.route('/data2',methods=['get','POST'])
# def givedata2():
#     gaugedata=data.gaugedata()
#     gdata={'gaugedata':gaugedata}
#     print(json.dumps(gaugedata))
#     return json.dumps(gdata)
    # return render_template('index.html') 

if __name__=='__main__':
    app.run()
