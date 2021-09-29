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
def register_new_user():


def Message(mess, title="あなたに贈る言の葉"):
    return render_template('msg.html', msg=mess, title=title)

if __name__ == '__main__':
     app.run(debug=True)
