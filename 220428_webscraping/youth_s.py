from time import sleep
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL = f"https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifList.do"
def get_today_info() :
    website = requests.get(URL)
    soup = BeautifulSoup(website.text,"html.parser")
   

    chrome_options = Options()
    chrome_options.add_argument( '--headless' )
    chrome_options.add_argument( '--log-level=3' )
    chrome_options.add_argument( '--disable-logging' )
    chrome_options.add_argument( '--no-sandbox' )
    chrome_options.add_argument( '--disable-gpu' )