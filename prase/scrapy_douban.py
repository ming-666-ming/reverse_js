import requests, re, json

url = 'https://movie.douban.com/top250'
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320"
}
resp = requests.get(url=url, headers=header)
print(resp.text)