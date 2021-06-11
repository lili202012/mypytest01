import csv
import os

class Readcsv:
    def __init__(self,file):
        self.file = file

    # 获取yaml文件的地址
    def getpath(self):
        # 获取当前文件所在的目录地址
        current_dir = os.path.abspath(".")
        # 获取当前脚本的地址
        # curPath = os.path.realpath(__file__)
        # 获取db.yaml的地址,即用上一级的目录地址加上yamlPath
        path = os.path.dirname(current_dir) + self.file
        return path
    #打开excel
    def open_csv(self):
        if not os.path.isfile(self.getpath()):
            raise FileNotFoundError("文件路径不存在，请检查路径是否正确：%s" % self.getpath())
        wb = open(self.getpath(),'r',encoding='gbk')
        self.wb = wb
        return wb

    #读取csv文件
    def read_csv(self):
        data = list()
        readcsv = self.open_csv()
        with readcsv as f:
            reader = csv.reader(f)
            # next(reader)，表示不读取第一行的数据
            next(reader)
            for item in reader:
                data.append(item)
        return data

    #写入csv文件
    def write_csv(self,row):
        # 1. 创建文件对象
        with open(self.getpath(),"a",newline='') as csvfile:
            # 2. 基于文件对象构建 csv写入对象
            writer = csv.writer(csvfile)
            # 3. 写入csv文件内容
            writer.writerow(row)
            #csvfile.close()  # 4. 关闭文件

if __name__ == '__main__':
    #row = ["8", "2", "哈哈", "aa", "66"]
    bb = Readcsv("\conf\csvt.csv")
    #bb.write_csv(row)
    print(bb.read_csv())
    print(type(bb.read_csv()))
    #print(readCsv("test_csv.csv"))
    #print(type(readCsv("test_csv.csv")))