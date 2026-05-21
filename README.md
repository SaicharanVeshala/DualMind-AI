# DualMind AI

DualMind AI is a lightweight open-source AI assistant built using Python, Streamlit, Ollama, and TinyLlama.  
The project was created to explore conversational AI, safety guardrails, and local LLM inference without relying on paid APIs or cloud-based frontier models.

The assistant supports multi-turn conversations, basic contextual interaction, and harmful prompt filtering through a simple guardrail system.

---

# Features

- Conversational AI chatbot interface
- Local LLM inference using Ollama
- TinyLlama open-source model integration
- Multi-turn conversation support
- Safety filtering for harmful prompts
- Lightweight and beginner-friendly architecture
- Streamlit-based responsive UI

---

# Tech Stack

- Python
- Streamlit
- Ollama
- TinyLlama
- Custom Safety Guardrails

---

# Project Structure

```bash
ai-assistant-comparison/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assistants/
│   └── oss_assistant.py
│
├── guardrails/
│   └── safety.py
│
├── evals/
│   └── evaluation.py
│
└── screenshots/