#encoding=utf-8
import logging
import os
from datetime import datetime
class RecordLog(object):
    def __init__(self,logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 2.将log信息输出到log文件中
        # 2.1 先定位看将log文件输出到哪里去
        current_dir = os.path.dirname(os.path.abspath(__file__))
        print(current_dir)  # D:\MySpace\Python\WebTesting\util
        log_dir = os.path.join('../Result')
        # 日志名称构建
        log_file_name = datetime.now().strftime("%Y-%m-%d") + '.log'
        log_file_path = log_dir + '/' + log_file_name
        print(log_file_path)

        # 2.2 好的，将日志写进log文件中
        self.file_handle = logging.FileHandler(log_file_path, 'a', encoding='utf-8')
        self.file_handle.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s %(name)s %(levelname)s ---> %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

    def get_log(self):
        return self.logger




if __name__ == "__main__":
    rl = RecordLog()
    log_info = rl.get_log()
    log_info.debug('输出到文件中去')
    rl.close_handle()
