from flask import Flask, session, redirect

USER_LIST = {}

def is_login():
    return 'login' in session
