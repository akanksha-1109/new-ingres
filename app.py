import streamlit as st
from datetime import datetime
import os

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="INGRES AI Chat",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- LOAD EXTERNAL CSS ---
css_file = os.path.join("styles", "chat_styles.css")
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- APP TITLE ---
st.markdown("<h1 style='text-align: center; color: #6C5B7B;'>INGRES AI Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #355C7D;'>Talk to your AI assistant below</p>", unsafe_allow_html=True)

# --- SESSION STATE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

if "input" not in st.session_state:
    st.session_state.input = ""

# --- AI RESPONSE FUNCTION ---
def get_ai_response(prompt: str) -> str:
    msg = prompt.strip().lower()
    if msg == "hello":
        return "Welcome to INGRES AI! How can I help you today?"
    elif msg in ["hi", "hey"]:
        return "Hello! Welcome to INGRES AI. How can I assist you?"
    return f"This is the AI response to: {prompt}"

# --- SEND MESSAGE CALLBACK ---
def send_message():
    user_text = st.session_state.input
    if user_text:
        timestamp = datetime.now().strftime("%H:%M")
        st.session_state.messages.append({"role": "user", "content": user_text, "time": timestamp})

        # AI response
        ai_resp = get_ai_response(user_text)
        timestamp_ai = datetime.now().strftime("%H:%M")
        st.session_state.messages.append({"role": "ai", "content": ai_resp, "time": timestamp_ai})

        # Clear input safely
        st.session_state.input = ""

# --- USER INPUT AND BUTTONS ---
with st.container():
    col1, col2 = st.columns([4,1])
    with col1:
        st.text_input(
            "Type your message here...",
            key="input",
            placeholder="Write something...",
            on_change=send_message
        )
    with col2:
        if st.button("Clear Chat"):
            st.session_state.messages = []

# --- DISPLAY CHAT HISTORY ---
chat_placeholder = st.empty()

with chat_placeholder.container():
    st.markdown("<div class='chat-container' id='chat-box'>", unsafe_allow_html=True)
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(
                f"<div class='user-message'>{msg['content']}<div class='timestamp'>{msg['time']}</div></div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div class='ai-message'>{msg['content']}<div class='timestamp'>{msg['time']}</div></div>",
                unsafe_allow_html=True
            )
    st.markdown("</div>", unsafe_allow_html=True)

# --- SCROLL TO BOTTOM SCRIPT ---
st.markdown("""
<script>
var chatBox = window.parent.document.querySelector('.chat-container');
if (chatBox) {
    chatBox.scrollTop = chatBox.scrollHeight;
}
</script>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.header("About INGRES AI")
    st.markdown("""
    - 
    """)
