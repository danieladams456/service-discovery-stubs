import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "You hit root.  You should try /weather/<city>"

@app.route("/weather/<city>")
def weather(city):
    return "Weather in " + city + ": " + random_weather()

def random_weather():
    possibilities = ["Sunny and hot",
                     "Sunny but not hot",
                     "Not sunny but hot",
                     "Not sunny and not hot"]
    return random.choice(possibilities)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
