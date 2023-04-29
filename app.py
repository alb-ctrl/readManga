from flask import Flask, render_template, abort, send_from_directory
import os

app = Flask(__name__)

manga_folder = './static/manga'

@app.route('/')
def index():
    mangas = os.listdir(manga_folder)
    return render_template('index.html', mangas=mangas)

@app.route('/<manga>/')
def list_chapters(manga):
    manga_path = os.path.join(manga_folder, manga)
    if not os.path.exists(manga_path):
        abort(404)
    chapters = sorted(os.listdir(manga_path))
    return render_template('chapters.html', manga=manga, chapters=chapters)

@app.route('/<manga>/<chapter>/')
def read(manga, chapter):
    chapter_path = os.path.join(manga_folder, manga, chapter)
    if not os.path.exists(chapter_path):
        abort(404)
    pages = sorted(os.listdir(chapter_path))
    return render_template('read.html', manga=manga, chapter=chapter, pages=pages)

@app.route('/<manga>/<chapter>/<page>')
def get_page(manga, chapter, page):
    page_path = os.path.join(manga_folder, manga, chapter, page)
    if not os.path.exists(page_path):
        abort(404)
    return send_from_directory(os.path.join(manga_folder, manga, chapter), page)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

