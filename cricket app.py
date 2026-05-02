import streamlit as st
import google.generativeai as genai
import os

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Cricket AI Assistant",
    page_icon="🏏",
    layout="wide"
)

# -----------------------------
# DARK THEME CSS
# -----------------------------
st.markdown("""
<style>

body {
    background-color: #0f172a;
}

.stApp {
    background-color: #0f172a;
    color: white;
}

h1,h2,h3,h4,h5,p,label {
    color: white !important;
}

.stTextInput input {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 10px;
    border: 1px solid #334155;
}

.stButton button {
    background: linear-gradient(90deg,#2563eb,#7c3aed);
    color: white !important;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
    font-weight: bold;
}

.stButton button:hover {
    background: linear-gradient(90deg,#1d4ed8,#6d28d9);
}

.result-box {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #334155;
    color: white;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# GEMINI API CONFIG
# -----------------------------
genai.configure(api_key=os.getenv("AIzaSyD1NHJzVu5AtGceMHpyMA8eYJGpG2IdPW8"))

# Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🏏 Cricket AI")

st.sidebar.markdown("""
### About

This AI assistant uses:

• Google Gemini  
• AI cricket analysis  

You can ask about:

✔ Live match scores  
✔ Player stats  
✔ Cricket news  
✔ Records & history  
✔ Teams & tournaments
""")

# -----------------------------
# HEADER
# -----------------------------
st.title("🏏 Cricket AI Assistant")

st.markdown("Ask anything about **live matches, players, records, or teams**")

# -----------------------------
# USER INPUT
# -----------------------------
query = st.text_input("Ask a cricket question")

# -----------------------------
# BUTTON ACTION
# -----------------------------
if st.button("Ask AI"):

    if query.strip() == "":
        st.warning("Please enter a cricket question.")
    else:
        with st.spinner("Analyzing cricket data..."):

            prompt = f"""
            You are an expert cricket analyst AI.

            Give clear, short, and accurate answers about:
            - Live scores
            - Cricket players
            - Match stats
            - Cricket news
            - Records and history
            - Teams and tournaments

            User Question:
            {query}
            """

            try:
                response = model.generate_content(prompt)

                st.markdown("### 📊 Answer")

                st.markdown(
                    f"<div class='result-box'>{response.text}</div>",
                    unsafe_allow_html=True
                )

            except Exception as e:
                st.error(f"Error: {e}")