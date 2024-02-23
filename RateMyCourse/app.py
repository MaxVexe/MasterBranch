#creates the imports for the app
import sqlite3
from flask import Flask,render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


#create to the database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

#make the apps work envirnoment install correct
app = Flask(__name__)
#need encryption key to be able to work. Security
app.config['SECRET_KEY'] = '1234'


#route the app to the home directory
@app.route('/',methods =('GET','POST'))

#This is the index function where the main page lives 
def index():

    #return the template and html
        return render_template('amyHome.html')
    
@app.route('/registor',methods =('GET','POST'))

def register():
      #checks if a request method was called
    if request.method == 'POST':
#sets all the variables to the html form
        name = request.form['name'] 
        username = request.form['username']
        password = request.form['password']

        if not name or not username or not password:
            flash('Please fill out all info!')
        else:
            #sets conn to get into the database
            conn = get_db_connection()
            #create a courses variable to be use for homepage
            conn.execute('INSERT INTO Users (username,password,name) VALUES (?, ?, ?)',
                         (name,username,password))

            #commit connection to the db
            conn.commit()
            #close Db 
            conn.close()
            
            return render_template('amyRegistor.html')
    else:  
      return render_template('amyRegistor.html')

@app.route('/login', methods =('GET','POST'))

def loggingtion():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Please Enter Fields')
        else: 
            print("hello")
    
        return render_template('amyLogin.html')
    else:
        return  render_template('amyLogin.html')