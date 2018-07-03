import requests,os
from lxml import etree
def get_mainpage_title_and_url(url):
    res=requests.get(url)
    res.encoding='utf-8'
    root=etree.HTML(res.text)
    href=root.xpath('//*[@id="pins"]//li/a/@href')
    title=root.xpath('//*[@id="pins"]//li/a/img/@alt')
    title_and_url=list(zip(href,title))
    return title_and_url
#get_mainpage_title_and_url('http://www.mzitu.com/xinggan')
def max_pages(url):
    res=requests.get(url)
    res.encoding='utf-8'
    root=etree.HTML(res.text)
    maxpage=root.xpath('//div[@class="pagenavi"]/a[5]/span/text()')
    return maxpage

def download(href,title):
    maxpage = max_pages(href)
    if not os.path.exists(r'D:\meinv\{}'.format(title)):
        os.makedirs(r'D:\meinv\{}'.format(title))
    for num in range(1, int(maxpage[0]) + 1):
        res=requests.get(href+'/'+str(num))
        res.encoding='utf-8'
        root=etree.HTML(res.text)
        pic_url = root.xpath('//div[@class="main-image"]/p/a/img/@src')[0]
        req=requests.get(pic_url)
        pic_url1=pic_url.replace(':','').replace('/','')
        with open(r'D:\meinv\{}\{}.jpg'.format(title,pic_url1),'wb')as f:
            f.write(req.content)
for i in range(1,3):
    mainurl='http://www.mzitu.com/xinggan/page/'+str(i)
    title_and_url=get_mainpage_title_and_url(mainurl)
    for href,title in title_and_url:
        download(href,title)





