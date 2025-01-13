from groq import Groq
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Environment variables setup
# os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Create Groq client
# Access API key from secrets.toml
GROQ_API_KEY = st.secrets["GROQ_API_KEY"] 
client = Groq(api_key=GROQ_API_KEY)

# Create Streamlit interface
st.title("AI Assistant with :blue[_Groq_] 🙂")
# st.title("_Streamlit_ is :blue[cool] :sunglasses:")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful AI assistant that provides accurate and informative answers."}
    ]

# Display chat history
for message in st.session_state.messages:
    if message["role"] != "system":  # Don't display system messages
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # Get assistant's response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # Create chat completion
                chat_completion = client.chat.completions.create(
                    messages=st.session_state.messages,  # Include full chat history
                    model="llama3-70b-8192",
                    temperature=0.7,
                    max_tokens=1024,
                    top_p=1,
                    stream=True  # Enable streaming
                )

                # Create an empty placeholder for the response
                message_placeholder = st.empty()
                full_response = ""

                # Stream the response
                for chunk in chat_completion:
                    if chunk.choices[0].delta.content is not None:
                        full_response += chunk.choices[0].delta.content
                        # Update the placeholder with the accumulated response
                        message_placeholder.markdown(full_response + "▌")
                
                # Final update without the cursor
                message_placeholder.markdown(full_response)
                # Add the complete response to session state
                st.session_state.messages.append({"role": "assistant", "content": full_response})

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")