import streamlit as st

st.title('Chai Maker App')

if st.button("Make Chai"):
    st.success("Your Chai is being brewed")

add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("Masala Added to your chai")

tea_type = st.radio("Pick your chai base: ", ["Milk", "Water", "Almond Milk"])
st.write(f"Selected base {tea_type}")

flavour = st.selectbox("Choose flavour: ", ["Adrak", "Kesar", "Tulsi"])

st.write(f"Selected flavour {flavour}")

sugar = st.slider("Sugar Level", 0 , 10 , 5)

st.write(f"Selected sugar spoon: {sugar}")

cups = st.number_input("How many cups", min_value=1, max_value=10, step=1)
st.write(f"Selected sugar level {cups}")

name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome, {name} ! Your Chai is on the way")

dob = st.date_input("Select your DOB")
st.write(f"Your Dob is: {dob}")