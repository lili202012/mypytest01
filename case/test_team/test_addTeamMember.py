
#添加项目团队成员的用例
import pytest
from api.team.searchUser import SrerchUser
from api.project.addProject import AddProject
from api.team.addTeamMember import AddTeamMember

# 添加项目然后获取项目的projectid
ap = AddProject().addProject()
#这个接口返回的是text，是字符串类型，所以可以
pid = ap['id']
# 根据用户名查找用户的userid，
name = "lock"
su = SrerchUser().searchUser(name)
uid = su[0]['value']


#测试正常添加用户
@pytest.mark.parametrize("pro,user",[(pid,uid)])
def test_addTM01(pro,user):
    #参数固定不变的，可以不用放到参数化里面，直接再请求里赋值即可，比如下面的username
    res = AddTeamMember().addTeamMeber(projectid=pro,userid=user,username=name)
    #这个接口异常时返回的不是json格式，所以这里的断言可以用in或者not in
    assert '"code":1' in res
    print(res)


#测试projectid数据异常时
@pytest.mark.parametrize("pro",["","a12"])
def test_addTM02(pro):
    res = AddTeamMember().addTeamMeber(projectid=pro,username=name)
    assert '"code":1' not in res
    print(res)

#测试userid数据异常时
@pytest.mark.parametrize("user",["","123"])
def test_addTM03(user):
    res = AddTeamMember().addTeamMeber(userid=user)
    assert '"code":1' not in res
    print(res)

#projectid和userid的交叉测试,这里已经把上面2个数据异常的情况包含了，所以上面2个可以省略的
@pytest.mark.parametrize("pro",["","a12",pid])
@pytest.mark.parametrize("user",["","123",uid])
def test_addTM04(pro,user):
    res = AddTeamMember().addTeamMeber(projectid=pro,userid=user,username=name)
    #这里虽然最后一种情况projectid和userid是正确的，但是前面第一个用例中已经添加了，所以这里仍然会是不成功的
    assert '"code":1' not in res
    print(res)

