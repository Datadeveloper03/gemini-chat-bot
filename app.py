
import streamlit as st
import google.generativeai as genai
st.title("AI companion using Gemini")
genai.configure(api_key="AIzaSyC66FsncXja8d_rDkXcyATfusHu4nUlO_8")
text = st.text_input("Enter Your Question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
st.toggle("activate")
st.radio("Select", ["Short", "brief"])



if st.button("Click Here"):
    response = chat.send_message(text)
    st.checkbox("I agree")
    st.write(response.text)
st.feedback("thumbs")
