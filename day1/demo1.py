# -*- coding: utf-8 -*-
# @Author   : HeLaoshi
# @Time     : 2022/5/24 20:24
# @File     : demo1.py
# @Project  : pythonProject
import requests


url = 'http://www.whggzy.com/front/search/category'
headers = {
    'Accept': "*/*",
    'Content-Type': "application/json",
    'X-Requested-With': "XMLHttpRequest",
    # 最基本两个
    'Referer': 'http://www.whggzy.com/PoliciesAndRegulations/index.html?utm=sites_group_front.4dd516b0.0.0.0aeeb380992811ec85e0b5fac8c3351d',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}
data = "{\"utm\":\"sites_group_front.4dd516b0.0.0.0aeeb380992811ec85e0b5fac8c3351d\",\"categoryCode\":\"GovernmentProcurement\",\"pageSize\":15,\"pageNo\":1}"
response = requests.post(url, headers=headers, data=data).text
print(response)