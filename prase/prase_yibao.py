import requests, json

url = 'https://translate.googleapis.com/translate_a/t?anno=3&client=te_lib&format=html&v=1.0&key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw&logld=vTE_20220523&sl=en&tl=zh-CN&tc=1&dom=1&sr=1&tk=855808.658742&mode=1'
headers = {
"user-agent": "Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320",
"x-client-data": "CIm2yQEIpbbJAQjBtskBCKmdygEIlqHLAQjnhMwBCIerzAEIsa7MAQiIsMwB"
}
data = {
    "anno":3,
    "client":"te_lib",
    "format":"html",
    "v":1.0,
    "key":"AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw",
    "logld":"vTE_20220523",
    "sl":"en",
    "tl":"zh-CN",
    "tc":"1",
    "dom":"1",
    "sr":"1",
    "tk":"855808.658742",
    "mode":1
}
res = requests.post(url=url, headers=headers, data=data)
print(res.status_code)

