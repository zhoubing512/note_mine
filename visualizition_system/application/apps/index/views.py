from . import index_blu
from flask import render_template,request,flash,jsonify


@index_blu.route("/")
def index():
    return "首页"


#显示学生信息
@index_blu.route('/students')
def students():
    from .models import Student
    '''学生列表'''
    student_list=Student.query.filter(Student.name=='zhoubing')
    data=[]
    print(student_list)
    for student in student_list:
        data.append({
            'id': student.id,
            'name':student.name,
            'age':student.age,
            'sex':'男' if student.sex else '女',
            'description':student.description,
            'class_number':student.class_number,
        })
    return render_template('students.html',students=data)


@index_blu.route('/student_list')
def students_list():
    from .models import Student
    '''学生列表'''
    student_list=Student.query.filter(Student.name=='zhoubing')
    data=[]
    print(student_list)
    for student in student_list:
        data.append({
            'id': student.id,
            'name':student.name,
            'age':student.age,
            'sex':'男' if student.sex else '女',
            'description':student.description,
            'class_number':student.class_number,
        })
    return jsonify(data)



@index_blu.route("/add",methods=["POST","GET"])
def add_student():
    from .models import Student
    from application import db
    if request.method == "POST":
        # 接受数据
        name = request.form.get("username")
        age = int( request.form.get("age") )if request.form.get("age") else 0
        sex = True if request.form.get("sex") == '1' else False
        class_number = request.form.get("class_number")
        description = request.form.get("description")
        # 验证数据
        if age < 0 or age > 120:
            #闪现消息[用于返回错误信息给客户端，只显示一次]
            flash("非法的年龄数值")

        # 保存入库
        student = Student(name=name,age=age,sex=sex,class_number=class_number,description=description)
        try:
            db.session.add(student)
            db.session.commit()
        except:
            # 事物回滚
            db.session.rollback()
    return render_template("add_students.html")


 