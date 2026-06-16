import streamlit as st 
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("gemini")
genai.configure(api_key=api_key)
model=genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="My own chatbot",
    layout="wide"
)
st.title("My ai assistant")
st.caption("chatgpt style chatbot using gemini")
if "messages" not in st.session_state:
    st.session_state.messages=[]
with st.sidebar:
    st.header("settings")
    if st.button("clear convo"):
        st.session_state.messages=[]
        st.rerun()
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])
prompt=st.chat_input("ask anything....")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({
        "role":"user",
        "content":prompt
    })
    with st.chat_message("assistant"):
        message_placeholder=st.empty()
        try:
            response=model.generate_content(prompt)
            reply=response.text
        except Exception as e:
            reply=f"Error:{e}"
        message_placeholder.markdown(reply)
    st.session_state.messages.append({
        "role":"assistant",
        "content":reply
    })