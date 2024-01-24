import json

from flask import Flask,render_template,request,jsonify

from dataclass import data

app=Flask(__name__)


data=data()
@app.route('/',methods=['get','post'])
def index():
    global int_param
    if request.method=='POST':
        int_param=int(request.form.get('name'))
    else:
        int_param=10
    return render_template('index.html',int_param=int_param)

@app.route('/index',methods=['get','post'])
def iframepage():
    return render_template('iframehtml.html')

@app.route('/test')
def test():
    return  render_template('test.html')

@app.route('/data')
def givedata():
    zhudata=data.zhudata(int_param)
    mapdata=data.mapdata()
    sadata=data.sadata()
    gaugedata=data.gaugedata()
    stdata=data.stdata()
    rddata=data.rddata()
    wdcd_data=data.wdcd()
    histdata=data.hist()
    pdata=data.pscatter()
    gdata={'zhudata':zhudata,
           'mapdata':mapdata,
           'sadata':sadata,
           'gaugedata':gaugedata,
           'stdata':stdata,
           'rddata':rddata,
           'wdcd':wdcd_data,
           'histdata':histdata,
           'pdata':pdata}
    return json.dumps(gdata)



if __name__=='__main__':
    app.run()
