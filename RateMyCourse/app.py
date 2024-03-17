#creates the imports for the app
import sqlite3
from flask import Flask,render_template, request, url_for, flash, redirect
import hashlib
from werkzeug.exceptions import abort

MainAccount = None
#create to the database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

#make the apps work envirnoment install correct
app = Flask(__name__)
#need encryption key to be able to work. Security
app.config['SECRET_KEY'] = '1234'

#mysql=  MYSQL(app)

#route the app to the home directory
@app.route('/',methods =('GET','POST'))

#This is the index function where the main page lives 
def index():

    #return the template and html
        return render_template('amyHome.html')
    
@app.route('/registor',methods =('GET','POST'))

def register():
      #checks if a request method was called
    msg =''
    if request.method == 'POST':
#sets all the variables to the html form
        name = request.form['name'] 
        username = request.form['Username']
        email = request.form['email']
        password = request.form['password']
#Testing hasing password
        # hash = password+app.secret_key
        # hash = hashlib.sha1(hash.encode()).hexdigest() 
        # password += hash


        if not name or not username or not password or not email:
            flash('Please fill out all info!')
        else:
            #sets conn to get into the database
            conn = get_db_connection()
            #create a courses variable to be use for homepage
            conn.execute('INSERT INTO Users (username,password,name,email) VALUES (?, ?, ?, ?)',
                         (username,password,name,email))
            
            #commit connection to the db
            conn.commit()
            #close Db 
            conn.close()
            
            return render_template('amyRegistor.html')
    else:  
      return render_template('amyRegistor.html')

@app.route('/login',methods =('GET','POST'))

def loggingtion():
    if request.method == 'POST':
        #assign variable name to the form info
        email = request.form['email']
        password = request.form['password']
        # check if the user has put in information 
        if not email or not password:
            flash('Fill out the form bruh')
        else: 
            conn = get_db_connection()
        #simple way to salt the password to help against hackers
           #salting is adding random strings before passwords
           # hash = password+app.secret_key
            #create an object an it making it turn to biSnary
            #hash = hashlib.sha1(hash.encode())
            #converts the binary hash into its hexdec and assign it to pass
           # password = hash.hexdigest()
            # when passing agrument make sure to have , after first agru
            #conn.execute('SELECT * FROM Users WHERE username = (?)', (name,))
            
            #create a cursor to access the query
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Users WHERE email = (?)', (email,))
            account = cursor.fetchone()
            MainAccount = account
            loginVerifed = ""

            #check if account is found then run following 
            if account:
                #set information from 
                username_from_db = account['email']
                password_from_db = account['password']
                if password == password_from_db:
                    return homeRender(MainAccount)
                else: 
                    loginVerifed = "Incorrect Password"
                return render_template('loginPage.html',account = account,loginVerifed = loginVerifed)

             #commit connection to the db
            conn.commit()
            #close Db 
            conn.close()
          

            return render_template('amyLogin.html',account = account)

    return render_template('amyLogin.html')


@app.route('/home', methods = ('GET','POST'))

def homeRender(MainAccount):
    return render_template('Homepage.html', MainAccount = MainAccount)

@app.route('/about', methods = ('GET','POST'))


def profileRender(MainAccount):
    return render_template('profileTest.html',MainAccount = MainAccount)