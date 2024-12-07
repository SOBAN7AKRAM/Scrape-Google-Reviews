import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv('quarterly_ratings.csv')

fig1, ax1 = plt.subplots(figsize=(16, 6))
ax1.plot(df['quarter'], df['ratings_sum'], marker='o')
ax1.set_xlabel('Quarter')
ax1.set_ylabel('Average Ratings')
ax1.set_title('Average Ratings per Quarter')

fig2, ax2 = plt.subplots(figsize=(16, 6))
ax2.plot(df['quarter'], df['reviews_count'], marker='o')
ax2.set_xlabel('Quarter')
ax2.set_ylabel('Reviews Count')
ax2.set_title('Reviews Count per Quarter')

st.title('Quarterly Ratings')
st.pyplot(fig1)
st.pyplot(fig2)