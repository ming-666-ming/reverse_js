# coding:utf-8
"""
Name : test_boss.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/7/4 20:38
Desc:
"""
import json

import requests

url = "https://www.zhipin.com/wapi/zppassport/get/zpToken"
headers = {
    "accept": "*/*",
    "cookie":"wd_guid=789ac887-f95d-473c-ab82-dd711ea70881; historyState=state; _bl_uid=thlag0gn4kbz8yatpddvty42p0m1; lastCity=101280100; __fid=23b769e9073fc8d8a5bb96309d8de7fb; __g=-; SL_G_WPT_TO=zh; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1656979675,1656980316,1656997689,1657001494; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1657009717; wt2=DAkaXsPv2vsg5mmYGxoTSD75TYcSjktHlFkY3W_CDCtBLExhlQ7LPOa0K5MN9MF0mFLR1Jf1NCqntC4snftDHrQ~~; wbg=0; __zp_stoken__=6252dSF12FGIeQjgWBi06Z3V1YDE7AkgPBEh6fgEiJ3UsdSApQQ4CWhIDeFNDNCtyYGVNdRBIPFpJVUsSDCI4bTdRYnQoVkZCN2RFWhdRaW10OEp8NQQ+fDdDM0ctHA8JOkREJF4YSyZUbjsVKH5cT3YGAUNID2dpcBUqSBl7SzUOLiYqPgg2GiYuGAxvJT13IE5FWAlWRQ==; __c=1657001492; __l=l=/www.zhipin.com/web/geek/job?query=%E5%B0%8F%E7%B1%B3%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8&city=101280100&r=&g=&s=3&friend_source=0&s=3&friend_source=0; __a=28497587.1654607012.1656997688.1657001492.885.52.46.222",

    "x-requested-with": "XMLHttpRequest",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
for i in range(5):
    response = requests.get(url=url, headers=headers)
    data = json.loads(response.text)

    print(data["zpData"]["token"])
from datetime import datetime
import urllib3

urllib3.disable_warnings()

start_time = datetime.now()
headers = {
    "accept": "*/*",
    'cookie': 'wd_guid=789ac887-f95d-473c-ab82-dd711ea70881; historyState=state; _bl_uid=thlag0gn4kbz8yatpddvty42p0m1; lastCity=101280100; __fid=23b769e9073fc8d8a5bb96309d8de7fb; __g=-; SL_G_WPT_TO=zh; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1656933607,1656941412,1656979675,1656980316; SL_wptGlobTipTmp=1; SL_GWPT_Show_Hide_tmp=1; acw_tc=0b6e703216569836624123964e015d140e6ef4061ff0c2f656c299d823f336; wt2=DUMWPpRPzyi-w5TQbdzlvS-zLCnHU6xrFYyfmjwaGo5MarA6DxtAsWwRPWmxWThiFvzoOwYOHOZvsoo0CWBD54w~~; wbg=0; __l=l=/www.zhipin.com/web/geek/recommend&r=&g=&s=3&friend_source=0&s=3&friend_source=0; geek_zp_token=V1QNglEeL6015uVtRvyhsRIS6w6TnXxSw~; __c=1656980315; __a=28497587.1654607012.1656979674.1656980315.757.50.45.94; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1656984514; __zp_stoken__=6252dPBcNF3kjaW1zc1IEGUs2bjxQUAJcPHdjVlAxfmtmPzl6XRIYfzJoaE8SICpNGm5HJTYTRAlBTFkmGjgfMwY1HSofVEJaJAw0aSNFc0IuCQNZWXpkOlIPczl9M0EGWFd1W0RsNH4JViU=',

    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    # "x-requested-with": "XMLHttp?Request",
    "sec-fetch-mode": "navigate",
    'referer': 'https://www.zhipin.com/web/geek/job?query=小米科技有限责任公司&city=101280100',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'document'
}
data = {}

# for page in range(1,2):
#
#     url = "https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=Python&city=101280100&experience=&degree=&industry=&scale=&stage=&position=&salary=&multiBusinessDistrict=&page={page}&pageSize=30".format(
#         page=page)
#     response = requests.get(url=url, headers=headers)
#
#     zpData = json.loads(response.text)
#
#     job_list = zpData['zpData']['jobList']
#     for recruit in job_list:
#         data['securityId'] = recruit['securityId']  # securityId
#         data['encryptJobId'] = recruit['encryptJobId']    # encryptJobId.html
#         data['lid'] = recruit['lid']    # lid
#         data['brandName'] = recruit['brandName']          # 公司名字
#         if '华为' in recruit['brandName']:
#             brandName_url = 'https://www.zhipin.com/job_detail/{}.html?lid={}&securityId={}'.format(data["encryptJobId"], data['lid'], data['securityId'])
#             res_brandName = requests.get(url=brandName_url, headers=headers).text
#             print(res_brandName)


url = "https://www.zhipin.com/job_detail/aff41080ef0d30a71XVz3Ny6GVNZ.html?lid=85DpdCCiQ2m.search.15&securityId=YlnlBNyRiaGI9-g1mKC1HgB517J96X8PGWQSc4Sxcs95hYQ7jDBbQa2NPF98LTw9poGJc9_kW_6XTKkD6-_-wguVBL7vt5wb1ezmcdobbN-I0BNCxX4~"
PROXY_POOL_URL = 'http://127.0.0.1:5555/random'


def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            print(response.text)
            return response.text
    except ConnectionError:
        return None
# proxy = get_proxy()

# proxies = {
#     'http':'http://' + proxy,
#     # 'https':'https://' + proxy
# }
# response = requests.get(url=url, headers=headers)
#
# # print(response.text)
# jon_html = etree.HTML(response.text)
# job_detail = ''.join(jon_html.xpath('//div[@class="job-sec"]/div[@class="text"]//text()')).strip()
# print(job_detail)
# end_time = datetime.now() - start_time
# print(end_time)
