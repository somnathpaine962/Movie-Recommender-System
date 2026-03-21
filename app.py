import streamlit as st
import pickle
import pandas as pd
import requests
session = requests.Session()
# Replace with your API key and movie ID
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=bb74c40200a9cc38f7bb7763e55b81bb"

        response = session.get(
            url,
            timeout=5,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        data = response.json()
        poster_path = data.get('poster_path')

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"

    except requests.exceptions.RequestException as e:
        print("Error:", e)

    return "https://via.placeholder.com/500x750?text=No+Image"
def recommend(movies):
    index = movie[movie['title'] == movies].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommend_movies=[]
    recommend_movies_poster=[]
    for i in distances[1:6]:
        movie_id=movie.iloc[i[0]].movie_id
        recommend_movies_poster.append(fetch_poster(movie_id))
        #fetch poster from API
        recommend_movies.append(movie.iloc[i[0]].title)
    return recommend_movies , recommend_movies_poster


similarity = pickle.load(open('similarity.pkl','rb'))
movies_list=pickle.load(open('movie_list_dict.pkl','rb'))
movie=pd.DataFrame(movies_list)


st.title('Movie Recommendation System')
selected_movie_name = st.selectbox("Select Movie", movie['title'].values)
if st.button('Recommend'):
    name,poster =recommend(selected_movie_name)
    col1, col2, col3 ,col4,col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])
    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4]) 

