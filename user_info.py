from flask import Flask, session, redirect
from functools import wraps

USER_LIST = {
    'root':'master',
}

def IsLogin():
    return 'login' in session

def TryLogin(form):
    user_id = form.get('user_id', '')
    password = form.get('password', '')
    if user_id not in USER_LIST:
        return False
    if USER_LIST[user_id] != password:
        return False
    session['login'] = user_id
    return True

def TryLogout():
    session.pop('login', None)

def GetUserID():
    return session['login'] if IsLogin() else 'No login user'

def RegistNewUser(new_user_id, new_password):
    if new_user_id in USER_LIST:
        return False
    USER_LIST[new_user_id] = new_password
    return True

def RequireLogin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not IsLogin():
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper
