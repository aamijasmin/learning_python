from flask import Flask, render_template,request
app = Flask(__name__)
@app.route("/")
def welcom():
    return "welcome to my world"
@app.route("/table")
def table_get():
    return render_template('table.html')


@app.route("/table", methods= ['POST'])
def table():
    text = request.form['text']
    print(text.strip())
    # j = 5
    # return render_template('result.html',j=j)
    try:
        j= int(text.strip())
        return render_template('result.html',j=j)
    except:
        return render_template('error.html')


