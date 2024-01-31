from flask import Flask, render_template

app = Flask(__name__)

# name = input('enter your name:\n')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
    
    
@app.route('/profile')
def profile():
    pass


@app.route('/register')
def register():
    pass

@app.route('/login')
def login():
    pass


