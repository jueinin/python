from lxml import etree
import requests,pymongo,xlwt
all_href=[]
client=pymongo.MongoClient('localhost',27017)
big_href=client['big_href']
sheet1=big_href['sheet1']
'''res=requests.get('http://bj.58.com/sale.shtml')
res.encoding='utf-8'
root=etree.HTML(res.text)
big_class_href=root.xpath('//ul[@class="ym-submnu"]//li/b/a/@href')
big_class_href1=['http://www.bj.58.com'+i+'1/' for i in big_class_href]#
del big_class_href1[1]
for url in big_class_href1:'''
for url in ['http://bj.58.com/shouji/1/']:
    for num in range(1,1000):
        url1=url+'pn'+str(num)+'/'
        res=requests.get(url+'pn'+str(num)+'/')
        res.encoding='utf-8'
        root1=etree.HTML(res.text)
        if len(root1.xpath('//td[@class="t"]'))==0:
            break
        hrefs = [i for i in root1.xpath('//td[@class="t"]/a/@href') if len(i) > 40]
        all_href.extend(hrefs)
def get_message(url):
    res=requests.get(url)
    res.encoding='utf-8'
    root=etree.HTML(res.text)
    price=root.xpath('//*[@id="content"]/div[1]/div[1]/div[3]/ul/li[1]/div[2]/span[1]/text()')
    chengse=root.xpath('//*[@id="content"]/div[1]/div[1]/div[3]/ul/li[2]/div[2]/span/text()')
    title=root.xpath('//*[@id="content"]/div[1]/div[1]/div[1]/h1/text()')
    sheet1.insert_one({'title':title,'price':price,'chengse':chengse,'url':url})
for url in all_href:
    get_message(url)
wps=xlwt.Workbook(encoding='utf-8')
sheet2=wps.add_sheet('sheet2',cell_overwrite_ok=True)
sheet2.write(0,0,'标题')
sheet2.write(0,1,'价格');sheet2.write(0,2,'网址');sheet2.write(0,3,'成色')
i=0
for tiao in sheet1.find():
    sheet2.write(i,0,str(tiao['title']).replace('[','').replace(']',''))
    sheet2.write(i,1, str(tiao['price']).replace('[', '').replace(']',''))
    sheet2.write(i,2, str(tiao['url']).replace('[', '').replace(']',''))
    sheet2.write(i,3, str(tiao['chengse']).replace('[', '').replace(']',''))
    i=i+1
wps.save('58.xlsx')
