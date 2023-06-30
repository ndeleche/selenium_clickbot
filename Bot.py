import os
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

    

driver = webdriver.Chrome()

# Your code for interacting with the browser goes here

# Navigate the browser to a specific URL
driver.get("http://iamndeleche.pythonanywhere.com/")

time.sleep(0.1)

driver.maximize_window()

time.sleep(0.)

# Scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(0.2)


image_urls = [
    "https://iamndeleche.pythonanywhere.com/static/images/adsbanner/ad2.jpg",
    "https://iamndeleche.pythonanywhere.com/static/images/adsbanner/ad1.jpg",
    "https://iamndeleche.pythonanywhere.com/static/images/adsbanner/ad4.png",
    "https://iamndeleche.pythonanywhere.com/static/images/adsbanner/ad3.jpg"
]

for url in image_urls:
    driver.get(url)
    time.sleep(5)


# Keep the browser window open
input("Press Enter to close the browser...")
driver.quit()