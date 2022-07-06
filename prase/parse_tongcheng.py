# coding:utf-8
"""
Name : parse_tongcheng.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/5/30 12:14
Desc: parse tongcheng hotel
"""
import requests
import pymongo, pymysql
import time
import json
from threading import Lock, Thread
from redis import StrictRedis
lock = Lock()  # 线程锁
TOTAL_ITEM = 0  # 爬取数量


# 连接MySQL
mysql_db = pymysql.connect(host='localhost', user='car', password='admin', port=3306, db='hotel')
cursor = mysql_db.cursor()

# 连接MongoDB
client =pymongo.MongoClient()
mongo_db = client['hotel']
connections = mongo_db['hotels']


# 连接redis
redis_db = StrictRedis(host='localhost', port=6379, db=0)


def parse_html(_time, page):
    """
    解析网页
    :return:
    """
    params = {
        "pageSize": "20",
        "t": _time,
        "city": "321",
        "inDate": "2022 - 05 - 30",
        "outDate": "2022 - 05 - 31",
        "filterList": "6_60000283, 8888_1",
        "pageIndex": page,
        "sugActInfo": "",
    }
    url = 'https://www.ly.com/tapi/v2/list?'
    response = requests.get(url=url, params=params)
    _json = json.loads(response.text)
    return _json


def parse_json(_json):
    """
    解析数据
    :param _json:
    :return:
    """
    items = _json.get("data").get('hotelList')
    for item in items:
        hotel_list = {}
        hotel_list["hotelAddress"] = item.get("hotelAddress")
        hotel_list["hotelName"] = item.get("hotelName")
        hotel_list["trafficInfo"] = item.get("trafficInfo")
        yield hotel_list


def get_time():
    """
    获取时间戳
    :return:
    """
    _time = round(time.time() * 1000)
    # print(_time)
    # 解析时间戳
    # time.strftime("%Y-%m-%d: %H:%M", time.localtime(float(str(_time)[0:10])))
    return _time


def save_to_redis(i, hotel):
    """
    保存到redis
    :return:
    """
    if redis_db.hmset("{i}".format(i=i), dict(hotel)):
        print("save_to_redis")


def save_to_mysql(hotel):
    """
    保存到mysql
    :return:
    """
    keys = ','.join(hotel.keys())
    # hotelAddress = hotel.get('hotelAddress')

    # hotelName = hotel.get('hotelName')
    # trafficInfo = hotel.get('trafficInfo')
    values = ','.join(['%s'] * len(hotel))
    # 创建表
    # create_db_sql = "CREATE TABLE IF NOT EXISTS hotels (hotelAddress varchar(255) NOT NULL , " \
    #                 "hotelName varchar(255) NOT NULL,  trafficInfo varchar(255) NOT NULL )"

    # 插入表
    insert_db_sql = " INSERT INTO hotels ({keys}) VALUES({values}) on DUPLICATE KEY UPDATE".format(keys=keys, values=values)

    # select_db_sql = "SELECT hotelAddress, hotelName, trafficInfo From hotels WHERE hotelAddress={hotelAddress} and " \
    #                 "hotelName={hotelName}".format(hotelAddress=hotelAddress, hotelName=hotelName)
    update_db_sql = ','.join(["{key} = %s".format(key=key) for key in hotel.keys()])
    # print(update_db_sql)
    insert_db_sql += update_db_sql
    try:
        # cursor.execute(create_db_sql)

        # if cursor.execute(insert_db_sql, (hotelAddress, hotelName, trafficInfo)):
        if cursor.execute(insert_db_sql, tuple(hotel.values())*2):
            print("Successful")
            mysql_db.commit()
    except:
        print("Failed")
        mysql_db.rollback()


def save_to_mongo(hotel):
    """
    :return:
    """
    if not connections.find_one(hotel): 
        connections.insert_one(hotel)
        print("save_to_Mongo")


def get_hotel_result(hotel_list):
    for i,hotel in enumerate(hotel_list):
        global TOTAL_ITEM
        TOTAL_ITEM += 1
        if TOTAL_ITEM % 10 == 0:
            print("已获取{}条".format(TOTAL_ITEM))
        print(hotel)
        save_to_redis(i, hotel)
        # save_to_mysql(hotel)
        # save_to_mongo(hotel=hotel)


def process_thread(i):
    lock.acquire()
    _json = parse_html(get_time(), page=i)
    hotel_list = parse_json(_json)
    get_hotel_result(hotel_list)
    lock.release()


def main():
    """
        主函数
    :return:
    """
    start_time = time.time()
    for i in range(5):
        hotel_thread = Thread(target=process_thread, args=(i,))
        hotel_thread.start()

    need_time = time.time() - start_time
    print(need_time)
    mysql_db.close()


if __name__ == '__main__':
    main()
