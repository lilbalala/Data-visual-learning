import random
import numpy as np
import pandas as pd


class data():
    def zhudata(self,param):
        return np.random.randint(10*param,50*param,(1,7))[0].tolist()
    def mapdata(self):
        mapdata=[
            {'name': '北京', 'value': random.randint(100,12000)},
            {'name': '天津', 'value': random.randint(100,12000)},
            {'name': '上海', 'value': random.randint(100,12000)},
            {'name': '重庆', 'value': random.randint(100,12000)},
            {'name': '河北', 'value': random.randint(100,12000)},
            {'name': '河南', 'value': random.randint(100,12000)},
            {'name': '云南', 'value': random.randint(100,12000)},
            {'name': '辽宁', 'value': random.randint(100,12000)},
            {'name': '黑龙江', 'value': random.randint(100,12000)},
            {'name': '湖南', 'value': random.randint(100,12000)},
            {'name': '安徽', 'value': random.randint(100,12000)},
            {'name': '山东', 'value': random.randint(100,12000)},
            {'name': '新疆', 'value': random.randint(100,12000)},
            {'name': '江苏', 'value': random.randint(100,12000)},
            {'name': '浙江', 'value': random.randint(100,12000)},
            {'name': '江西', 'value': random.randint(100,12000)},
            {'name': '湖北', 'value': random.randint(100,12000)},
            {'name': '广西', 'value': random.randint(100,12000)},
            {'name': '甘肃', 'value': random.randint(100,12000)},
            {'name': '山西', 'value': random.randint(100,12000)},
            {'name': '内蒙古', 'value': random.randint(100,12000)},
            {'name': '陕西', 'value': random.randint(100,12000)},
            {'name': '吉林', 'value': random.randint(100,12000)},
            {'name': '福建', 'value': random.randint(100,12000)},
            {'name': '贵州', 'value': random.randint(100,12000)},
            {'name': '广东', 'value': random.randint(100,12000)},
            {'name': '青海', 'value': random.randint(100,12000)},
            {'name': '西藏', 'value': random.randint(100,12000)},
            {'name': '四川', 'value': random.randint(100,12000)},
            {'name': '宁夏', 'value': random.randint(100,12000)},
            {'name': '海南', 'value': random.randint(100,12000)},
            {'name': '台湾', 'value': random.randint(100,12000)},
            {'name': '香港', 'value': random.randint(100,12000)},
            {'name': '澳门', 'value': random.randint(100,12000)}
        ]
        return mapdata
    def sadata(self):
        sadata=[]
        for i in range(5):
            templist=[int(x) for x in list(np.random.randint(100,400,7))]
            sadata.append(templist)
        return sadata
    def gaugedata(self):
        gaugedata=random.randrange(10,100)
        return gaugedata
    def stdata(self):
        country=['Australia','Canada','China','Cuba','Finland','France','Germany','Iceland','India','Japan']
        year=[x for x in range(1990,2023)]
        y1=random.sample(year,1)[0]
        year.remove(y1)
        y2=random.sample(year,1)[0]
        list1=[[random.randrange(3000,35000),random.randrange(50,100),random.randrange(200000,1200000),x,y1] for x in country]
        list2 = [[random.randrange(3000, 35000), random.randrange(50, 100),random.randrange(300000,1400000), x, y2] for x in country]
        stdata=[list1,list2]
        return y1,y2,stdata
    def rddata(self):
        list1=np.random.randint(10,100,6).tolist()
        list2 = np.random.randint(10, 100, 6).tolist()
        rddata=[[int(x) for x in list1],[int(x) for x in list2]]
        return rddata
    def wdcd(self):
        wdcd_data=[
            {'value': random.randint(10,40), 'name': '智农通'},
            {'value': random.randint(10,40), 'name': 'OPPO'},
            {'value': random.randint(10,40), 'name': 'HONOR'},
            {'value': random.randint(10,40), 'name': '红米'},
            {'value': random.randint(10,40), 'name': '小米'},
            {'value': random.randint(10,40), 'name': '美图'},
            {'value': random.randint(10,40), 'name': 'ONEPLUS'},
            {'value': random.randint(10,40), 'name': '魅族'},
            {'value': random.randint(10,40), 'name': '红手指'},
            {'value': random.randint(10,40), 'name': 'SAMSUNG'},
            {'value': random.randint(10,40), 'name': '金立'},
            {'value': random.randint(10,40), 'name': 'BLACKBERRY'},
            {'value': random.randint(10,40), 'name': '诺基亚'},
            {'value': random.randint(10,40), 'name': '锤子'},
            {'value': random.randint(10,40), 'name': '大疆'},
            {'value': random.randint(10,40), 'name': '361'},
            {'value': random.randint(10,40), 'name': '摩托罗拉'},
            {'value': random.randint(10,40), 'name': '联想'},
            {'value': random.randint(10,40), 'name': '玩家国度'},
        ]
        return wdcd_data
    def hist(self):
        histdata=np.random.randint(1,50,size=(100,))[:,np.newaxis].tolist()
        return histdata
    def pscatter(self):
        parray=np.random.randint(1,10,size=(9,4))
        pdf=pd.DataFrame(parray,columns=['A','B','C','D'])
        pdf['category']=['a']*3+['b']*3+['c']*3
        pdict={'pdata':pdf.values.tolist(),'dlen':len(pdf.columns.tolist()),'col':pdf.columns.tolist(),'cat':pdf['category'].drop_duplicates().tolist()}
        return pdict
if __name__=='__main__':
    data=data()
    print(data.zhudata(10))