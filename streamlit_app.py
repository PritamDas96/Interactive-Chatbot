import os
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI

# Set your Google API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyBtQxK4iHj1DgscIz0x7JGNhH-N5YAPiP4"

# Initialize Gemini model in LangChain
llm = GoogleGenerativeAI(model="gemini-pro", temperature=0.9)

# Streamlit UI
st.title("AI Question Answering with Gemini")
st.write("Ask any question, and the AI will generate an answer.")

# Input box for user question
user_question = st.text_input("Enter your question:")

# Generate answer on button click
if st.button("Get Answer"):
    if user_question:
        answer = llm.invoke(user_question)
        st.subheader("Answer:")
        st.write(answer or "No data available")

    else:
        st.warning("Please enter a question before clicking the button.")
