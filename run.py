import undetected_chromedriver.v2 as uc
from flask import Flask, jsonify
from bs4 import BeautifulSoup
import os

app = Flask('')

chrome_options = uc.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = uc.Chrome(options=chrome_options)

@app.route('/v3/bedwars/')
def bedwarsv3():
    global driver
    url = "https://www.spigotmc.org/resources/screaming-bedwars-1-9-1-16.63714/"
    driver.get_in(url, delay=5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    data = soup.find("dl", {"class": "downloadCount"}).find("dd").text.replace(",", "")
    return jsonify({"result": data})

app.run(host="0.0.0.0", port=int(os.environ.get("PORT")))
