from flask import Flask, Blueprint,request,jsonify
from flask_login import LoginManager,login_required
import logging
from Controller.UserController import UserController
from Controller.BookController import BookController
from waitress import serve

app = Flask(__name__)


@app.route('/user/login',methods=['GET','POST'])
def Userlogin():
    res = UserController().UserLoginController(request.values)
    return jsonify(res)

@app.route('/user/register',methods=['GET','POST'])
def UserRegister():
    res = UserController().UserRigisterController(request.values)
    return jsonify(res)

@app.route('/user/logout',methods=['GET','POST'])
def UserLogout():
    res = UserController().UserLogOutController(request.values)
    return jsonify(res)

@app.route('/user/closeaccount',methods=['GET','POST'])
def UserCloseAccount():
    res = UserController().UserCloseAccountController(request.values)
    return jsonify(res)

@app.route('/user/changeuserinfo',methods=['GET','POST'])
def UserChangeInfo():
    res = UserController().UserChangeInfoController(request.values)
    return jsonify(res)


@app.route('/user/query',methods=['GET','POST'])
def UserQuery():
    res = UserController().UserQueryInfoController(request.values)
    return jsonify(res)

@app.route('/book/upload',methods=['GET','POST'])
def BookUpload():
    res = BookController().BookUpLoadController(request.values)
    return jsonify(res)

@app.route('/book/uploadisbn',methods=['GET','POST'])
def BookUploadIsbn():
    res = BookController().BookUpLoadISBNcontroller(request.values)
    return jsonify(res)

@app.route('/book/delete',methods=['GET','POST'])
def BookDelete():
    res = BookController().BookDeleteController(request.values)
    return jsonify(res)

@app.route('/book/changeInfo',methods=['GET','POST'])
def BookChangeInfo():
    res = BookController().BookChangeBookInfoController(request.values)
    return jsonify(res)

@app.route('/book/query',methods=['GET','post'])
def BookQuery():
    res = BookController().BookQueryController(request.values)
    return jsonify(res)


if __name__ == '__main__':
    app.debug = True

    logging.basicConfig(
                    filename='log_new.log',  # 将日志写入log_new.log文件中
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )

    app.run(host='localhost', port=5000)