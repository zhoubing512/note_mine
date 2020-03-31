# -*- coding: UTF-8 -*-
import time, sys
sys.path.insert(0, '.')
import cmsc.time_tools as tt

print('\n' + tt.fmt_timestamp(time.time()))
print(tt.fmt_timestamp(time.time(), lang = 'cn'))
print(tt.fmt_timestamp(time.time(), lang = 'en', scale = 'mdHM'))
print(tt.fmt_timestamp(time.time(), lang = 'cn', scale = 'YmdH'))

stime = time.time()
time.sleep(1.564)
print('\n耗时: ' + tt.fmt_timediff(stime))
print('耗时: ' + tt.fmt_timediff(stime, lang = 'en'))
print('耗时: ' + str(tt.timediff(stime)))

print('')
print(tt.to_timestamp('2019-11-17 17:02:41'))
print(tt.to_timestamp('19-11-17 17:02:41'))
print(tt.to_timestamp('  2019年11月17日 17时02分39秒'))
print(tt.to_timestamp('19年11月17日 17时02分39秒'))
print(tt.to_timestamp('Sat Nov 23 09:22:57 2019'))
print(tt.to_timestamp('  Nov 23 09:22:57 2019'))
print(tt.to_timestamp('2019年11月17日 17时02分39秒', '%Y年%m月%d日 %H时%M分%S秒'))
t = tt.Timer()
t2 = tt.Timer()
time.sleep(1)
t.stop()
time.sleep(1)
t2.stop()
print(t, t2)
print(t + t2)

# nvidia示例
import cmsc.nvidia_info as ni
nv = ni.NvidiaInfo()
nv.print_nvidia_info()
print(nv)
nv

# 坐标转换示例
import cmsc.geo_tools as geo
proxy = 'proxy.cmsc.tech:3128'
proxies = {
    'http':'http://' + proxy,
    'https':'https://' + proxy,
}
ak = 'd'
geo_list = [[104.275632, 30.986269], [104.175632, 30.886269]]
print(geo.bd_geoconv(geo_list, ak = ak, proxies = proxies, from_code = 1, to_code = 5))
# print(help(geo.bd_geoconv))

# geo_code系列
print(geo.geo_encode(104.2262, 30.91316))
print(geo.geo_encode((104.2262, 30.91316)))
print(geo.geo_decode('726C0DF5F7'))
print(geo.geo_distance('726C0DF5F7', '726C188BCD'))
print(geo.geo_distance((104.413891, 31.183834), (104.423504, 31.177311)))
print(geo.geo_offset('726C0DF5F7', 2, 100, 'cv'))
print(geo.geo_offset('726C0DF5F7', 2, 100, 'cg'))
print(geo.geo_direction('726C0DF5F7', '726C188BCD'))
print(geo.geo_direction((104.413891, 31.183834), (104.423504, 31.177311)))
print(geo.geo_direction((0, 0), (0, 0)))
print(geo.geo_direction((0, 0), (0, 1)))
print(geo.geo_direction((0, 0), (1, 1)))
print(geo.geo_direction((0, 0), (1, 0)))
print(geo.geo_direction((0, 0), (1, -1)))
print(geo.geo_direction((0, 0), (0, -1)))
print(geo.geo_direction((0, 0), (-1, -1)))
print(geo.geo_direction((0, 0), (-1, 0)))
print(geo.geo_direction((0, 0), (-1, 1)))
print(geo.geo_neighbors('726C0DF5F7'))
print(geo.geo_neighbors('726C0DF5F7', 'RT'))
print(geo.geo_isneighbor('726C0DF5F7', '726C18A0A2'))

# 全角转换
import cmsc.text_tools as tet
dbstr = '我们。．，－ａ１　３５６７｀'
print(dbstr, tet.full_width_2_half_width(dbstr))
