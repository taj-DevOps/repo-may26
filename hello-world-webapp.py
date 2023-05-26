print('This is sample web-application for helloworld app')


from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Welcome to hello-World webapp!'
