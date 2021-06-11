
#对excel进行操作
import openpyxl
import os

class ReadExcel:
    def __init__(self,file,sheet):
        self.file = file
        self.sheet = sheet
    def pathexcel(self):
        # 获取当前文件所在的目录地址
        current_dir = os.path.abspath(".")
        # 获取当前脚本的地址
        # curPath = os.path.realpath(__file__)
        # 获取db.yaml的地址,即用上一级的目录地址加上yamlPath
        path = os.path.dirname(current_dir) + self.file
        return path
    #打开excel
    def open_excel(self):
        wb = openpyxl.load_workbook(self.pathexcel())
        self.wb = wb
        return wb
    #获取表单
    def open_sheet(self):
        sheet = self.open_excel()[self.sheet]
        return sheet
    #读取excel数据
    def read_excel(self):
        data = list(self.open_sheet().rows)
        #print("data:%s" % data)
        reslut = []
        title = []
        # 获取第一行的数据,表头
        for tit in data[0]:
            title.append(tit.value)

        for rows in data[1:]:
            dic = {}
            # 将所有行的数据以列表的形式存储
            #enumerate()将一个可遍历的数据对象组合为一个索引序列,同时列出数据和数据下标，一般用在 for 循环当中。
            for index, row in enumerate(rows):
                dic[title[index]] = row.value

            reslut.append(dic)
        return reslut
    #修改excel数据
    def write_excel(self,row,column,value):
        sheet = self.open_sheet()
        sheet.cell(row,column).value = value
        #保存excel
        self.open_excel().save(self.pathexcel())
        #关闭excel
        #self.open_excel().close()


if __name__ == "__main__":
    aa = ReadExcel('\conf\lanren.xlsx', 'ceshi')
    result = aa.read_excel()
    #print(type(result))
    print(result)
    #cc = result[0]
    #print(type(cc))