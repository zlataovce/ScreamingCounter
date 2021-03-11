import requests
from flask import Flask, jsonify
from statistics import mean
import time
from threading import Thread

app = Flask('')

avgvalues = [0, 0, 3, 1, 5]

cached_value = 0
mathed_value = 0

def count_update(avgvalues):
    global mathed_value
    while True:
        mathed_value = mathed_value + int(round(mean(avgvalues)))
        time.sleep(900)

def cache_update():
    global cached_value, mathed_value
    while True:
        url = "https://api.spiget.org/v2/resources/63714"
        r = requests.get(url).json()
        if not cached_value == r['downloads']:
            cached_value = r['downloads']
            mathed_value = r['downloads']
        time.sleep(1800)


@app.route('/v2/bedwars/')
def bedwarsv2():
    global mathed_value
    url = "https://api.spiget.org/v2/resources/63714"
    r = requests.get(url).json()
    x = {"approximate": mathed_value, "real": r['downloads']}
    return jsonify(x)

@app.route('/v1/bedwars/')
def bedwars():
    url = "https://api.spiget.org/v2/resources/63714"
    r = requests.get(url).json()
    return "<p>" + str(r['downloads']) + "</p>"

url = "https://api.spiget.org/v2/resources/63714"
r = requests.get(url).json()
Thread(target=cache_update).start()
Thread(target=lambda: count_update(avgvalues)).start()
app.run(host="0.0.0.0", port=8080)
