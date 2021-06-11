
#登陆测试用例
import pytest
from api.login.login import LogIn
#from common.log2 import MyLog
from common.logs import logger

#成功登陆
def test_login01():
    res = LogIn().login()
    assert res['code'] == 1
    print(res)

#测试用例
@pytest.mark.parametrize("name,password,except1",
                        [("密码为空","",0),
                         ("错误的密码","aa",1),
                         ("正确的密码","opms123456",1)]
                        )
def test_login02(name,password,except1):
    #mylog = MyLog()
    #mylog.info("测试登录，密码为{}".format(password))
    logger.info("登录接口，{}".format(name))
    #logger.error("登录接口，{}，断言失败".format(name))
    lg = LogIn(password=password)
    res = lg.login()
    if res['code'] != except1:
        logger.error("登录接口，{}，断言失败".format(name))
    assert res['code'] == except1
    print(res)







