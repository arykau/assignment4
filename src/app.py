from flask import Flask,request,render_template,redirect
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/coin',methods=['POST','GET'])
def coin():
    if request.method == 'POST':
        coin_name = request.form['name'].lower()
        URL = "https://coinmarketcap.com/currencies/" + coin_name
        page = requests.get(URL)
        scrapper = BeautifulSoup(page.content,"lxml")
        infos = scrapper.find("div", class_ = "sc-16r8icm-0 kjciSH contentClosed hasShadow")
        print(infos)
        for info in infos:
            data = info.text
            return render_template('index.html', data=data)
    elif request.method == 'GET':
        return render_template('index.html')
                
if __name__ == '__main__':
    app.run(debug=True, port=8080)