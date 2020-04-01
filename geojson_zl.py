
import json

with open("E:/Desktop/grid_dy_conv_20200326_utf8.json",'r',encoding='UTF-8') as f:
    geojson_dy = json.load(f)


geojson_dy[0]['name']

geojson_dy[0]['bd_path']

guanghan_json_str = '''{
    "type": "FeatureCollection",
    "features": [
        
    ]
    }'''

wangge_json_str = '''{
            "type": "Feature",
            "properties": {
                "adcode": 510623,
                "name": "中江县",
                "center": [
                    104.677831,
                    31.03681
                ],
                "centroid": [
                    104.79847,
                    30.881228
                ],
                "childrenNum": 0,
                "level": "district",
                "subFeatureIndex": 1,
                "acroutes": [
                    100000,
                    510000,
                    510600
                ],
                "parent": {
                    "adcode": 510600
                }
            },
            "geometry": {
                "type": "MultiPolygon",
                "coordinates": [
                    [
                        [
                            ]
                    ]
                ]
            }
        }'''
guanghan_json = json.loads(guanghan_json_str)
wangge_json = json.loads(wangge_json_str)

for i in range(len(geojson_dy)):
    wangge_json = json.loads(wangge_json_str)
    if geojson_dy[i]['name'][:2] == '广汉':
        wangge_json['properties']['name'] = geojson_dy[i]['name']
        wangge_json['geometry']['coordinates'][0][0] = geojson_dy[i]['bd_path']
        guanghan_json['features'].append(wangge_json)

#直接输出会漏掉
#file = open('E:/Desktop/zb_work/notes/note_mine/guanghan_geojson.json','w')
#json.dump(guanghan_json,file)

file = open('E:/Desktop/zb_work/notes/note_mine/guanghan_geojson.json','w')
file.write(json.dumps(guanghan_json))
file.close()

#德阳
deyang_json = json.loads(guanghan_json_str)
wangge_json = json.loads(wangge_json_str)
for i in range(len(geojson_dy)):
    wangge_json = json.loads(wangge_json_str)
    wangge_json['properties']['name'] = geojson_dy[i]['name']
    wangge_json['geometry']['coordinates'][0][0] = geojson_dy[i]['bd_path']
    deyang_json['features'].append(wangge_json)

#直接输出会漏掉
#file = open('E:/Desktop/zb_work/notes/note_mine/guanghan_geojson.json','w')
#json.dump(guanghan_json,file)

file = open('E:/Desktop/zb_work/notes/note_mine/deyang_geojson.json','w')
file.write(json.dumps(deyang_json))
file.close()

#德阳 gd_path
deyang_json = json.loads(guanghan_json_str)
wangge_json = json.loads(wangge_json_str)
for i in range(len(geojson_dy)):
    wangge_json = json.loads(wangge_json_str)
    wangge_json['properties']['name'] = geojson_dy[i]['name']
    wangge_json['geometry']['coordinates'][0][0] = geojson_dy[i]['gd_path']
    deyang_json['features'].append(wangge_json)

#直接输出会漏掉
#file = open('E:/Desktop/zb_work/notes/note_mine/guanghan_geojson.json','w')
#json.dump(guanghan_json,file)

file = open('E:/Desktop/zb_work/notes/note_mine/deyang_geojson_gd.json','w')
file.write(json.dumps(deyang_json))
file.close()
