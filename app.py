from flask import Flask, render_template, request, send_file
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    menu = {'home': 1, 'menu1': 0, 'menu2': 0}

    return render_template('index.html', menu=menu)


@app.route('/menu1', methods=['GET', 'POST'])
def menu1():    # 춤 일치도 분석
    menu = {'home': 0, 'menu1': 1, 'menu2': 0}
    if request.method == 'GET':
        return render_template('menu1.html', menu=menu)
    else:
        # month = int(request.form['month'])
        # region = request.form['region']
        # temp = request.form['temp']
        # temp_graph(region, month, temp)
        
        return render_template('menu1_res.html', menu=menu)


@app.route('/menu2', methods=['GET', 'POST'])
def menu2():    # 춤 입히기
    menu = {'home': 0, 'menu1': 0, 'menu2': 1}
    if request.method == 'GET':
        return render_template('menu2.html', menu=menu)
    else:
        # month = request.form['month']
        # temp = request.form['temp']
        # folium_visual(month, temp)
        # return render_template('menu2_res.html', menu=menu, month=month, temp=temp)
        
        return render_template('menu2_res.html', menu=menu)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)