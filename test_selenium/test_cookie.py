import json
from selenium import webdriver
import time

class TestCookies():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        time.sleep(5)

    def test_get_cookies(self):
        cookies = self.driver.get_cookies()
        with open("cookies.json","w") as f:
            json.dump(cookies,f)

    def test_login_cookies(self):
        cookies = json.load(open("cookies.json"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        time.sleep(10)
        self.driver.refresh()
        time.sleep(2)

    def teardown(self):
        self.driver.quit()