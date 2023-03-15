from flask import Flask, render_template, request
import random
app = Flask(__name__)

cars = ['tavera', 'swift', 'alto 800', 'creta', 'harrier', 'punch', 'nexon', 'bolero', 'thar', 'fortuner', 'xuv700' ]

user_1={
        "name":'jasmin',
        "age": 20,
        "add": 'takagachh'
        }
user_2 ={
        "name":'barun',
        "add":'jkdm',
        "phon":'6297063622'
        }

@app.route("/")
def welcome():
    return "<h2>Welcome to hacker's world !</h2>"

@app.route("/items")
def items():
    return "Many items are available right now"

@app.route("/jackpot")
def jack():
    r = random.randint(0,10)
    car = cars[r]
    if (r==5):
        r = f"😞 Nothing here "
    else:
        r = f"<h3>Voila ! you got {car} 😇"

    return r


@app.route("/d")
def details():
    r = user_1
    return r["age"]

@app.route("/wise")
def wise():
    return "have a nice day"

@app.route("/hello")
def hello():
  return render_template('home.html')  # return "hii dear! how are you',"  ", 'hii big bro kii koro',"  ", 'manas daa tumi plz chup chap thako nahole sobai chole jabe palaya"
@app.route("/rose-day")
def roseday():
    return render_template('rose-day.html')

@app.route("/table")
def table_get():
    return render_template('table.html')


@app.route("/table", methods=['POST'])
def table():
    text = request.form['text']
    print(text.strip())
    try:
        n = int(text.strip())
        return render_template('result.html', n=n)
    except:
        return render_template(('error.html'))
@app.route("/welcom")
def welcom():
    return render_template('nice.html') 

