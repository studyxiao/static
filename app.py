import os

from flask import Flask, request, render_template, session, redirect, url_for, jsonify, flash, send_from_directory
from werkzeug.utils import secure_filename

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        if username == app.config.get(
                'USERNAME') and password == app.config.get('PASSWORD'):
            session['username'] = app.config.get('USERNAME')
            return redirect(url_for('manage'))
        return 'error'


@app.route('/manage', methods=['GET'])
def manage():
    if (session.get('username') == app.config.get('USERNAME')):
        filenames = File.query.all()
        # 可操作
        filenames = [{
            'name': item.name,
            'path': item.path
        } for item in filenames]
        return render_template('manage.html', filenames=filenames)
        pass

    return redirect('login')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    f = request.files['file']
    if f.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if f:
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        name = request.form['name']
        exited = File.query.filter_by(name=name).first()
        if exited:
            # 更新文件
            exited.path = filename
            db.session.commit()
        else:
            # 创建一条记录
            file = File()
            file.name = name
            file.path = filename
            db.session.add(file)
            db.session.commit()
    return redirect(url_for('manage'))


@app.route('/<filename>', methods=['GET'])
def get_file(filename):
    file = File.query.filter_by(name=filename).first()
    if not file:
        return 'error'

    return send_from_directory(app.config['UPLOAD_FOLDER'], file.path)


from model import File
