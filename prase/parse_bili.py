import requests
import urllib
import json


def parse_html():
    """
    解析网页
    :return:
    """
    url = "https://api.bilibili.com/x/web-interface/search/type?__refresh__=true&_extra=&context=&page=2&page_size=30&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=%E7%BE%8E%E5%A5%B3%E7%9B%B4%E6%92%AD&category_id=&search_type=video&dynamic_offset=30&preload=true&com2co=true"

    res = requests.get(url=url).text
    print(json.loads(res)['data']['result'])


def main():
    """
    主函数
    :return:
    """
    parse_html()





if __name__ == '__main__':
    main()

