import logging
from common.rwYaml import ReadYaml
import os

class LoggerHandler(logging.Logger):
    def __init__(self,name="root",level="DEBUG",file=None,format=None):
        super().__init__(name)
        self.setLevel(level)
        fmt = logging.Formatter(format)
        if file:
            #输出到文件
            file_handler=logging.FileHandler(file, encoding='utf-8')
            # 设置日志处理器级别
            file_handler.setLevel(level)
            #处理器按指定格式输出日志
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)
        #设置StreamHandler,输出日志到控制台
        stream_handler=logging.StreamHandler()
        stream_handler.setLevel(level)
        stream_handler.setFormatter(fmt)
        self.addHandler(stream_handler)

#  从yaml配置文件中读取logging相关配置
#ry = ReadYaml("\conf\log.yaml").readyaml()
#path = os.path.dirname(os.path.abspath("."))
logger=LoggerHandler(name="ITester",
                     level = "DEBUG",
                     file = r"E:\anzhuang\pycharm\opmsOpject\logs\example.log",
                     format = "%(asctime)s %(levelname)s %(filename)s [%(lineno)d] %(threadName)s : %(message)s")
                     #format = "%(filename)s-%(lineno)d-%(asctime)s-%(levelname)s-%(message)s")

print(os.path.abspath("../"))