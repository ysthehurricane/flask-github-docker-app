from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask with Docker!"


@app.route('/index')
def index():
    return "Hello, I am Yash!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
