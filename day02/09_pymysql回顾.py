'''创建库spiderdb,表t1,插入1条记录'''
import pymysql
# 处理警告模块
import warnings

# 过滤警告,hu lue yu ju xia de jing gao
warnings.filterwarnings("ignore")

# 创建数据库连接对象
db = pymysql.connect("localhost",
                     "root",
                     "123456",
                     charset="utf8")
# 创建游标对象
cursor = db.cursor()
# 利用游标对象的execute()方法执行命令
cdb='create database if not exists \
    spiderdb charset utf8'
udb = 'use spiderdb'
ctab = 'create table if not exists \
        t1(id int)'
ins = 'insert into t1 values(1)'

cursor.execute(cdb)
cursor.execute(udb)
cursor.execute(ctab)
cursor.execute(ins)

# 提交到数据库执行
db.commit()
# 关闭游标
cursor.close()
# 断开数据库连接
db.close()










