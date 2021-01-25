from page_object_model.register_business import RegisterBusiness
from selenium import webdriver
import unittest
from time import sleep
import random
import csv
import codecs
from itertools import islice
import parameterized
import warnings
from Log.record_log import RecordLog
from selenium.webdriver.firefox.options import Options
from Screenshot.get_picture import Get_picture

data=csv.reader(codecs.open('C:/Users/lisijie/Desktop/123.csv','r','gbk'))
users=[]
for line in islice(data,1,None):
    users.append(line)
print(users)

log=RecordLog('RegisterTestcase').get_log()
class RegisterTestcase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.register_url = 'http://www.5itest.cn/register'
        firefox_options = Options()
        firefox_options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=firefox_options)
        self.driver.get(self.register_url)
        self.rb = RegisterBusiness(self.driver)
        self.gp=Get_picture(self.driver)


    # 注册邮箱错误，但用例执行成功
    @parameterized.parameterized.expand(users)
    def test_error(self,register_email,register_nickname,register_password,captcha_code):
        register_input=self.rb.common_register(register_email,register_nickname,register_password,captcha_code)
        print(register_email,register_nickname,register_password,captcha_code)
        filename=r'C:/Users/lisijie/Desktop/登录界面测试截图/'+register_email+register_nickname+register_password+captcha_code+'.png'
        if register_input is True:
            log.info("注册成功")
            print("注册成功\n-------------------")
        else:
            self.gp.get_picture(filename)
            log.error("注册失败")
            print("注册失败\n-------------------")

    def tearDown(self) :
        self.driver.quit()

"""
        #邮箱错误，但用例执行成功‘
        register_email_error = self.rb.register_email_error(x,y,y,z)
        print(x,y,y,z)
        if register_email_error is True:
            print("账号注册失败，该用例执行成功")
        else:
            print("账号注册成功，该用例执行失败")
        self.driver.refresh()

        #用户名错误，但用例执行成功‘
        register_nickname_error=self.rb.register_nickname_error(w,x,y,z)
        print(w,x,y,z)
        if register_nickname_error is True:
            print("账号注册失败，该用例执行成功")
        else:
            print("账号注册成功，该用例执行失败")
        self.driver.refresh()

        #密码错误，但用例执行成功‘
        register_password_error=self.rb.register_password_error(w,y,z,z)
        print(w,y,z,z)
        if register_password_error is True:
            print("账号注册失败，该用例执行成功")
        else:
            print("账号注册成功，该用例执行失败")
        self.driver.refresh()

        # 验证码错误，但用例执行成功‘
        captcha_code_error = self.rb.captcha_code_error(w,y,y,z)
        print(w,y,y,z)
        if captcha_code_error is True:
            print("账号注册失败，该用例执行成功")
        else:
            print("账号注册成功，该用例执行失败")
        self.driver.refresh()
"""

if __name__ == "__main__":
      unittest.main()

