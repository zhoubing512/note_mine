# -*- coding:utf-8 -*-

from flask import Flask,render_template,request,flash
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'zhoubing'





#配置数据库地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:zhoubing@127.0.0.1:3306/flask_sql_demo'
#跟踪数据库的修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
'''
两张表
角色（管理员、普通用户）
用户（角色ID）
'''
#数据库的模型，需要继承db.Model
class Role(db.Model):
    #定义表名
    __tablename__ = 'roles'
    #定义字段
    #db.Column 表示一个字段
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16),unique=True)

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16),unique=True)
    #db.ForeignKey('roles.id') 表示外键  表名.id
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

class LoginForm(FlaskForm):
    username = StringField('用户名：',validators=[DataRequired()])
    password = PasswordField('密码：',validators=[DataRequired()])
    password2 = PasswordField('确认密码：',validators=[DataRequired(),EqualTo('password','密码填入不一致')])
    submit = SubmitField('提交')

@app.route('/form',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if request.method == 'POST':
        username = request.form.get('username') 
        password = request.form.get('password') 
        password2 = request.form.get('password2') 
        if login_form.validate_on_submit():
            print(username,password)
            return 'success'
        else:
            flash('参数有误')
    return render_template('index.html',form=login_form)

@app.route('/',methods=['GET','POST'])
def hello_world():
    # return 'hello world!'
    # url_str = 'www.baidu.com'
    # my_list = [1,2,3,4,5]
    # my_dict = {
    #     'name':'zhangsan',
    #     'address':'乐山市'
    #         }
    return render_template('index.html',url_str=url_str,my_list=my_list,my_dict=my_dict)


@app.route('/orders/<int:order_id>')
def get_order_id(order_id):
    print(type(order_id))
    return 'order_id %s' % order_id


if __name__=='__main__':
    
    #删除表
    db.drop_all()
    #创建表
    db.create_all()
    app.run()

