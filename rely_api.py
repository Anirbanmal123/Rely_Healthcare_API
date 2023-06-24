#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet


# In[2]:


df=pd.read_csv("C:/Users/bidyu/Desktop/Rely Healthcare Internship Work/rely_work.csv")
df.head()


# In[3]:


del df['Unnamed: 0']


# In[4]:


df.head()


# In[5]:


from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/Rely_API/<string:api_name>/<string:attribute>/<string:factor>/<string:thing>/<int:y>/<int:n>/<int:itemid>/<int:cateid>')
def rely(api_name,attribute,factor,thing,y,n,itemid,cateid):
    if(api_name=='MonthlyReportByYear'):
            xd=df[df[factor]==thing]
            xd=xd[['SaleDate',attribute]]
            m = Prophet()
            xd.columns=['ds','y']
            if(xd.shape[0]>2):
                model=m.fit(xd)
                future=m.make_future_dataframe(periods=4000,freq='D')
                forecast = m.predict(future)
                forecast
                f=forecast
                f['Year'] = f['ds'].dt.year
                f['Month'] = f['ds'].dt.month
                new = f[f['Year']==y]
        
                jan = new[new['Month']==1]
                month1 = jan['yhat'].sum()
                month1 = round(month1,2)
                month1
        
                feb = new[new['Month']==2]
                month2 = feb['yhat'].sum()
                month2 = round(month2,2)
                month2
        
                mar = new[new['Month']==3]
                month3 = mar['yhat'].sum()
                month3 = round(month3,2)
                month3
        
                apr = new[new['Month']==4]
                month4 = apr['yhat'].sum()
                month4 = round(month4,2)
                month4
        
                may = new[new['Month']==5]
                month5 = may['yhat'].sum()
                month5 = round(month5,2)
                month5
        
                jun = new[new['Month']==6]
                month6 = jun['yhat'].sum()
                month6 = round(month6,2)
                month6
        
                jul = new[new['Month']==7]
                month7 = jul['yhat'].sum()
                month7 = round(month7,2)
                month7
        
                aug = new[new['Month']==8]
                month8 = aug['yhat'].sum()
                month8 = round(month8,2)
                month8
        
                sep = new[new['Month']==9]
                month9 = sep['yhat'].sum()
                month9 = round(month9,2)
                month9
        
                oct = new[new['Month']==10]
                month10 = oct['yhat'].sum()
                month10 = round(month10,2)
                month10
        
                nov = new[new['Month']==11]
                month11 = nov['yhat'].sum()
                month11 = round(month11,2)
                month11
        
                dec = new[new['Month']==12]
                month12 = dec['yhat'].sum()
                month12 = round(month12,2)
                month12
        
                month=['January','February','March','April','May','June','July','August','September',
                    'October','November','December']
                value=[month1,month2,month3,month4,month5,month6,month7,month8,month9,month10,month11,month12]
                result=[]
        
                final_dict={}
                for i in range(len(month)):
                    final_dict['Month']=month[i]
                    final_dict['Value']=value[i]
                    result.append(final_dict)
                    final_dict={}
            
                return(result)
    
    
    elif(api_name=='MonthlyReportByYearForItem'):
            xd=df[df[factor]==thing]
            xd=xd[xd['ItemCode']==itemid]
            xd=xd[['SaleDate',attribute]]
            m = Prophet()
            xd.columns=['ds','y']
            if(xd.shape[0]>2):
                model=m.fit(xd)
                future=m.make_future_dataframe(periods=3650,freq='D')
                forecast = m.predict(future)
                forecast
                f=forecast
                f['Year'] = f['ds'].dt.year
                f['Month'] = f['ds'].dt.month
                new = f[f['Year']==y]

                jan = new[new['Month']==1]
                month1 = jan['yhat'].sum()
                month1 = round(month1,2)
                month1

                feb = new[new['Month']==2]
                month2 = feb['yhat'].sum()
                month2 = round(month2,2)
                month2

                mar = new[new['Month']==3]
                month3 = mar['yhat'].sum()
                month3 = round(month3,2)
                month3

                apr = new[new['Month']==4]
                month4 = apr['yhat'].sum()
                month4 = round(month4,2)
                month4

                may = new[new['Month']==5]
                month5 = may['yhat'].sum()
                month5 = round(month5,2)
                month5

                jun = new[new['Month']==6]
                month6 = jun['yhat'].sum()
                month6 = round(month6,2)
                month6

                jul = new[new['Month']==7]
                month7 = jul['yhat'].sum()
                month7 = round(month7,2)
                month7

                aug = new[new['Month']==8]
                month8 = aug['yhat'].sum()
                month8 = round(month8,2)
                month8

                sep = new[new['Month']==9]
                month9 = sep['yhat'].sum()
                month9 = round(month9,2)
                month9

                oct = new[new['Month']==10]
                month10 = oct['yhat'].sum()
                month10 = round(month10,2)
                month10

                nov = new[new['Month']==11]
                month11 = nov['yhat'].sum()
                month11 = round(month11,2)
                month11

                dec = new[new['Month']==12]
                month12 = dec['yhat'].sum()
                month12 = round(month12,2)
                month12

                month=['January','February','March','April','May','June','July','August','September','October','November','December']
                value=[month1,month2,month3,month4,month5,month6,month7,month8,month9,month10,month11,month12]
                result=[]

                final_dict={}
                for i in range(len(month)):
                    final_dict['Month']=month[i]
                    final_dict['Value']=value[i]
                    result.append(final_dict)
                    final_dict={}

                return(result)
        
        
        
    elif(api_name=='MonthlyReportByYearForCategory'):
            xd=df[df[factor]==thing]
            xd=xd[xd['CatID']==cateid]
            xd=xd[['SaleDate',attribute]]
            m = Prophet()
            xd.columns=['ds','y']
            if(xd.shape[0]>2):
                model=m.fit(xd)
                future=m.make_future_dataframe(periods=3650,freq='D')
                forecast = m.predict(future)
                forecast
                f=forecast
                f['Year'] = f['ds'].dt.year
                f['Month'] = f['ds'].dt.month
                new = f[f['Year']==y]

                jan = new[new['Month']==1]
                month1 = jan['yhat'].sum()
                month1 = round(month1,2)
                month1

                feb = new[new['Month']==2]
                month2 = feb['yhat'].sum()
                month2 = round(month2,2)
                month2

                mar = new[new['Month']==3]
                month3 = mar['yhat'].sum()
                month3 = round(month3,2)
                month3

                apr = new[new['Month']==4]
                month4 = apr['yhat'].sum()
                month4 = round(month4,2)
                month4

                may = new[new['Month']==5]
                month5 = may['yhat'].sum()
                month5 = round(month5,2)
                month5

                jun = new[new['Month']==6]
                month6 = jun['yhat'].sum()
                month6 = round(month6,2)
                month6

                jul = new[new['Month']==7]
                month7 = jul['yhat'].sum()
                month7 = round(month7,2)
                month7

                aug = new[new['Month']==8]
                month8 = aug['yhat'].sum()
                month8 = round(month8,2)
                month8

                sep = new[new['Month']==9]
                month9 = sep['yhat'].sum()
                month9 = round(month9,2)
                month9

                oct = new[new['Month']==10]
                month10 = oct['yhat'].sum()
                month10 = round(month10,2)
                month10

                nov = new[new['Month']==11]
                month11 = nov['yhat'].sum()
                month11 = round(month11,2)
                month11

                dec = new[new['Month']==12]
                month12 = dec['yhat'].sum()
                month12 = round(month12,2)
                month12

                month=['January','February','March','April','May','June','July','August','September','October','November','December']
                value=[month1,month2,month3,month4,month5,month6,month7,month8,month9,month10,month11,month12]
                result=[]

                final_dict={}
                for i in range(len(month)):
                    final_dict['Month']=month[i]
                    final_dict['Value']=value[i]
                    result.append(final_dict)
                    final_dict={}

                return(result)
        
        
    elif(api_name=='TopItemsByPlaces'):
        collection = df['Item'].unique()
        name=[]
        value=[]
        result=[]
        xd=df[df[factor]==thing]
        for i in collection :
            sb=xd[xd['Item']==i]
            sb=sb[['SaleDate',attribute]]
            m = Prophet()
            sb.columns=['ds','y']
            if(sb.shape[0]>2):
                model=m.fit(sb)
                future=m.make_future_dataframe(periods=3650,freq='D')
                forecast = m.predict(future)
                f=forecast
                f['Year'] = f['ds'].dt.year
                new = f[f['Year']==y]
                z=new['yhat'].sum()
                z = round(z,2)
                name.append(i)
                value.append(z)

        a,b = zip(*sorted(zip(value,name),reverse=True))
        final_dict={}
        for i in range(len(name)):
            final_dict['Item']=b[i]
            final_dict['Value']=a[i]
            result.append(final_dict)
            final_dict={}   
        k=result[0:n]
        return(k)
        
        
    elif(api_name=='TopPlacesByItems'):
        collection = df['Place'].unique()
        name=[]
        value=[]
        result=[]
        xd=df[df['ItemCode']==itemid]
        for i in collection :
            sb=xd[xd['Place']==i]
            sb=sb[['SaleDate',attribute]]
            m = Prophet()
            sb.columns=['ds','y']
            if(sb.shape[0]>2):
                model=m.fit(sb)
                future=m.make_future_dataframe(periods=3650,freq='D')
                forecast = m.predict(future)
                f=forecast
                f['Year'] = f['ds'].dt.year
                new = f[f['Year']==y]
                z=new['yhat'].sum()
                z = round(z,2)
                name.append(i)
                value.append(z)

        a,b = zip(*sorted(zip(value,name),reverse=True))
        final_dict={}
        for i in range(len(name)):
            final_dict['Place']=b[i]
            final_dict['Value']=a[i]
            result.append(final_dict)
            final_dict={}
        k=result[0:n]
        return(k)
    
if __name__=="__main__":
    app.run(debug=True)


# In[ ]:





# In[ ]:




