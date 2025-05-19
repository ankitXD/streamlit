import streamlit as st

st.title('Prgamming Language Picker App')
st.write('Choose your favorite programming language')

pl = st.selectbox(
    'Select your favorite Programming Language:',
    ('C', 'C++', 'Java', 'Javascript', 'Python')
)

st.write(f"You selected: {pl}. Excellent choice!")

st.success('Enjoy your fav Programming Language!')