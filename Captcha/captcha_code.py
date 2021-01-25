from PIL import Image
from time import sleep
from selenium import webdriver
import pytesseract
import re


class DiscernCaptcha(object):
    def __init__(self, driver):
        self.driver =driver
    # 获取照片
    def get_captcha_code_image(self):
        self.driver.save_screenshot('C:/Users/lisijie/Desktop/captcha_code.png')
        captcha_image = self.driver.find_element_by_id('getcode_num')
        left = captcha_image.location['x']
        top = captcha_image.location['y']
        right = captcha_image.size['width'] + left
        height = captcha_image.size['height'] + top
        im = Image.open('C:/Users/lisijie/Desktop/captcha_code.png')
        img = im.crop((left, top, right, height))
        img.save('C:/Users/lisijie/Desktop/captcha_code.png')
        return img

    def processing_image(self):
        img = self.get_captcha_code_image() # 获取验证码
        img1 = img.convert('L')  # 转灰度
        pixdata = img1.load()
        w, h = img1.size
        threshold = 160  # 该阈值不适合所有验证码，具体阈值请根据验证码情况设置
        # 遍历所有像素，大于阈值的为黑色
        for y in range(h):
            for x in range(w):
                if pixdata[x, y] < threshold:
                    pixdata[x, y] = 0
                else:
                    pixdata[x, y] = 255
        img1.save('C:/Users/lisijie/Desktop/captcha_code1.png')
        return img1

    def delete_spot(self):
        img2 = self.processing_image()
        data = img2.getdata()
        w, h = img2.size
        black_point = 0
        for x in range(1, w - 1):
            for y in range(1, h - 1):
                mid_pixel = data[w * y + x]  # 中央像素点像素值
                if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
                    top_pixel = data[w * (y - 1) + x]
                    left_pixel = data[w * y + (x - 1)]
                    down_pixel = data[w * (y + 1) + x]
                    right_pixel = data[w * y + (x + 1)]
                    # 判断上下左右的黑色像素点总个数
                    if top_pixel < 10:
                        black_point += 1
                    if left_pixel < 10:
                        black_point += 1
                    if down_pixel < 10:
                        black_point += 1
                    if right_pixel < 10:
                        black_point += 1
                    if black_point < 1:
                        img2.putpixel((x, y), 255)
                    black_point = 0
        img2.save('C:/Users/lisijie/Desktop/captcha_code2.png')
        return img2

    def image_str(self):
        image = self.delete_spot()
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"# 设置pyteseract路径
        result = pytesseract.image_to_string(image)  # 图片转文字
        resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", result)  # 去除识别出来的特殊字符
        img3 = resultj[0:4]  # 只获取前4个字符
        # print(resultj)  # 打印识别的验证码
        print(result)


if __name__ == "__main__":
    register_url = 'http://www.5itest.cn/register'
    driver = webdriver.Firefox()
    driver.get(register_url)
    driver.maximize_window()
    dc = DiscernCaptcha(driver)
    dc.get_captcha_code_image()
    dc.processing_image()
    dc.delete_spot()
    dc.image_str()
    driver.close()
