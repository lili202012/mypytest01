
#添加项目
import requests
from api.login.login import LogIn

host = "http://192.168.10.121:8088"
header = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}

class AddProject:
    def __init__(self,s=requests.session()):
        self.s=s
    def addProject(self,name="项目2",aliasname="项目02"):
        url = host+"/project/add"
        data = {
            "name": name,
            "aliasname": aliasname,
            "started": "2021-06-07",
            "ended": "2021-06-07",
            "desc": "哈哈",
            "id": "0"
        }
        #登陆
        lg = LogIn(s=self.s).login()
        r = self.s.post(url,data,header)
        res = r.json()
        return res

if __name__ == '__main__':
    ap = AddProject().addProject(name="项目3",aliasname="项目03")
    print(ap)









