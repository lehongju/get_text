#!/urs/bin/python3
#conding:utf-8

#引入开发包
import requests
import os
from bs4 import BeautifulSoup
import re
import time

req_url_base='http://www.qiushu.cc/t/'
#请求头,模拟浏览器
req_header={
'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Referer':'http://www.80txt.com/txtml_76675.html',
'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
}

def get_txt(txt_id):
    txt={}
    txt['title']=''
    txt['id']=str(txt_id)
    try:
        txt['id']=input("请输入需要下载的小说编号：")
        numbers=eval(input("由第几章下载："))-1
        req_url=req_url_base+ txt['id']+'/'                        #根据小说编号获取小说URL
        print("小说编号："+txt['id'])
        res=requests.get(req_url,params=req_header)             #获取小说目录界面
        res.encoding = 'utf-8
        soups=BeautifulSoup(res.text,"html.parser")           #soup转化
        #获取小说题目
        txt['title']=soups.select('.xiaoshuo .title h1')[0].text
        txt['author']=soups.select('.xiaoshuo .title .author')[0].text
        print("编号："+'{0:0>8}   '.format(txt['id'])+  "小说名：《"+txt['title']+"》  开始下载。")
        print("正在寻找第一章页面.......")
        #获取小说所有章节信息
        first_page=soups.select('.book_con_list > ul > li > a')
        #获取小说总章页面数
        section_ct=len(first_page)
        #获取小说第一章页面地址
        first_page = req_url + first_page[numbers]['href']
        #.split('/')[1]
        #设置现在下载小说章节页面
        txt_section=first_page
        #打开小说文件写入小说相关信息
        fo = open('{0:0>8}-{1}.txt'.format(txt['id'],txt['title']), "ab+")
        fo.write((txt['title']+"\r\n").encode('UTF-8'))
        fo.write((txt['author'] + "\r\n").encode('UTF-8'))
        fo.write(("******************\r\n").encode('UTF-8'))
        #进入循环，写入每章内容
        while(1):
            try:
                #请求当前章节页面
                r=requests.get(txt_section,params=req_header)
                r.encoding = 'utf-8'
                #r.encoding = 'gb18030'
                #soup转换
                soup=BeautifulSoup(r.text,"html.parser")
                #获取章节名称
                section_name=soup.select('.date h1')[0].text
                section_text = soup.find_all(class_="book_content")[0]
                #删除无用标签
                stsm = soup.find_all(id="stsm")[0]
                stsm_removed = stsm.extract()
                con_1 = soup.find_all(class_="con_l")[0]
                con_1_removed = con_1.extract()
                #获取章节文本
                section_text=re.sub( '\s+', '\r\n\t', section_text.text).strip('\r\n')#
                #获取下一章地址
                txt_section1=soup.select('.book_page a')[2]['href']
                txt_section = req_url + txt_section1
                #判断是否最后一章，当为最后一章时，会跳转至目录地址，最后一章则跳出循环
                if(txt_section1=='./'):
                    print("编号："+'{0:0>8}   '.format(txt['id'])+  "小说名：《"+txt['title']+"》 下载完成")
                    break
                #以二进制写入章节题目
                fo.write(('\r'+section_name+'\r\n').encode('UTF-8'))
                #以二进制写入章节内容
                fo.write((section_text).encode('UTF-8'))
                print(txt['title']+' 章节：'+section_name+'     已下载')
            except:
                if (txt_section1 != ''):
                    print( "小说名：《" + txt['title'] + "》" + section_name + "下一章内容为空，下载失败！")
                    print("页面地址：" + txt_section)
                    break
        fo.close()
        os.rename('{0:0>8}-{1}.txt.download'.format(txt['id'],txt['title']), '{0:0>8}-{1}.txt'.format(txt['id'],txt['title']))
    except:     #出现错误会将错误信息写入dowload.log文件，同时答应出来
        fo_err = open('dowload.log', "ab+")
        fo_err.write(('[' + time.strftime('%Y-%m-%d %X', time.localtime()) + "]：编号：" + '{0:0>8}   '.format(
            txt['id']) + "下载中断。\r\n").encode('UTF-8'))
    finally: #关闭文件
        fo_err.close()

if __name__="__main__":
    get_txt(1)

##cd get_text
#python get_text.py
