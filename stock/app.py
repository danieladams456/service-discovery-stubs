import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "You hit root.  You should try /stock/<symbol>"

@app.route("/stock/<symbol>")
def stock(symbol):
    return "Stock report for " + symbol + ": " + random_report()

def random_report():
    possibilities = ["Good", "Bad", "Ugly"]
    return random.choice(possibilities)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
