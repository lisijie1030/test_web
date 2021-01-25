from page_object_model.register_handle import RegisterHandle
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from Log.record_log import RecordLog

log=RecordLog('RegisterBusiness').get_log()

class RegisterBusiness(object):
    def __init__(self, driver):
        self.rh = RegisterHandle(driver)
        self.driver=driver

    # 正常注册
    def common_register(self, register_email, nickname, password, captcha):
        self.rh.send_register_email(register_email)
        self.rh.send_register_nickname(nickname)
        self.rh.send_register_password(password)
        self.rh.send_register_code(captcha)
        self.rh.click_register_btn()
        if self.rh.is_element_exist("#register_email-error"):
            print("注册邮箱错误")
            log.info("注册邮箱错误")

        if self.rh.is_element_exist("#register_nickname-error"):
            print("用户昵称错误")
            log.info("用户昵称错误")

        if self.rh.is_element_exist("#register_password-error"):
            print("密码错误")
            log.info("密码错误")

        if self.rh.is_element_exist("#captcha_code-error"):
            print("验证码错误")
            log.info("验证码错误")






"""
    # 判断是否注册成功
   def success_or_fail(self):
        if self.rh.get_register_btn.text is None:
            print("注册失败")
            return True
        else:
            print("不知道")
            return False

    # 邮箱错误
    def register_email_error(self, register_email, nickname, password, captcha):
        self.common_register(register_email, nickname, password, captcha)
        if self.rh.get_user_text('register_email_error') =="请输入有效的电子邮件地址":
            print("注册邮箱输入错误")
            return True
        else:
            return False


    # 用户昵称错误
    def register_nickname_error(self, register_email, nickname, password, captcha):
        self.common_register(register_email, nickname, password, captcha)
        if self.rh.get_user_text('register_nickname_error')=="字符长度必须小于等于18，一个中文字算2个字符":
            print("用户昵称错误")
            return True
        else:
            return False


    # 用户密码错误
    def register_password_error(self, register_email, nickname, password, captcha):
        self.common_register(register_email, nickname, password, captcha)
        if self.rh.get_user_text('register_password_error')=="最少需要输入 5 个字符" :
            print("用户密码错误")
            return True
        else:
            return False


    # 验证码错误
    def captcha_code_error(self, register_email, nickname, password, captcha):
        self.common_register(register_email, nickname, password, captcha)
        if self.rh.get_user_text('captcha_code_error') == "验证码错误" :
            print("验证码错误")
            return True
        else:
            print("不知道")
            return False
"""


if __name__ == "__main__":
    register_url = 'http://www.5itest.cn/register'
    driver = webdriver.Firefox()
    driver.get(register_url)
    rb = RegisterBusiness(driver)
    rb.register_email_error('23', 'passed123', 'test@123', 'sds')

    sleep(3)