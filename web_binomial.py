from flask import Flask
from flask import render_template
from binomial_coefs import binomial_coefs

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Returning Pascals Rectangle!</p>"

@app.route('/num/<int:cnt>')
def get_coef(cnt):
    bin_gen = binomial_coefs()
    result = [next(bin_gen) for _ in range(cnt)]
    return result

@app.route('/num/<int:cnt>/rectangle')
def get_coef_render(cnt):
    bin_gen = binomial_coefs()
    result = [next(bin_gen) for _ in range(cnt)]
    return render_template("num.html", result = result)
