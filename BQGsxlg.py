# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import codecs
def get_url_list(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
    html = requests.get(url,headers)
    soup = BeautifulSoup(html.content, 'lxml')#content如果换成text会有乱码
    url_list = []
    list = soup.select(".zjbox > ul > li > a ")
    for i in list:
        i = i.get("href")
        i = 'https://www.qksw.com/49/49718/' + i
        url_list.append(i)
    url_list = url_list[9:-1]
    print (url_list)
    return url_list
def get_data(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'lxml')
    fo = codecs.open('output.txt', 'a+', 'utf-8');
    # 以二进制写入章节题目 需要转换为utf-8编码，否则会出现乱码
    section_name = soup.select('#main  h1')[0].text
    print (section_name)
    fo.write(('\r\n' + section_name + '\r\n'))
    section_text = soup.select('#content')
    for x in section_text:
        a = x.text.replace('readx();', '').replace('https://www.qksw.com/49/49718/', '')
        fo.write((a)+ '\r\n')
    # 以二进制写入章节内容
    fo.close()  # 关闭小说文件
if '__main__' == __name__:
    url = 'https://www.qksw.com/49/49718/'
    url_list = get_url_list(url)
    for n in url_list:
        get_data (n)

# 作者：远在远方的风比远方更远 
# 来源：CSDN 
# 原文：https://blog.csdn.net/qq_22073849/article/details/78018980 
# 版权声明：本文为博主原创文章，转载请附上博文链接！