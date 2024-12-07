from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# Set up Selenium with Chrome
options = Options()
options.headless = True  # Run headless if you don't need to see the browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://www.google.com/maps/place/ECM+Air+Conditioning+(East+Coast+Mechanical)/@26.5378999,-80.0702446,15z/data=!4m8!3m7!1s0x88d8df35bb71b4ad:0xd3322b65c1171e8b!8m2!3d26.5398781!4d-80.0742246!9m1!1b1!16s%2Fg%2F1thhl9dl?entry=ttu&g_ep=EgoyMDI0MTIwMi4wIKXMDSoASAFQAw%3D%3D"
driver.get(url)

time.sleep(10)

# Get total number of reviews from the page
reviews_element = driver.find_element(By.XPATH, "//div[@class='fontBodySmall' and contains(text(), 'reviews')]")

reviews_text = reviews_element.text
reviews_number = reviews_text.split(" ")[0]
total_reviews = int(reviews_number.replace(',', ''))
print(f"Total reviews expected: {total_reviews}")

# get the scrollable div
scrollable_div = driver.find_element(By.CSS_SELECTOR, '.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde')
current_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)

while True:
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
    time.sleep(4) 
    new_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)
    if new_height == current_height:
        break
    current_height = new_height

reviews_html = scrollable_div.get_attribute('outerHTML')
with open('reviews.html', 'w', encoding='utf-8') as f:
    f.write(reviews_html)
driver.quit()
