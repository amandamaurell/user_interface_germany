import streamlit as st
import requests

api_key = st.secrets.GIPHY.api_key_2

url = 'https://api.giphy.com/v1/gifs/random'

gif_ = st.text_input('Please, add the animal you prefer...', value='cat')

col1, col2 = st.columns(2)


query_params = {'api_key':api_key,
                'tag':gif_}

with col1:
    response = requests.get(url, params=query_params).json()

    giphy = response['data']['embed_url']

    st.write(f"<iframe src={giphy}>", unsafe_allow_html=True)


with col2:
    response = requests.get(url, params=query_params).json()

    giphy = response['data']['embed_url']

    st.write(f"<iframe src={giphy}>", unsafe_allow_html=True)

button_ = st.button('press me for ballons')

if button_:
    st.balloons()
