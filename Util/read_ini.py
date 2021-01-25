import configparser


class ReadIni(object):
    # 初始化配置文件路径及节点加载
    def __init__(self, file_name=None, node=None):
        if file_name is None:
            self.file_name = 'C:/Users/lisijie/PycharmProjects/Register/Register/RegisterElement.ini'
        if node is None:
            self.node = 'RegisterElement'
        else:
            self.node = node

        self.cf = self.load_ini()

    # 加载配置文件
    def load_ini(self):
        cf = configparser.ConfigParser()
        cf.read(self.file_name)
        return cf

    # 获取各个配置项的值
    def get_value(self, key):
        data = self.cf.get(self.node, key)
        return data


if __name__ == "__main__":
    ri = ReadIni()
    print(ri.get_value('register_nickname'))