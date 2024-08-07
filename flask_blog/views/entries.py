from flask_blog import app
from flask import request,redirect,url_for,render_template,flash,session
from datetime import datetime


@app.route('/')
def show_entries():
    return '全ての記事を表示'

@app.route('/entries',methods=['GET','POST'])
def add_entry():
    return '新しく記事が追加されました'

@app.route('/entries/new',methods=['GET','POST'])
def new_entry():
    return '記事の入力フォームを表示'

@app.route('/entries/<int:id>',methods=['GET','POST'])
def show_entry(id):
    entry={
        'id': 1,
        'title':"初めての投稿",
        'text':"初めての内容",
        'created_at':datetime.now()
    }
    return render_template('entries/show.html',entry=entry)

@app.route('/entries/<int:id>/edit',methods=['GET','POST'])
def edit_entry(id):
    return f'記事{id}の編集フォームを表示'

@app.route('/entries/<int:id>/update',methods=['GET','POST'])
def update_entry(id):
    return f'記事{id}が更新されました'

@app.route('/entries/<int:id>/delete',methods=['GET','POST'])
def delete_entry(id):
    return f'記事{id}が削除されました'
