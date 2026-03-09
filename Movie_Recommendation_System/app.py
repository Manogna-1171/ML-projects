import streamlit as st
import pickle
import pandas as pd

# Fix 1: Load .pkl files with pickle, not pd.read_csv()
movies = pickle.load(open("movies.pkl", "rb"))

# Fix 2: Load similarity BEFORE it's needed
similarity = pickle.load(open("similarity.pkl", "rb"))

movie_list = movies["original_title"].values

def recommend(movie):
    i = movies[movies["original_title"] == movie].index[0]
    movies_list = sorted(list(enumerate(similarity[i])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for j in movies_list:
        recommended_movies.append(movies.iloc[j[0]].original_title)
    return recommended_movies

st.title("Movie Recommender System")
selected_movie = st.selectbox("Which movie have you watched?", movie_list)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)