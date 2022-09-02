# 导入模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def login(name,password):
    # #窗口模式
    # browser = webdriver.Chrome()
    # browser.maximize_window()
    #无头模式
    chrome_options = Options()
    chrome_options.add_argument(
        'User-Agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_argument('--start-maximized')
    # browser = webdriver.Chrome(options=chrome_options)
    browser = webdriver.Remote("http://localhost:4444/wd/hub", options=chrome_options)

    url = "http://seat.ysu.edu.cn/"
    browser.get(url)
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div/div[1]/div[5]/div/div[1]/form/div[1]/div/div[1]/input').send_keys(name)
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div/div[1]/div[5]/div/div[1]/form/div[2]/div/div[1]/input').send_keys(password)
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div/div[1]/div[5]/div/div[1]/form/div[3]/div/button').click()

    #获取cookie列表
    cookie_list = browser.get_cookies()
    cookie_dict={}

    #格式化打印cookie
    for cookie in cookie_list:
        cookie_dict[cookie['name']]=cookie['value']
    browser.quit()
    c=cookie_dict['ic-cookie']
    c='ic-cookie'+'='+c
    return c
