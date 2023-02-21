import sqlite3
from flask import Flask, render_template,request, url_for
app = Flask(__name__)
app.secret_key="__private_key_"


@app.route('/home')
def home():
    return render_template('ho.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        connection = sqlite3.connect('userdata.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']
        print(name,password)

        query = "SELECT name, password FROM users  where name='"+name+"' and password='"+password+"'"
        cursor.execute(query)
        result = cursor.fetchall()

        if len(result) == 0:
            return render_template('msg.html')
            #print("sorry incorrect credentials provided Try again")
        else:
            return render_template("login.html")


    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5400 ,debug=True)





