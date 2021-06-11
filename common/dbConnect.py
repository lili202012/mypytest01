
#连接数据库，和数据库操作方法封装
import pymysql
from common.rwYaml import ReadYaml

# dbinfo={
#     "host": "localhost",
#     "port": 3306,
#     "user": "root",
#     "password": "123456",
#     "charset":"utf8"
# }

#读取db.yaml文件，获取数据连接的数据
db = ReadYaml("\conf\db.yaml").readyaml()
dbinfo = db['localhost']

class DbConnect:
    def __init__(self,db_cof,database="qa"):
        self.db_cof = db_cof
        #打开数据库连接
        self.dbconnect = pymysql.connect(database=database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **db_cof)
        # 使用cursor()方法获取操作游标
        self.dbcursor = self.dbconnect.cursor()

    # 查询数据库
    def select(self,sql):
        try:
            # 执行sql语句
            self.dbcursor.execute(sql)
            # 获取所有记录列表
            results = self.dbcursor.fetchall()
            # print(results)
        except:
            print("Error:不能连接数据库")
        return results

    # 数据库增删改
    def execute(self,sql):
        try:
            # 执行sql语句
            self.dbcursor.execute(sql)
            # 提交到数据库执行
            self.dbconnect.commit()
        except:
            # 若是发送错误就回滚
            self.dbconnect.rollback()

    # 关闭数据库连接
    def close(self):
        self.dbconnect.close()

#数据库查询
def select_sql(sql,db_cof=dbinfo,database="qa"):
    # 连接数据库
    readdb = DbConnect(db_cof,database)
    # 查询数据
    res = readdb.select(sql)
    # 关闭数据库
    readdb.close()
    return res

#数据库增删改
def execute_sql(sql,db_cof=dbinfo,database="qa"):
    # 连接数据库
    readdb = DbConnect(db_cof,database)
    # 对数据库进行增删改
    readdb.execute(sql)
    # 关闭数据库
    readdb.close()

if __name__ == "__main__":
    #增加数据
    # sql1 = "INSERT INTO my_class (id, name, class) VALUES ('6', '数学', 'd101')"
    # a = execute_sql(sql1)

    #查询数据
    sql = "SELECT * FROM my_class WHERE name = '数学'"
    a = select_sql(sql)
    print(a)


