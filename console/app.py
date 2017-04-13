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
    return "You hit root.  You should try /console"

@app.route("/console")
def console():
    return "Welcome to the console!\nYou can either try /console/weather/{city} or /console/stock/{symbol}"

@app.route("/console/weather/<city>")
def weather(city):
    url = BASE_URL + "/weather/" + city
    logger.info("Service URL: " + url)
    r = requests.get(url)
    message = "Querying URL " + url + "\n" + r.text
    return message

@app.route("/console/stock/<symbol>")
def stock(symbol):
    url = BASE_URL + "/stock/" + symbol
    logger.info("Service URL: " + url)
    r = requests.get(url)
    message = "Querying URL " + url + "\n" + r.text
    return message

if __name__ == "__main__":
    app.run(host='0.0.0.0')
