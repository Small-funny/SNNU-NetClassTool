# coding = utf-8
from selenium import webdriver
import time as tm
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import re
import requests
from PIL import Image
from io import BytesIO
import pytesseract
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

loginUrl = r'http://passport2.chaoxing.com/login?fid=1924&refer=http://i.mooc.chaoxing.com'
chromePath = r'chromedriver.exe'
#谷歌浏览器驱动下载网址：http://npm.taobao.org/mirrors/chromedriver/

ac = str(input('请输入账号'))
psw = str(input('请输入密码'))
classNumber = int(input('请输入要观看列表中第几门课程')) - 1

img_numcode = requests.get('http://passport2.chaoxing.com/num/code?1548142274872')
img = Image.open(BytesIO(img_numcode.content))

#对图片进行灰度处理
table = []
for i in range(256):
    if i < 210:
        table.append(0)
    else:
        table.append(1)
imgry = img.convert('L')
img = imgry.point(table, '1')
img.show()
numcode = str(pytesseract.image_to_string(img,lang='eng'))
numcode = numcode.replace(' ','')
print(numcode + '  xxxxx')

browser = webdriver.Chrome(executable_path=chromePath)
try:
    print("打开登录页面并登陆")
    browser.get(loginUrl)
    browser.find_element_by_name('uname').send_keys(ac)
    browser.find_element_by_name('password').send_keys(psw)
    browser.find_element_by_name('numcode').send_keys(numcode)
    browser.find_element_by_class_name('zl_btn_right').click()
except:
    pass