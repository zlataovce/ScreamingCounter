import requests
from flask import Flask

app = Flask('')


@app.route('/bedwars')
def bedwars():
    url = "https://api.spiget.org/v2/resources/63714"
    r = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Macintosh; '
                                                 'Intel Mac OS X 10_12_6) AppleWebKit/53'
                                                 '7.36(KHTML, like Gecko) Chrome/63.0.32'
                                                 '39.132 Safari/537.36'}).json()
    return str(r['downloads'])


@app.route('/sbahypixelify')
def hypixelify():
    url = "https://api.spiget.org/v2/resources/79505"
    r = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Macintosh; '
                                                 'Intel Mac OS X 10_12_6) AppleWebKit/53'
                                                 '7.36(KHTML, like Gecko) Chrome/63.0.32'
                                                 '39.132 Safari/537.36'}).json()
    return str(r['downloads'])


@app.route('/')
def main():
    return "ScreamingBedWars: " + bedwars() + ", SBAHypixelify: " + hypixelify()


app.run(host="0.0.0.0", port=8080)
