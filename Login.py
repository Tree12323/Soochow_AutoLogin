# -*- coding: utf-8 -*
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import time
import requests

class Login:
    def __init__(self, url, username, password, browser_url):
        self.username = username
        self.password = password
        self.url = url
        self.browser_url = browser_url

    def login(self):
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            browser = webdriver.Chrome(executable_path=self.browser_url, options=chrome_options)

            browser.get(self.url)
            browser.find_element_by_id('username').send_keys(self.username)
            browser.find_element_by_id('password').send_keys(self.password)
            browser.find_element_by_id('login').click()
        except:
            print(self.getCurrentTime(), "登陆函数异常")
        finally:
            browser.close()
    #获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

    #判断当前是否可以连网
    def canConnect(self):
        try:
            baidu_request=requests.get("http://www.baidu.com")
            if(baidu_request.status_code==200):
                baidu_request.encoding = 'utf-8'
                baidu_request_bsObj = BeautifulSoup(baidu_request.text, 'html.parser')
                baidu_input = baidu_request_bsObj.find(value="百度一下")
                if baidu_input==None:
                    return False
                return True
            else:
                return False
        except:
            print('error')

    #主函数
    def main(self):
        print(self.getCurrentTime(), "自动登陆脚本正在运行")
        while True:
            while True:
                can_connect = self.canConnect()
                if not can_connect:
                    print(self.getCurrentTime(), "断网了...")
                    try:
                        self.login()
                    except:
                        print(self.getCurrentTime(), "浏览器出了bug")
                    finally:
                        time.sleep(2)
                        if self.canConnect():
                            print(self.getCurrentTime(), "重新登陆成功")
                        else:
                            print(self.getCurrentTime(), "登陆失败，再来一次")
                else:
                    print(self.getCurrentTime(), "一切正常...")
                    time.sleep(60)
                time.sleep(1)
            time.sleep(self.every)

if __name__ == "__main__":
    # 学号
    username = '*********'

    # 密码
    password = '**********'

    # 登陆网址
    url = 'http://a.suda.edu.cn/'

    # 使用Chrome
    browser_url = './chromedriver'

    # 使用Firefox
    # browser_url = './geckodriver'

    login = Login(
        username=username,
        password=password,
        url=url,
        browser_url=browser_url,
    )
    login.main()

