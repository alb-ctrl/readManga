from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/read')
def read():
    manga_folder = './static/manga_folder/test'
    manga_files = os.listdir(manga_folder)
    manga_pages = sorted([f for f in manga_files if f.endswith('.jpg') or f.endswith('.png')])

    return render_template('read.html', manga_pages=manga_pages)

if __name__ == '__main__':
    app.run()

