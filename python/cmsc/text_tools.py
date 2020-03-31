# -*- coding: UTF-8 -*-


def full_width_2_half_width(full_width_str):
    """
    将字符串中的全角字符转为半角字符。full_width to half_width. 同 DBC2SBC
    :param full_width_str: str，待转换的字符串
    :return: str，转换后的字符串
    """
    return DBC2SBC(full_width_str)


def DBC2SBC(db_str):
    """
    将字符串中的全角字符转为半角字符。double byte code TO single byte code. 同 full_width_2_half_width
    :param db_str: str，待转换的字符串
    :return: str，转换后的字符串
    """
    # '全角转半角'
    sb_str = ""
    for uchar in db_str:
        inside_code = ord(uchar)
        if inside_code == 0x3000:
            inside_code = 0x0020
        else:
            inside_code -= 0xfee0
            if not (0x0021 <= inside_code <= 0x7e):
                sb_str += uchar
                continue
        sb_str += chr(inside_code)
    return sb_str
