import requests, json, execjs


url = 'https://yhgscx.miit.gov.cn/fuel-consumption-center/fcSearchCtr/queryList'
headers = {"Accept": 'application/json, text/plain, */*', "Authorization": '', "Content-Type": 'application/json;charset=utf-8'}


data = "{\"reportType\":\"1\",\"currentPage\":1,\"pageSize\":10,\"position\":\"right\",\"pageSizes\":[10,30,50,100,200],\"layout\":\"sizes, total,prev, pager, next, jumper\"}"
ress = requests.post(url=url, headers=headers, data=data).text
print(ress)