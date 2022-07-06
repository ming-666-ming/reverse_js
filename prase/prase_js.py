import requests
url = 'http://www.whggzy.com/front/search/category'
headers = {
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest'
}

data = "{\"utm\":\"sites_group_front.4dd516b0.0.0.0aeeb380992811ec85e0b5fac8c3351d\",\"categoryCode\":\"GovernmentProcurement\",\"pageSize\":15,\"pageNo\":1}"

res = requests.post(url=url, headers=headers, data=data).text
print(res)


url = 'http://www.whggzy.com/front/search/category'
headers = {'Content-Type': 'application/json', 'Accept': '*/*', 'X-Requested-With': 'XMLHttpRequest'}
data = "{\"utm\":\"sites_group_front.4dd516b0.0.0.0aeeb380992811ec85e0b5fac8c3351d\",\"categoryCode\":\"GovernmentProcurement\",\"pageSize\":15,\"pageNo\":1}"
responds = requests.post(url=url, headers=headers, data=data).text
import json
ress = json.loads(responds)
print(ress)