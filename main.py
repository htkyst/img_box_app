from flask import Flask, redirect, render_template
from flask import request, Markup
import os, time
import user_info as user

app = Flask(__name__)
app.secret_key = 'kfjgFIEJfefoej12'

@app.route('/')
@user.RequireLogin
def index():
    return render_template('index.html', user_id=user.GetUserID())

@app.route('/login')
def login():
    return render_template('login_form.html')

@app.route('/login/try', methods=['POST'])
def login_try():
    status = user.TryLogin(request.form)
    if status is False:
        return Message('ログイン失敗')
    return redirect('/')

@app.route('/logout')
@user.RequireLogin
def logout():
    user.TryLogout()
    return Message('ログアウトしました')

@app.route('/login/new_user', methods=['POST'])
def regist_user():
    return render_template('regist_user.html')

@app.route('/login/new_user/try', methods=['POST'])
def regist_try():
    new_user_id, new_password = user.GetNewUserInfo(request.form)
    if user.RegistNewUser(new_user_id, new_password):
        return render_template('index.html', user_id=new_user_id)
    else:
        return Message('そのユーザIDは使用されています')

def Message(mess, title="あなたに贈る言の葉"):
    return render_template('msg.html', msg=mess, title=title)

if __name__ == '__main__':
     app.run(debug=True)
