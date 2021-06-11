
#根据用户名查询用户
import requests
from api.login.login import LogIn

host = "http://192.168.10.121:8088"

class SrerchUser:
    def __init__(self,s=requests.session()):
        self.s=s
    def searchUser(self,term="lock"):
        #登陆
        lg = LogIn(self.s).login()
        url = host + "/user/ajax/search?term=%s"%term
        #url = host + "/user/ajax/search?term={}".format(term)
        r = self.s.get(url=url)
        res = r.json()
        return res

if __name__ == '__main__':
    su = SrerchUser().searchUser("test01")
    print(su)






