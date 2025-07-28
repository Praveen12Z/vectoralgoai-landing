import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(
    page_title="VectorAlgoAI",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Load logo
logo = Image.open("logo.png")
st.image(logo, width=200)

# Hero Section
st.markdown("<h1 style='text-align: center;'>Build Your Trading Bot with One Sentence</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>No coding. No downloading. Just describe your strategy — we'll handle the rest.</p>", unsafe_allow_html=True)

st.markdown("---")

# Features
st.markdown("### ✅ What You Get")
st.markdown("""
- 🤖 **AI-Powered Expert Advisor** based on your natural language strategy  
- 📈 **Real-Time Trading Dashboard** in your browser  
- 🧠 **GPT-based Sentiment Analysis** integrated into trading signals  
- ☁️ No installs, no complexity — 100% web-based
""")

st.markdown("---")

# Email Collection
st.markdown("## 🚀 Join the Waitlist")
email = st.text_input("Enter your email to get early access:")
if st.button("Submit"):
    if email:
        with open("emails.txt", "a") as f:
            f.write(email + "\n")
        st.success("✅ You’ve been added to the waitlist!")
    else:
        st.error("Please enter a valid email.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Built by Praveen Kumar · © 2025 VectorAlgoAI</p>", unsafe_allow_html=True)

