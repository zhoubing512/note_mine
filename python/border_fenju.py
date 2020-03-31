import pandas
import cmsc.geo_tools as geo

data_jingyang = pandas.read_csv('E:/git_learning_file/work/geocode/jingyang.txt',',')

neighbor_list = []
for geocode in data_jingyang['geo_code']:
    neighbor_list += geo.geo_neighbors(geocode)

#差集 neighbor_list - data_jingyang['geo_code']
#求差集的neighbor，再和data_jingyang['geo_code']求交集，可得到边界的geocode
neighbor_list_diff = list(set(neighbor_list).difference(set(data_jingyang['geo_code'])))
neighbor_list_diff_neighbor = []
for geocode in neighbor_list_diff:
    neighbor_list_diff_neighbor += geo.geo_neighbors(geocode)

data_jingyang_border = list(set(neighbor_list_diff_neighbor)&set(data_jingyang['geo_code']))

data_jingyang_border_lonlat = []
for geo_ in data_jingyang_border:
    temp = list(data_jingyang[data_jingyang['geo_code']==geo_].index)[0]
    data_jingyang_border_lonlat.append([data_jingyang[data_jingyang['geo_code']==geo_].loc[temp,'lon'],data_jingyang[data_jingyang['geo_code']==geo_].loc[temp,'lat']])


file = open('E:/git_learning_file/work/geocode/jingyang_border.txt','w')
file.write(str(data_jingyang_border_lonlat))
file.close()