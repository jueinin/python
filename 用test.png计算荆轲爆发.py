from PIL import Image
import pytesseract,os
if not os.path.exists(r'D:\a'):
    os.makedirs(r'D:\a')
hp=[];wufang=[];
def dengji_(dengji,gongjili):
    a = {1: {1: 0, 2: 1, 3: 0}, 2: {1: 1, 2: 1, 3: 0}, 3: {1: 1, 2: 2, 3: 0}, 4: {1: 1, 2: 2, 3: 1},
         5: {1: 1, 2: 3, 3: 1}, 6: {1: 2, 2: 3, 3: 1}, 7: {1: 1, 2: 4, 3: 1}, 8: {1: 1, 2: 4, 3: 2},
         9: {1: 1, 2: 5, 3: 2}, \
         10: {1: 3, 2: 5, 3: 2}, 11: {1: 3, 2: 6, 3: 2}, 12: {1: 3, 2: 6, 3: 3}, 13: {1: 4, 2: 6, 3: 3},
         14: {1: 5, 2: 6, 3: 3}, 15: {1: 6, 2: 6, 3: 3}}
    b = {1: {1: 200, 2: 240, 3: 280, 4: 320, 5: 360, 6: 400}, 2: {1: 390, 2: 440, 3: 490, 4: 540, 5: 590, 6: 640},
         3: {1: 450, 2: 640, 3: 830}}
    sum_of_jineng = b[1][a[dengji][1]] + b[2][a[dengji][2]] + b[3][a[dengji][3]] + 3.65 * gongjili
    return sum_of_jineng
def baofa(gongjili,dengji,hujia,HPzuidazhi,baifenbihuchuan=0.45,gudinghuchuan=96):
    shijihujia = hujia * (1 - baifenbihuchuan) - gudinghuchuan
    shanghaijianmian = shijihujia / (602 + shijihujia)
    gongjili_all = dengji_(dengji, gongjili) + gongjili
    shijishanghai = int(gongjili_all * (1 - shanghaijianmian))
    restHP = int(HPzuidazhi - shijishanghai)
    shanghaibaifenbi = shijishanghai / HPzuidazhi
    print('一套伤害约为{},占总血量的{:.2f}%剩余血量约为{}'.format(shijishanghai, shanghaibaifenbi * 100, restHP))
img=Image.open('test.png')
dengji=input('输入等级')
for j in range(1,6):
    test=img.crop((1540,357+(j-1)*132,1600,400+(j-1)*132))
    test.save(r"D:\a\wufang_"+str(j)+'.jpg')
    title = 'wufang_' + str(j) + '.jpg'
    wufang.append(pytesseract.image_to_string(Image.open(r'D:\a\\'+title)))
    HP=img.crop((1230,357+(j-1)*132,1320,400+(j-1)*132))
    HP.save(r"D:\a\HP_"+str(j)+'.jpg')
    title_hp='HP_'+str(j)+'.jpg'
    hp.append(pytesseract.image_to_string(Image.open(r'D:\a\\' + title_hp)))
    name=img.crop((283,298+132*(j-1),459,332+132*(j-1)))
    name.save(r'D:\a\name_'+str(j)+'.jpg')
    title_name='name_'+str(j)+'.jpg'
    try:
        if 'Roy' in pytesseract.image_to_string(Image.open(r'D:\a\\'+title_name)):
            gongjili_=img.crop((283+109,298+132*(j-1)+58,459,332+132*(j-1)+55))
            gongjili_.save(r'D:\a\gongjili.jpg')
            gongjili=pytesseract.image_to_string(Image.open(r'D:\a\gongjili.jpg'))
            print('攻击力',gongjili)
    except:
        pass
print(hp,wufang)
for HP,hujia in list(zip(hp,wufang)):
    baofa(int(gongjili),int(dengji),int(hujia),int(HP))



