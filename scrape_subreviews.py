from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

with open('reviews.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')
elements = soup.findAll(class_='al6Kxe')

data_hrefs = [element.get('data-href') for element in elements if element.get('data-href')]

# Set up Selenium with Chrome
options = Options()
options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

for href in data_hrefs:
    url = href
    driver.get(url)
    scrollable_div = driver.find_element(By.CSS_SELECTOR, '.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde')
    current_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)
    while True:
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
        time.sleep(5) 
        new_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)
        if new_height == current_height:
            break
        current_height = new_height
    reviews_html = scrollable_div.get_attribute('outerHTML')
    with open('sub_reviews.html', 'a', encoding='utf-8') as f:
        f.write(reviews_html)
driver.quit()