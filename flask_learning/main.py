# -*- coding:utf-8 -*-

from flask import Flask,render_template,request,flash
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'zhoubing'
'''
1、配置数据库
    a.导入sqlalchemy扩展
    b.创建db对象，并配置参数
    c.终端创建数据库
2.添加书和作者模型
    a、模型继承db.Model
    b、__tablename__：表名
    c、db.Column：字段名
    d、db.relationship：关系引用
3.添加数据
4.使用模板显示数据库查询的数据
5.使用wtf显示表单
6.实现相关的增删逻辑
'''
'''
数据库表：

Author(作者表)
id   name           books
1    zb程序员       python入门、flask入门

Book(书籍表)
id      name        autho_id(外键)多        author(应用)
1       python入门      1                       author.name=zb程序员
2       flask入门       1
'''
#定义书和作者模型
#作者模型

class Author(db.Model):
    #定义表名
    __tablename__ = 'authors'
    #定义字段
    #db.Column 表示一个字段
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16),unique=True)
    #关系应用
    #books是给自己(Author模型)用的，author是给Book模型用的
    books = db.relationship('Book', backref='author')
    def __repr__(self):
        return 'Author: %s' % self.name

#书籍模型
class Book(db.Model):
    #定义表名
    __tablename__ = 'books'
    #定义字段
    #db.Column 表示一个字段
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16),unique=True)
    author_id = db.Column(db.Integer,db.ForeignKey('authors.id'))

    def __repr__(self):
        return 'Book: %s %s' % (self.name,self.author_id)




#配置数据库地址
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:zhoubing@127.0.0.1:3306/flask_sql_demo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:zhoubing@127.0.0.1:3306/flask_books'
#跟踪数据库的修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
'''
# 两张表
# 角色（管理员、普通用户）
# 用户（角色ID）
# '''
# #数据库的模型，需要继承db.Model
# class Role(db.Model):
#     #定义表名
#     __tablename__ = 'roles'
#     #定义字段
#     #db.Column 表示一个字段
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(16),unique=True)

#     #在一的一方，写关联; users = db.relationship('Users'): 表示和Users模型发生了关联，增加了一个users属性
#     #backref='role': 表示role是Users要用的属性
#     users = db.relationship('Users', backref='role')

#     # repr()方法显示一个可读的字符串
#     def __repr__(self):
#         return '<Role: %s %s>' % (self.name,self.id)

# class Users(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(16),unique=True)
#     email = db.Column(db.String(32),unique=True)
#     password = db.Column(db.String(32))
#     #db.ForeignKey('roles.id') 表示外键  表名.id
#     role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

#     #Users 希望有一个role属性，但是这个属性的定义，需要在另一个模型中定义

#     def __repr__(self):
#         return '<User: %s %s %s %s>' % (self.name,self.id,self.email,self.password)

# class LoginForm(FlaskForm):
#     username = StringField('用户名：',validators=[DataRequired()])
#     password = PasswordField('密码：',validators=[DataRequired()])
#     password2 = PasswordField('确认密码：',validators=[DataRequired(),EqualTo('password','密码填入不一致')])
#     submit = SubmitField('提交')

# @app.route('/form',methods=['GET','POST'])
# def login():
#     login_form = LoginForm()
#     if request.method == 'POST':
#         username = request.form.get('username') 
#         password = request.form.get('password') 
#         password2 = request.form.get('password2') 
#         if login_form.validate_on_submit():
#             print(username,password)
#             return 'success'
#         else:
#             flash('参数有误')
#     return render_template('index.html',form=login_form)

@app.route('/',methods=['GET','POST'])
def hello_world():
    # return 'hello world!'
    # url_str = 'www.baidu.com'
    # my_list = [1,2,3,4,5]
    # my_dict = {
    #     'name':'zhangsan',
    #     'address':'乐山市'
    #         }
    # return render_template('index.html',url_str=url_str,my_list=my_list,my_dict=my_dict)
    return render_template('books.html')


@app.route('/orders/<int:order_id>')
def get_order_id(order_id):
    print(type(order_id))
    return 'order_id %s' % order_id


if __name__=='__main__':
    
    # #删除表
    # db.drop_all()
    # #创建表
    # db.create_all()

    # #插入角色数据
    # ro1 = Role(name='admin')
    # db.session.add(ro1)
    # db.session.commit()
    # #再插入一条数据
    # ro2 = Role(name='user')
    # db.session.add(ro2)
    # db.session.commit()

    # #插入用户数据
    # user1 = Users(name='wang',email='wang@163.com',password='123456',role_id=ro1.id)
    # user2 = Users(name='zhang',email='zhang@163.com',password='201512',role_id=ro2.id)
    # user3 = Users(name='chen',email='chen@163.com',password='987654',role_id=ro2.id)
    # user4 = Users(name='zhou',email='zhou@163.com',password='457896',role_id=ro1.id)
    # user5 = Users(name='tang',email='tang@163.com',password='156324',role_id=ro2.id)
    # user6 = Users(name='wu',email='wu@163.com',password='698543',role_id=ro2.id)
    # user7 = Users(name='qian',email='qian@163.com',password='123456',role_id=ro1.id)
    # user8 = Users(name='liu',email='liu@163.com',password='765432',role_id=ro1.id)
    # user9 = Users(name='li',email='li@163.com',password='239654',role_id=ro2.id)
    # user10 = Users(name='sun',email='sun@163.com',password='345863',role_id=ro2.id)
    # db.session.add_all([user1,user2,user3,user4,user5,user6,user7,user8,user9,user10])
    # db.session.commit()
    app.run()

