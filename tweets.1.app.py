import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(page_title="Twitter Sentiment Analysis", layout="centered")

# Title
st.title("✈️ Twitter Airline Sentiment Analysis")

# Load data
DATA_URL = 'https://raw.githubusercontent.com/NdongesitBassey/NB/refs/heads/main/Tweets.csv'
@st.cache_data
def load_data():
    return pd.read_csv(DATA_URL)

tweets = load_data()

# Show data preview
if st.checkbox("Show raw data"):
    st.subheader("Raw Tweet Data")
    st.write(tweets.head())

# Pie Chart of Sentiment Distribution
st.subheader("Sentiment Distribution")
sentiment_counts = tweets['airline_sentiment'].value_counts().reset_index()
sentiment_counts.columns = ['airline_sentiment', 'count']

fig_pie = px.pie(sentiment_counts, values='count', names='airline_sentiment',
                 title='Sentiment Distribution of Airline Tweets')
st.plotly_chart(fig_pie)

# Bar Plot of Number of Tweets by Airline
st.subheader("Number of Tweets by Airline")
airline_counts = tweets['airline'].value_counts().reset_index()
airline_counts.columns = ['airline', 'count']

fig_bar, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='airline', y='count', data=airline_counts, palette='pastel', ax=ax)
ax.set_xlabel('Airline')
ax.set_ylabel('Number of Tweets')
ax.set_title('Number of Tweets by Airline')
st.pyplot(fig_bar)
