
# -*- coding:utf-8 -*-
from flask import Flask,redirect,render_template,request
from common.MysqlObject import Mysqls
import requests
import os

app=Flask(__name__,template_folder='../templates',static_folder='static')



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/phone', methods=['GET', 'POST'])
def phone():
    return render_template('phone.html')

@app.route('/project', methods=['GET', 'POST'])
def project():
    # os.chdir('C:/Users/wangchaoyue/PycharmProjects/handsome')
    # os.system('python run.py')
    # return render_template('index.html')
    return render_template('project.html')

@app.route('/user/signing', methods=['GET', 'POST'])
def user_signing():

    try:
        if request.method=='POST':
            phone=request.form.get('phone')
            sql="UPDATE t_saas_user_signing set signing_status=2 where user_id=(select id from t_saas_alliance_user where phone="+phone+")"
            stas=Mysqls().get_up(sql)
            return redirect("/phone")
            # sure = requests.post(url=url, data=data, headers=header,verify=False)
            # print(sure)

    except:
        return redirect("/phone")


@app.route('/saas', methods=['GET', 'POST'])
def saas():
    return render_template('saas.html')

@app.route('/kpz', methods=['GET', 'POST'])
def kpz():

    try:
        if request.method=='POST':
            phone=request.form.get('phone')
            phonec=request.form.get('phonec')
            print(phone,phonec)
    except:
        return redirect("/phone")

@app.route('/phoneurl', methods=['GET', 'POST'])
def phoneurl():
    return render_template('index1.html')
