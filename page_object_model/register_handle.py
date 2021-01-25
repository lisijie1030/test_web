from page_object_model.regitser_page import RegisterPage
from selenium import webdriver
from time import sleep
from Basic.find_element import FindElement

class RegisterHandle(object):
    def __init__(self, driver):
        self.rp = RegisterPage(driver)
        self.rs=FindElement(driver)
        self.driver=driver


    # 输入注册邮箱
    def send_register_email(self, email):
        self.rp.get_register_email().send_keys(email)

    # 输入用户昵称
    def send_register_nickname(self, nickname):
        self.rp.get_register_nickname().send_keys(nickname)

    # 输入注册密码
    def send_register_password(self, password):
        self.rp.get_register_password().send_keys(password)

    # 输入验证码
    def send_register_code(self, captcha):
        self.rp.get_getcode_num().send_keys(captcha)

    # 点击注册按钮
    def click_register_btn(self):
        self.rp.get_register_btn().click()


    def is_element_exist(self,css):
        s=self.driver.find_elements_by_css_selector(css_selector=css)
        if len(s)==0:
            return False
            #print("元素未找到:%s"%css)
        elif len(s)==1:
            return True
        else:
            print("找到%s个元素:%s"%(len(s),css))
"""
    # 获取错误信息
    def get_user_text(self, error_info):
        text = None
        if error_info == "register_email_error":
            text = self.rs.get_element("register_email_error").text
        elif error_info == 'register_nickname_error':
            text = self.rs.get_element("register_nickname_error").text
        elif error_info == 'register_password_error':
            text = self.rs.get_element("register_password_error").text
        elif error_info == "captcha_code_error":
            text = self.rs.get_element("captcha_code_error").text
        else:
            print("error element not found")
        return text
"""



if __name__ == "__main__":
    register_url = 'http://www.5itest.cn/register'
    driver = webdriver.Firefox()
    driver.get(register_url)
    rh = RegisterHandle(driver)
    rh.send_register_email('jjij@163.com')
    rh.send_register_nickname('MiFan')
    rh.send_register_password('123@123abc')
    rh.send_register_code('qwer')
    rh.click_register_btn()
    sleep(5)
    driver.close()