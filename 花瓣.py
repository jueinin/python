import re,requests,time
count=10
def hb(mainpage):
    global count
    count=count+1
    try:
        res=requests.get(mainpage)
        res.encoding='utf-8'
        content=re.compile('app\.page\["pins"\].*').findall(res.text)[0]
        pinid_and_key=re.compile('"pin_id".{1,22}user_id.*?type').findall(content)
        pinid=[ i[9:18] for i in pinid_and_key]
        keys=[re.compile('"key":".*?"').findall(i)[0] for i in pinid_and_key]
        key=[i[7:-1] for i in keys]
        for i in key:
            url='http://img.hb.aicdn.com/'+i+'_fw658'
            res=requests.get(url)
            res.encoding='utf-8'
            with open(r'D:\meinv\%s.jpg'%i,'wb')as f:
                f.write(res.content)
        if count<2000:
            return hb('http://huaban.com/favorite/beauty/?&max='+pinid[-1]+'&limit=100&wfl=1')
    except:
        print(pinid[-1])
hb('http://huaban.com/favorite/beauty/?&max='+'554896326'+'&limit=100&wfl=1')
#last_pinid:216692173
