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

# @app.route('/files', method=['post'])
# def files():
#     file = request.files['xxx']
#     file.filename # abc.mp4
#     path = '' + file.filename
#     file.save(path)

# 춤 일치도 분석
@app.route('/menu1', methods=['GET', 'POST'])
def menu1():
    menu = {'home': 0, 'menu1': 1, 'menu2': 0}
    if request.method == 'GET' :
        return render_template('menu1.html', menu=menu)
    else :
        # 변수1 = request.form['변수1']
        # 변수2 = request.form['변수2']
        # ...
        # 사용자함수(변수1, 변수2, ...)
        
        # return render_template('menu2_res.html', 변수1=, 변수2=, ...)
        return render_template('menu1.html', menu=menu)

# 춤 입히기
@app.route('/menu2', methods=['GET', 'POST'])
def menu2():
    menu = {'home': 0, 'menu1': 0, 'menu2': 1}
    # dance_video = './src_ref/dance/*'
    # character_images = './src_ref/character/*'
    # background_image = './src_ref/background/*'
    if request.method == 'GET':
        dance_options = [
            {'disp':'BTS - DNA', 'val':'DNA'},
            {'disp':'Blackpink - Kill this love', 'val':'Kill this love'},
            {'disp':'BTS - Dynamite', 'val':'Dynamite'},
            {'disp':'SOF - Hey mama', 'val':'Hey mama'},
            {'disp':'Aespa - Girls', 'val':'Girls'},
            {'disp':'PSY - 강남스타일', 'val':'강남스타일'},
            {'disp':'직접추가', 'val':'direct'}
        ]
        character_options = [
            {'disp':'기본1', 'val':'basic2'},
            {'disp':'기본2', 'val':'basic2'},
            {'disp':'직접녹화', 'val':'record_vid'},
            {'disp':'직접추가', 'val':'direct3'}
        ]
        background_options = [
            {'disp':'기본', 'val':'basic'},
            {'disp':'화려함', 'val':'fancy'},
            {'disp':'직접추가', 'val':'direct2'}
        ]
        
        return render_template('menu2.html', menu=menu, dance_options=dance_options,
                               background_options=background_options, character_options=character_options)
    else:
        
        #dance_video = request.form['']
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # def upload():
        #     uploaded_files = request.files.getlist("file[]")
        #     print(uploaded_files)
        # # 변수1 = request.form['변수1']
        # # 변수2 = request.form['변수2']
        # # ...
        # # 사용자함수(변수1, 변수2, ...)
        
        # # return render_template('menu2_res.html', 변수1=, 변수2=, ...)
        return render_template('menu2.html', menu=menu)
    


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5500, debug=True)