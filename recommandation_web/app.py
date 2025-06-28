import streamlit as st
import pickle
import requests

movies_list = pickle.load(open('movies.pkl','rb'))
movies_l = movies_list['title'].values
similarity = pickle.load(open('similarity.pkl','rb'))


import requests

def fetch_poster(movie_title):
    api_key = "fb2e58cb"  # API key
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        poster_url = data.get('Poster')
        if poster_url and poster_url != "N/A":
            return poster_url
        else:
            return "https://via.placeholder.com/300x450.png?text=No+Poster"
    except Exception as e:
        print("Error fetching poster:", e)
        return "https://via.placeholder.com/300x450.png?text=Error"



def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = list(enumerate(similarity[movie_index]))
    movies = sorted(distances, reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies:
        title = movies_list.loc[i[0], 'title']
        recommended_movies.append(title)
        recommended_movies_posters.append(fetch_poster(title))
    return recommended_movies,recommended_movies_posters

st.title("Movie Recommender System")

selected_movie = st.selectbox(
    "select a movie",
    movies_l,
)

if st.button("Recommended"):
    names,posters = recommend(selected_movie)

    col1, col2, col3, col4, col5= st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
