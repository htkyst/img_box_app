from flask import Flask, redirect, render_template
from flask import request, Markup
import os, time
import user_info as user
import page_list as *

app = Flask(__name__)

@app.route(ROOT_PAGE)
@user.RequireLogin
def index():


@app.route(LOGIN_PAGE)
def login():
    return render_template('login_form.html')

if __name__ == '__main__':
     app.run(debug=True)
