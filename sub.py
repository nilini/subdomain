# -*- coding: utf-8 -*-
import requests
import re

url = "http://www.baidu.com/s?wd=site:tom.com"
page_url = ['/s?wd=site:baidu.com']
sub_url = []
baidu = ''

def request(url):
    r = requests.get(url)
    content = r.text
    return content

def get_page_url(content):
    page_div = re.findall(r'<div id="page" >([\s\S]*?)</div>', content)
    #第一页第二页....
    page_url = re.findall(r'<a href="([\S]*?)">', page_div[0])
    #下一页
    ########
    return page_url

def get_sub_url(content):
    sub = re.findall(r'>([\S]*?)/&nbsp;</a>', content)
    return sub

baidu_html = request(url) # 首页html
page_url.extend(get_page_url(baidu_html)) # 分页url
for i in range(len(page_url)):
    p = request('http://www.baidu.com'+page_url[i])
    s = get_sub_url(p)
    sub_url.extend(s)

for i in range(len(sub_url)):
    value = sub_url[i].replace('https://','')
    print value

print len(sub_url)