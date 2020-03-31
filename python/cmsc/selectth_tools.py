# -*- coding: UTF-8 -*-

def selectth(num):
    '''
    传入11位字符串格式号码，返回号码是否特号，特号类型。
    :param num: 传入11位字符串格式电话号码，str格式
    :return: 匹配到返回特号类型，没有匹配到返回null, str格式
    '''

    if int(num[1]) == int(num[3]) == int(num[5]) == int(num[7]) == int(num[9]) and int(num[2]) == int(num[4]) == int(
            num[6]) == int(num[8]) == int(num[10]) and int(num[1]) \
            ^ int(num[3]) ^ int(num[5]) ^ int(num[7]) ^ int(num[9]) ^ int(num[2]) ^ int(num[4]) ^ int(num[6]) ^ int(
        num[8]) ^ int(num[10]) != 0:
        return "ABABABABAB"
    elif int(num[3]) == int(num[5]) == int(num[7]) == int(num[9]) and int(num[4]) == int(num[6]) == int(num[8]) == int(
            num[10]) and int(num[3]) != int(num[4]):
        return "ABABABAB"
    elif int(num[1]) == int(num[3]) == int(num[5]) == int(num[7]) == int(num[9]) and int(num[0]) \
            == int(num[2]) == int(num[4]) == int(num[6]) == int(num[8]) and int(num[10]) != int(num[1]) != int(num[2]):
        return "ABABABABAB*"
    elif num[10] == num[9] == num[8] == num[7] == num[6] == num[5] \
            and num[5] in ('6', '8', '9') and num[5] != num[4]:
        return "689六同"
    elif num[10] == num[9] == num[8] == num[7] == num[6] == num[5] \
            and num[5] in ('0', '1', '2', '3', '5', '7') and num[5] != num[4]:
        return "012357六同"
    elif num[10] == num[9] == num[8] == num[7] == num[6] == num[5] \
            and int(num[5]) == 4 and num[5] != num[4]:
        return "444444六同"
    elif num[10] == num[9] == num[8] == num[7] == num[6] \
            and num[6] in ('6', '8', '9') and num[6] != num[5]:
        return "689五同"
    elif num[10] == num[9] == num[8] == num[7] == num[6] \
            and num[6] in ('6', '8', '9') and num[6] != num[5]:
        return "689五同"
    elif (int(num[10]) == int(num[9]) - 1 == int(num[8]) - 2 == int(num[7]) - 3 == int(num[6]) - 4 == int(
            num[5]) - 5 and int(num[5]) != int(num[4]) - 1) \
            or (int(num[10]) == int(num[9]) + 1 == int(num[8]) + 2 == int(num[7]) + 3 == int(num[6]) + 4 == int(
        num[5]) + 5 and int(num[5]) != int(num[4]) + 1):
        return "ABCDEF或FEDCBA六位升降序"
    elif num[10] == num[9] == num[8] == num[7] == num[6] \
            and num[6] in ('0', '1', '2', '3', '5', '7') and num[6] != num[5]:
        return "012357五同"
    elif num[9] == num[7] == num[5] == num[3] and (
            (int(num[10]) == int(num[8]) + 1 == int(num[6]) + 2 == int(num[4]) + 3) or (
            int(num[10]) == int(num[8]) - 1 == int(num[6]) - 2 == int(num[4]) - 3)):
        return "ABACADAE、AEADACAB隔位升降序"
    elif num[10] == num[9] == num[8] == num[7] == num[6] \
            and int(num[6]) == 4 and num[6] != num[5]:
        return "44444五同"
    elif (num[10] == num[9] == num[8] and num[7] == num[6] == num[5] and num[8] != num[7] and num[5] != num[4]) or (
            int(num[10]) == int(num[9]) + 1 == int(num[8]) + 2 and int(num[7]) + 3 and num[7:11] == num[3:7]):
        return "AAABBB或ABCDABCD"
    elif (int(num[10]) == int(num[9]) - 1 == int(num[8]) - 2 == int(num[7]) - 3 == int(num[6]) - 4 and int(
            num[6]) != int(num[5]) - 1) \
            or (int(num[10]) == int(num[9]) + 1 == int(num[8]) + 2 == int(num[7]) + 3 == int(num[6]) + 4 and int(
        num[6]) != int(num[5]) + 1):
        return "ABCDE或EDCBA五位升降序"
    elif num[10] == num[9] == num[8] == num[7] and num[7] in ('6', '8', '9') and num[7] != num[6]:
        return "689四同"
    elif num[10] == num[9] == num[8] == num[7] and num[7] in ('0', '1', '2', '3', '5', '7') and num[7] != num[6]:
        return "012357四同"
    elif (num[9] == num[8] == num[7] == num[6] == num[5] and num[10] != num[9]) or (
            int(num[10]) == int(num[9]) + 1 == int(num[8]) + 2 and num[8:11] == num[5:8]):
        return "AAAAA*、ABCABC"
    elif (int(num[10]) == int(num[9]) - 1 == int(num[8]) - 2 == int(num[7]) - 3 and int(num[7]) != int(num[6]) - 1) \
            or (
            int(num[10]) == int(num[9]) + 1 == int(num[8]) + 2 == int(num[7]) + 3 and int(num[7]) != int(num[6]) + 1):
        return "ABCD或DCBA四位升降序"
    elif num[10] == num[9] == num[8] and num[8] in ('6', '8', '9') and num[8] != num[7] and ('4' in num):
        return "689三同带4"
    elif num[10] == num[9] == num[8] and num[8] in ('6', '8', '9') and num[8] != num[7] and ('4' not in num):
        return "689三同不带4"
    elif num[10] == num[9] == num[8] == num[7] and int(num[8]) == 4 and num[7] != num[6]:
        return "4444四同"
    elif num[10] == num[9] == num[8] and num[8] in ('0', '1', '2', '3', '5', '7') and num[8] != num[7]:
        return "012357三同"
    elif num[10] == num[9] == num[8] and int(num[8]) == 4 and num[8] != num[7]:
        return "444三同"
    else:
        return "null"


