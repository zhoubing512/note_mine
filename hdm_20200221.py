# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:17:27 2020

@author: zhoubing
"""

##有观看记录的模型拟合以及预测
c_name = [ 'onnet_month', 'sex', 'main_prc_outfee',
       'avg_3mon_arpu', 'avg_3mon_main_prc_infee', 'avg_3mon_main_prc_outfee',
       'over_voc_fee', 'over_gprs_fee', 'avg_3mon_over_voc_fee',
       'avg_3mon_over_gprs_fee', 'mon_dur', 'online_days', 'day_avg_dur',
        'shifoukuandai', 'shifouyingxiao',
       'call_times_gprs_means', 'call_times_gprs_std', 'call_times_gprs_dif',
       'call_times_gprs_dif_std', 'call_times_gprs_trend',
       'call_duration_gprs_means', 'call_duration_gprs_std',
       'call_duration_gprs_dif', 'call_duration_gprs_dif_std',
       'call_duration_gprs_trend', 'call_times_voc_means',
       'call_times_voc_std', 'call_times_voc_dif', 'call_times_voc_dif_std',
       'call_times_voc_trend', 'call_duration_voc_means',
       'call_duration_voc_std', 'call_duration_voc_dif',
       'call_duration_voc_dif_std', 'call_duration_voc_trend', 'flow_means',
       'flow_std', 'flow_day_dif', 'flow_day_dif_std', 'flow_trend',
       'mon_search_times', 'six_no', 'pay_no', 'tv_pay', 'pay_time',
       'demand_time', 'demand_no', 'back_time', 'back_no', 'watch_times_means',
       'watch_times_std', 'watch_times_day_dif', 'watch_times_day_dif_std',
       'watch_times_trend',  'month_07_day_minute',
       'month_08_day_minute', 'month_09_day_minute', 'month_10_day_minute',
       'month_11_day_minute', 'month_12_day_minute', 'dm_label']

c_name = [ 'onnet_month', 'sex', 'main_prc_outfee',
       'avg_3mon_arpu', 'avg_3mon_main_prc_infee', 'avg_3mon_main_prc_outfee',
       'over_voc_fee', 'over_gprs_fee', 'avg_3mon_over_voc_fee',
       'avg_3mon_over_gprs_fee', 'mon_dur', 'online_days', 'day_avg_dur',
        'shifoukuandai', 'shifouyingxiao',
       'call_times_gprs_means', 'call_times_gprs_std', 'call_times_gprs_dif',
       'call_times_gprs_dif_std', 'call_times_gprs_trend',
       'call_duration_gprs_means', 'call_duration_gprs_std',
       'call_duration_gprs_dif', 'call_duration_gprs_dif_std',
       'call_duration_gprs_trend', 'call_times_voc_means',
       'call_times_voc_std', 'call_times_voc_dif', 'call_times_voc_dif_std',
       'call_times_voc_trend', 'call_duration_voc_means',
       'call_duration_voc_std', 'call_duration_voc_dif',
       'call_duration_voc_dif_std', 'call_duration_voc_trend', 'flow_means',
       'flow_std', 'flow_day_dif', 'flow_day_dif_std', 'flow_trend', 'month_07_day_minute',
       'month_08_day_minute', 'month_09_day_minute', 'month_10_day_minute',
       'month_11_day_minute', 'month_12_day_minute', 'dm_label']


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegressionCV,LinearRegression
from sklearn.metrics import roc_auc_score,roc_curve,precision_recall_curve

##读取数据 数据清洗处理
data = pd.read_table('C:\\Users\\zhoubing\\Desktop\\dm20200221数据\\zb_dm_train_20200221.txt',sep=',')
data0 = data.drop(['phone_no','open_date','key_phone_no','watch'],axis=1)
columns_name = data0.columns
len(columns_name)
data0 = data0.replace('\\N',np.NaN)
data0 = data0[data0['onnet_month'].notnull()]
data0 = data0[columns_name].astype(np.float64)
data0.loc[data0['onnet_month'] >= 20,'onnet_month'] = np.NaN
data1 = data0.fillna(data0.mean())
data1 = data0.fillna(0)
data1['dm_label'] = data1['dm_label'].astype(np.int)
len(data0[data0['onnet_month']>=20])
#检查空值
s = {}
for i in c_name:
    s[i] = data1[i].isnull().value_counts()
 
1：
x = data1[c_name[0:60]]
y = data1[c_name[60]]

2：
x = data1[c_name[0:21]]
y = data1[c_name[21]]

X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.3,random_state=0)

##重采样
from imblearn.over_sampling import SMOTE, ADASYN
from collections import Counter
X_train, Y_train = SMOTE().fit_sample(X_train, Y_train)

sorted(Counter(Y_train).items())

X_train, Y_train = ADASYN().fit_sample(X_train, Y_train)

sorted(Counter(Y_train).items())


#标准化
ss = StandardScaler()
X_train = ss.fit_transform(X_train)


##逻辑回归
from sklearn.utils import class_weight
class_weights = class_weight.compute_class_weight('balanced',np.unique(Y_train),Y_train)
lr = LogisticRegressionCV(class_weight = 'balanced', multi_class="ovr",fit_intercept=True,Cs=np.logspace(-2,2,20),cv=2,penalty="l2",solver="sag",tol=0.01)

re_model = lr.fit(X_train,Y_train)
r = re_model.score(X_train,Y_train)
print("R值(准确率):",r)
print("参数:",re_model.coef_)
print("截距:",re_model.intercept_)
print("稀疏化特征比率:%.2f%%" %(np.mean(lr.coef_.ravel()==0)*100))
print("=========sigmoid函数转化的值，即：概率p=========")
print(re_model.predict_proba(X_test))

##训练集
Y_train_predict = lr.predict(X_train)
Y_train_pre=lr.predict_proba(X_train)
Y_0 = np.array(Y_train_pre[:,1])

from sklearn import metrics
print('AUC: %.4f' % metrics.roc_auc_score(Y_train,Y_0))
print('ACC: %.4f' % metrics.accuracy_score(Y_train,Y_train_predict))
print('Recall: %.4f' % metrics.recall_score(Y_train,Y_train_predict))#查全率
print('F1-score: %.4f' %metrics.f1_score(Y_train,Y_train_predict))
print('Precesion: %.4f' %metrics.precision_score(Y_train,Y_train_predict))#查准率 
metrics.confusion_matrix(Y_train,Y_train_predict)

#预测
X_test = ss.fit_transform(X_test)       #数据标准化
Y_predict = lr.predict(X_test)      #预测
y_pre=lr.predict_proba(X_test)
y_0=np.array(y_pre[:,1])    #取第二列数据，因为第二列概率为趋于0时分类类别为0，概率趋于1时分类类别为1

from sklearn import metrics
print('AUC: %.4f' % metrics.roc_auc_score(Y_test,y_0))
print('ACC: %.4f' % metrics.accuracy_score(Y_test,Y_predict))
print('Recall: %.4f' % metrics.recall_score(Y_test,Y_predict))#查全率
print('F1-score: %.4f' %metrics.f1_score(Y_test,Y_predict))
print('Precesion: %.4f' %metrics.precision_score(Y_test,Y_predict))#查准率 
metrics.confusion_matrix(Y_test,Y_predict)



##Adaboost

from sklearn.ensemble import AdaBoostClassifier
AB = AdaBoostClassifier(n_estimators=1000)
AB.fit(X_train,Y_train)
predict_results=AB.predict(X_test)
print(metrics.accuracy_score(predict_results, Y_test))
conf_mat = metrics.confusion_matrix(Y_test, predict_results)
print(conf_mat)
print(metrics.classification_report(Y_test, predict_results))



##xgboost
#4. Xgboost建模
#4.1 模型初始化设置

import xgboost as xgb
dtrain=xgb.DMatrix(X_train,label=Y_train)
dtest=xgb.DMatrix(X_test)

params={'booster':'gbtree',
    'objective': 'binary:logistic',
    'eval_metric': 'auc',
    'max_depth':6,
    'lambda':10,
    'subsample':0.75,
    'colsample_bytree':0.75,
    'min_child_weight':2,
    'eta': 0.025,
    'seed':0,
    'nthread':8,
     'silent':1}

watchlist = [(dtrain,'train')]

#4.2 建模与预测

bst=xgb.train(params,dtrain,num_boost_round=200,evals=watchlist)

ypred=bst.predict(dtest)

# 设置阈值, 输出一些评价指标
y_pred = (ypred >= 0.5)*1

from sklearn import metrics
print('AUC: %.4f' % metrics.roc_auc_score(Y_test,ypred))
print('ACC: %.4f' % metrics.accuracy_score(Y_test,y_pred))
print('Recall: %.4f' % metrics.recall_score(Y_test,y_pred))
print('F1-score: %.4f' %metrics.f1_score(Y_test,y_pred))
print('Precesion: %.4f' %metrics.precision_score(Y_test,y_pred))
metrics.confusion_matrix(Y_test,y_pred)

# 显示重要特征
from xgboost import plot_importance
from matplotlib import pyplot as plt
plot_importance(bst)
plt.show()

#4.3.1 得分
#默认的输出就是得分, 这没什么好说的, 直接上code.
ypred = bst.predict(dtest)
ypred

ypred_leaf = bst.predict(dtest, pred_leaf=True)
ypred_leaf

#可视化第一棵树的生成情况
xgb.to_graphviz(bst, num_trees=0)



