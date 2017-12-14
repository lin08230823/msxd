# -*- coding:UTF-8 -*-

import requests

def searchweather(city='北京'):

    url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city
    req = requests.get(url)
    result = req.json()
    s = result['data']
    k = s['forecast'][0]
    print('日期：',k['date'])
    print('最高温度：',k['high'])
    print('最低温度：',k['low'])
    print('风向：',k['fengxiang'])
    print('天气：',k['type'])
if __name__ == '__main__':
    city = input('请输入城市名称：')
    searchweather(city)