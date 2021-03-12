from flask import Flask, jsonify
import requests

app = Flask('')

@app.route('/v3/bedwars/')
def bedwarsv3():
    url = "http://144.91.124.110:8080/bw"
    r = requests.get(url, data={'key': 'habibi'})
    print(r)
    return jsonify({"result": r.content})

app.run(host="0.0.0.0", port=8080)
