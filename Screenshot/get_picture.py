from PIL import Image
from selenium import webdriver
from time import sleep
class Get_picture(object):
    def __init__(self,driver):
        self.driver=driver

    def get_picture(self,filename):
        self.driver.save_screenshot(filename)
        code_element = self.driver.find_element_by_xpath("//*[@class='col-xs-5']")
        #print("验证码的图片左上角顶点的坐标为：", code_element.location)
        #print("验证码的图片高宽的大小为：", code_element.size)

        # (3)计算图片四个定点的位置
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        image = Image.open(filename)

        # (4)将图片验证截取
        code_image = image.crop((left, top, right, height))
        code_image.save(filename)




if __name__=='__main__':
    driver=webdriver.Firefox()
    driver.get("http://www.5itest.cn/register")
    gp=Get_picture(driver)
    filename='C:/Users/lisijie/Desktop/789.png'
    gp.get_picture(filename)
    driver.quit()








