from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to my app!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

    # Test comment 1
    # Test comment 2