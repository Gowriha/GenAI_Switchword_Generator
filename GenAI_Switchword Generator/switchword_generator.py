import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="insert_your_api_key")

model = genai.GenerativeModel("gemini-1.5-flash")

# Set Streamlit page layout
st.set_page_config(page_title="Switchword Generator", layout="centered")

# Custom CSS for minimal & calm UI
st.markdown("""
    <style>
    body {
        background-color: #F7F6F3;
        font-family: 'Segoe UI', sans-serif;
    }
    .block-container {
        padding-top: 3rem;
    }
    .stTextArea textarea {
        background-color: #FFFDF9;
        border: 1px solid #d9d9d9;
        border-radius: 12px;
        padding: 12px;
        font-size: 16px;
    }
    .stButton > button {
        background-color: #B9AEDC;
        color: white;
        font-size: 16px;
        border-radius: 10px;
        padding: 10px 20px;
        margin-top: 20px;
    }
    .switch-card {
        background-color: #ffffff;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0px 4px 14px rgba(0, 0, 0, 0.05);
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<h1 style='text-align: center; color: #6B5CA5;'> Switchword Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Describe your situation or emotional state. Get powerful switchwords with meaning.</p>", unsafe_allow_html=True)

# Input Area
scenario = st.text_area("What's on your mind?", placeholder="e.g., I feel anxious about my exams")

# Button
if st.button("Generate", key="generate"):
    if scenario.strip():
        prompt = f"""
You are a mindful spiritual guide and coach. 
The user will provide a situation or emotional struggle.
Your job is to generate 2 or 3 **switchword combinations** using well-known switchwords (like TOGETHER, DIVINE, REACH, etc.) that match the scenario.

Each suggestion must include:
- The **switchword phrase**
- A short **explanation** of how it helps
- Write clearly and spiritually

Example format:
1. **TOGETHER-DIVINE-REACH**  
   Brings unity of mind, divine flow, and helps achieve goals effortlessly.

Only give the results. Don't include intro or extra notes.
Now generate for this: {scenario}
"""
        try:
            response = model.generate_content(prompt)
            st.markdown("<div class='switch-card'>", unsafe_allow_html=True)
            st.markdown("### Your Switchwords")
            st.markdown(response.text.strip())
            st.markdown("</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"❌ Gemini API Error: {str(e)}")
    else:
        st.warning("Please describe your emotional state or situation first.")
