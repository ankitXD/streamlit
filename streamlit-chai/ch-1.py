import streamlit as st

#to run this file -> uvx streamlit run main.py

st.title('Hello Chai App')
st.subheader('Brewed with love by Chai')
st.text('This is a simple Streamlit app to demonstrate the integration with Chai.')
st.write('Choose your favorite chai:')

chai = st.selectbox(
    'Select your favorite chai:',
    ('Masala Chai', 'Ginger Chai', 'Cardamom Chai', 'Lemon Chai', 'Mint Chai')
)

st.write(f"You selected: {chai}. Excellent choice!")

st.success('Enjoy your cup of chai!')

# Programming Language Picker App Assignment