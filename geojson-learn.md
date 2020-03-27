##geojson结构
* 一个点的数据表示  

```javascript
{
  "type": "FeatureCollection",
  "features": [
        {"type":"Feature",
        "properties":{},
        "geometry":{
            "type":"Point",
            "coordinates":[105.380859375,31.57853542647338]
            }
        }
    ]
}
```
  
&nbsp;&nbsp;&nbsp;&nbsp;geojson 将所有的地理要素分为Point、MultiPoint、LineString、MultiLineString、Polygon、MultiPolygon、GeometryCollection。首先是将这些要素封装到单个的geometry里，然后作为一个个的Feature（也就是要素）；要素放到一个要素集合里，从树状结构来理解FeatureCollection就是根节点，表示为：
```javascript
{
  "type": "FeatureCollection",
  "features": []
}
```

