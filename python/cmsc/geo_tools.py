# -*- coding: UTF-8 -*-
import json
import math
import urllib.request as req


def bd_geoconv(geo_list: list, from_code: int = 1, to_code: int = 5, ak: str = "",
               proxies: dict = None, url: str = "http://api.map.baidu.com/geoconv/v1/?") -> list:
    """
    调用百度API进行坐标转换，将其他类型的坐标系转换为百度的坐标系
    :param geo_list: list，经纬度数据列表
    :param from_code: int，源坐标类型：
        1：GPS设备获取的角度坐标，WGS84坐标;
        2：GPS获取的米制坐标、sogou地图所用坐标;
        3：google地图、soso地图、aliyun地图、mapabc地图和amap地图所用坐标，国测局（GCJ02）坐标;
        4：3中列表地图坐标对应的米制坐标;
        5：百度地图采用的经纬度坐标;
        6：百度地图采用的米制坐标;
        7：mapbar地图坐标;
        8：51地图坐标
    :param to_code: int，目标坐标系类型
        5：bd09ll(百度经纬度坐标);
        6：bd09mc(百度米制经纬度坐标)
    :param ak: str，申请的百度地区API的ak，申请地址：http://lbsyun.baidu.com/apiconsole/key/create
    :param proxies: dict，代理
    :param url: 百度api的地址
    :return: list，返回转换后的list
    """
    assert ak is not None and len(ak) > 0, "ak不能为空！"

    req_param = f"from={from_code}&to={to_code}&ak={ak}&coords="

    # 使用代理
    proxy_handler = req.ProxyHandler(proxies)
    openr = req.build_opener(proxy_handler)

    length = len(geo_list)
    step = 100
    result_list = []

    # 超过100个数据 需要分批请求
    for i in range(0, math.ceil(length / step) * step, step):
        coords = ';'.join([','.join([str(i) for i in j]) for j in geo_list[i: min(i + step, length)]])
        req_url = url + req_param + coords

        # http 请求百度api
        request = req.Request(req_url, method='GET')
        response = openr.open(request).read()
        result = json.loads(response.decode('utf-8'))
        if result['status'] == 0:
            result = result['result']
        else:
            print('ERROR: ', result)
            return None

        for res in result:
            result_list.append((res['x'], res['y']))

    return result_list


def geo_encode(lon: (float, tuple), lat: float = None) -> str:
    """
    将经纬度转化为geo_code编码。
    :param lon: float or tuple，经度 或 经纬度的tuple，如 104.2262
    :param lat: float，纬度，如 30.91316
    :return: str，geo编码，如 7266ABDBD2
    """
    lon, lat = lon if type(lon) in (tuple, list) else (lon, lat)
    # 转换经纬度为二进制
    slon = str(bin(math.floor((lon + 180) * math.pow(2, 20 - 1) / 180)))[2:]
    slat = str(bin(math.floor((lat + 90) * math.pow(2, 19 - 1) / 90)))[2:]
    slon = '0' * (20 - len(slon)) + slon
    slat = '0' * (20 - len(slat)) + slat
    # 合并经纬度的二进制编码
    geo_code_bin = ''.join((''.join([y, x]) for x, y in zip(slon, slat)))
    return hex(int('0b' + geo_code_bin, 0))[2:].upper()


def geo_decode(geo_code: str, precision: int = 6) -> tuple:
    """
    geo_code解码为经纬度。
    :param geo_code: str，待解码的geo_code编码，如 726C0DF5F7
    :param precision: int，返回数据的精度，默认保留6位小数
    :return: tuple，解码后的经纬度(经度, 纬度)，如 (104.413891, 31.183834)
    """
    if geo_code is None: return None
    geo_code = geo_code.strip()
    # 判断是否是16进制
    import re
    if not re.match('^[0-9a-fA-F]+$', geo_code): return None
    # 转换为二进制
    geo_code_bin = bin(int('0x' + geo_code, 0))[2:]
    geo_code_bin = '0' * (40 - len(geo_code_bin)) + geo_code_bin
    # 转化为经纬度
    blon, blat = geo_code_bin[1::2], geo_code_bin[0::2]
    ilon, ilat = tuple(map(lambda x: int('0b' + x, 0), [blon, blat]))
    lon = (ilon + 0.5) * 180 / math.pow(2, len(blon) - 1) - 180
    lat = (ilat + 0.5) * 90 / math.pow(2, len(blat) - 2) - 90
    return round(lon, precision), round(lat, precision)


def geo_distance(loc1, loc2, precision: int = 2) -> float:
    """
    返回两个位置的距离。
    :param loc1: tuple or str，位置1，可以为经纬度的tuple或geo_code字符串，如(104.413891, 31.183834)或'726C0DF5F7'
    :param loc2: tuple or str，位置2，可以为经纬度的tuple或geo_code字符串，如(104.423504, 31.177311)或'726C188BCD'
    :param precision: int，返回数据的精度，默认保留2位小数
    :return: float，返回两个位置的距离，单位为米，如 1168.53
    """
    import re
    pattern = re.compile('^[0-9a-fA-F]+$')
    assert (type(loc1) in (tuple, list) and len(loc1) == 2) or (
            type(loc1) is str and re.match(pattern, loc1)), '输入数据类型不正确！'
    assert (type(loc2) in (tuple, list) and len(loc2) == 2) or (
            type(loc2) is str and re.match(pattern, loc2)), '输入数据类型不正确！'
    # 地球半径
    RADIUS = 6378.137
    # 转为经纬度
    lon1, lat1 = loc1 if type(loc1) in (tuple, list) else geo_decode(loc1)
    lon2, lat2 = loc2 if type(loc2) in (tuple, list) else geo_decode(loc2)
    # 转为弧度
    lon1, lat1, lon2, lat2 = tuple(map(lambda x: math.radians(x), (lon1, lat1, lon2, lat2)))
    # 求距离
    return round(2 * math.asin(math.sqrt(math.pow(math.sin(lat2 / 2 - lat1 / 2), 2)
                                         + math.cos(lat2) * math.cos(lat1) * math.pow(math.sin(lon1 / 2 - lon2 / 2),
                                                                                      2))) * 1000 * RADIUS
                 , precision)


def geo_offset(loc, bearing: int = 0, distance: (float, int) = 0, option: str = 'CV'
               , precision: int = 6) -> [str, tuple]:
    """
    求指定位置按给定方向和距离偏移后的位置。
    :param loc: tuple or str，位置1，可以为经纬度的tuple或geo_code字符串，如(104.413891, 31.183834)或'726C0DF5F7'
    :param bearing: int，方向角度或编码，若为编码，1表示0度，2表示120度，3表示240度，如 2
    :param distance: float，偏移距离，如 100.0
    :param option: str，指定输入bearing的类型和输出类型，in ['cv', 'cg', 'dv', 'dg']，不区分大小写。如cv，cg
        第一位为c表示bearing输入的为编码，否则为角度；第二位为v表示输入经纬度值，否则输入geo_code编码。
    :param precision: int，返回数据的精度，默认保留6位小数
    :return: tuple or str，如 (104.4148, 31.183385) 或 726C18A0A4
    """
    import re
    pattern = re.compile('^[0-9a-fA-F]+$')
    assert (type(loc) in (tuple, list) and len(loc) == 2) or (type(loc) is str and re.match(pattern, loc)), \
        '输入的位置数据不正确！'
    assert type(option) is str and option.upper() in ['CV', 'CG', 'DV', 'DG'], \
        "option必须为['CV', 'CG', 'DV', 'DG']其中一个！"
    option = option.upper()

    # 地球半径，每一纬度代表的距离(米)
    RADIUS, DLAT = 6378.137, 111319.49
    bearing_d = {1: 0, 2: 120, 3: 240}

    # 如果偏移距离为 0
    if distance == 0 or distance <= 0.00001:
        return (loc if type(loc) in (tuple, list) else geo_decode(loc)) if option[1] == 'V' \
            else (geo_encode(loc) if type(loc) in (tuple, list) else loc)

    # 取得偏移角度
    bearing = math.radians(bearing if option[0] == 'D' else bearing_d[bearing])

    # 位置的经纬度
    lon, lat = loc if type(loc) in (tuple, list) else geo_decode(loc)

    # 根据公式得到新的经纬度
    lon = round(lon + distance * math.sin(bearing) / (RADIUS * math.pi * math.cos(math.radians(lat)) * 1000 / 180)
                , precision)
    lat = round(lat + distance * math.cos(bearing) / DLAT, precision)
    return (lon, lat) if option[1] == 'V' else geo_encode(lon, lat)


def geo_direction(loc1, loc2) -> float:
    """
    求loc2相对于loc1的角度。
    :param loc1: tuple or str，位置1，可以为经纬度的tuple或geo_code字符串，如(104.413891, 31.183834)或'726C0DF5F7'
    :param loc2: tuple or str，位置2，可以为经纬度的tuple或geo_code字符串，如(104.423504, 31.177311)或'726C188BCD'
    :return: float，角度，相对于正北方向，如128.42
    """
    import re
    pattern = re.compile('^[0-9a-fA-F]+$')
    assert (type(loc1) in (tuple, list) and len(loc1) == 2) or \
           (type(loc1) is str and re.match(pattern, loc1)), '输入数据类型不正确！'
    assert (type(loc2) in (tuple, list) and len(loc2) == 2) or \
           (type(loc2) is str and re.match(pattern, loc2)), '输入数据类型不正确！'

    # 转为经纬度
    lon1, lat1 = loc1 if type(loc1) in (tuple, list) else geo_decode(loc1)
    lon2, lat2 = loc2 if type(loc2) in (tuple, list) else geo_decode(loc2)
    # 求角度
    angle = math.degrees(math.atan2((lon2 - lon1) * math.cos(math.radians(lat1)), lat2 - lat1))
    angle = (360 + angle) if lon2 < lon1 else angle
    return round(angle, 2)


def geo_neighbors(geo_code: str, direction: str = None):
    """
    求给定位置编码的相邻位置编码。
    :param geo_code: str，给定的位置编码；
    :param direction: str，相邻的方向，不区分大小写：
        None    返回所有相邻的编码，
        L, LEFT 返回左侧的编码，
        R, RIGHT    返回右侧的编码，
        T, TOP  返回上侧的编码，
        B, BOTTOM   返回下侧的编码，
        LT, TL, LeftTop, TopLeft    返回左上侧的编码，
        RT, TR, RightTop, TopRight  返回右上侧的编码，
        LB, BL, LeftBottom, BottomLeft  返回左下侧的编码，
        RB, BR, RightBottom, BottomRight    返回右下侧的编码；
    :return: list or str，若无指定方向或方向不正确，则范围所有相邻编码，否则返回指定方向的编码。
    """
    import re
    pattern = re.compile('^[0-9a-fA-F]+$')
    assert re.match(pattern, geo_code), '输入数据类型不正确！'

    geo_code = geo_code.upper()
    # 常量
    TOP, RIGHT, BOTTOM, LEFT = 0, 1, 2, 3

    direction = None if direction is None else direction.upper()
    if direction in ["L", "LEFT"]:
        return _geo_neighbors_search(geo_code, LEFT)
    if direction in ["R", "RIGHT"]:
        return _geo_neighbors_search(geo_code, RIGHT)
    if direction in ["T", "TOP"]:
        return _geo_neighbors_search(geo_code, TOP)
    if direction in ["B", "BOTTOM"]:
        return _geo_neighbors_search(geo_code, BOTTOM)
    if direction in ["TL", "LT", "TOPLEFT", "LEFTTOP"]:
        return _geo_neighbors_search(_geo_neighbors_search(geo_code, LEFT), TOP)
    if direction in ["TR", "RT", "TOPRIGHT", "RIGHTTOP"]:
        return _geo_neighbors_search(_geo_neighbors_search(geo_code, RIGHT), TOP)
    if direction in ["BL", "LB", "BOTTOMLEFT", "LEFTBOTTOM"]:
        return _geo_neighbors_search(_geo_neighbors_search(geo_code, LEFT), BOTTOM)
    if direction in ["BR", "RB", "BOTTOMRIGHT", "RIGHTBOTTOM"]:
        return _geo_neighbors_search(_geo_neighbors_search(geo_code, RIGHT), BOTTOM)
    # 结果
    result = list(map(lambda x: _geo_neighbors_search(geo_code, x), [LEFT, RIGHT, TOP, BOTTOM]))
    result.extend(list(map(lambda x: _geo_neighbors_search(result[0], x), [TOP, BOTTOM])))
    result.extend(list(map(lambda x: _geo_neighbors_search(result[1], x), [TOP, BOTTOM])))
    return result


def _geo_neighbors_search(geo_code: str, direction: int):
    """
    按direction的方向搜索邻接位置编码。
    :param geo_code: str，位置编码；
    :param direction: int，方向，[0, 1, 2, 3] 对应 [上, 右, 下, 左]；
    :return: str，相邻位置的编码。
    """
    if geo_code.strip() == "": return ""

    HEXSTRING = "0123456789ABCDEF"
    NEIGHBORS = ["238967CDAB01EF45", "143650729CBED8FA", "AB01EF45238967CD", "50721436D8FA9CBE"]
    BORDERS = ["ABEF", "57DF", "0145", "028A"]
    last_char = geo_code[-1]
    geo_base = geo_code[0: -1]
    # 如果在边界上，则base同样需要进行邻接查找
    if last_char in BORDERS[direction]:
        geo_base = _geo_neighbors_search(geo_base, direction)
    # 如果最后geocode只有一位了，且在边界上，则说明没有对应的邻接格子；或者如果返回的strBase为空字符串，则说明第一位都没有找到，则也没有邻接的格子
    if (last_char in BORDERS[direction] and len(geo_code) == 1) \
            or (len(geo_code) != 1 and geo_base == ""):
        return ""
    else:
        return geo_base + NEIGHBORS[direction][HEXSTRING.index(last_char)]

def geo_isneighbor(geo_code1: str, geo_code2: str) -> bool:
    """
    判断两个位置编码是否相邻。
    :param geo_code1: str，位置编码1
    :param geo_code2: str，位置编码2
    :return: bool，是否邻接
    """
    return geo_code2 in geo_neighbors(geo_code1)

def is_in_polygon(point: tuple, border: list) -> bool:
    """
    判断给定的点是否在一个区域范围内。

    :param point: 需要判断的点
    :type point: tuple or list 
    :param border: list, 区域的边界
    :type border: list 
    :return: 给定点是否在范围内
    :rtype: bool

    Usage::
        >>> from cmsc import geo_tools as geo  
        >>> geo.is_in_polygon((104.2, 31.3), [(104.2, 31.3), (104.1, 31.5), (104.4, 31.8)])
        True
    """

    # 取消类型检查 以提高运行效率
    # assert type(point) in (tuple, list) and len(point) == 2\
    #     , 'point 须为 tuple 或 list, 如形式: (lon, lat)' 
    # assert type(border) == list and len(border) > 2 \
    #     , 'border 须为 list, 且长度大于2' 
    border_point_typeset = set([type(i) for i in border])
    border_point_type = border_point_typeset.pop()
    assert len(border_point_typeset) == 0, 'border 中只能有一种数据类型'
    # assert border_point_type in (list, tuple) and len(border_point_typeset) == 0 \
    #     , 'border 中的点须为 tuple 或 list' 
    # border_point_lenset = set([len(i) for i in border])
    # border_point_len = border_point_lenset.pop()
    # assert border_point_len == 2 and len(border_point_lenset) == 0 \
    #     , 'border 中的点的形式须为 (lon, lat) 或 [lon, lat]' 

    # 如果 point 为 list 转为 tuple
    if type(point) == list:
        point = tuple(point)

    # 如果 border 由 list 构成, 转为 tuple
    border = border.copy()
    if border_point_type == list:
        border = [tuple(i) for i in border]
    assert len(set(border)) > 2, 'border 至少需要有3个不同的点' 

    # 如果 point 为端点 直接返回true
    if point in border: 
        return True 

    # 需要确保 边界 闭合
    if border[0] != border[-1]: 
        border.append(border[0])

    # 边界范围
    # from functools import reduce 
    # lon_max, lat_max, lon_min, lat_min = reduce(\
    #     lambda x, y: \
    #         (max(x[0], y[0]), max(x[1], y[1]), min(x[0], y[0]), min(x[1], y[1]))\
    #     , border)

    lon_list, lat_list = zip(*border)
    lon_max, lon_min = max(lon_list), min(lon_list)
    lat_max, lat_min = max(lat_list), min(lat_list)

    # 如果点在边界范围外 直接 false 否则还需进一步判断
    if point[0] > lon_max or point[0] < lon_min \
            or point[1] > lat_max or point[1] < lat_min:
        return False 

    # 判断点东向的射线是否与任意一条相交 相交点的个数为奇数个则说明在内部
    # 生成东向的一条线段
    # segment = (point, (lon_max + .01, point[1]))
    # 判断segment和多边形每一条线段是否相交 并求交点的个数
    cross_times = 0
    for seg in zip(border[:-1], border[1:]):
        # 如果在线段上 则直接返回true
        if is_on_segment(point, seg):
            return True 
        # 这个函数对于这个问题不是最优的 
        # 这个函数可用于任意两条线段 本问题有一条是固定的水平线 且y轴上是固定值 所以可以优化的
        # if is_seg_intersected(segment, seg):
        # 优化版
        if _is_east_intersected(point, seg):
            # 如果 seg 也是水平线 需要 加2 
            cross_times += 1 if seg[0][1] != seg[1][1] else 2  
    
    return cross_times % 2 == 1 

def _is_east_intersected(point: tuple, segment: tuple):
    """
    判断给定的点的东向射线是否与线段相交。

    :param point: 点 
    :type point: tuple or list 
    :param segment: 线段 
    :type segment: tuple or list 
    :return: 点的东向射线是否与线段相交 
    :rtype: bool 

    Usage::
        >>> from cmsc import geo_tools as geo  
        >>> geo._is_east_intersected((1.3, 1.5), ((1, 1), (2, 2)))
        True
    """
    # 取消类型检查 以提高运行效率
    # assert type(point) in (tuple, list) and len(point) == 2\
    #     , 'point 须为 tuple 或 list, 如形式: (lon, lat)' 
    # assert type(segment) in (tuple, list) and len(segment) == 2\
    #     , '线段的形式须为: ((lon1, lat1), (lon2, lat2)), 可接受 list 或 tuple' 
    # segment_point_typeset = set([type(i) for i in segment])
    # segment_point_type = segment_point_typeset.pop()
    # assert segment_point_type in (list, tuple) \
    #         and len(segment_point_typeset) == 0 \
    #     , 'segment 的形式须为: ((lon1, lat1), (lon2, lat2)), 端点可接受 list 或 tuple, 但不能混用' 
    # segment_point_lenset = set([len(i) for i in segment])
    # segment_point_len = segment_point_lenset.pop()
    # assert segment_point_len == 2 and len(segment_point_lenset) == 0 \
    #     , 'segment 的形式须为: ((lon1, lat1), (lon2, lat2)), 端点可接受 list 或 tuple, 但不能混用' 

    # 条件分别为 point 在 segment 的: 右侧, 上方, 下侧, 否则需要进一步判断
    if (point[0] > segment[0][0] and point[0] > segment[1][0]) \
            or (point[1] > segment[0][1] and point[1] > segment[1][1]) \
            or (point[1] < segment[0][1] and point[1] < segment[1][1]):
        return False 

    # 求交点 
    cross_lon = (point[1] * (segment[1][0] - segment[0][0]) \
            - segment[0][1] * segment[1][0] + segment[1][1] * segment[0][0]) \
        / (segment[1][1] - segment[0][1]) 
    
    return cross_lon >= point[0] 


def is_on_segment(point: tuple, segment: tuple):
    """
    判断给定的点是否在线段上。

    :param point: 点 
    :type point: tuple or list 
    :param segment: 线段 
    :type segment: tuple or list 
    :return: 点是否在线段上 
    :rtype: bool 

    Usage::
        >>> from cmsc import geo_tools as geo  
        >>> geo.is_seg_intersected((1.5, 1.5), ((1, 1), (2, 2)))
        True
    """
    # 取消类型检查 以提高运行效率
    # assert type(point) in (tuple, list) and len(point) == 2\
    #     , 'point 须为 tuple 或 list, 如形式: (lon, lat)' 
    # assert type(segment) in (tuple, list) and len(segment) == 2\
    #     , '线段的形式须为: ((lon1, lat1), (lon2, lat2)), 可接受 list 或 tuple' 
    # segment_point_typeset = set([type(i) for i in segment])
    # segment_point_type = segment_point_typeset.pop()
    # assert segment_point_type in (list, tuple) \
    #         and len(segment_point_typeset) == 0 \
    #     , 'segment 的形式须为: ((lon1, lat1), (lon2, lat2)), 端点可接受 list 或 tuple, 但不能混用' 
    # segment_point_lenset = set([len(i) for i in segment])
    # segment_point_len = segment_point_lenset.pop()
    # assert segment_point_len == 2 and len(segment_point_lenset) == 0 \
    #     , 'segment 的形式须为: ((lon1, lat1), (lon2, lat2)), 端点可接受 list 或 tuple, 但不能混用' 
    
    # 三点的斜率是否相同
    if (segment[1][1] - point[1]) * (segment[0][0] - point[0]) \
            == (segment[0][1] - point[1]) * (segment[1][0] - point[0]):
        # point 在线段的范围内就肯定在线段上
        return point[0] <= max(segment[0][0], segment[1][0]) \
            and point[0] >= min(segment[0][0], segment[1][0]) 
    return False 

def is_seg_intersected(seg1: tuple, seg2: tuple):
    """
    判断给定的两条线段是否相交。

    :param seg1: 线段1
    :type seg1: tuple or list 
    :param seg2: 线段2
    :type seg2: tuple or list 
    :return: 两条线段是否相交
    :rtype: bool

    Usage::
        >>> from cmsc import geo_tools as geo  
        >>> geo.is_seg_intersected(((1, 1), (2, 2)), ((1, 2), (2, 1)))
        True
    """
    # 取消类型检查 以提高运行效率
    # assert type(seg1) in (tuple, list) and len(seg1) == 2\
    #         and type(seg2) in (tuple, list) and len(seg2) == 2\
    #     , '线段的形式须为: ((lon1, lat1), (lon2, lat2)), 可接受 list 或 tuple' 
    # seg1_point_typeset = set([type(i) for i in seg1])
    # seg1_point_type = seg1_point_typeset.pop()
    # assert seg1_point_type in (list, tuple) \
    #         and len(seg1_point_typeset) == 0 \
    #     , 'seg1 的形式须为: ((lon1, lat1), (lon2, lat2)), 端点可接受 list 或 tuple, 但不能混用' 
    # seg2_point_typeset = set([type(i) for i in seg2])
    # seg2_point_type = seg2_point_typeset.pop()
    # assert seg2_point_type in (list, tuple) \
    #         and len(seg2_point_typeset) == 0 \
    #     , 'seg2 的形式须为: ((lon1, lat1), (lon2, lat2)), 端点可接受 list 或 tuple, 但不能混用' 
    # seg1_point_lenset = set([len(i) for i in seg1])
    # seg1_point_len = seg1_point_lenset.pop()
    # assert seg1_point_len == 2 and len(seg1_point_lenset) == 0 \
    #     , 'seg1 的形式须为: ((lon1, lat1), (lon2, lat2)), 端点可接受 list 或 tuple, 但不能混用' 
    # seg2_point_lenset = set([len(i) for i in seg2])
    # seg2_point_len = seg2_point_lenset.pop()
    # assert seg2_point_len == 2 and len(seg2_point_lenset) == 0 \
    #     , 'seg2 的形式须为: ((lon1, lat1), (lon2, lat2)), 端点可接受 list 或 tuple, 但不能混用' 

    seg1_max_lon, seg1_max_lat, seg1_min_lon, seg1_min_lat = \
        max(seg1[0][0], seg1[1][0]), max(seg1[0][1], seg1[1][1]) \
        , min(seg1[0][0], seg1[1][0]), min(seg1[0][1], seg1[1][1]) 
    seg2_max_lon, seg2_max_lat, seg2_min_lon, seg2_min_lat = \
        max(seg2[0][0], seg2[1][0]), max(seg2[0][1], seg2[1][1]) \
        , min(seg2[0][0], seg2[1][0]), min(seg2[0][1], seg2[1][1]) 

    # 条件分别为 seg1 在 seg2 的: 下方, 上方, 左侧, 右侧, 否则需要进一步判断
    if seg1_max_lat < seg2_min_lat or seg1_min_lat > seg2_max_lat \
            or seg1_max_lon < seg2_min_lon or seg1_min_lon > seg2_max_lon:
        return False 

    # 如果是平行的
    if (seg1[1][0] - seg1[0][0]) * (seg2[0][1] - seg2[1][1]) \
            == (seg2[0][0] - seg2[1][0]) * (seg1[1][1] - seg1[0][1]):
        # 如果在一条直线上
        if (seg1[1][0] - seg1[0][0]) * (seg2[0][1] - seg1[0][1]) \
                == (seg2[0][0] - seg1[0][0]) * (seg1[1][1] - seg1[0][1]):
            # 那么seg1如果其中一个点在seg2的范围内 则相交
            return (seg1_max_lon >= seg2_min_lon and seg1_max_lon <= seg2_max_lon) \
                or (seg1_min_lon >= seg2_min_lon and seg1_min_lon <= seg2_max_lon)
        else: 
            return False 
        pass 

    # 求交点  根据交点公式
    t = ((seg1[1][0] - seg1[0][0]) * (seg2[0][1] - seg1[0][1]) \
                - (seg2[0][0] - seg1[0][0]) * (seg1[1][1] - seg1[0][1])) \
            / ((seg1[1][0] - seg1[0][0]) * (seg2[0][1] - seg2[1][1]) \
                - (seg2[0][0] - seg2[1][0]) * (seg1[1][1] - seg1[0][1])) 
    cross_point = seg2[0][0] + t * (seg2[1][0] - seg2[0][0])\
        , seg2[0][1] + t * (seg2[1][1] - seg2[0][1])
    
    # 判断交点是否在线段的范围内 
    if cross_point[0] >= seg1_min_lon and cross_point[0] >= seg2_min_lon \
            and cross_point[0] <= seg1_max_lon and cross_point[0] <= seg2_max_lon:
        return True 

    return False  

def polygon_distance(polygon1: tuple, polygon2: tuple, distance_type: str='point2polygon'):
    """
    求两个多边形的最近距离。

    :param polygon1: 多边形1
    :type polygon1: tuple or list 
    :param polygon2: 多边形2
    :type polygon2: tuple or list 
    :param distance_type: 想要求的距离的类型
        'point2polygon': 点到多边形的最小距离, 此时参数1须为点, 参数2须为多边形
    :type distance_type: str
    :return: 多边形1 到 多边形2的最小距离, 相交或在里面 返回 0 
    :rtype: double

    Usage::
        >>> from cmsc import geo_tools as geo  
        >>> geo.polygon_distance(((1, 2)), ((1, 2), (2, 1), (2, 3)))
        0
    """
    if distance_type == 'point2polygon':
        point=polygon1
        border = polygon2.copy()
        border_point_typeset = set([type(i) for i in border])
        border_point_type = border_point_typeset.pop()
        assert len(border_point_typeset) == 0, 'polygon 中只能有一种数据类型'
        # 如果 border 由 list 构成, 转为 tuple
        border = border.copy()
        if border_point_type == list:
            border = [tuple(i) for i in border]
        assert len(set(border)) > 2, 'polygon2 至少需要有3个不同的点' 

        # 如果 point 为 list 转为 tuple
        if type(point) == list:
            point = tuple(point)

        # 如果 point 为端点 直接返回true
        if point in border: 
            return 0 

        # 需要确保 边界 闭合
        if border[0] != border[-1]: 
            border.append(border[0])

        # 如果在里面 则返回 0 
        if is_in_polygon(point, border):
            return 0 

        # 求交点和每一条线段距离
        distances = []
        for seg in zip(border[:-1], border[1:]):
            distances.append(polygon_distance(point, seg, 'point2segment'))
        
        # 返回最小值
        return min(distances)
    
    elif distance_type == 'point2segment':
        # 先求点到直线的距离 然后再看垂足点是否在线段的范围内 如果在返回距离 如果不在返回点到两个端点的最小距离
        # 关于求垂足点 可以用 直线的两点式(线段所在直线) 和 点斜式(垂线) 的方程联合求解 只需要求横坐标或纵坐标
        # x = ((x2 - x1)(y2 - y1)(y3 - y1) + x1(y2 - y1)^2 + x3(x2 - x1)^2) / ((y2 - y1)^2 + (x2 - x1)^2)
        # y = ((x2 - x1)(y2 - y1)(x3 - x1) + y1(x2 - x1)^2 + y3(y2 - y1)^2) / ((y2 - y1)^2 + (x2 - x1)^2)
        # x 即为垂足点的横坐标, 3 为point, 1和2为直线上的点
        x1, y1, x2, y2 = polygon2[0][0], polygon2[0][1], polygon2[1][0], polygon2[1][1]
        x3, y3 = polygon1[0], polygon1[1]
        x4 = ((x2 - x1) * (y2 - y1) * (y3 - y1) \
                + x1 * math.pow(y2 - y1, 2) \
                + x3 * math.pow(x2 - x1, 2)) \
            / (math.pow(y2 - y1, 2) + math.pow(x2 - x1, 2))
        # 如果交点在x1 和 x2 范围内
        if x4 >= min(x1, x2) and x4 <= max(x1, x2):
            return polygon_distance(polygon1, polygon2, 'point2line')
        else:
            return min(map(lambda x: polygon_distance(polygon1, x, 'point2point'), polygon2))
    elif distance_type == 'point2line':
        # 点到直线的距离
        # 直线公式为 (y2 - y1)x - (x2 - x1)y + (y1x2 - y2x1) = 0   =>  Ax + By + C = 0 
        # 距离公式为 d = abs((Ax3 + By3 + C) / sqrt(A^2 + B+2) )
        # x1, y1, x2, y2 = polygon2[0][0], polygon2[0][1], polygon2[1][0], polygon2[1][1]
        # x3, y3 = polygon1[0], polygon1[1]
        # return math.fabs(((y2 - y1) * x3 - (x2 - x1) * y3 + y1 * x2 - y2 * x1) \
        #     / math.sqrt(math.pow(y2 - y1, 2) + math.pow(x1 - x2, 2)))

        # 由于是在这个地图工具里  还是返回实际距离吧
        x1, y1, x2, y2 = polygon2[0][0], polygon2[0][1], polygon2[1][0], polygon2[1][1]
        x3, y3 = polygon1[0], polygon1[1]
        x4 = ((x2 - x1) * (y2 - y1) * (y3 - y1) \
                + x1 * math.pow(y2 - y1, 2) \
                + x3 * math.pow(x2 - x1, 2)) \
            / (math.pow(y2 - y1, 2) + math.pow(x2 - x1, 2))
        y4 = ((x2 - x1) * (y2 - y1) * (x3 - x1) \
                + y1 * math.pow(x2 - x1, 2) \
                + y3 * math.pow(y2 - y1, 2)) \
            / (math.pow(y2 - y1, 2) + math.pow(x2 - x1, 2))
        return geo_distance(polygon1, (x4, y4), precision=6) 
    elif distance_type == 'point2point':
        # 两点之间的距离
        # return math.sqrt(sum(map(lambda x: math.pow(x, 2)\
        #         , [polygon2[1] - polygon1[1], polygon2[0] - polygon1[0]])))
        # from functools import reduce
        # return math.sqrt(reduce(lambda x, y: math.pow(x, 2) + math.pow(y, 2)\
        #         , [polygon2[1] - polygon1[1], polygon2[0] - polygon1[0]]))
        # return math.sqrt(math.pow(polygon2[0] - polygon1[0], 2) \
        #         + math.pow(polygon2[1] - polygon1[1], 2))

        # 由于是在这个地图工具里  还是返回实际距离吧
        return geo_distance(polygon1, polygon2, precision=6) 
    return None 
