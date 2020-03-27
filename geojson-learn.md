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
  
&emsp;geojson 将所有的地理要素分为 <font color=red size=4><b>*Point、MultiPoint、LineString、MultiLineString、Polygon、MultiPolygon、GeometryCollection*</b></font>。首先是将这些要素封装到单个的geometry里，然后作为一个个的Feature（也就是要素）；要素放到一个要素集合里，从树状结构来理解FeatureCollection就是根节点，表示为：
```javascript
{
  "type": "FeatureCollection",
  "features": []
}
```
* **点要素Point**
&nbsp;&nbsp;&nbsp;&nbsp;点要素是最简单的，类型type对应Point，然后坐标是一个1维的数组，里面有两个元素（如果是立体的坐标就是三维x,y,z），分别为经度和纬度。properties里面可以封装各种属性，例如名称、标识颜色等等

```javascript
{"type":"Feature",
    "properties":{},
    "geometry":{
        "type":"Point",
        "coordinates":[105.380859375,31.57853542647338]
        }
    }
```
* **多点要素MultiPoint**
```javascript
{"type":"Feature",
    "properties":{},
    "geometry":{
        "type":"MultiPoint",
        "coordinates":[[105.380859375,31.57853542647338],
                [105.580859375,31.52853542647338]
            ]
        }
        }
```

* **线要素LineString**
&emsp;线要素就是指线段，记录的是线的端点坐标，可视化时会按照记录顺序联结。对于曲线（如贝塞尔曲线）目前还没有很好的表达，但是在地理数据中，曲线一般会用LineString去拟合，现实地理世界中也没有标准的曲线地理要素。

&emsp;&emsp;<font color=red size=5>线要素、多点要素geometry区别，tpye不同、coordinates相同</font>
```javascript
{"type":"Feature",
    "properties":{},
    "geometry":{
        "type":"LineString",
        "coordinates":[[105.6005859375,30.65681556429287],
        [107.95166015624999,31.98944183792288],
        [109.3798828125,30.031055426540206],
        [107.7978515625,29.935895213372444]]
        }
    }
````

* **MultiLineString**

```javascript
{"type":"Feature",
    "properties":{},
    "geometry":{
        "type":"MultiLineString",
        "coordinates":
        [
            [
                [105.6005859375,30.65681556429287],
                [107.95166015624999,31.98944183792288],
                [109.3798828125,30.031055426540206],
                [107.7978515625,29.935895213372444]
            ],
            [
                [109.3798828125,30.031055426540206],
                [107.1978515625,31.235895213372444]
            ]
        ]
                }
    }
```
***tip:*** (**MultiLineString / Polygon**) coordinates 均是三维数组、仅type不同

