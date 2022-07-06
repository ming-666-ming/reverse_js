import json
from urllib.parse import urlencode

import pymongo
import requests
from pyquery import PyQuery as pq


def parase_html():
    params = {
        "type": "uid",
        "value": "3502279044",
        "containerid": "1076033502279044"
    }
    # print(urlencode(params))
    url = "https://m.weibo.cn/api/container/getIndex?" + urlencode(params)
    headers = {

        # "referer": "https://weibo.com/u/3502279044",
        "Accept": 'application/json, text/plain, */*',
        "X-Requested-With": 'XMLHttpRequest',
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
    }

    response = requests.get(url=url, headers=headers)

    return json.loads(response.text)


def parse_page(_json):
    """
    提取内容
    :return:
    """
    if _json:
        items = _json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo


client = pymongo.MongoClient()
db = client['weibo']
collection = db['weibos']


def save_to_mongo(result):
    if collection.insert_one(result):
        print("saved to Mongo")


def main():
    """
    主函数
    :return:
    """
    _json = parase_html()
    results = parse_page(_json)

    for result in results:
        save_to_mongo(result)
        print(result)


if __name__ == "__main__":
    main()
