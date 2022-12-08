# IMPORT NECCESSARY LIB
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.date import now
from utils.cardbacks import scrape as cardbacks_scrapper

# CONFIG FOR PRODUCTION ENV
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

print('Scraping in progress...........................', now())
cardbacks_scrapper(webdriver, Service, chrome_options, WebDriverWait, By, EC)

