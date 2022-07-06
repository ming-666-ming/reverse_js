import requests

from urllib.parse import quote

from lxml import etree

query = quote('小米科技有限责任公司')

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'cookie': 'wd_guid=789ac887-f95d-473c-ab82-dd711ea70881; historyState=state; _bl_uid=thlag0gn4kbz8yatpddvty42p0m1; lastCity=101280100; __fid=23b769e9073fc8d8a5bb96309d8de7fb; __g=-; SL_G_WPT_TO=zh; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1656979675,1656980316,1656997689,1657001494; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1657004986; wt2=DJgbkBwHhGS4gsC8drX58ObquZhd6NwPMc25g4GAAhCKKvaTHNLWGg4v5zIpJjJANuPwLODxcQ3CNrv5BiS4O1A~~; wbg=0; __c=1657001492; __l=l=/www.zhipin.com/web/geek/job?query=%E5%B0%8F%E7%B1%B3%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8&city=101280100&r=&g=&s=3&friend_source=0&s=3&friend_source=0; __a=28497587.1654607012.1656997688.1657001492.855.52.16.192; __zp_stoken__=6252dSF12FGIeQjceElcXaUdgIERXU1RhEBV6fgEiJ0ZeLzYtSUxYEFNbbWdbBQtcYGVNdRBbTg88dzNdBxQWTFo4WkBeVkZCN2RFVQc/bnlPUVk8IQFUfzQSe0ctHA8JOkREJTVEXiZDYEo/MHlYSw0mIgQBBGJpcBUqSBl7S31fLSVAOxx2CU8VGAxvJT13IE5FWAlWRQ==; geek_zp_token=V1QNglEeL6015uVtRvyhoYKS616zLSzS4~'
}
data = {}
url = 'https://www.zhipin.com/job_detail/f00b569d4a2ae0fb1nN43ti1E1tW.html?lid=8clXhTtQqAL.search.11&securityId=gVtK4UtE6f3NN-x16EiyHGZ4in8uvQM_w37DPkOI9UyD42teR_zIDEjlYIWIgSeCNh8DNsJ6_-DWddPyHhrsvUgMv4qb3PnAcJmUj2YTYlSJK-BQHqijIBejiF1DZ2HQZeRLAiqf'
session = requests.Session()
response = session.get(url=url, headers=headers)
# print(response.text)
jon_html = etree.HTML(response.text)
job_detail = ''.join(jon_html.xpath('//div[@class="job-sec"]/div[@class="text"]//text()')).strip()
print(job_detail)
encryptBrandId = '6f1aa1d6b1d033ad33B43N0~'
company_info_url = 'https://www.zhipin.com/gongsi/{}.html?ka=job-comintroduce'.format(
                encryptBrandId)
res_company_info = requests.get(url=company_info_url, headers=headers)
company_info = etree.HTML(res_company_info.text)
es_company_info = ''.join(company_info.xpath('//ul[@class="company-info-list"]/li/div/text()')).strip()

print(es_company_info)
