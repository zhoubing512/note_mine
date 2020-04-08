# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:34:13 2020

@author: ShiningLu
"""
c_name1 = ['flow_11_1', 'flow_11_2', 'flow_11_3', 'flow_11_4', 'times_11_1',
       'times_11_2', 'times_11_3', 'times_11_4', 'time_duration_11_1',
       'time_duration_11_2', 'time_duration_11_3', 'time_duration_11_4']
c_name2 = ['flow_12_1', 'flow_12_2', 'flow_12_3', 'flow_12_4', 'times_12_1',
       'times_12_2', 'times_12_3', 'times_12_4', 'time_duration_12_1',
       'time_duration_12_2', 'time_duration_12_3', 'time_duration_12_4']
#有观看记录的
c_name = [ 'call_times_gprs_means', 'call_times_gprs_std', 'call_times_gprs_dif',
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
       'month_11_day_minute', 'month_12_day_minute']
#无观看记录的
c_name = [ 'call_times_gprs_means', 'call_times_gprs_std', 'call_times_gprs_dif',
       'call_times_gprs_dif_std', 'call_times_gprs_trend',
       'call_duration_gprs_means', 'call_duration_gprs_std',
       'call_duration_gprs_dif', 'call_duration_gprs_dif_std',
       'call_duration_gprs_trend', 'call_times_voc_means',
       'call_times_voc_std', 'call_times_voc_dif', 'call_times_voc_dif_std',
       'call_times_voc_trend', 'call_duration_voc_means',
       'call_duration_voc_std', 'call_duration_voc_dif',
       'call_duration_voc_dif_std', 'call_duration_voc_trend', 'flow_means',
       'flow_std', 'flow_day_dif', 'flow_day_dif_std', 'flow_trend',
       'month_07_day_minute',
       'month_08_day_minute', 'month_09_day_minute', 'month_10_day_minute',
       'month_11_day_minute', 'month_12_day_minute']
c_name_week_data = ['month_07_wm_times', 'month_08_wm_times',
       'month_09_wm_times', 'month_10_wm_times', 'month_11_wm_times',
       'month_12_wm_times', 'month_07_wm_time_duration',
       'month_08_wm_time_duration', 'month_09_wm_time_duration',
       'month_10_wm_time_duration', 'month_11_wm_time_duration',
       'month_12_wm_time_duration', 'month_07_dm_times', 'month_08_dm_times',
       'month_09_dm_times', 'month_10_dm_times', 'month_11_dm_times',
       'month_12_dm_times', 'month_07_dm_time_duration',
       'month_08_dm_time_duration', 'month_09_dm_time_duration',
       'month_10_dm_time_duration', 'month_11_dm_time_duration',
       'month_12_dm_time_duration', 'month_07_dm_flow', 'month_08_dm_flow',
       'month_09_dm_flow', 'month_10_dm_flow', 'month_11_dm_flow',
       'month_12_dm_flow', 'flow_11_1', 'flow_11_2', 'flow_11_3', 'flow_11_4',
       'times_11_1', 'times_11_2', 'times_11_3', 'times_11_4',
       'time_duration_11_1', 'time_duration_11_2', 'time_duration_11_3',
       'time_duration_11_4', 'flow_12_1', 'flow_12_2', 'flow_12_3',
       'flow_12_4', 'times_12_1', 'times_12_2', 'times_12_3', 'times_12_4',
       'time_duration_12_1', 'time_duration_12_2', 'time_duration_12_3',
       'time_duration_12_4', 'month_07_day_minute', 'month_08_day_minute',
       'month_09_day_minute', 'month_10_day_minute', 'month_11_day_minute',
       'month_12_day_minute ']

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
##data = pd.read_table('C:\\Users\\zhoubing\\Desktop\\20200105\\zb_dm_appflow_all_1112_fenduan.txt',sep=',')
data = pd.read_table('C:\\Users\\zhoubing\\Desktop\\dm20200221数据\\zb_dm_week_data.txt',sep=',')

##data0 = data.drop(['phone_no','open_date','key_phone_no','watch'],axis=1)
data0 = data.drop(['phone_no'],axis=1)
columns_name = data0.columns
len(columns_name)
data0 = data0.replace('\\N',np.NaN)
data0 = data0[columns_name].astype(np.float64)
data1 = data0.fillna(0)
data1['dm_label'] = data1['dm_label'].astype(np.int)
data1 = data1[c_name_week_data]

ss = StandardScaler()
data2 = ss.fit_transform(data1)

#最大最小值标准化
scaler = MinMaxScaler()
data2 = scaler.fit_transform(data1)

kmeans=KMeans(n_clusters=6,random_state=0)   #n_clusters:number of cluster  
kmeans.fit(data2)  
 
print(kmeans.labels_)
sum(kmeans.labels_)                        #显示每个样本所属的簇
print(kmeans.cluster_centers_)                #4个中心点的坐标
print(kmeans.inertia_)                        #用来评估簇的个数是否合适，代表所有点到各自中心的距离和，距离越小说明簇分的越好，选取临界点的簇个数
r1 = pd.Series(kmeans.labels_).value_counts()
print(r1)                                  #统计每个类别下样本个数
res = {}
for i in range(5):
    res[i] = sum(data1[(kmeans.labels_ == i)]['dm_label'])

data1[(kmeans.labels_ == 0)].mean()

# '利用SSE选择k'
SSE = []  # 存放每次结果的误差平方和
for k in range(1, 9):
    estimator = KMeans(n_clusters=k)  # 构造聚类器
    estimator.fit(data2)
    SSE.append(estimator.inertia_)
X = range(1, 9)
plt.xlabel('k')
plt.ylabel('SSE')
plt.plot(X, SSE, 'o-')
plt.show()

#导出文件
data_result = data
data_result['class'] = kmeans.labels_
data_result.to_csv('C:\\Users\\zhoubing\\Desktop\\dm20200221数据\\cluster_result\\zb_dm_week_data_result_6type_not0.txt',sep=',',index=False)


