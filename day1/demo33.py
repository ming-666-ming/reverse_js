# -*- coding: utf-8 -*-
# @Author   : HeLaoshi
# @Time     : 2022/5/24 21:59
# @File     : demo33.py
# @Project  : pythonProject
import base64

import execjs  # 执行js的=


with open('./234.js', 'r', encoding='utf-8') as f:
    jscode = f.read()
ctx = execjs.compile(jscode).call('getApiKey')
apikey = base64.b64encode(ctx.encode()).decode()
print(apikey)