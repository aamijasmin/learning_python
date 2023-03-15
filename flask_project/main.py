from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def welcome ():
    return "welcom to online world"

@app.route("/img")
def img():
    return render_template('home.html')

@app.route("/img_get")
def img_get():
    return render_template('img.html')


@app.route("/jas_get")
def jas_get():
    return render_template('jasmin.html')



