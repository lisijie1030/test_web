from PIL import Image
import pytesseract
import re
image =Image.open('C:/Users/lisijie/Desktop/2021.png')
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"  # 设置pyteseract路径
result = pytesseract.image_to_string(image)  # 图片转文字
resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", result)  # 去除识别出来的特殊字符
img3 = resultj[0:4]  # 只获取前4个字符
    # print(resultj)  # 打印识别的验证码
print(result)
