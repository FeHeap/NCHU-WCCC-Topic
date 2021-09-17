# -*- coding = utf-8 -*-
# @Time : 2021/9/15 下午 12:10
# @Author : Fe
# @File : app.py
# @Software : PyCharm

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/receivePOST',methods=['POST'])
def receivePOST():
    if request.method == 'POST':
        result = request.form
        print(result)
        return render_template("index.html")


if __name__ == "__main__":
    app.run()