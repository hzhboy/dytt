# -*- coding:utf-8 -*-
from multiprocessing import Pool
import getpass
import urllib

def getHtmlCode(url):
    htmlCode = urllib.urlopen(url).read()
    return htmlCode

def getDownloadList(url):
    htmlCode = getHtmlCode(url)

    tmp = 0
    list = []
    for i in range(htmlCode.count("ulink")):
        Urllist2 = htmlCode.find("ulink", tmp, )
        Urllist1 = htmlCode.rfind("href", Urllist2-50, Urllist2-9)
        movlist = "https://www.dytt8.net"+htmlCode[Urllist1+6:Urllist2-9]
        if movlist not in list:
            list.append(movlist)
        tmp = Urllist2 + 1
    return list

def getDownloadUrl(url):
    htmlCode = getHtmlCode(url)
    #htmlCode = htmlCode.decode('gb2312').encode('utf-8')  # 解决乱码
    #获取下载地址
    numUrl0 = htmlCode.find("td style")
    numUrl1 = htmlCode.rfind("=", numUrl0, numUrl0+300)
    numUrl2 = htmlCode.rfind("\">", numUrl0, numUrl0+300)
    movUrl = htmlCode[numUrl1+2:numUrl2]
    #print "%s\n" %movUrl

    #保存文件
    filename = "C:/Users/" + getpass.getuser() + "/Desktop/download list.txt"
    file = open(filename, "a+")
    file.write("%s\n"%movUrl)
    file.close()

if __name__ == '__main__':

    for i in range(1, 2):
        url = "https://www.dytt8.net/html/gndy/dyzz/list_23_%d.html" % i
        print url
        list = getDownloadList(url)
        pool = Pool(10)  # 创建拥有10个进程数量的进程池
        pool.map(getDownloadUrl, list)# 处理列表中数据的函数,要处理的数据列表
        pool.close()  # 关闭进程池，不再接受新的进程
        pool.join()  # 主进程阻塞等待子进程的退出
        #for url in list:
        #   getDownloadUrl(url)
        #   print "%s : ok" % url

#下载最新电影
