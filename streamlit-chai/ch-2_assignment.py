import streamlit as st
from datetime import date

#Calculator jisme aaj ki date to ho hi or jaise hi user apna date of birth daale to uski kitni age hogayi hai

st.title("Calculator Which Tells The Age Of User Based on Today's Date")

today = date.today()
formatted_date = today.strftime("%d/%m/%Y")

dob = st.date_input("Select your DOB", min_value=date(1900,1,1), format="DD/MM/YYYY")

st.subheader(f"Your Age as on {formatted_date} is : {today.year - dob.year}")