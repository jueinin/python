import requests, os
from lxml import etree
def getmaxpage(mainurl):
    res=  requests.get(mainurl)
    res.encoding=  'utf-8'
    root=  etree.HTML(res.text)
    maxpage=  root.xpath('//div[@class= "pagenavi"]//a[5]//text()')
    return maxpage[0]

def getpicurl(url):
    res= requests.get(url)
    res.encoding= 'utf-8'
    root= etree.HTML(res.text)
    picurl= root.xpath('//div[@class= "main-image"]/p/a/img/@src')
    return picurl[0]
fail= 0;succ= 0
for a in [a for a in range(1,2)]:
    res= requests.get('http://www.mzitu.com/xinggan/page/'+str(a))
    res.encoding= 'utf-8'
    root= etree.HTML(res.text)
    title= root.xpath("//li/span/a/text()")
    mainurl= root.xpath('//li/span/a/@href')
    for mainurl1 in mainurl:
        os.makedirs('D:\meinv\%s'%title[mainurl.index(mainurl1)])
        for b in [m for m in range(1,int(getmaxpage(mainurl1)))]:
            req= requests.get(getpicurl(mainurl1+'/'+str(b)))
            try:
                with open('D:\meinv\%s\%s'%(title[mainurl.index(mainurl1)],getpicurl(mainurl1+'/'+str(b)).replace('/','').replace(':','')),'wb')as f:
                    f.write(req.content)
            except:
                fail= fail+1
                print('第%d个错误'%fail)
            else:
                succ= succ+1
                print('成功%d个，第%d页，第%d页'%(succ,a,mainurl.index(mainurl1)+1))



