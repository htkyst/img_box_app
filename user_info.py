from flask import Flask, session, redirect

USER_LIST = {}

def is_login():
    return 'login' in session

def RequireLogin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_login():
            return redirect('login')
        return func(*args, **kwargs)
    return wrapper
