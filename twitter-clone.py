from flask import Flask, render_template
import os
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='twitter',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn


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

@app.route('/users')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('users.html', books=books)



if __name__ == '__main__':
    app.run(debug=True)