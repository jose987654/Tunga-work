from flask import Flask
app = Flask(__name__)

# route for "/"
@app.route('/')
def first():
    return "Hello Joseph Wasswa"

# route for "/about"
@app.route('/about')
def about():
    return "About Me page"

if __name__ == '__main__':
    app.run()
        