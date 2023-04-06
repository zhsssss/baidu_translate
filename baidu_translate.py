# -*- coding: utf-8 -*-
# @Time : 2023/4/6 10:18
# @Author : zhi.hanshi
# @File : baidu_fy
# @Project : pythonProject1
import requests
import subprocess
import re
def get_baidu_id():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.get('https://fanyi.baidu.com/',headers=headers)
    cookies = response.cookies.get_dict()
    return cookies
cookies = {
    'BAIDUID': 'C0217226872F146DC2E0C4ED739028FC:FG=1',
    'BAIDUID_BFESS': 'C0217226872F146DC2E0C4ED739028FC:FG=1',
}
def get_token(cookies):
    # cookies = {
    #     'BAIDUID': 'C0217226872F146DC2E0C4ED739028FC:FG=1',
    #     'BAIDUID_BFESS': 'C0217226872F146DC2E0C4ED739028FC:FG=1',
    # }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'BAIDUID=C0217226872F146DC2E0C4ED739028FC:FG=1; BAIDUID_BFESS=C0217226872F146DC2E0C4ED739028FC:FG=1',
        'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    params = {
        'aldtype': '16047',
    }
    response = requests.get('https://fanyi.baidu.com/', params=params, cookies=cookies, headers=headers)
    token = re.findall(r'token: \'(.*?)\'', response.text, re.S)
    return token
cookie = get_baidu_id()
# print(cookie)
def fanyi(cookies,token,word):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://fanyi.baidu.com',
        'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    params = {
        'from': 'zh',
        'to': 'en',
    }
    word = '你好'
    result = subprocess.run(['node','baidu_fanyi_sign.js',word],capture_output=True)
    output = result.stdout.decode('utf-8').strip()
    sign = output

    data = {
        'from': 'zh',
        'to': 'en',
        'query': word,
        'simple_means_flag': '3',
        'sign': sign,
        'token': token,
        'domain': 'common',
    }
    response = requests.post('https://fanyi.baidu.com/v2transapi', params=params, cookies=cookies, headers=headers, data=data)
    print(response.json())
if __name__ == '__main__':
    # cookies = get_baidu_id()
    # token = get_token(cookies)
    # print(cookies,token)
    fanyi({'BAIDUID': 'E249B1F08853C998A59E4F1779C1AEF6:FG=1', 'BAIDUID_BFESS': 'E249B1F08853C998A59E4F1779C1AEF6:FG=1'},'f83c73e6288fe7dc3bd70745fccd481b','你好')