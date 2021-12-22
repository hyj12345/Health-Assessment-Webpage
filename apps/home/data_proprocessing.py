#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
path='/Users/hanbujishenmebuhui/Desktop/21Fall/BIS634/final/'
data = pd.read_csv(path+'brfss_final.csv')
feat=['hlthpln1', 'htm4', 'marital', 'income2', 'sex',
       'X_ageg5yr', 'chccopd1', 'havarth3', 'addepev2', 'chckidny', 'diabete3',
       'blind', 'smokday2', 'toldhi2', 'cvdinfr4', 'cvdcrhd4', 'cvdstrk3',
       'asthma3', 'chcscncr', 'chcocncr', 'bphigh4', 'bloodcho', 'wtkg3',
       'strength', 'exerhmm', 'exact', 'X_drnkdy4', 'sleptim1','genhlth']
print(len(feat))
# data_age=data['X_ageg5yr']
# print(data_age)
#
# data_age.to_csv(path+'age.csv')
data_final=data[feat]
data_final2=data_final[data_final['genhlth'].notna()]
print(data_final)
data_final2.to_csv(path+'brfss_final.csv')
data_final=pd.read_csv(path+'brfss_final.csv')
print(data_final)

#####plot the label genhlth
print("result\n", pd.value_counts(data_final['genhlth']))
import matplotlib.pyplot as plt
import seaborn as sns
pd.options.display.notebook_repr_html=False
plt.rcParams['figure.dpi'] = 75
sns.set_theme(style='darkgrid')
hs = sns.histplot(x=data_final['genhlth'], kde=False,color="m")
hs.text('Very good', 159076, str(159076), fontsize=10)
hs.text('Poor',  27951, str( 27951), fontsize=10)
hs.text('Good', 150555, str(150555), fontsize=10)
hs.text('Fair', 66726, str(66726), fontsize=10)
hs.text('Excellent', 85482, str(85482), fontsize=10)
hs.set_title('Histogram of General Health (lables)')
plt.show()

##pearson
import scipy.stats as stats
print(len(data_final.columns))

def cal_pearson(data,p_value):
    data=data.dropna()
    significant_list=[]
    for i in range(len(data.columns)-1):
        try:
            result=stats.pearsonr(data[data.columns[i]],
                         data['genhlth'].factorize()[0])
        except TypeError:
            result = stats.pearsonr(data[data.columns[i]].factorize()[0],
                                data['genhlth'].factorize()[0])

        print('{} and genhlth pearson correlation coefficients and significant results are {}'.format(
    data.columns[i],result))
        if result[1]<p_value:
            significant_list.append((data.columns[i],result[0]))
    return significant_list

significant_list=cal_pearson(data=data_final,p_value=0.01)
significant_list.sort(key=lambda x:x[1],reverse=True)

pearson_list=[i[1] for i in significant_list]
#bubble plot
np.random.rand(123)
x=np.random.rand(len(significant_list))
y=np.random.rand(len(significant_list))
sns.set(style="white", font_scale=1.5)
plt.scatter(x,y,
            color=['red' if i>0 else 'orange' for i in pearson_list],
            alpha=0.5,
            s=[abs(i[1]*18000) for i in significant_list])
for i in range(len(x)):#round(pearson_list[i],4)
    plt.text(x[i]-0.02,y[i]+0.02,significant_list[i][0], fontsize=8)
plt.title('Scatter plot of significant correlation')

plt.show()

print(len(significant_list))
x=list(x)
y=list(y)
significant_list1=[i[1] for i in significant_list]
for i in range(len(x)):
    print("x:{},y:{},r:{},".format(x[i],y[i],significant_list1[i]*1000))

##Typical Persona
num_list=pd.DataFrame(data_final.describe()).columns
data_group=data_final.groupby('genhlth')
columns_list=data_final.columns[1:-1]

def groupby1(feat):
    colunms_=data_group[feat].value_counts().unstack().columns
    res=data_group[feat].value_counts().unstack().apply(lambda x: colunms_[list(x).index(max(list(x)))], axis=1)
    res=pd.DataFrame(res)
    res.columns=[feat]
    return res

a=groupby1('toldhi2')
b=groupby1('income2')

def groupby2(feat):
    res=data_group[feat].mean()
    res=pd.DataFrame(res)
    res.columns=[feat]
    return res


def groupby(data):
    gb_result = groupby1('hlthpln1')
    from pandas.core.groupby.groupby import DataError
    for i in columns_list[1:]:
        try:
            res=groupby2(i)
        except DataError:
            res=groupby1(i)
        gb_result=pd.merge(gb_result, res, left_index=True, right_index=True)
    return gb_result

gb_result=groupby(data_group)

#gb_result.to_csv(path+'gb_result.csv',index_label=False)




######Q2

#Yes,missing. Missing matrix
import missingno as msno
msno.matrix(data_final, figsize = (20, 20))
plt.show()
#References: https://blog.csdn.net/sanjianjixiang/article/details/104556177
def missing_values_table(df):
    mis_val = df.isnull().sum()
    mis_val_percent = 100 * df.isnull().sum() / len(df)
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
    mis_val_table_ren_columns = mis_val_table.rename(columns={0: 'Missing Values',1: '% of Total Values'})
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:, 1] != 0].sort_values('% of Total Values', ascending=False).round(1)

    print('Your selected dataframe has {} columns.\nThere are {} columns that have missing values.'.format(df.shape[1],
                                                                                                           mis_val_table_ren_columns.shape[                                                                                 0]))
    return mis_val_table_ren_columns
##missing table
missing_values_table(data_final)

### remove data where all variables values are null
data_final_1=data_final.iloc[:,:-1].dropna(how='all')#[489790 rows x 35 columns]

###the responses like 999 and 777 will use 0 instead
#weight2 7777 9999 0
data_final['weight2']=data_final['weight2'].replace(7777,0)
data_final['weight2']=data_final['weight2'].replace(9999,0)
#height3 7777 9999 0
data_final['height3']=data_final['height3'].replace(7777,0)
data_final['height3']=data_final['height3'].replace(9999,0)
#exeroft1 777 999 0
data_final['exeroft1']=data_final['exeroft1'].replace(777,0)
data_final['exeroft1']=data_final['exeroft1'].replace(999,0)
#exerhmm1 777 999 0
data_final['exerhmm1']=data_final['exerhmm1'].replace(777,0)
data_final['exerhmm1']=data_final['exerhmm1'].replace(999,0)
#exeroft2 777 999 0
data_final['exeroft2']=data_final['exeroft2'].replace(777,0)
data_final['exeroft2']=data_final['exeroft2'].replace(999,0)
#exerhmm2 777 999 0
data_final['exerhmm2']=data_final['exerhmm2'].replace(777,0)
data_final['exerhmm2']=data_final['exerhmm2'].replace(999,0)
#strength 777 999 888 0
data_final['strength']=data_final['strength'].replace(777,0)
data_final['strength']=data_final['strength'].replace(999,0)
data_final['strength']=data_final['strength'].replace(888,0)
#X_drnkdy4 9900 0
data_final['X_drnkdy4']=data_final['X_drnkdy4'].replace(9900,0)
#sleptim1 77 99 0
data_final['sleptim1']=data_final['sleptim1'].replace(77,0)
data_final['sleptim1']=data_final['sleptim1'].replace(99,0)

##weight2
weight_2=list()
for i in range(len(data_final['weight2'])):
    if data_final['weight2'][i] in range(50,1000):
        weight_2.append(round(data_final['weight2'][i]*0.45359237,0))
    else:
        weight_2.append(data_final['weight2'][i])
data_final['weight2']=weight_2

##height3
height_3=list()
for i in range(len(data_final['height3'])):
    if data_final['height3'][i] in range(9000 , 9999):
        height_3.append(round(data_final['height3'][i]*0.0254,0))
    else:
        height_3.append(data_final['height3'][i])
data_final['height3']=height_3

##exeroft2
exeroft_2=list()
for i in range(len(data_final['exeroft2'])):
    if data_final['exeroft2'][i] in range(101,200):
        exeroft_2.append(round(data_final['exeroft2'][i] /7,0))
    elif data_final['exeroft2'][i] in range(200,300):
        exeroft_2.append(round(data_final['exeroft2'][i] /30,0))
    else:
        exeroft_2.append(data_final['exeroft2'][i])
data_final['exeroft2']=exeroft_2

##exeroft1
exeroft_1=list()
for i in range(len(data_final['exeroft1'])):
    if data_final['exeroft1'][i] in range(101,200):
        exeroft_1.append(round(data_final['exeroft1'][i] /7,0))
    elif data_final['exeroft1'][i] in range(200,300):
        exeroft_1.append(round(data_final['exeroft1'][i] /30,0))
    else:
        exeroft_1.append(data_final['exeroft1'][i])

data_final['exeroft1']=exeroft_1

#data_final.to_csv(path+'brfss_final_clean.csv',index_label=False)

data_final_clean=pd.read_csv(path+'brfss_final_clean.csv')
print(data_final_clean['weight2'])


# import xmltodict
# with open(path+'Health/myhealthdata/export.xml', 'r') as xml_file:
#     input_data = xmltodict.parse(xml_file.read())
#
# with open(path+'Health/myhealthdata/export_cda.xml', 'r') as xml_file:
#     input_data_cda = xmltodict.parse(xml_file.read())
#
# records_list = input_data['HealthData']['Record']
#
# myhealthdata = pd.DataFrame(records_list)
#
# print(myhealthdata.columns)
#
# print(myhealthdata['@type'].unique())
#
# print(input_data_cda)
#
# records_list_cda = input_data_cda['HealthData']['Record']
#
# myhealthdata_cda = pd.DataFrame(records_list_cda)
#
# print(myhealthdata_cda.columns)
#
# print(myhealthdata_cda['@type'].unique())