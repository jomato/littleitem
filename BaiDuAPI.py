# -*- coding: utf8 -*-
import urllib2
import random
import json
import uniout
import requests
import webbrowser
import urllib

headers = {'apikey':'您的api'}#这是一个 字典中间应当用冒号


def get_joke():
    page = random.randint(1, 500)
    req = urllib2.Request( url='http://apis.baidu.com/showapi_open_bus/showapi_joke/joke_text?page=%d'% page)
    req.add_header('apikey', '您的api')
    res = urllib2.urlopen(req)
    data = res.read()
    cont = json.loads(data)#将json格式的文件转换为dict
    index = random.randint(0, 19)
    if cont.get('showapi_res_code') == 0:
        text = cont['showapi_res_body']['contentlist'][index]['text']
        text = text.replace('</p>', '').replace('<p>', '').replace('<br />', '')
        title = cont['showapi_res_body']['contentlist'][index]['title']
        print title, '\n', text
    else:
        print cont


def get_wxhot():
    raw_word = raw_input('请输入关键词:')
    param = {'word':raw_word}
    word = urllib.urlencode(param)#编码
    url = 'http://apis.baidu.com/txapi/weixin/wxhot?num=6&rand=1'
    url = url + '&' +word
    data = requests.get(url, headers=headers)
    cont = data.json()
    index = random.randint(0, 5)
    if cont.get('code')==200:
        text_url = cont['newslist'][index]['url']
        webbrowser.open(text_url)
    else:
        print cont


def ip_address():
    ip = raw_input('请输入您的ip:')
    url = 'http://apis.baidu.com/apistore/iplookupservice/iplookup?ip=' + ip
    res = requests.get(url, headers=headers)
    data = res.json()
    data_ip = data.get('retData')
    if data.get('errNum') == 0:
        print data_ip['country'], data_ip['province'], data_ip['city'], data_ip['district'], data_ip['carrier']
    else:
        print data


def get_stock():
    stock = raw_input('输入股票代码（如 sh600001, sz000001）：')
    url = 'http://apis.baidu.com/apistore/stockservice/stock?list=0&stockid=' + stock
    res = requests.get(url, headers=headers)
    data = res.json()
    print data
    if data.get('errNum') == 0:
        data_stock = data['retData']['stockinfo']
        if data_stock['closingPrice'] != 0:
            print data_stock['name'], data_stock['currentPrice'], #加逗号是为了在同一行进行输出
            percent = (data_stock['currentPrice'] - data_stock['closingPrice']) / data_stock['closingPrice'] * 100
            print '%.2f%%' % percent
        else:
            print '无效的股票代码'
    else:
        print data


while True:
    choice = raw_input('1.查IP 2.查股票 3.讲个笑话 (回车退出)\n')
    if choice == '1':
        ip_address()
    elif choice == '2':
        get_stock()
    elif choice == '3':
        get_joke()
    elif choice == '':
        break









