import time

import requests, execjs, json

def getmcode():
    with open('../prasejs/main_shenzhen.js', 'r', encoding='utf-8') as f:
        jscode = f.read()
    mcode = execjs.compile(jscode).call("getResCode")
    return mcode


mcode = getmcode()
url = 'https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007'
headers = {
    "Referer": "https://webapi.cninfo.com.cn/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53",
    "mcode": mcode
}
data = {
    'tdate': '2022-05-24',
    'market': 'SZE'
}
res = requests.post(url=url, headers=headers, data=data)
resss = json.loads(res.text)['records']
# print(json.loads(res.text))
time.sleep(1)
# print(resss)
for i in resss:
    print(i)
    

