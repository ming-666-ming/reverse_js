# coding:utf-8
"""
Name : redirests.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/7/6 9:35
Desc:
"""
import re
import time

import requests
from lxml import etree
import urllib3
from threading import Thread, Lock

urllib3.disable_warnings()
lock = Lock()


def get_page(i):
    """获取江门人才网html"""
    lock.acquire()
    print("正在爬取第{}页".format(i))

    headers = {
        'Host': 'www.jobjm.com',
        'Referer': 'https://www.jobjm.com/job/list/0-0-0-0_0_0_0_0_0_0-0-0-0-{}.html'.format(i+2),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

    }
    url = 'https://www.jobjm.com/job/list/0-0-0-0_0_0_0_0_0_0-0-0-0-{}.html'.format(i)

    response = requests.get(url=url, headers=headers, verify=False)
    parse_page(response.text, headers)
    lock.release()


def parse_page(html, headers):
    pq_html = etree.HTML(html)
    job_lists = pq_html.xpath('/html/body/div[4]/div/div[4]/div')
    for job_list in job_lists:

        job_href = job_list.xpath('./div/div[1]/div[1]/a/@href')
        data = {}
        for href in job_href:
            data['code'] = ''.join(re.findall('\d+', str(href)))
            response = requests.get(url=str(href), headers=headers)
            detail = etree.HTML(response.text)
            data['name'] = ''.join(detail.xpath('/html/body/div[5]/div[3]/div[1]/div/div[1]/h1/text()'))
            data['address'] = ''.join(detail.xpath('/html/body/div[5]/div[3]/div[1]/div/div[1]/h1/text()'))
            data['income'] = ''.join(detail.xpath('/html/body/div[5]/div[3]/div[1]/div/div[2]/span[1]/text()')).replace('￥', '')
            data['time'] = ''.join(detail.xpath('/html/body/div[5]/div[3]/div[1]/div/div[2]/div[2]/text()')).replace('更新', '')
            data['experience'] = ''.join(detail.xpath('/html/body/div[5]/div[3]/div[1]/div/div[2]/span[2]/text()'))
            data['education'] = ''.join(detail.xpath('/html/body/div[5]/div[3]/div[1]/div/div[2]/span[3]/text()'))
            data['count'] = ''.join(detail.xpath('/html/body/div[5]/div[3]/div[3]/div[1]/div[2]/div[2]/div/span/text()')).replace('招聘', '')
            data['company'] = ''.join(detail.xpath('/html/body/div[5]/div[4]/div[1]/div[2]/a/text()')).strip()
            data['nature'] = ''.join(detail.xpath('/html/body/div[5]/div[4]/div[1]/div[5]/ul/li[2]/span//text()')).strip()
            data['scale'] = ''.join(detail.xpath('/html/body/div[5]/div[4]/div[1]/div[4]/ul/li[4]/span//text()')).strip()
            data['business'] = ''.join(detail.xpath('/html/body/div[5]/div[4]/div[1]/div[4]/ul/li[1]/span/text()')).strip()
            # data['responsibility'] = ''
            # data['requirement'] = ''
            print(data)


def main():
    """线程抓取江门人才网"""
    start_time = time.time()
    for i in range(1, 21):
        thread = Thread(target=get_page, name="thread", args=(i, ))
        thread.start()

    end_time = time.time() - start_time
    print('采集耗时：{}'.format(end_time))


if __name__ == '__main__':
    main()

