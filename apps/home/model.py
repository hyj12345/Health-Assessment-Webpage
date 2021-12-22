#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
path='/Users/hanbujishenmebuhui/Desktop/21Fall/BIS634/final/'
dataset_ = pd.read_csv(path+'brfss_final.csv')
z=dataset_['X_ageg5yr']

dataset=dataset_
for i in range(2,dataset.shape[1]):
    if not isinstance(dataset[dataset.columns[i]][0], (float,int)):
        dataset[dataset.columns[i]] = dataset[dataset.columns[i]].factorize()[0]

data=dataset.iloc[:,2:]
for i in range(1000):
    print(i,z[i],data['X_ageg5yr'][i])

data['X_ageg5yr'][966]
#Age 55 to 59 0
#Age 60 to 64 1
#Age 50 to 54 2
#Age 65 to 69 3
#Age 45 to 49 4
#Age 35 to 39 5
#Age 40 to 44 6
#Age 70 to 74 7
#Age 30 to 34 8
#Age 75 to 79 9
#Age 25 to 29 10
#Age 18 to 24 11
#Age 80 or older 12
#966Age 80 or older  966
#960 Age 40 to 44
from xgboost.sklearn import XGBClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer
from sklearn.metrics import roc_auc_score,roc_curve
from sklearn.model_selection import train_test_split


data_train_x,data_test_x,y_train,y_test = train_test_split(
    data.drop(['genhlth'],axis=1),data['genhlth'],random_state=42,train_size=0.7)

def eval_auc(y_true, y_pred):
    return roc_auc_score(y_true, y_pred)

def eval_ks(y_true, y_pred):
    fpr, tpr, thresh = roc_curve(y_true, y_pred)
    ks = round(np.max(abs(tpr - fpr)) * 100, 2)
    return ks

KS_score = make_scorer(eval_ks, greater_is_better=True, needs_proba=True)
AUC_score = make_scorer(eval_auc, greater_is_better=True, needs_proba=True)
scoring = {'AUC': AUC_score, 'KS': KS_score}



def xgb_model(train_x,train_y,test_x,test_y):
    param_test = {

        # 'max_depth': [3,4,5],  #
        #     'learning_rate': [0.1,0.2],#
            # 'reg_lambda': [0,20],#0
        'n_estimators' : [20,50,100]#
        }
    grid = GridSearchCV(estimator=XGBClassifier(
            min_child_weight=1,
        max_depth=4,
        learning_rate=0.1,
            gamma=0,
            reg_lambda=20,
            verbosity=1,
            colsample_bytree=1,
        objective='multi:softprob',
            subsample=1,use_label_encoder=False,
            seed=27),
            param_grid=param_test, cv=5,
             verbose=True)
    grid.fit(train_x, train_y)
    XGBM=grid.best_estimator_
    print('*' * 25, 'Xgboost', '*' * 25)
    print("INFO:best_params_:",grid.best_estimator_)
    print("INFO:best_score_:",grid.best_score_)

    # y_pred_train = XGBM.predict_proba(train_x)
    # ar = np.array(y_pred_train)
    # predictions_train = ar[:,1]
    # auc_train = roc_auc_score(train_y, predictions_train)
    # ks_value_train = eval_ks(train_y, predictions_train)
    # print('auc_train', auc_train)
    # print('ks_value_train', ks_value_train)
    #
    # y_pred_test = XGBM.predict_proba(test_x)
    # ar3 = np.array(y_pred_test)
    # predictions_test = ar3[:,1]
    # auc_test = roc_auc_score(test_y, predictions_test)
    # ks_value_test = eval_ks(test_y, predictions_test)
    # print('auc_test', auc_test)
    # print('ks_value_test', ks_value_test)

    return  XGBM


xgb_model=xgb_model(data_train_x,y_train,data_test_x,y_test)
from sklearn.metrics import roc_auc_score
y_pred_test=xgb_model.predict_proba(data_test_x)
roc_auc_score(y_test, y_pred_test,average='macro',multi_class='ovo')

y_pred_train=xgb_model.predict_proba(data_train_x)
roc_auc_score(y_train, y_pred_train,average='macro',multi_class='ovo')


pickle.dump(xgb_model, open(path+'model.pkl','wb'))
# dataset.iloc[1,1:-1]
model = pickle.load(open(path+'model.pkl','rb'))
# print(model.predict(dataset.iloc[:,1:-1]))

feat=['hlthpln1', 'htm4', 'marital', 'income2', 'sex',
       'X_ageg5yr', 'chccopd1', 'havarth3', 'addepev2', 'chckidny', 'diabete3',
       'blind', 'smokday2', 'toldhi2', 'cvdinfr4', 'cvdcrhd4', 'cvdstrk3',
       'asthma3', 'chcscncr', 'chcocncr', 'bphigh4', 'bloodcho', 'wtkg3',
       'strength', 'exerhmm', 'exact', 'X_drnkdy4', 'sleptim1']
ID=49
d=dataset[dataset.ID==ID]
wtkg3=60
strength=0
exerhmm=100
exact=1
sleptim1=12
hlthpln1=d['hlthpln1'][ID]
htm4=d['htm4'][ID]
marital=d[ 'marital'][ID]
income2=d['income2'][ID]
sex=d['sex'][ID]
X_ageg5yr=d['X_ageg5yr'][ID]
chccopd1=d['chccopd1'][ID]
havarth3=d['havarth3'][ID]
addepev2=d['addepev2'][ID]
chckidny=d['chckidny'][ID]
diabete3=d['diabete3'][ID]
blind=d['blind'][ID]
smokday2=d['smokday2'][ID]
toldhi2=d['toldhi2'][ID]
cvdinfr4=d['cvdinfr4'][ID]
cvdcrhd4=d['cvdcrhd4'][ID]
cvdstrk3=d['cvdstrk3'][ID]
asthma3=d['asthma3'][ID]
chcscncr=d['chcscncr'][ID]
chcocncr=d['chcocncr'][ID]
bphigh4=d['bphigh4'][ID]
bloodcho=d['bloodcho'][ID]
X_drnkdy4=d['X_drnkdy4'][ID]


int_features=[hlthpln1, htm4, marital, income2, sex,
       X_ageg5yr, chccopd1, havarth3, addepev2, chckidny, diabete3,
       blind, smokday2, toldhi2, cvdinfr4, cvdcrhd4, cvdstrk3,
       asthma3, chcscncr, chcocncr, bphigh4, bloodcho, wtkg3*100,
       strength, exerhmm, exact, X_drnkdy4, sleptim1]
final_features = [np.array(int_features)]
print(model.predict(pd.DataFrame(final_features)))

import matplotlib.pyplot as plt
import seaborn as sns
importance=[]
for i in range(data_train_x.shape[1]):
    importance.append([data_train_x.columns[i],model.feature_importances_[i]])
importance.sort(key=lambda x:x[1],reverse=True)
#importance[:10]
sns.set(style="white", font_scale=1.5)
plt.bar([i[0] for i in importance[:10]],[i[1] for i in importance[:10]],color='m')
plt.xticks(rotation=10)
plt.tick_params(labelsize=8)
plt.title('Top 10 of feature importance')
plt.show()

from sklearn.metrics import confusion_matrix
y_pre_label=model.predict(data_test_x)
cmatrix=confusion_matrix(y_test, y_pre_label)
print(cmatrix)

#Good 0
#Fair 1
#Very good 2
#Excellent 3
#poor 4

d=dataset[dataset.ID!=ID]
d_kmeans=d.iloc[:,2:30]
d_add=pd.DataFrame(final_features)
d_add.columns=d_kmeans.columns
d_kmeans=pd.concat([d_kmeans,d_add]).reset_index(drop=True)


from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=5)   #n_clusters:number of cluster

kmeans.fit(d_kmeans.fillna(0))
print(kmeans.labels_)

d_kmeans['K_label']=kmeans.labels_
data_k=d_kmeans[d_kmeans.K_label==d_kmeans.iloc[-1,:].K_label]
groups=data_k.shape[0]
groups_ratio=round(100*groups/(d_kmeans.shape[0]),2)

s_sleep=round(np.mean(data_k['sleptim1']),1)

s_exerhmm=round(np.mean(data_k['exerhmm']),1)

s_strength=round(np.mean(data_k['strength']),1)

feat_d=['chccopd1','havarth3','addepev2','chckidny','diabete3','blind','toldhi2','cvdinfr4',
        'cvdcrhd4','cvdstrk3','asthma3','chcscncr','chcocncr','bphigh4']
#chccopd1 1有 havarth3 addepev2 0有 chckidny 1有 diabete3 1有 blind toldhi2  cvdinfr4 1有 cvdstrk3 1有
#asthma3  chcscncr chcocncr  bphigh4 1有

disease=data_k[feat_d]
for i in range(disease.shape[1]):
    if disease.columns[i] in ['havarth3','addepev2']:
        disease[disease.columns[i]]=np.ones(disease.shape[0])-disease[disease.columns[i]]

s_disease=round(np.mean(np.sum(disease,axis=1)),0)


s_BMI=round(np.mean(100*data_k['wtkg3']/data_k['htm4']**2),1)
# s_Number_of_diseases=

# s_BMI

best=dataset[dataset.genhlth==3]
b_sleep=round(np.mean(best['sleptim1']),1)

b_exerhmm=round(np.mean(best['exerhmm']),1)

b_strength=round(np.mean(best['strength']),1)



disease_b=best[feat_d]
for i in range(disease_b.shape[1]):
    if disease_b.columns[i] in ['havarth3','addepev2']:
        disease_b[disease_b.columns[i]]=np.ones(disease_b.shape[0])-disease_b[disease_b.columns[i]]


b_disease=round(np.mean(np.sum(disease_b,axis=1)),0)

b_BMI=round(np.mean(100*best['wtkg3']/best['htm4']**2),1)