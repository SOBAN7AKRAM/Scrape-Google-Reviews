# Description

Scrape over 2500+ Google reviews of ECM company websites. Extract reviews ratings and times and then display the trend of rating and number of reviews quarterly.

## File explanation

- **scrape_reviews.py:** Extract the reviews from the website
- **scrape_subreviews.py:** Extract the sub_reviews using the href of reviews
- **write.py:** Write the ratings and times of reviews into **.csv** file after parsing the html
- **mining.py:** Convert the time into quarterly alongside no.  of reviews and ratings and store them in .csv file
- **visualization.py:** Display the trend on dashboard
- **Run.py:** Automate the running of scripts

### How to start

- First run `pip install -r requirements.txt` to install all the required dependencies
- To visualize the trend run **streamlit run visualization.py**
- To perform all the task again run **python Run.py**