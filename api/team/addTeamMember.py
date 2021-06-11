
#添加项目，并给项目添加团队成员
import requests
from api.login.login import LogIn
from api.team.searchUser import SrerchUser
from api.project.addProject import AddProject

host = "http://192.168.10.121:8088"
header = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}

class AddTeamMember:
    def __init__(self,s=requests.session()):
        self.s=s
    def addTeamMeber(self,projectid="622528328150028288",userid="605930616063528960",username="test01"):
    #def addTeamMeber(self,projectid,userid,username="test01"):
        #登陆
        lg = LogIn(self.s).login()
        url = host + "/team/add/%s"%projectid
        data= {
            "username": username,
            "projectid": projectid,
            "userid": userid
        }
        s = self.s.post(url,data)
        #res = s.json()
        #当测试异常情况时，返回的不是json格式的数据，所以这里最好用s.text
        res = s.text
        return res



if __name__ == '__main__':
    atm = AddTeamMember().addTeamMeber()
    print(atm)




