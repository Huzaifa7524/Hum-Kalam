import streamlit as st
import random
import time
import google.generativeai as palm

st.title("Ham Kalam Chatbot")

# Add a sidebar with copyright information and API key input field

user_api_key = st.sidebar.text_input("Enter your API Key:", "")
st.sidebar.markdown("© 2023 Huzaifa Tahir. All rights reserved.")
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Check if an API key is provided
if user_api_key:
    # Configure the "palm" API key using user input
    palm.configure(api_key=user_api_key)

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Ham Kalam ho ja?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Use the "palm" library to get the assistant's response
        response = palm.chat(messages=prompt)
        assistant_response = response.last

        # Check if assistant_response is not None
        if assistant_response:
            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                st.markdown(assistant_response)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        else:
            st.write("Assistant's response is empty. Please try again.")
    else:
        st.write("Please enter a message in the chat.")
else:
    st.write("Please enter your API key in the sidebar to enable the chat.")
