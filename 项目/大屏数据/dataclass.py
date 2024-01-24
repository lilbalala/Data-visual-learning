import random
import numpy as np
import pandas as pd
data=pd.read_csv('../data.csv')

class setdata():
    def __init__(self,data):
        self.data=data
    def t_y_m_mount(self):
        t_y_m_mount = self.data.groupby(['t_year', 't_month'])['buy_mount'].sum()
        t_y_m_mount_x=[str(x) for x in t_y_m_mount.index.tolist()]
        t_y_m_mount_y=t_y_m_mount.tolist()
        return t_y_m_mount_x,t_y_m_mount_y
    def category_1_mount(self):
        category_1_mount = self.data.groupby('category_1')['buy_mount'].sum()
        category_1_mount = [{'name':str(x[0]),'value':x[1]} for x in zip(category_1_mount.index.tolist(), category_1_mount.tolist())]
        return category_1_mount
    def category_2_mount(self):
        category_2_mount = self.data['category_2'].value_counts()
        category_2_mount = [{'name':x[0],'value':x[1]} for x in zip(category_2_mount.index.tolist(), category_2_mount.tolist())]
        return category_2_mount
    def category(self):
        category = self.data[['category_1', 'category_2', 'buy_mount']]
        category1_count = category[['category_1', 'category_2']].drop_duplicates()['category_1'].value_counts()
        category1_count_x=[str(x) for x in category1_count.index.tolist()]
        category1_count_y=category1_count.tolist()
        return category1_count_x,category1_count_y
    def category_1_2(self):
        category = self.data[['category_1', 'category_2', 'buy_mount']]
        category_1_2 = category.pivot_table('buy_mount', columns='category_1', index='category_2', aggfunc='sum')
        data_28 = category_1_2.sort_values(by=28, ascending=False)[28][:5]
        data_38 = category_1_2.sort_values(by=38, ascending=False)[38][:5]
        data_50008168 = category_1_2.sort_values(by=50008168, ascending=False)[50008168][:5]
        data_50014815 = category_1_2.sort_values(by=50014815, ascending=False)[50014815][:5]
        data_50022520 = category_1_2.sort_values(by=50022520, ascending=False)[50022520][:5]
        data_122650008 = category_1_2.sort_values(by=122650008, ascending=False)[122650008][:5]
        data_28=[{'name':z[0],'value':z[1]} for z in zip(data_28.index.tolist(),data_28.tolist())]
        data_38=[{'name':z[0],'value':z[1]} for z in zip(data_38.index.tolist(),data_38.tolist())]
        data_50008168=[{'name':z[0],'value':z[1]} for z in zip(data_50008168.index.tolist(),data_50008168.tolist())]
        data_50014815=[{'name':z[0],'value':z[1]} for z in zip(data_50014815.index.tolist(),data_50014815.tolist())]
        data_50022520=[{'name':z[0],'value':z[1]} for z in zip(data_50022520.index.tolist(),data_50022520.tolist())]
        data_122650008=[{'name':z[0],'value':z[1]} for z in zip(data_122650008.index.tolist(),data_122650008.tolist())]
        return data_28,data_38,data_50008168,data_50014815,data_50022520,data_122650008
    def gender_c1(self):
        data_gender = self.data[self.data['gender'].notnull()]
        gender_c1=data_gender.pivot_table('buy_mount','category_1','gender','sum')
        gender_c1_28=gender_c1.loc[28,:].tolist()
        gender_c1_38 = gender_c1.loc[38, :].tolist()
        gender_c1_50008168 = gender_c1.loc[50008168, :].tolist()
        gender_c1_50014815 = gender_c1.loc[50014815, :].tolist()
        gender_c1_50022520 = gender_c1.loc[50022520, :].tolist()
        gender_c1_122650008 = gender_c1.loc[122650008, :].tolist()
        return gender_c1_28,gender_c1_38,gender_c1_50008168,gender_c1_50014815,gender_c1_50022520,gender_c1_122650008

if __name__=='__main__':
    data=setdata(data)
    print(data.category_2_mount())
