# -*- codeing = utf-8 -*-
# @Time : 2022/2/16 16:41
# @Author : songyuye
# @File : 1.py
# @Software: PyCharm
import requests
import re
url = 'https://www.douyin.com/video/6993227354059443487'
headers = {
    'cookie': 'ttcid=280c306974484b5683098e25648bfcb618; ttwid=1%7CWIf87MHbaS-OiziOWXwfLrNXJFlSj4qCQlyLeVXk964%7C1644996180%7Ca8fe294d33190eeee6788f5ccb489c1cc502559c6c65a876164625036706eb3d; MONITOR_WEB_ID=f9f7f1c3-8f19-4b4c-abc0-48bad35be91f; MONITOR_DEVICE_ID=15691d2f-28f3-4ba4-ad2f-4b5dfbf03484; _tea_utm_cache_6383=undefined; douyin.com; AB_LOGIN_GUIDE_TIMESTAMP=1644996180710; MONITOR_WEB_ID=9239b4bc-5c4a-4250-b88e-bce82492ccc2; s_v_web_id=verify_kzp895f7_r0dOSlWF_b5YY_4XCA_9JGO_F1xLZfyXph6D; passport_csrf_token_default=c9ea2cb52089a5eff98188176f859fa9; passport_csrf_token=c9ea2cb52089a5eff98188176f859fa9; _tea_utm_cache_1300=undefined; THEME_STAY_TIME=299294; IS_HIDE_THEME_CHANGE=1; pwa_guide_count=3; tt_scid=PWyjKyZzl3waCr.LSmF9tt5CbkiQr.bLEG9sJ6YF4EY7.kteheRqjhYJd0CRKkvkb3a7; msToken=LYM8zCYOCpXo3rO8HdlvT0ZdQHr2WGa2Qot3pnVb1IZT_WSBl8n5LMq0uD0yUDvHQVwkIflAGT2L4Y9PWPeKCo7WPAjO-H-cqkGtzfq28tmhWUwe9rtIMWSRedqpOhEu; msToken=ctNUXpAlpYJOE1wZmRFRteTtq-ZVkobQi2FEQdC7rmDo9GrdRmO24-EHhJG3LUAokRSPMRVbBrhgnG2CzfTTL6ygerWJcWrjnvPbEfqHb5RT70LmwpwyLHx7; __ac_nonce=0620cbc0d0029df96ff5a; __ac_signature=_02B4Z6wo00f01wenY8gAAIDDh6WZijjwt88Hg2dAAKPvAYkYXIPB4bTN5dsNWVBC2DgLBCgF6KLYAs6Hjdp4NJtRolT5EKs.LS9qAzlg1LjaIaVWsAfE3d8bWY7rfhTZgEYq0waV15yYi41n24; home_can_add_dy_2_desktop=1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50'
}
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
title = re.findall('<title data-react-helmet="true"> (.*?)</title>', response.text)[0]
video_data = re.findall('src(.*?)vr%3D%2',response.text)[1]
video_url = requests.utils.unquote(video_data).replace('":"', 'https:')
print(video_data)
print(video_url)
video_content = requests.get(url=video_url,headers=headers).content
with open('video\\'+ title + '.mp4', mode='wb') as f:
    f.write(video_content)
    print(title, '保存成功')