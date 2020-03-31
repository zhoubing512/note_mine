# -*- coding: UTF-8 -*-
import time
import re


# 定义一个计时器类，使用更方便
class Timer:
    """
    一个计时器，以创建时间为开始时间，也可使用start()来更新开始时间，使用stop()来结束计时。
    每次计时结束时才可以重新更新开始时间。
    直接使用时，若计时未结束，返回截至当前时间的时长；若计时已结束，返回截至stop_time的时长。
    """
    def __init__(self, lang='cn', start_time = None, stop_time = None):
        self.start_time = time.time() if start_time is None else start_time 
        self.stop_time = stop_time 
        self.time_diff = None if stop_time is None else stop_time - start_time 
        self.lang = lang 
        # 计时器的状态
        self.stopped = False if stop_time is None else True 
        # 用来标记是否是首次创建的计时器
        self.__new_flag = True 
        self.__new_flag = False if stop_time is not None else self.__new_flag 

    # 如果是停止状态, 或是仅仅是初始化的 
    def start(self, lang=None):
        if self.stopped or self.__new_flag:
            self.start_time = time.time() 
            self.stop_time = None
            self.stopped = False
            self.__new_flag = False
            lang = lang if lang is not None else self.lang 
        return fmt_timestamp(self.start_time, lang=lang)

    def now(self, lang=None):
        lang = lang if lang is not None else self.lang 
        return fmt_timestamp(time.time(), lang=lang)

    def restart(self, lang=None):
        self.stopped = False
        self.__new_flag = False 
        self.stop_time = None 
        self.start_time = time.time()
        lang = lang if lang is not None else self.lang 
        return fmt_timestamp(self.start_time, lang=lang)

    def stop(self, lang=None):
        if not self.stopped:
            self.stop_time = time.time() 
            self.time_diff = self.stop_time - self.start_time
            self.stopped = True
            self.__new_flag = False
        lang = lang if lang is not None else self.lang 
        return fmt_timestamp(self.stop_time, lang=lang)

    def __repr__(self, lang=None):
        self.__new_flag = False
        lang = lang if lang is not None else self.lang 
        return fmt_timediff(self.start_time, self.stop_time, lang=lang)

    __str__ = __repr__

    def __add__(self, other):
        assert self.stopped is True and other.stopped is True, '相加的计时器中有未停止的！'
        return Timer(self.lang, self.start_time, self.stop_time + other.stop_time - other.start_time)


# 返回当前时间
def now(scale: str = 'YmdHMS', lang: str = 'en') -> str:
    return fmt_timestamp(time.time(), scale=scale, lang=lang)

# 计算时间差的别名
def timediff(start_time: float, stop_time: float = None) -> float:
    """
    计算截止时间到开始时间的时间差。
    :param start_time: float, 开始的timestamp。
    :param stop_time: float, 结束时的timestamp，缺省值为当前时间。
    :return: float, 单位为 秒 Seconds, 精确到毫秒
    """
    stop_time = time.time() if stop_time is None else stop_time
    return round(stop_time - start_time, 3)


# 计算时间差
def fmt_timediff(start_time: float, stop_time: float = None, lang: str = 'cn') -> str:
    """
    计算截止时间到开始时间的时间差，并格式化。
    :param start_time: float，开始的timestamp。
    :param stop_time: float，结束时的timestamp，缺省值为当前时间。
    :param lang: str，['cn', 'en']，指定输出格式为中文格式还是英文格式。
    :return: str，格式化的时间差。如 20分32秒 或 20 Minutes 32 Seconds。最大的单位为 天 Days，最小的单位为 秒 Seconds
    """
    stop_time = time.time() if stop_time is None else stop_time
    time_diff = round(stop_time - start_time)
    time_diff, seconds = time_diff // 60, time_diff % 60 
    time_diff, minutes = time_diff // 60, time_diff % 60 
    days, hours = time_diff // 24, time_diff % 24 
    units = {'day': ' Days ', 'hour': ' Hours ', 'minute': ' Minutes ', 'second': ' Seconds'} \
        if lang == 'en' else {'day': '天', 'hour': '小时', 'minute': '分', 'second': '秒'}
    formatted_str = str(seconds) + units['second'] 
    formatted_str = str(minutes) + units['minute'] + formatted_str if minutes > 0 else formatted_str
    formatted_str = str(hours) + units['hour'] + formatted_str if hours > 0 else formatted_str
    formatted_str = str(days) + units['day'] + formatted_str if days > 0 else formatted_str
    return formatted_str 


# 格式化日期
def fmt_timestamp(unix_time: float, scale: str = 'YmdHMS', lang: str = 'en') -> str:
    """
    格式化timestamp为常用的格式。
    :param unix_time: float，待转换的timestamp
    :param scale: str，缺省为'YmdHMS'。可接受'YmdHMS'的子字符串，分别表示年月日时分秒，顺序不可乱，如 mdHM
    :param lang: str，['cn', 'en']，指定输出格式为中文格式还是英文格式。如 cn
    :return: str，返回格式化后的时间，如 12月16日18时26分
    """
    assert lang in ('en', 'cn'), "只能是cn(中文格式), en(英文格式)" 
    assert scale in 'YmdHMS' or scale in 'ymdHMS', "输出刻度只能是'(Y|y)mdHMS'的子字符串, 如HMS"
    units = {'y': '-', 'Y': '-', 'm': '-', 'd': ' ', 'H': ':', 'M': ':', 'S': ''} \
        if lang == "en" else {'y': '年', 'Y': '年', 'm': '月', 'd': '日 ', 'H': '时', 'M': '分', 'S': '秒'}
    time_format = ''.join("%" + i + units[i] for i in scale) 
    time_format = time_format[:-1] if time_format[-1] in (' ', '-', ':') else time_format 
    formatted_time = time.strftime(time_format, time.localtime(unix_time))
    return formatted_time


# 从正常日期到unixtime的转化 
def to_timestamp(time_str: str, fmt: str = None) -> float:
    """
    将已格式化的时间字符串转换为timestamp。已支持的格式包括：'%Y-%m-%d %H:%M:%S', '%Y年%m月%d日 %H时%M分%S秒',
        '%y-%m-%d %H:%M:%S', '%y年%m月%d日 %H时%M分%S秒', '%a %b %d %H:%M:%S %Y'
    :param time_str: str，待转换的时间字符串。
    :param fmt: str，指定输入的时间字符串格式format，若未输入，则尝试内部定义的格式类型。
    :return: float，转换后的timestamp
    """
    time_str = time_str.strip()
    if fmt is None:
        fmts = ('%Y-%m-%d %H:%M:%S', '%Y年%m月%d日 %H时%M分%S秒', '%y-%m-%d %H:%M:%S'
                        , '%y年%m月%d日 %H时%M分%S秒', '%a %b %d %H:%M:%S %Y', '%b %d %H:%M:%S %Y')
        patterns = (r'^\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}$'
                    , r'^\d{4}年\d{1,2}月\d{1,2}日 \d{1,2}时\d{1,2}分\d{1,2}秒$'
                    , r'^\d{2}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}$'
                    , r'^\d{2}年\d{1,2}月\d{1,2}日 \d{1,2}时\d{1,2}分\d{1,2}秒$'
                    , r'^\S{3} \S{3} +\d{1,2} \d{1,2}:\d{1,2}:\d{1,2} \d{4}$'
                    , r'^\S{3} +\d{1,2} \d{1,2}:\d{1,2}:\d{1,2} \d{4}$'
                    )
        patterns = tuple(map(re.compile, patterns))
        for i, pattern in enumerate(patterns):
            if re.match(pattern, time_str):
                fmt = fmts[i]
                break

    try:
        unixtime = time.mktime(time.strptime(time_str, fmt))
    except Exception as e:
        raise e
    return unixtime


# 从正常日期到unixtime的转化 原来的
def _to_unixtime2(time_str: str) -> float:
    """
    将已格式化的时间字符串转换为timestamp。已支持的格式包括：'%Y-%m-%d %H:%M:%S', '%Y年%m月%d日 %H时%M分%S秒',
        '%y-%m-%d %H:%M:%S', '%y年%m月%d日 %H时%M分%S秒', '%a %b %d %H:%M:%S %Y'
    :param time_str: str，待转换的时间字符串。
    :return: float，转换后的timestamp
    """
    time_formats = ('%Y-%m-%d %H:%M:%S', '%Y年%m月%d日 %H时%M分%S秒', '%y-%m-%d %H:%M:%S'
                    , '%y年%m月%d日 %H时%M分%S秒', '%a %b %d %H:%M:%S %Y')
    for i in range(len(time_formats)):
        try:
            unixtime = time.mktime(time.strptime(time_str, time_formats[i]))
        except Exception as e:
            if i == len(time_formats) - 1:
                raise e
            else:
                continue
        return unixtime

