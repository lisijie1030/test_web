from Basic.find_element import FindElement
from selenium import webdriver

class RegisterPage(object):
    # 初始化元素查找类，执行该类的时候就会加载
    def __init__(self, driver):
        self.fe = FindElement(driver)

    # 注册邮箱
    def get_register_email(self):
        return self.fe.get_element('register_email')

    # 用户昵称
    def get_register_nickname(self):
        return self.fe.get_element('register_nickname')

    # 密码
    def get_register_password(self):
        return self.fe.get_element('register_password')

    # 验证码输入框
    def get_getcode_num(self):
        return self.fe.get_element('captcha_code')

    def get_register_btn(self):
        return self.fe.get_element('register-btn')


    # 注册邮箱框文本提示语
    def get_register_email_placeholder(self):
        print(self.fe.get_element('register_email').get_attribute('placeholder'))
        return self.fe.get_element('register_email').get_attribute('placeholder')

    # 用户昵称框文本提示语
    def get_register_nickname_placeholder(self):
        print(self.fe.get_element('register_nickname').get_attribute('placeholder'))
        return self.fe.get_element('register_nickname').get_attribute('placeholder')

    # 密码框文本提示语
    def get_register_password_placeholder(self):
        print(self.fe.get_element('register_password').get_attribute('placeholder'))
        return self.fe.get_element('register_password').get_attribute('placeholder')

    # 验证码框文本提示语
    def get_captcha_code_placeholder(self):
        print(self.fe.get_element('captcha_code').get_attribute('placeholder'))
        return self.fe.get_element('captcha_code').get_attribute('placeholder')

   # 不合法注册邮箱错误提示语
    def get_register_email_error(self):
        return self.fe.get_element('register_email_error')

    # 不合法注册用户错误提示语
    def get_register_nickname_error(self):
        return self.fe.get_element('register_nickname_error')

    # 不合法密码错误提示语
    def get_register_password_error(self):
        return self.fe.get_element('register_password_error')

    # 不合法验证码错误提示语
    def get_captcha_code_error(self):
        return self.fe.get_element('captcha_code_error')


if __name__ == "__main__":
    register_url = 'http://www.5itest.cn/register'
    driver = webdriver.Firefox()
    driver.get(register_url)
    rp = RegisterPage(driver)
    rp.get_register_email_placeholder()
    rp.get_register_nickname_placeholder()
    rp.get_register_password_placeholder()
    rp.get_captcha_code_placeholder()
    driver.close()