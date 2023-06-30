import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

driver.get("http://iamndeleche.pythonanywhere.com/")

time.sleep(0.1)

driver.maximize_window()

time.sleep(0.1)

# Scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(0.1)

image_urls = [
    "https://iamndeleche.pythonanywhere.com/static/images/adsbanner/ad2.jpg",
    "https://iamndeleche.pythonanywhere.com/static/images/adsbanner/ad1.jpg",
    "https://iamndeleche.pythonanywhere.com/static/images/adsbanner/ad4.png",
    "https://iamndeleche.pythonanywhere.com/static/images/adsbanner/ad3.jpg"
]

index = 0
while True:
    url = image_urls[index]
    driver.get(url)
    time.sleep(5)
    index = (index + 1) % len(image_urls)

# Keep the browser window open
input("Press Enter to close the browser...")
driver.quit()
