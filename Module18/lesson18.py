import pandas as pd
import streamlit as st
import plotly.express as px

st.header("Displaying Data Frames")

data = pd.DataFrame({
    'Name' : ["Alice","Michael","Andy"],
    'Age' : [25,31,19],
    'City' : ["Miami","London","Boston"]
})

st.write(data)

books_df = pd.read_csv("Module18/bestsellers_with_categories_2022_03_27.csv")


st.title('Bestselling Books Analysis')
st.write('This app analyses the Amazon Top Selling books from 2009 to 2022.')


st.subheader("Summary Statistics")
total_books = books_df.shape[0]
unique_titles = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()

col1,col2,col3,col4 = st.columns(4)

col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_titles)
col3.metric("Average Rating", f"{average_rating:.2f}")
col4.metric("Average Price", f"${average_price:.2f}")

st.subheader("Dataset Preview")
st.write(books_df.head())

col1,col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Book Titles")
    top_titles = books_df["Name"].value_counts().head(10)
    st.bar_chart(top_titles)

with col2:
    st.subheader("Top 10 Authors")
    top_authors = books_df["Author"].value_counts().head(10)
    st.bar_chart(top_authors)

st.subheader("Genre Distribution")
fig = px.pie(books_df, names='Genre',title='Most Liked Genre (2009-2022)',color='Genre',color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Number of Fiction vs Non-Fiction Books Over the Years")
size = books_df.groupby(['Year','Genre']).size().reset_index(name='Count')
fig = px.bar(size,x='Year',y='Count',color='Genre',title='Number of Fiction vs Non-fiction Books from 2009-2022',
             color_discrete_sequence=px.colors.sequential.Plasma,barmode="group")
st.plotly_chart(fig)


st.header('Top 15 Authors by Counts of Books Published ')
top_authors = books_df['Author'].value_counts().head(15).reset_index()
top_authors.columns = ['Author','Count']
fig = px.bar(top_authors, x='Count',y='Author',orientation='h',title='Top 15 Authors by Books Published',labels={'Count':'Counts of Books Published','Author':'Author'},color='Count',color_continuous_scale=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Filter Data by Genre")
genre_filter = st.selectbox('Select Genre',books_df['Genre'].unique())
filter_df = books_df[books_df['Genre'] == genre_filter]
st.write(filter_df)
