import requests
from lxml import etree

url = 'https://www.hetushu.com/book/27/17756.html'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}
resp = requests.get(url,headers=headers)
# resp.encoding = 'urf-8'
print(resp.text)
e = etree.HTML(resp.text)
info = e.xpath('//div[@id="content"]/div/text()')
print(info)
info = '\n'.join(info)
title = '\n'.join(e.xpath('//div[@id="content"]/h2/text()'))

with open('douluo.txt','w',encoding='utf-8') as f:
    f.write(title+'\n'+info)