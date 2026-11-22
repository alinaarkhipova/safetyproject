from flask import Flask
from model.model import model_img_box
app = Flask(__name__)
@app.route('/')
def index():
    return 'Привет мирииир:)'
if __name__ == '__main__':
    app.run(debug=True)
