from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Continuous integration and deployment!"

if __name__ == "__main__":
    app.run(debug = True)