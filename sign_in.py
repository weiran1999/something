import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def sign_in():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    url = r"https://wxyqfk.zhxy.net/?yxdm=10623#/login"  
    browser.get(url)
    browser.find_element_by_css_selector('input[type][placeholder="请输入学号"].van-field__control').send_keys("XUEHAO")
    browser.find_element_by_css_selector('input[type][placeholder="请输入姓名"].van-field__control').send_keys("XINGMING")
    browser.find_element_by_css_selector('input[type][placeholder="请输入密码(初始密码为学号)"].van-field__control').send_keys("MIMA")
    #browser.find_element_by_css_selector('button.sign-in-btn.van-button.van-button--info.van-button--normal').click()
    browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/button').click()
    time.sleep(1)#有时候定位不到，就暂停一秒
    browser.find_element_by_xpath('/html/body/div[4]/div[3]').click()
    print("打卡成功")
    browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/ul/li[1]/p').click()

sign_in()

