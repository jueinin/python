import re,requests,time,os,xlwt
from bs4 import BeautifulSoup
successful=0
fail=0
start=input('输入起始页')
finsh=input('输入结束页(包括起始和终止页)')
list1=[i for i in range(int(start),int(finsh)+1)]
for num in list1:
    url='http://www.52pojie.cn/forum-16-'+ str(num)+'.html'
    res=requests.get(url)
    res.encoding='gbk'
    soup=BeautifulSoup(res.text,'html.parser')
    a=soup.find_all(class_='s xst')
    href=[]
    title=[]
    for b in a:
        href.append(b['href'])
        title.append(b.text.replace(',',''))
    c=soup.find_all('em')
    classify=[]
    for d in c:
        e=re.compile('\[.*?\]').findall(d.text)
        if len(e)>0:
            classify.append(e[0])
    z=zip(title,href,classify)
    for z1 in z:
        m=str(z1).replace('(','').replace(')','').replace("'","")
        try:
            with open('52.txt','a')as f:
                f.write(m+'\n')
        except UnicodeEncodeError:
            fail=fail+1
            print("编码错误，第%d个错误。。。。。。。。。。。。。。。"%fail)
        else:
            print("已经到%d页了"%num)

f=open('52.txt','r')
wb=xlwt.Workbook(encoding='utf-8')
ws1=wb.add_sheet('52')
ws1.col(0).width=256*80
ws1.col(1).width=256*40
ws1.col(2).width=256*10
i=0
for line in f.readlines():
    j=0
    for item in line.split(','):
        item.strip()
        ws1.write(i,j,item)
        j+=1
    i+=1
f.close()
os.remove('52.txt')
wb.save('52.xlsx')


