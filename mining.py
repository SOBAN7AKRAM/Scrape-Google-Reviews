import pandas as pd
from datetime import datetime, timedelta

df = pd.read_csv('reviews.csv')

def convert_to_date(relative_time):
    current_date = datetime.now()
    if "day ago" in relative_time:
        return current_date - timedelta(days=1)
    elif "days ago" in relative_time:
        days = int(relative_time.split()[0])
        return current_date - timedelta(days=days)
    elif "week ago" in relative_time:
        return current_date - timedelta(weeks=1)
    elif "weeks ago" in relative_time:
        weeks = int(relative_time.split()[0])
        return current_date - timedelta(weeks=weeks)
    elif "month ago" in relative_time:
        return current_date - timedelta(days=30)
    elif "months ago" in relative_time:
        months = int(relative_time.split()[0])
        return current_date - timedelta(days=months * 30)  # Approximation
    elif "a year ago" in relative_time:
        return current_date - timedelta(days=365)
    elif "years ago" in relative_time:
        years = int(relative_time.split()[0])
        return current_date - timedelta(days=years * 365)
    return current_date

df['times'] = df['times'].apply(convert_to_date)
df['quarter'] = df['times'].dt.to_period('Q')
quarterly_ratings = df.groupby('quarter').agg(
    ratings_sum=('ratings', 'mean'),
    reviews_count=('ratings', 'count')
)
quarterly_ratings.to_csv('quarterly_ratings.csv', header=True)

