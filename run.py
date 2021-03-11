from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from flask import Flask, jsonify
from bs4 import BeautifulSoup
from time import sleep

def get(driver, url):
    try:
        driver.get(url)
    finally:
        sleep(4)

app = Flask('')

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=chrome_options)
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

@app.route('/v3/bedwars/')
def bedwarsv3():
    global driver
    url = "https://www.spigotmc.org/resources/screaming-bedwars-1-9-1-16.63714/"
    get(driver, url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    data = soup.find("dl", {"class": "downloadCount"}).find("dd").text.replace(",", "")
    return jsonify({"result": data})

app.run(host="0.0.0.0", port=8080)
