from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello There!</h1>"

@app.route('/information')
def info():
    return "<h1>Just some information</h1>"

@app.route('/user/<name>')
def user(name):
    return "<h1>Hi there {}!</h1>".format(name)

if __name__ == "__main__":
    app.run(debug=True)