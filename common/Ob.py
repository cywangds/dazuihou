# -*- coding:utf-8 -*-
from selenium import webdriver
import time

devie=webdriver.Chrome()
devie.get('https://www.yuntongxun.com/user/login')
devie.maximize_window()
time.sleep(5)
#devie.find_element_by_xpath('//*[@id="UN"]').click()
devie.find_element_by_xpath('//*[@id="UN"]').send_keys('yinbin@yxvzb.com')

passw=devie.find_element_by_xpath('//*[@id="PWD"]').send_keys('k*r8y(zaBAGj')
sure=devie.find_element_by_xpath('//*[@id="loginBtn"]').click()
