import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def sign_in():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.implicitly_wait(10) # 隐性等待，最长等10秒
    url = r"https://wxyqfk.zhxy.net/?yxdm=10623#/login"  
    browser.get(url)
    browser.find_element_by_css_selector('input[type][placeholder="请输入学号"].van-field__control').send_keys("XUEHAO")
    browser.find_element_by_css_selector('input[type][placeholder="请输入姓名"].van-field__control').send_keys("XINGMING")
    browser.find_element_by_css_selector('input[type][placeholder="请输入密码(初始密码为学号)"].van-field__control').send_keys("MIMA")
    browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/button').click()
    try:
        browser.find_element_by_xpath('/html/body/div[4]/div[3]').click()
    except:
        pass
    time.sleep(5)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/ul/li[1]/p').click()
    time.sleep(15)#必要的等待加载
    browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/button').click()
    browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[1]/p/span[1]/label').click()
    browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/p/span[1]/label').click()
    browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[3]/p/span[1]/label').click()
    browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[5]/p/span[1]/label').click()
    browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[6]/p/span[1]/label').click()
    browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[7]/button').click()
    browser.quit()
    print("打卡成功！")
    
sign_in()

