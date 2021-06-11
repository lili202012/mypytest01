
#读取yaml文件数据
import yaml
import os

class ReadYaml:
    def __init__(self,yamlPath="\conf\db1.yaml"):
        self.yamlPath = yamlPath

    #获取yaml文件的地址
    def getpath(self):
        #获取当前文件所在的目录地址
        current_dir = os.path.abspath(".")
        #获取当前脚本的地址
        #curPath = os.path.realpath(__file__)
        #获取db.yaml的地址,即用上一级的目录地址加上yamlPath
        path = os.path.dirname(current_dir) + self.yamlPath
        return path

    #读取yaml文件
    def readyaml(self):
        path = self.getpath()
        '''读取yaml文件内容
           参数path: 相对路径，起始路径：项目的根目录
           realPath: 文件的真实路径,绝对路径地址 '''
        if not os.path.isfile(path):
            raise FileNotFoundError("文件路径不存在，请检查路径是否正确：%s" % path)
        # open方法打开直接读出来
        #r表示可读，w表示可写，a表示可读可写
        # f = open(path, 'r', encoding='utf-8')
        # # 读取，此时读取出来的是字符串
        # y = f.read()
        # # 将读取的内容转化成字典，也可以直接y = yaml.load(f,Loader=yaml.FullLoader)
        # d = yaml.load(y, Loader=yaml.FullLoader)
        with open(path, 'r', encoding='utf-8') as f:
            y = f.read()
            d = yaml.load(y, Loader=yaml.FullLoader)
        return d

    #写数据到yaml中，
    def writeyaml(self):
        wpath = self.getpath()
        # 此字符串写入yaml中
        aproject = {
            "host": "localhost",
            "port": 3306,
            "user": "root",
            "password": "123456",
            "charset": "utf8"
        }
        # 若是写入中文，则要注意添加encoding='utf-8'，且dump中要添加default_flow_style=False,encoding='utf-8',allow_unicode=True
        with open(wpath, 'w', encoding='utf-8') as f:
            yaml.dump(aproject, f, default_flow_style=False, encoding='utf-8', allow_unicode=True)
        # f = open(wpath, 'w', encoding='utf-8')
        # yaml.dump(aproject, f, default_flow_style=False, encoding='utf-8', allow_unicode=True)


if __name__ == '__main__':
    #wy = ReadYaml("\conf\db.yaml").writeyaml()
    ry = ReadYaml("\conf\log.yaml").readyaml()
    print(ry)




