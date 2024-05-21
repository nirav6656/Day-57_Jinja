import requests
from flask import Flask, render_template


app = Flask(__name__)



@app.route('/')
def blog():
    data = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", posts = data)

@app.route('/post/<id_no>')
def posting(id_no):
    data = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
    print(type(id_no))
    return render_template("post.html", id_no = int(id_no)-1, posts = data)

if __name__ == "__main__":
    app.run(debug=True)
