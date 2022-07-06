# coding:utf-8
"""
Name : xiaomi.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/7/5 9:42
Desc:   crawl xiaomi job
"""
# coding:utf-8
import csv
import time

from lxml import etree

"""
Name : test_boss.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/7/4 20:38
Desc:
"""

# url = "https://www.zhipin.com/wapi/zppassport/get/zpToken"
# headers = {
#     "cookie": "wd_guid=789ac887-f95d-473c-ab82-dd711ea70881; historyState=state; _bl_uid=thlag0gn4kbz8yatpddvty42p0m1; lastCity=101280100; __g=-; SL_G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1656905412,1656905433,1656932358,1656933607; wt2=DvNlMoECz5QGZ6MzThbkHTyjNpQHrBJgDFF9GHMVthA9tGBLcxo_LuAuZ6D_zMfTREUVj3mqUxzquMxuOB0neWg~~; wbg=0; acw_tc=0b328f2a16569374425375929e011578ffad54831d8abd6e702a6132ed7a06; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1656937444; __zp_stoken__=847adCzFTIx88Exl5DikrZ3RQehRub2JLXx4uJV9fGl5zHVkBMj18PVY7aHYUMHNhHkx+ElY8c14vSwAfAzJ6bGhwTBk0Il0yQF1YUDg5NUdFKzo3TkgAITZcKgBmW0EqXHVMbCRDUDxtBXw=; __c=1656933602; __l=l=/www.zhipin.com/web/geek/job?query=Python&city=101280100&r=&g=&s=3&friend_source=0&s=3&friend_source=0; __a=28497587.1654607012.1656932354.1656933602.657.47.25.111",
#     "x-requested-with": "XMLHttpRequest",
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
# }
# for i in range(5):
#     response = requests.get(url=url, headers=headers)
#     print(response.text)
import json
from datetime import datetime
import urllib3
from parsel import Selector
from pyquery import PyQuery as pq

import requests

urllib3.disable_warnings()

start_time = datetime.now()
from urllib.parse import quote

query = quote('小米科技有限责任公司')

headers = {
    "accept": "*/*",
    "cookie": 'wd_guid=789ac887-f95d-473c-ab82-dd711ea70881; historyState=state; _bl_uid=thlag0gn4kbz8yatpddvty42p0m1; lastCity=101280100; __fid=23b769e9073fc8d8a5bb96309d8de7fb; acw_tc=0b32974e16570171501948126e012a5f8ef4a1ff0cc6f9d7ab0d0c759ac7c9; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1657001494,1657013604,1657016152,1657018719; SL_G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1657018724; wt2=Dp2oh6IWbAKQ3OXdDQaIOouX86gMzMhC7u63eEbqPRQqlO7EENKbHBvVjDpYgH7PYlFnMPQTzph9xk5IUaZ8WZw~~; wbg=0; __c=1657018719; __l=l=/www.zhipin.com/web/geek/job?query=%E5%B0%8F%E7%B1%B3%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8&city=101280100&r=&g=&s=3&friend_source=0&s=3&friend_source=0; __a=28497587.1654607012.1657016151.1657018719.963.55.5.29; __zp_stoken__=6252dPBcNF3kjaWN4bywhGUs2bjwRUxoPLxtjVlAxfhA6IyI5ABIYfzJoclVVF2VNGm5HJV5mHwZeGCAmAFVsGkZLJnUZfUZpWQMOaSNFc0IuCQMWbj1+IFIPczl9bkEGWFd1W0RsNH4JViU=',
    "x-requested-with": "XMLHttpRequest",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
headers_joblist = {
    "accept": "*/*",
    'cookie': 'wd_guid=789ac887-f95d-473c-ab82-dd711ea70881; historyState=state; _bl_uid=thlag0gn4kbz8yatpddvty42p0m1; lastCity=101280100; __fid=23b769e9073fc8d8a5bb96309d8de7fb; acw_tc=0b32974e16570171501948126e012a5f8ef4a1ff0cc6f9d7ab0d0c759ac7c9; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1657001494,1657013604,1657016152,1657018719; SL_G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1657018937; __c=1657018719; __l=l=/www.zhipin.com/web/geek/job?query=%E5%B0%8F%E7%B1%B3%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8&city=101280100&r=&g=&s=3&friend_source=0&s=3&friend_source=0; __a=28497587.1654607012.1657016151.1657018719.967.55.9.33; __zp_stoken__=6252dSF12FGIeQmJtGycxX3xReTYuSD5AKV56fgEiJ3l8KU1fAQBeDCVRZhd6XHJIYGVNdRAORB9NFGJjfQd4V0VYKmYEVkZCN2RFHFdQEnl/MHlIERsBFTUZS0ctHA8JOkRuIEBEQSZWGE03ThVSZjtdCmozAHxpcBUqSBl7S01ULE8VISwCKS4lGAxvJT13IE5FWAlWRQ==',

    # "scheme": 'https',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttp?Request",
    # "sec-fetch-mode": "navigate",
    "referer": "https://www.zhipin.com/web/geek/job?query={}&city=100010000".format(query),
}
data = {}
PROXY_POOL_URL = 'http://127.0.0.1:5555/random'

def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            print(response.text)
            return response.text
    except ConnectionError:
        return None


with open('xiaomicompayjobdetail.csv', mode='a', encoding='utf-8') as filecsv:
    fieldnames = ['brandName', 'locate', 'brandIndustry', 'brandStageName', 'brandScaleName', 'jobName', 'experience',
                  'education', 'skills', 'salaryDesc', 'welfareList', 'job_detail', 'company-info']
    writer = csv.DictWriter(filecsv, fieldnames=fieldnames)
    writer.writeheader()
    for page in range(1, 11):
        urls = "https://www.zhipin.com/wapi/zppassport/get/zpToken"
        response = requests.get(url=urls, headers=headers)
        data_token = json.loads(response.text)

        url = "https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query={}&city=101280100&experience=&degree=&industry=&scale=&stage=&position=&salary=&multiBusinessDistrict=&page={}&pageSize=30".format(query, page)

        session_1 = requests.Session()
        response = session_1.get(url=url, headers=headers_joblist)

        zpData = json.loads(response.text)

        job_list = zpData['zpData']['jobList']
        headers_job_detail = {
            'cookie': 'wd_guid=789ac887-f95d-473c-ab82-dd711ea70881; historyState=state; _bl_uid=thlag0gn4kbz8yatpddvty42p0m1; lastCity=101280100; __fid=23b769e9073fc8d8a5bb96309d8de7fb; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1657001494,1657013604,1657016152,1657018719; SL_G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; __l=l=/www.zhipin.com/web/geek/job?query=%E5%B0%8F%E7%B1%B3%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8&city=101280100&r=&g=&s=3&friend_source=0&s=3&friend_source=0; __zp_stoken__=6252dSF12FGIeQmJtGycxZ0cjdTM1VU4VAwR6fgEiJ3l8KU1fAW0GDFxyegoeSCNIYGVNdRAORB9NFGBdGzcXYC1RcEQYVkZCN2RFHFdQEnlQcmBNJRQTRBpXdEctHA8JOkRuIEATNSZIY0dxC1JDV2VWHRRQCFJpcBUqSBl7S3IaAx4HLhgHMGwKGAxvJT13IE5FWAlWRQ==; __c=1657018719; __a=28497587.1654607012.1657016151.1657018719.969.55.11.35; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1657018993',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': "zh-CN,zh;q=0.9':'zh-CN,zh;q=0.9",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        }
        for recruit in job_list:
            data['jobName'] = recruit['jobName']  # 岗位名称
            data['locate'] = "{}.{}.{}".format(recruit['cityName'], recruit['areaDistrict'],
                                               recruit['businessDistrict'])  # 工作地点
            data['salaryDesc'] = recruit['salaryDesc']  # 薪资
            data['experience'] = recruit['jobLabels'][0]  # 经验
            data['education'] = recruit['jobLabels'][1]  # 学历
            data['skills'] = "".join(recruit['skills'])  # 技能要求
            data['brandIndustry'] = recruit['brandIndustry']  # 公司类别
            data['brandStageName'] = recruit['brandStageName']  # 品牌阶段
            data['brandScaleName'] = recruit['brandScaleName']  # 员工数量
            data['welfareList'] = "".join(recruit['welfareList'])  # 福利

            securityId = ''.join(recruit['securityId']).strip()  # securityId
            encryptJobId = ''.join(recruit['encryptJobId']).strip()  # encryptJobId.html
            lid = ''.join(recruit['lid']).strip()  # lid
            encryptBrandId = recruit['encryptBrandId']  # encryptBrandId

            brandName_url = 'https://www.zhipin.com/job_detail/{}.html?lid={}&securityId={}'.format(encryptJobId,
                                                                                                    lid,
                                                                                                    securityId)
            session = requests.Session()
            res_brandName = session.get(url=brandName_url, headers=headers_job_detail)
            jon_html = etree.HTML(res_brandName.text)
            # 职位描述
            data['job_detail'] = ''.join(jon_html.xpath('//div[@class="job-sec"]/div[@class="text"]//text()')).strip()
            # 公司名字
            data['brandName'] = ''.join(jon_html.xpath('//div[@class="job-sec"]//div[@class="name"]/text()')).strip()
            # 公司介绍
            company_info_url = 'https://www.zhipin.com/gongsi/{}.html?ka=job-comintroduce'.format(
                encryptBrandId)
            res_company_info = session.get(url=company_info_url, headers=headers_job_detail)
            company_info = etree.HTML(res_company_info.text)
            data['company-info'] = ''.join(company_info.xpath('//ul[@class="company-info-list"]/li/div/text()')).strip()
            print(data)
            writer.writerow(data)


end_time = datetime.now() - start_time
print(end_time)

