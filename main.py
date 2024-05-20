from flask import Flask, render_template
import requests
import os

app = Flask(__name__)


API_KEY = os.environ["API_KEY"]
@app.route('/')
def home():
    return render_template("index.html")

# @app.route('/guess/<name>')
# def names(name):
#     response = requests.get(url=f"https://api.genderize.io?name={name}")
#     data = response.json()
#     user_gender = data["gender"]
#     return render_template("index.html", gender=user_gender,user_name = name)

@app.route('/blog')
def blog():
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    return render_template("index.html", posts = data)

if __name__ == '__main__':
    app.run(debug=True)