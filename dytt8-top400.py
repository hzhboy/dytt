# -*- coding:utf-8 -*-
from multiprocessing import Pool
import time
def getHtmlCode(url):
    # import urllib
    # htmlCode = urllib.urlopen(url).read()
    # return htmlCode

    import urllib2
    try:
        htmlCode = ""
        headers = {'User_Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36 Qiyu/2.1.1.2'}
        htmlCode = urllib2.urlopen(urllib2.Request(url, headers=headers), data=None, timeout=10).read()
    except:
        print "%s 跳过" %url
    else:
        return htmlCode


def getDownloadList(url):
    htmlCode = getHtmlCode(url)
    htmlCode = htmlCode.decode('gbk').encode('utf-8')  # 解决乱码
    Urllistb = htmlCode.find("发布时间")
    Urlliste = htmlCode.find("上一页")
    htmlCode = htmlCode[Urllistb:Urlliste]  # 截取中间部分

    tmp = 0
    list = []
    for i in range(htmlCode.count("href=")):
        Urllist1 = htmlCode.find("href=\"", tmp, )
        Urllist2 = htmlCode.rfind("\">", Urllist1, Urllist1 + 80)
        movlist = htmlCode[Urllist1 + 6:Urllist2]
        if movlist not in list:
            list.append(movlist)
        tmp = Urllist2 + 1
    return list

def getDownloadUrl(url):
    htmlCode = getHtmlCode(url)
    #htmlCode = htmlCode.decode('gb2312').encode('utf-8')  # 解决乱码
    if htmlCode != "":
        # 获取下载地址
        numUrl0 = htmlCode.find("td style")
        numUrl1 = htmlCode.rfind("=", numUrl0, numUrl0 + 300)
        numUrl2 = htmlCode.rfind("\">", numUrl0, numUrl0 + 300)
        movUrl = htmlCode[numUrl1 + 2:numUrl2]
        # print "%s\n" %movUrl

        # 保存文件
        file = open("C:\Users\wangzhe\Desktop\download list top400.txt", "a+")
        file.write("%s\n" % movUrl)
        file.close()
    else:
        pass

if __name__ == '__main__':
    URLlist = ("https://www.dytt8.net/html/gndy/jddy/20160320/50523.html",
               "https://www.dytt8.net/html/gndy/jddy/20160320/50523_2.html",
               "https://www.dytt8.net/html/gndy/jddy/20160320/50523_3.html",
               "https://www.dytt8.net/html/gndy/jddy/20160320/50523_4.html")
    for i in range(4):
        print(URLlist[i])
        list = getDownloadList(URLlist[i])
        print list
        pool = Pool(3)  # 创建拥有10个进程数量的进程池
        try:
            pool.map(getDownloadUrl, list)  # 处理列表中数据的函数,要处理的数据列表
            time.sleep(3)
        except:
            pass
        pool.close()  # 关闭进程池，不再接受新的进程
        pool.join()  # 主进程阻塞等待子进程的退出
        # for url in list:
        #     getDownloadUrl(url)

#下载电影top400