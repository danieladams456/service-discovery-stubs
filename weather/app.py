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
    return "You hit root.  You should try /weather/<city>"

@app.route("/weather/<city>")
def weather(city):
    message =  "Weather in " + city + ": " + random_weather()
    if city == "extrabacon":
        message += "<br>" + extra_bacon(city)
    return message

def random_weather():
    possibilities = ["Sunny and hot",
                     "Sunny but not hot",
                     "Not sunny but hot",
                     "Not sunny and not hot"]
    return random.choice(possibilities)

#get a stock too to showcase service discovery
def extra_bacon(symbol):
    url = BASE_URL + "/stock/" + symbol
    logger.info("EXTRABACON Service URL: " + url)
    r = requests.get(url)
    message = "Querying EXTRABACON URL " + url + "<br>" + r.text
    return message


if __name__ == "__main__":
    app.run(host='0.0.0.0')
