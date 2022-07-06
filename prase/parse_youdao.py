# coding:utf-8
"""
Name : parse_youdao.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/5/31 12:38
Desc:
"""
import time

# def parse_html():
#     data = {
#         "i": "你好",
#     "from": "AUTO",
#     "to": "AUTO",
#     "smartresult": "dict",
#     "client": "fanyideskweb",
#     "salt": "16539718893708",
#     "sign": "bfe4b4e63c002753db0bc4a9b0405c66",
#     "lts": "1653971889370",
#     "bv": "f6814c1c974e0612ddcf7cf95130f445",
#     "doctype": "json",
#     "version": "2.1",
#     "keyfrom": "fanyi.web",
#     "action": "FY_BY_REALTlME"
#     }
#
# headers = {
#         "Accept": "application/json, text/javascript, */*; q=0.01",
#         "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#         "X-Requested-With": "XMLHttpRequest"
# }
#
# def get_time():
#     """
#     获取时间戳
#     :return:
#     """
#     _time = time.strftime("%Y-%m-%d: %H:%M", time.localtime(float(str(1653971889370)[0:10])))
#
#     # _time = time.strftime("%Y-%m-%d: %H:%M", time.localtime(float(str(1653971891175))[0:10]))
#     print(_time)
#
# get_time()
#
# print(len("7786c15d7aeec90f099daa04398c1089"))

import time
import random
import hashlib
import requests


def md5(obj):
    # md5加密参数
    md5 = hashlib.md5()
    md5.update(obj.encode())
    return md5.hexdigest()


def youdao(translate):
    ts = int(time.time() * 1000)
    salt = str(ts) + str(random.randint(1, 9))
    bv = md5(
        '5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36')

    sign = md5("fanyideskweb" + translate + salt + "Tbh5E8=q6U3EXe+&L[4c@")

    url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    headers = {
        'Host': 'fanyi.youdao.com',
        'Origin': '',
        'Referer': '',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-1644523005@10.108.160.100; OUTFOX_SEARCH_USER_ID_NCOO=857549368.4207594; JSESSIONID=aaahQdbLzSjY3dSU_V1Fx; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcXf1BO34WgqbzPvg3Fx; _ntes_nnid=550e7be268d446cac20d6f763fbdc8c7,1614758394523; ___rl__test__cookies=1615258741826'
    }
    data = {
        "i": translate,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "lts": ts,
        "bv": bv,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }

    res = requests.post(url, headers=headers, data=data).json()
    result = res['translateResult'][0][0]['tgt']
    return result


if __name__ == '__main__':
    translate = input('输入翻译内容：')
    result = youdao(translate)
    print(result)