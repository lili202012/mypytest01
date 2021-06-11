
#获取header.yaml文件中的header数据
from common.rwYaml import ReadYaml

class GetHeader:
    def __init__(self,ry = ReadYaml("\conf\header.yaml").readyaml()):
        self.ry = ry

    #获取测试环境host
    def getdevhost(self):
        host = self.ry['host']['dev']
        return host
    #获取线上环境的host
    def getprohost(self):
        host = self.ry['host']['pro']
        return host
    #获取header
    def getheader(self):
        header = self.ry['header']
        return header


if __name__ == '__main__':
    gh = GetHeader()
    dev = gh.getdevhost()
    hd = gh.getheader()
    print(dev)
    print(hd)
