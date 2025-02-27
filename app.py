import streamlit as st
import google.generativeai as genai

# Set up Streamlit UI
st.title("💬 Gemini AI Chatbot")
st.markdown("A chatbot powered by Google's Gemini AI.")

# Configure Gemini API key
genai.configure(api_key="AIzaSyDjiWY7_cy6DC4PFAGeDquic5zFRpRzkIM")  # Replace with your actual API key

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# User input
text = st.text_input("Ask me anything:")

# Additional UI elements
st.toggle("Activate")
st.radio("Response Type", ["Short", "Detailed"])

# Button to generate response
if st.button("Get Response"):
    if text.strip():
        response = chat.send_message(text)
        st.write("🤖 **Gemini AI:**", response.text)  # Display chatbot response
    else:
        st.warning("Please enter a question.")

# Feedback option
st.feedback("thumbs")
