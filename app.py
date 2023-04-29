from flask import Flask, render_template, abort, send_from_directory, request
import os

app = Flask(__name__)
app.static_folder = 'static'

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
     # get the current page from the query parameters
    page = request.args.get('page', pages[0])

    # find the index of the current page in the list of pages
    current_page_index = pages.index(page)

    # set the previous and next pages
    prev_page = pages[current_page_index - 1] if current_page_index > 0 else None
    next_page = pages[current_page_index + 1] if current_page_index < len(pages) - 1 else None

    return render_template('read.html', manga=manga, chapter=chapter, pages=pages,page=page, prev_page=prev_page, next_page=next_page)

@app.route('/<manga>/<chapter>/<page>')
def get_page(manga, chapter, page):
    page_path = os.path.join(manga_folder, manga, chapter, page)
    if not os.path.exists(page_path):
        abort(404)
    return send_from_directory(os.path.join(manga_folder, manga, chapter), page)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

