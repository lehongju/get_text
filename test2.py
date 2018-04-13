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
#获取章节名及内容
title=soup.select('.date h1')[0].text
txt=soup.find_all(class_="book_content")[0]
#删除子标签stsm，con_1
stsm=soup.find_all(id="stsm")[0]
stsm_removed=stsm.extract()
con_1=soup.find_all(class_="con_l")[0]
con_1_removed=con_1.extract()
#提取文本
txt1=txt.text
#打印生成txt文件
fo=open(title+".txt","wb")
fo.write((title).encode("utf-8"))
fo.write((txt1).encode("utf-8"))
fo.close()
print("下载成功")