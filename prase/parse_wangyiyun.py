# coding:utf-8
"""
Name : parse_wangyiyun.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/5/29 10:16
Desc: scrapy wangyiyun music
"""
import json

import requests
import urllib3

# urllib3.disable_warnings()  # 无视警告


def parse_html():
    """
    解析网页
    :return:
    """
    url = "https://music.163.com/discover/album/"
    headers = {
        "cookies": "wyy_uid=023a2d0b-8c95-426f-80d3-5ccdc8185831; locale=zh_CN; _gcl_au=1.1.1311777902.1649555658; __root_domain_v=.163.com; _qddaz=QD.756249555658732; _ntes_nuid=df892afbb13d360127ab56daa4ac40e6; _ntes_nnid=df892afbb13d360127ab56daa4ac40e6,1653790069590; NMTID=00Ohjh28OvkCUjJg0EQj0FkiVX7zEkAAAGBDZHNlg; SL_G_WPT_TO=zh; WNMCID=iydtfh.1653790070381.01.0; WEVNSM=1.0.0; SL_wptGlobTipTmp=1; SL_GWPT_Show_Hide_tmp=1; WM_TID=7ifTG3LfAJBFQVQQRAZq5tOHWF0BGt+Q; WM_NIKE=9ca17ae2e6ffcda170e2e6ee9bf321ad9dae91ec65889a8fa7c54a829f9f86c55ab59cfed2ef6ebb9cbfd3cf2af0fea7c3b92af19ea0affc4b92a7e5a9c57cb0ab858cd16388eaa19aeb7c92b5ac85c2618ce9baa9f67ef38fff8ab6508baea4d7c539f498b799f46088b5e186e525b3a7bab1ef66b590a7d1c96b929d89b5cd54abbfae8cf04d8da988b1e574bb9afe94c94383b4b6a8eb348eeba2a9d37d82b49eafcf70fb89b9a9e5338289aa85e47293e9aea7d837e2a3; WM_NI=3BPNyARy+HFpluKkRiD6oyhpRkddCkH7vHwv1Q1i7DIrl6F30HyxqTDk/ef/qyvPlnwPi0JaRCGTNXiabkmGOwHPfxyF2sJIAlzGh8N5nHPwBlRNLd9WwHf9BWfdazQ7bFU=; _iuqxldmzr_=33; JSESSIONID-WYYY=hrY6klb005DA/R00aSwD6g8HDYTPzdp8w2YhKmvNQMbU7vh5nU56UvBJkRCj4tAhi/lAB8G0hkUG5PxS9WzAUNPzBhq0/AdAs6SyJRNrtUqhsT/\447W2KJj2CEceHT9jQDExVM2Xc0Ul8MO5pESGdy+rP6ClcAIWFo0ilgdfzs99mca:1653792072034; MUSIC_U=f54550c2946fd27029df8b1f23c61cc2c77e64b33e02512ae9415263af7bdd76993166e004087dd3d6423566e40513f8e856ddaf16ce98d72887050c23e4cf3736edf5e611a0793dd4dbf082a8813684; __csrf=75108a26923b2e5db7f7d30c77818e3d; ntes_kaola_ad=1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url=url
                             )
        if response.status_code == 200:
            print(response.text)
            return json.loads(response.text, encoding='utf-8')
    except requests.ConnectionError as e:
        print("Error", e.args)


def main():
    """
    主函数
    :return:
    """
    ss = parse_html()


if __name__ == '__main__':
    main()
