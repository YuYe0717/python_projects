# -*- codeing = utf-8 -*-
# @Time : 2022/1/19 9:33
# @Author : songyuye
# @File : demo1.py
# @Software: PyCharm

import re
import requests
import time
from tqdm import tqdm
inp = input('请输入复制的快手分享链接：')
url = re.findall('https://v.kuaishou.com/\w{6}', inp)[0]
title = str(time.time())
headers = {
    'User-Agent': 'Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66'
}
res = requests.get(url=url, headers=headers)
url = re.findall('src="(.*?)"', res.text)[0]
res = requests.get(url)
total_size = round(int(res.headers["Content-Length"])/1024/1024)
with open('video\\'+ title +'.mp4', mode='wb') as f:
    for chunk in tqdm(iterable=res.iter_content(1024*1024), total=total_size, unit='KB'):
        f.write(chunk)

