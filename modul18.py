import pandas as pd
import streamlit as st
import plotly.express as px


#f = pd.DataFrame({
#    "Name":["Esmir","Darko","Timur"],
#    "Age":[25,16,18],
#    "City":["Tešanj","Sarajevo","Mostar"]

#})

#print(df)

#st.write(df)

#st.dataframe(df)

books_df = pd.read_csv("data/bestsellers_with_categories_2022_03_27.csv")


st.title("Bestselling Book Anlysis")
st.write("This app analyses the Amazon top seller from 2009 to 2022")
st.sidebar.header("Add new book data")

with st.sidebar.form("book_form"):
    new_name = st.text_input("Book name")
    new_author = st.text_input("Author")
    new_user_rating = st.slider("Users rating",0.0,5.0,0.0,0.1)
    new_price = st.number_input("Price",min_value=0,step=1)
    new_year = st.number_input("Year",min_value=2009,max_value=2022,step=1)
    new_reviews = st.text_input("Reviews")
    new_genre = st.selectbox("Genre",books_df["Genre"].unique())
    submit_button = st.form_submit_button(label="Add book")

if submit_button:
    new_data = {
        "Name": new_name,
        "Author":new_author,
        "User Rating":new_user_rating,
        "Price":new_price,
        "Year":new_year,
        "Genre":new_genre,
        "Reviews":new_reviews
    }

    books_df = pd.concat([pd.DataFrame(new_data,index=[0]),books_df],ignore_index=True)
    books_df.to_csv("data/bestsellers_with_categories_2022_03_27.csv",index=False)
    st.sidebar.success("New book Added succsefuly")
#Summyary statistics
st.subheader("Summery statistics")
total_books = books_df.shape[0]
unique_titles = books_df["Name"].nunique()
average_rating = books_df["User Rating"].mean()
average_price = books_df["Price"].mean()

col1,col2,col3,col4 = st.columns(4)
col1.metric("Total Books",total_books)
col2.metric("Unique titles",unique_titles)
col3.metric("Average ratinf",average_rating)
col4.metric("Average Price",average_price)

st.subheader("Dataset Prewiew")
st.write(books_df.head())

#Book title Distribution

col1,col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Book Titles")
    top_title = books_df["Name"].value_counts().head(10)
    st.bar_chart(top_title)
with col2:
    st.subheader("Top 10 Authors")
    top_author = books_df["Author"].value_counts().head(10)
    st.bar_chart(top_author)

#Genre Distribution Pie Chart
st.subheader("Genre Distribution")
fig = px.pie(books_df,title="Most Liked ganre 2009-2022",color="Genre",color_discrete_sequence=px.colors.sequential.Plasma,)#,color_discrete_sequence=px.colors.sequential.Plasma,,name="Ganre"

st.plotly_chart(fig)

st.subheader("Filted Data by Genre")
genre_filter = st.selectbox("Select Genre",books_df["Genre"].unique())
filtered_df = books_df[books_df["Genre"]== genre_filter]

st.write(filtered_df)

