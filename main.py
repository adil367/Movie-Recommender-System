import streamlit as st
import pickle
import pandas as pd
import requests
st.title('Movies Recommender System')


def fetch_poster(movie_id):
     response = requests.get(
          f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=894c0c64acd9547908cbe52ee6774c34&language=en-US')
     data=response.json()
     return 'http://image.tmdb.org/t/p/w500/' + data['poster_path']


def recommend(movie):
     distances = similarity[(movies[movies['title'] == movie].index[0])]
     rec_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
     movies_names=[]
     poster_paths=[]

     for i in rec_movies:
          movie_id=movies.iloc[i[0]].movie_id
          movies_names.append(movies.iloc[i[0]].title)
          poster_paths.append(fetch_poster(movie_id))
     return movies_names,poster_paths

movies=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies)
similarity=pickle.load(open('similarity.pkl','rb'))


movie_name = st.selectbox(
     'Enter Movie Name',
     movies['title'].values)

if st.button('Recommend'):
     recommended_movies,movie_posters = recommend(movie_name)
     col1,col2,col3,col4,col5=st.columns(5)
     with col1:
          st.text(recommended_movies[0])
          st.image(movie_posters[0])

     with col2:
          st.text(recommended_movies[1])
          st.image(movie_posters[1])

     with col3:
          st.text(recommended_movies[2])
          st.image(movie_posters[2])

     with col4:
          st.text(recommended_movies[3])
          st.image(movie_posters[3])

     with col5:
          st.text(recommended_movies[4])
          st.image(movie_posters[4])
