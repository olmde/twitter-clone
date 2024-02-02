from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template('landing.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/profile')
def profile():
    pass


@app.route('/register')
def register():
    pass




if __name__ == '__main__':
    app.run(debug=True)