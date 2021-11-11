from re import template
from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
import jwt
from sqlalchemy.sql.schema import Column
from werkzeug.security import check_password_hash
import datetime
import uuid
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['SECRET_KEY'] = '7xKlb34rb5wWRYM36wte'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:020716@localhost:5432/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.Text)
    password = db.Column(db.Text)
    token = db.Column(db.Text)

    def __init__(self,email,password,token):
        self.email = email
        self.password = password
        self.token = token

@app.route('/coin',methods=['POST','GET'])
def coin():
    
    if request.method == 'POST':
        coin_name = request.form.get('name')
        print(coin_name)
        URL = "https://coinmarketcap.com/currencies/" + coin.lower()
        page = requests.get(URL)
        scrapper = BeautifulSoup(page.content,"lxml")
        info = scrapper.find("div", class_ = "sc-2qtjgt-0 eApVPN").find_all("p")
        return render_template('index.html', info = info)
    elif request.method == 'GET':
        return render_template('index.html')
                
if __name__ == '__main__':
    app.run(debug=True, port=8080)