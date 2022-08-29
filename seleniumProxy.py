import random
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from seleniumwire import webdriver


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')

options = {
	'proxy': {
		'https':"http://davidnfgj09.gmail.com:123@gate1.proxyfuel.com:2000" ,
		'no_proxy': 'localhost,127.0.0.1'
	}
}

chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--log-level=3')
# chrome_options.add_argument(configuracion['idioma'])
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s,seleniumwire_options=options)
driver.get('http://checkip.amazonaws.com')

print("here")

# time.sleep(100)
# driver.quit()
