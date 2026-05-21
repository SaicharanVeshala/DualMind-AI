import streamlit as st
from datetime import datetime

from assistants.oss_assistant import generate_oss_response
from assistants.frontier_assistant import (
    generate_frontier_response
)

from guardrails.safety import is_safe


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="DualMind AI",
    page_icon="🤖",
    layout="centered"
)


# ---------------- CUSTOM HEADER ---------------- #

st.markdown(
    """
    <h1 style='text-align: center; color: #4F8BF9;'>
        🤖 DualMind AI
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style='text-align: center; font-size:18px; color:gray;'>
        Open-Source + Frontier AI Assistant Comparison
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()


# ---------------- SIDEBAR ---------------- #

st.sidebar.title("DualMind AI")

selected_model = st.sidebar.selectbox(
    "Choose Assistant",
    [
        "Open Source Assistant",
        "Frontier Assistant"
    ]
)

if selected_model == "Open Source Assistant":

    st.sidebar.success("Model: TinyLlama (Ollama)")

else:

    st.sidebar.success("Model: Gemini 1.5 Flash")


st.sidebar.info(
    """
    DualMind AI compares:
    
    • Open-source local LLMs
    
    • Frontier cloud-based models
    
    Features:
    - Multi-turn conversations
    - Safety guardrails
    - Local inference
    - Prompt evaluation
    """
)

# Clear chat button
if st.sidebar.button("🗑️ Clear Chat"):

    st.session_state.messages = []

    st.rerun()

st.sidebar.divider()

st.sidebar.caption(
    "Built using Streamlit, Ollama, and Gemini"
)


# ---------------- SESSION STATE ---------------- #

if "messages" not in st.session_state:

    st.session_state.messages = []


# ---------------- DISPLAY CHAT HISTORY ---------------- #

for msg in st.session_state.messages:

    avatar = "🤖" if msg["role"] == "assistant" else "👤"

    with st.chat_message(
        msg["role"],
        avatar=avatar
    ):

        st.write(msg["content"])

        st.caption(msg["time"])


# ---------------- USER INPUT ---------------- #

user_input = st.chat_input(
    "Ask about AI, Python, Machine Learning..."
)


# ---------------- HANDLE INPUT ---------------- #

if user_input:

    # Safety check
    if not is_safe(user_input):

        st.warning(
            "⚠️ Unsafe prompt detected."
        )

        st.stop()

    current_time = datetime.now().strftime(
        "%I:%M %p"
    )

    # Display user message
    with st.chat_message(
        "user",
        avatar="👤"
    ):

        st.write(user_input)

        st.caption(current_time)

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input,
            "time": current_time
        }
    )

    # ---------------- GENERATE RESPONSE ---------------- #

    with st.spinner("Thinking..."):

        try:

            # OSS Assistant
            if (
                selected_model
                == "Open Source Assistant"
            ):

                response = generate_oss_response(
                    user_input
                )

            # Frontier Assistant
            else:

                response = (
                    generate_frontier_response(
                        user_input
                    )
                )

        except Exception:

            response = (
                "Unable to generate response right now."
            )

    assistant_time = datetime.now().strftime(
        "%I:%M %p"
    )

    # Display assistant response
    with st.chat_message(
        "assistant",
        avatar="🤖"
    ):

        st.write(response)

        st.caption(assistant_time)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
            "time": assistant_time
        }
    )