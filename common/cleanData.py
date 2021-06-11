
#清除数据库数据操作
from common.dbConnect import execute_sql
from common.rwYaml import ReadYaml


class CleanData:
    #读取db.yaml文件，获取数据连接的数据
    def __init__(self,ry = ReadYaml("\conf\db.yaml").readyaml()):
        self.ry = ry
    #删除本地数据库的数据
    def cleanlocalhost(self,sql,database):
        #获取本地数据库的连接数据
        dbinfo = self.ry['localhost']
        #删除数据
        execute_sql(sql,dbinfo,database)
    #删除opms项目数据库的数据
    def cleanopms(self,sql,database):
        #获取opms项目数据库的连接数据
        dbinfo = self.ry['opms']
        #删除数据
        execute_sql(sql, dbinfo, database)

if __name__ == '__main__':
    cd = CleanData()
    # 删除数据
    sql = "delete from my_class where id=6"
    database = "qa"
    cl = cd.cleanlocalhost(sql,database)







