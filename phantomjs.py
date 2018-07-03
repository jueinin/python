from selenium import webdriver
from lxml import etree
import requests
def get_html(url):
    drive=webdriver.PhantomJS(executable_path=r'D:\js\bin\phantomjs.exe')
    drive.get(url)
    html=drive.page_source
    drive.close()
    return html
def picurl_list(html):
    root=etree.HTML(html)
    src=root.xpath("//a[@class='img x layer-view loaded']//img/@src")
    picurl=['http:'+i for i in src]
    return picurl
def download(picurl):
    for i in picurl:
        res=requests.get(i)
        res.encoding='utf-8'
        with open(r'D:\meinv\%s.jpg'%i[26:74],'wb')as f:
            f.write(res.content)
def last_pinid_url(html):
    root=etree.HTML(html)
    pinid1=root.xpath("//a[@class='img x layer-view loaded']/@href")
    last_pinid=[i[6:-1] for i in pinid1][-1]
    last_pinid_url='http://huaban.com/favorite/beauty/?max='+last_pinid+'&limit=20&wfl=1'
    return last_pinid_url
url='http://huaban.com/favorite/beauty/'
count=0
def down(url):
    global count
    count=count+1
    a=get_html(url)
    download(picurl_list(a))
    if count<80:
        return down(last_pinid_url(a))
down(url)

