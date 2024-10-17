import streamlit as st

st.title("My first streamlit app")
st.subheader("Introducing streamlit in automate everything with python")
st.write("This is my first streamlit app")


st.button("Reset", type="primary")
if st.button("Say Hello"):
  st.write("why hello there")
else:
  st.write("Goodbye")