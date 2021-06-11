
import logging
import os

"""
  format格式设置说明：
       asctime:日期信息
       levelname:日志等级
       filename:当前执行程序的文件名
       lineno:程序运行的行数
       threadName:线程名称
       message:具体的描述信息
"""

path = os.path.dirname(os.path.abspath("."))
# 配置日志文件
logging.basicConfig(
    filename=path+'\logs\example.log',  # 保存的文件名
    level=logging.DEBUG,
    datefmt='[%Y-%m-%d %H:%M:%S]',  # 日期格式
    format='%(asctime)s %(levelname)s %(filename)s [%(lineno)d] %(threadName)s : %(message)s',  # 保存数据格式
)

logging.debug('这个是调试时记录的日志信息')
logging.info('程序正常运行时记录的日志信息')
logging.warning('程序警告记录的信息')
logging.critical("特别严重的问题")
logging.error("程序错误时的记录，比如网络请求过慢等")