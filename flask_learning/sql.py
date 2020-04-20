from main import *

#对数据库进行增删查改

role = Role(name='admin')
#添加到session会话
db.session.add(role)
#提交到数据库
db.session.commit()