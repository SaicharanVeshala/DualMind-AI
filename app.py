import streamlit as st

from assistants.oss_assistant import generate_oss_response
from guardrails.safety import is_safe

# Page settings
st.set_page_config(
    page_title="DualMind AI",
    layout="centered"
)

# Title
st.title("DualMind AI")

st.caption(
    "Lightweight open-source AI assistant built using Transformers and Streamlit."
)


# Clear chat button
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()


# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# User input
user_input = st.chat_input("Ask something...")

if user_input:

    # Safety check
    if not is_safe(user_input):

        st.warning("Unsafe prompt detected.")

        st.stop()

    # Show user message
    st.chat_message("user").write(user_input)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Generate AI response
    with st.spinner("Thinking..."):

        response = generate_oss_response(user_input)

    # Show assistant response
    st.chat_message("assistant").write(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )