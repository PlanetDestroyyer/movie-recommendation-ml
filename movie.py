import streamlit as st
import pickle
import pandas as pd

st.title("Movie Recommendation")

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    movies_recommend = []
    for i in movies_list:
        movies_recommend.append(movies.iloc[i[0]].title)
    return movies_recommend

similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

option = st.selectbox(
    'Select a movie',
    movies['title'].tolist())  


if st.button('Recommend'):
    recommendation = recommend(option)
    for i in recommendation:
        st.write(i)
