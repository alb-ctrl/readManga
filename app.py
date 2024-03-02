from flask import Flask, render_template, abort, send_from_directory, request
import os

app = Flask(__name__)
app.static_folder = 'static'

manga_folder = 'static/manga'

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
    chapters_with_thumbnails = []
    for chapter in chapters:
        chapter_path = os.path.join(manga_path, chapter)
        if os.path.isdir(chapter_path):
            pages = sorted(os.listdir(chapter_path))
            thumbnail_path = os.path.join(chapter_path, pages[0])
            chapters_with_thumbnails.append((chapter, thumbnail_path))
    return render_template('chapters.html', manga=manga, chapters=chapters_with_thumbnails)

@app.route('/<manga>/<chapter>/')
def read(manga, chapter):
    chapter_path = os.path.join(manga_folder, manga, chapter)
    if not os.path.exists(chapter_path):
        abort(404)
    pages = sorted(os.listdir(chapter_path), key=lambda x: int(x.split('.')[0]))
    current_page = request.args.get('page', default=pages[0], type=str)

    # set the previous and next pages
    sorted_pages = sorted(pages, key=lambda x: int(x.split('.')[0]))
    current_page_index = sorted_pages.index(current_page)
    prev_page = sorted_pages[current_page_index - 1] if current_page_index > 0 else None
    next_page = sorted_pages[current_page_index + 1] if current_page_index < len(sorted_pages) - 1 else None

    return render_template('read.html', manga=manga, chapter=chapter, pages=pages, page=current_page, prev_page=prev_page, next_page=next_page)

@app.route('/<manga>/<chapter>/<page>')
def get_page(manga, chapter, page):
    page_path = os.path.join(manga_folder, manga, chapter, page)
    if not os.path.exists(page_path):
        abort(404)
    return send_from_directory(os.path.join(manga_folder, manga, chapter), page)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

