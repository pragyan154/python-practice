from flask import Flask
from birdseye import eye
app = Flask(__name__)

@eye
@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()