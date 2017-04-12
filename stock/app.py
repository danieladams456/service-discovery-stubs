import os
import random
import requests

from flask import Flask
app = Flask(__name__)

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

#BASE_URL = "http://services.internal.dadams.io"
BASE_URL = os.environ['BASE_URL']

@app.route("/")
def main():
    return "You hit root.  You should try /stock/<symbol>"

@app.route("/stock/<symbol>")
def stock(symbol):
    message =  "Stock report for " + symbol + ": " + random_report()
    if symbol == "extrabacon":
        message += "<br>" + extra_bacon(symbol)
    return message

def random_report():
    possibilities = ["Good", "Bad", "Ugly"]
    return random.choice(possibilities)

#get a stock too to showcase service discovery
def extra_bacon(city):
    url = BASE_URL + "/weather/" + city
    logger.info("EXTRABACON Service URL: " + url)
    r = requests.get(url)
    message = "Querying EXTRABACON URL " + url + "<br>" + r.text
    return message


if __name__ == "__main__":
    app.run(host='0.0.0.0')
