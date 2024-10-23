import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Top 100 books", layout="centered")

df_reviews = pd.read_csv("dataset/customer reviews.csv")
df_top100_Boooks = pd.read_csv("dataset/Top-100 Trending Books.csv")

# Books analisys

book_price = df_top100_Boooks["book price"]

max_price = book_price.max()
min_price = book_price.min()

filtered_price = st.sidebar.slider("Preço", min_price, max_price, max_price)
st.write(df_top100_Boooks[book_price <= filtered_price])

# Analysis publications

publication_year = df_top100_Boooks["year of publication"].value_counts()
best_sellers_year_publication = px.bar(publication_year)

st.plotly_chart(best_sellers_year_publication)

# Analysis prices

histogram_books_price = px.histogram(book_price)

# Reviwes Analisys

reviewer_rating = df_reviews["reviewer rating"]

max_review = reviewer_rating.max()
min_review = reviewer_rating.min()

filtered_review = st.sidebar.slider("Review", max_review, min_review, max_review)
st.write(df_reviews[reviewer_rating <= filtered_review])

st.plotly_chart(histogram_books_price)
