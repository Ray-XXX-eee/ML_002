import streamlit as st
import time

st.title("DB Agent")

if 'message' not in st.session_state:
    st.session_state.message = []

st.subheader("Chat History :")
for msg in st.session_state.message:
    if msg.role == 'user':
        st.markdown(f"**User**: {msg.content}")
    elif msg.role == 'agent':
        st.markdown(f"**agent**: {msg.content}")


user_input = st.text_input("Say 'Hi' to SQL agent",'')
if st.button('Send') and user_input.strip():
    st.session_state.message.append({'role':'user','content':user_input})
    
    with st.spinner('DBAgent is typing...'):
        time.sleep(2)
        ## call rag model
        
    