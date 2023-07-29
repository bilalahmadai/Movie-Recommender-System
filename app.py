import streamlit as st
import pickle
import requests
# https://developer.themoviedb.org/reference/movie-details
def fetch_poster(id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ca5129fdaebe44f026e49130504f00d6&language=en-US'.format(id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original/"+data['poster_path']


def recommend(movie):
    move_index = df[df['title']==movie].index[0]
    distance = similarity[move_index]
    movie_list= sorted(list(enumerate(distance)), reverse=True, key= lambda x:x[1])[1:6]
    recommend_list = []
    recommend_list_poster = []
    for i in movie_list:
        movie_id = df.iloc[i[0]].movie_id
        # fectch poster

        recommend_list.append(df.iloc[i[0]].title)
        recommend_list_poster.append(fetch_poster(movie_id))

    return recommend_list,recommend_list_poster


df = pickle.load(open('movie.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

moives_list=df['title'].values

st.title('Movie :blue[Recommender] System :film_frames:')


selected_movieName = st.selectbox(
    'Search for Moive',
    moives_list
    )
# if st.button('Recommend'):
name,poster=recommend(selected_movieName)


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.image(poster[0])
    st.markdown(name[0])
    
with col2:
    st.image(poster[1])
    st.markdown(name[1])
    
with col3:
    st.image(poster[2])
    st.markdown(name[2])
    
with col4:
    st.image(poster[3])
    st.markdown(name[3])
    
with col5:
    st.image(poster[4])
    st.markdown(name[4])
    



