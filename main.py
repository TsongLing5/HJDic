#coding = utf-8
import urllib.request
import sys
import codecs
import re
import chardet   #需要导入这个模块，检测编码格式
# encode_type = chardet.detect(html)

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

url='https://dict.hjenglish.com/jp/cj/%E6%A2%A6%E6%83%B3'


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url=url,headers=headers)
html=urllib.request.urlopen(req).read()

encode_type = chardet.detect(html)
html = html.decode(encode_type['encoding']) #进行相应解码，赋给原标识符（变量）


reg='class="detail-groups"'
text=re.compile(reg)
tt=re.findall(text,html)
# req=urllib.request.urlopen(url)
print(tt)