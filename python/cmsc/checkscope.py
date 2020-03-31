# -*- coding: UTF-8 -*-

def __is_in_scope(point: list, vertex_lst: tuple):
    """
    首先判断点是否在包含多边形轮廓的区域中，如果不在则返回false,如果在则返回true，且继续判断与多边形的交点。
    :param point: 点坐标
    :param vertex_lst: 顶点列表，表示范围
    :return: false or true
    """
    lngaxis, lataxis = zip(*vertex_lst)
    minlng, maxlng = min(lngaxis), max(lngaxis)
    minlat, maxlat = min(lataxis), max(lataxis)
    lng, lat = point
    isin = (minlng <= lng <= maxlng) & (minlat <= lat <= maxlat)
    return isin


def __is_intersect(poi, spoi, epoi):
    """
    判断坐标向东的射线与线段是否有交点。
    :param poi: 坐标点位置
    :param spoi: 起始点坐标位置
    :param epoi: 终点坐标位置
    :return:
    """
    # 初始点经纬度
    lng, lat = poi
    # 起始点经纬度
    slng, slat = spoi
    # 终点经纬度
    elng, elat = epoi
    if poi == spoi:
        # 在顶点上
        return None
    if slat == elat:  # 排除与射线平行、重合，线段首尾端点重合的情况
        return False
    if slat > lat and elat > lat:  # 线段在射线上边
        return False
    if slat < lat and elat < lat:  # 线段在射线下边
        return False
    if slat == lat and elat > lat:  # 射线穿过线段的下端点，对应spoint
        return False
    if elat == lat and slat > lat:  # 射线穿过线段下端点，对应epoint
        return False
    if slng < lng and elat < lat:  # 线段在射线左边
        return False
    # 已知交点的纬度，求交点的经度
    xseg = elng - (elng - slng) * (elat - lat) / (elat - slat)
    if xseg == lng:
        # 交点经度与坐标点相同，则交点就是已知的坐标点，即坐标点在线段上
        return None
    if xseg < lng:  # 坐标点在线段右边，与线段不相交
        return False
    return True  # 排除上述情况之后，坐标带你在


def is_in_polygon(poi: list, vertex_lst: tuple):
    """
    检查坐标点poi是否在vertex范围内，先检查是否外包矩形范围，如果在继续检查与所有线段有几个交点，如果为奇数个交点则在范围内，如果在线段或端点上则在
    :param poi:交点位置
    :param vertex_lst:范围
    :return:False,True，None，其中None值表示穿过来的值少于三个点，不能构成封闭图形。
    """
    # 判断传过来的元组少于3个点则不能构成一个封闭图形，则反馈None值
    if len(set([tuple(i) for i in vertex_lst])) < 2:
        return None

    # 判断是否在外包矩形内，如果不在，直接返回false
    if not __is_in_scope(poi, vertex_lst):
        return False
    # 如果在外包矩形内,继续判断与所有线段是否相交，交点个数，为奇数个则在范围内，否在不在。
    # 传过来的范围是非封闭图形，填充为封闭图形。
    if vertex_lst[0] != vertex_lst[-1]:
        tmpvertex_lst = list(vertex_lst)
        tmpvertex_lst.append(vertex_lst[0])
    else:
        tmpvertex_lst = list(vertex_lst)
    sinsc = 0
    for spoi, epoi in zip(tmpvertex_lst[:-1], tmpvertex_lst[1::]):
        intersect = __is_intersect(poi, spoi, epoi)
        # 交点在线段上是一种特殊情况，返回值为None，不进行交点计数。如果交点出现在线段上，则直接返回True。
        if intersect is None:
            return True
        elif intersect:
            sinsc += 1
    return sinsc % 2 == 1
