from bs4 import BeautifulSoup
import pandas as pd

with open('sub_reviews.html', 'r', encoding='utf-8') as f:
    html_content = f.read()
    
soup = BeautifulSoup(html_content, 'html.parser')
times_text = soup.findAll(class_='rsqaWe')
ratings_element = soup.findAll(class_='kvMYJc')
ratings = [rating_element.get('aria-label') for rating_element in ratings_element if rating_element.get('aria-label')]
data = {
    'times': [time.text.strip() for time in times_text],
    'ratings': [rating.split(' ')[0] for rating in ratings if rating]
}

df = pd.DataFrame(data)
df.to_csv('reviews.csv', index=False)
