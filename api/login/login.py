
#登陆
import requests
import json
import logging
import os

from common.logs import logger

host = "http://192.168.10.121:8088"
header = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
log = logging.getLogger(__name__)

class LogIn():
    def __init__(self,s=requests.session(),username="libai",password="opms123456"):
        self.s=s
        self.username=username
        self.password= password
    def login(self):
        #logger.info("ceshi")
        url = host+"/login"
        data= {
            "username" : self.username,
            "password": self.password
        }
        r = self.s.post(url,data,header)
        # 直接以字典的格式返回响应数据
        s1 = r.json()
        # 将字典类型的数据转化成json格式
        #res = json.dumps(s1, ensure_ascii=False, sort_keys=True, indent=2)
        return s1


if __name__ == '__main__':
    lg = LogIn()
    res = lg.login()
    print(res)





