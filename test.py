#!/usr/bin/pyhon3
#coding:utf-8

#引入开发包
import requests
import os
from bs4 import BeautifulSoup

url='http://www.qiushu.cc/t/76675/23617439.html'
#请求头,模拟浏览器
req_header={
'Accept':'*/*',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Connection':'keep-alive',
'Cookie':'Hm_lvt_ac168fe809d6bd1c9e16493…1c9e16493d086e741e=1523111879',
'DNT':'1',
'Host':'www.80txt.com',
'Referer':'http://www.80txt.com/txtml_76675.html',
'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
'X-Requested-With':'XMLHttpRequest'
}

#请求当前章节页面  params为请求参数
r=requests.get(url,params=req_header)
r.encoding = 'utf-8'
#soup转换
soup=BeautifulSoup(r.text,"html.parser")
for ss in soup.select("#stsm"):                #删除stsm标签
	ss.decompose()
#获取章节文本
section_text=soup.select('.book_content')[0].text
#打开/创建文件
fo = open('2.txt','wb')
fo.write((section_text).encode('utf-8'))
print(section_text)
#使用完后关闭文件
fo.close()
print('下载成功')