from selenium import webdriver
from time import sleep
from Util.read_ini import ReadIni
from Basic.find_element import FindElement
import random
from Log import record_log
testlogger=record_log.RecordLog('Register').get_log
class Register(object):
    def __init__(self, url):
        self.driver = self.get_driver(url=url)

    # 启动浏览器，打开目标测试页面url
    def get_driver(self, url):
        driver = webdriver.Firefox()
        driver.get(url=url)
        driver.maximize_window()
        return driver

    # 定位用户信息，获取元素element
    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key=key)
        return user_element

    # 输入用户信息
    def send_user_info(self, key, data):
        self.get_user_element(key=key).send_keys(data)

    # 获取随机数
    def get_range(self):
        number = ''.join(random.sample('abcdefg123456', 8))
        return number


    # 主函数
    def main(self):
        register_nickname = self.get_range()
        register_email = self.get_range() + '@163.com'
        register_password = self.get_range() + '@123'
        self.send_user_info('register_nickname', register_nickname)
        self.send_user_info('register_email', register_email)
        self.send_user_info('register_password', register_password)
        self.send_user_info('captcha_code', 1234)
        self.get_user_element('register-btn').click()
        sleep(5)
        captcha_code_error = self.get_user_element('captcha_code_error')
        if captcha_code_error is None:
            print("......恭喜你注册成功了......")
        else:
            self.driver.save_screenshot('C:/Users/lisijie/Desktop/1234.png')
            print(".......注册失败........")
        self.driver.quit()





if __name__ == "__main__":
    register_url = 'http://www.5itest.cn/register'
    r = Register(register_url)
    r.main()