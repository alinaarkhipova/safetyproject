import os
from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='static/html', static_folder='static')

UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():
    image_url = None

    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # На Шаге 3 сюда добавишь вызов функции Эмины:
            # img = model.model_img_box(img)

            image_url = url_for('static', filename=f'uploads/{filename}')

    return render_template('index.html', image_url=image_url)


if __name__ == '__main__':
    app.run(debug=True)
