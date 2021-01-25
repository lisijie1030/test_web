from Util.read_ini import ReadIni
from selenium import webdriver
class FindElement(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        ri = ReadIni()
        data = ri.get_value(key=key)
        by = data.split('>')[0]
        value = data.split('>')[1]

        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element_by_className(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            file_path = '../image/no_element.png'
            self.driver.save_screenshot(file_path)


if __name__ == "__main__":
    driver=webdriver.Firefox()
    driver.get("http://www.5itest.cn/register")
    fe = FindElement(driver)
    fe.get_element('register_nickname')