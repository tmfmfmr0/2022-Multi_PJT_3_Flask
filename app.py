from flask import Flask, redirect, render_template, request, send_file
from flask import current_app
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/')
def index():
    menu = {'home': 1, 'menu1': 0, 'menu2': 0}

    return render_template('index.html', menu=menu)

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
            {'disp':'BTS-Dynamite', 'val':'dynamite'},
            {'disp':'SOF-Hey mama', 'val':'heymama'},
            {'disp':'Aespa-Girls', 'val':'girls'},
            {'disp':'PSY-강남스타일', 'val':'gangnam'},
            {'disp':'직접선택', 'val':'direct1'}
        ]
        character_options = [
            {'disp':'기본1', 'val':'basic1'},
            {'disp':'기본2', 'val':'basic2'},
            {'disp':'직접선택', 'val':'direct2'}
        ]
        background_options = [
            {'disp':'기본', 'val':'basic'},
            {'disp':'화려함', 'val':'fancy'},
            {'disp':'직접선택', 'val':'direct3'}
        ]
        return render_template('menu2.html', menu=menu, dance_options=dance_options,
                                character_options=character_options, background_options=background_options)
    else:
        dance_options = request.form['dance_option']
        if not os.path.exists(os.path.join(current_app.root_path, 'static/upload')):
            os.makedirs(os.path.join(current_app.root_path, 'static/upload'))
        if dance_options == 'direct1':
            f_mp4 = request.files['dance_upload']
            file_mp4 = os.path.join(current_app.root_path, 'static/upload/') + f_mp4.filename
            f_mp4.save(file_mp4)
        else:
            file_mp4 = os.path.join(current_app.root_path, 'static/dance/') + dance_options + '.mp4'

        character_options = request.form['character_option']
        if not os.path.exists(os.path.join(current_app.root_path, 'static/upload')):
            os.makedirs(os.path.join(current_app.root_path, 'static/upload'))
        if character_options == 'direct2':
            f_cha_mp4 = request.files['character_upload']
            file_cha_mp4 = os.path.join(current_app.root_path, 'static/upload/') + f_cha_mp4.filename
            f_cha_mp4.save(file_cha_mp4)
        else:
            file_cha_mp4 = os.path.join(current_app.root_path, 'static/character/') + character_options + '.mp4'
            
        background_options = request.form['background_option']
        if not os.path.exists(os.path.join(current_app.root_path, 'static/upload')):
            os.makedirs(os.path.join(current_app.root_path, 'static/upload'))
        if background_options == 'direct3':
            bg_png = request.files['background_upload']
            file_bg = os.path.join(current_app.root_path, 'static/upload/') + bg_png.filename
            bg_png.save(file_bg)
        else:
            file_bg = os.path.join(current_app.root_path, 'static/character/') + background_options + '.png'
            
        return redirect('/menu2', menu=menu)
    


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5500, debug=True)