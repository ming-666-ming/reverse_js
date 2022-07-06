import json
import pymongo
import requests, urllib3
import time, threading


urllib3.disable_warnings()
loc = threading.Lock()
client = pymongo.MongoClient()
db = client['dog']
collections = db['dog_pictures']
# db.drop_collection('dog_pictures')


def parse_html(url):
    """
    处理网页
    :return:
    """
    loc.acquire()

    headers = {
        "Cookie": "msToken=tCJVwnyRbYtk6LOiaqUj-56-Qc3VAl6X0apRmI-NzIJE8wj3OVnk6-13z4Me8tezAw6MGLYQKVZzjoGF-N59sEcWCeoPdsf7I73kyyZM6ffo; tt_webid=7102285520604677662; _S_DPR=1.25; _S_IPAD=0; MONITOR_WEB_ID=7102285520604677662; SL_G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; ttwid=1%7C3ONEBU3gojnxJtbmzZS100OC9cTugFi3NjdnBDY-cA0%7C1653630178%7Cdc4c84d76c8698e1ab963b22ee63087e2a7ddff590b3aaf760febf7edaa85e44; _S_WIN_WH=1536_150",
        "Accept": 'application/json, text/plain, */*',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
    }

    response = requests.get(url=url, headers=headers)
    items = response.json().get('rawData').get('data')
    dog_pictures = {}
    for item in items:
        dog_pictures['text'] = item.get('text')
        dog_pictures['img_url'] = item.get('img_url')
        print(dog_pictures)
        # save_to_mongo(dog_pictures.copy())
    loc.release()


# def save_to_mongo(item):
#     if collections.insert_one(item):
#         print("saved to MongoDB")

def main():
    """
    主函数
    :return:
    """

    start_time = time.time()
    li = []
    for page in range(5):
        url = "https://so.toutiao.com/search?keyword=美女&pd=atlas&source=search_subtab_switch&dvpf=pc&aid=4916&page_num={}&rawJSON=1&search_id=202205271445500101510440284965C596".format(
            page)
        t = threading.Thread(target=parse_html, name='第{}个线程'.format(page), args=(url,))
        li.append(t)
    for i in li:

        i.start()

    end_time = time.time() - start_time

    print(end_time)


if __name__ == '__main__':
    main()
