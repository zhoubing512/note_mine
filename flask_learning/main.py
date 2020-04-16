# -*- coding:utf-8 -*-

from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def hello_world():
    # return 'hello world!'
    url_str = 'www.baidu.com'
    my_list = [1,2,3,4,5]
    my_dict = {
        'name':'zhangsan',
        'address':'乐山市'
            }
    return render_template('index.html',url_str=url_str,my_list=my_list,my_dict=my_dict)


@app.route('/orders/<int:order_id>')
def get_order_id(order_id):
    print(type(order_id))
    return 'order_id %s' % order_id


if __name__=='__main__':
    app.run()

