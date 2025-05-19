import streamlit as st

st.title("Chai Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://images.pexels.com/photos/29421579/pexels-photo-29421579.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2")
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image("https://images.pexels.com/photos/29421578/pexels-photo-29421578.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2")
    vote2 = st.button("Vote Adrak Chai")

if vote1:
    st.success("Thanks for Voting Masala chai")
elif vote2:
    st.success("Thanks for Voting Adrak chai")

name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose your chai", ["Masala", "Kesar", "Adrak"])

st.write(f"Welcome {name} and your {tea} chai is getting ready")


with st.expander("Show Chai Making Instructions"):
    st.write(""" 
    1. Boil Water with tea leaves
    2. Add Milk and spices
    3. Serve hot
""")
    
st.markdown('## Welcome to Chai App')
st.markdown('> BlockQuote')