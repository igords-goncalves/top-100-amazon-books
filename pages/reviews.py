import pandas as pd
import streamlit as st

st.set_page_config(page_title="Reviews", layout="wide")

df_reviews = pd.read_csv("dataset/customer reviews.csv")
df_top100_Boooks = pd.read_csv("dataset/Top-100 Trending Books.csv")

books = df_top100_Boooks["book title"]
reviews = df_reviews["book name"]

# Filtering by books and review

unique_books = books.unique()
book = st.sidebar.selectbox("Livros", unique_books)

book_filtered = df_top100_Boooks[books == book]
reviewes_filtered = df_reviews[reviews == book]

# Fileted by columns

title = book_filtered["book title"].iloc[0]
genre = book_filtered["genre"].iloc[0]
price = f"${book_filtered['book price'].iloc[0]}"
rating = f"★ {book_filtered['rating'].iloc[0]}"
year = book_filtered["year of publication"].iloc[0]

st.title(title)
st.header(genre)

col1, col2, col3 = st.columns(3)

col1.metric("Price", price)
col2.metric("Rating", rating)
col3.metric("Year of publication", year)

st.divider()

# Reviwes

for row in reviewes_filtered.values:
  message = st.chat_message(str(row[4]))
  message.write(f"**{row[2]}**")
  message.write(row[5])