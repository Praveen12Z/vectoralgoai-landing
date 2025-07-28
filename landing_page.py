import streamlit as st
from PIL import Image

# ---- Page Config ----
st.set_page_config(page_title="AI Trading Assistant", layout="centered")

# ---- Custom Styling ----
st.markdown("""
    <style>
        .main { background-color: #f9fafb; }
        h1, h2, h3, p { color: #1f2937; font-family: 'Inter', sans-serif; }
        .stButton button {
            background-color: #3b82f6;
            color: white;
            padding: 0.7em 1.2em;
            font-size: 1rem;
            border-radius: 8px;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# ---- Hero Section ----
st.title("🚀 AI Trading Assistant")
st.markdown("### Smarter Signals. Real-time News. AI-Powered Decisions.")
st.markdown("Welcome to your next-gen trading partner powered by LSTM, GPT, and real-time market insights.")

st.button("👉 Join the Beta Program")

# ---- Features ----
st.markdown("## 🔍 Features")
cols = st.columns(3)

with cols[0]:
    st.subheader("📊 Smart Signals")
    st.write("Predictive LSTM models combined with technical indicators.")

with cols[1]:
    st.subheader("📰 GPT News Sentiment")
    st.write("Real-time news interpreted by GPT for market impact.")

with cols[2]:
    st.subheader("📈 Visual Dashboard")
    st.write("Clean GUI with charts, open positions, and trade logic.")

# ---- Optional: Image / GIF ----
st.markdown("---")
st.markdown("### 👇 Preview")
st.image("ai_trading_dashboard_sample.png", caption="Example Dashboard", use_column_width=True)

# ---- Email Capture (Optional Google Form / Mailchimp) ----
st.markdown("---")
st.markdown("## 📬 Stay Updated")

email = st.text_input("Enter your email to get early access and updates:")

if st.button("Notify Me"):
    if email and "@" in email:
        st.success("✅ Thanks! You'll be notified.")
        # You can write logic to save email to Google Sheets / database here
    else:
        st.error("Please enter a valid email.")

# ---- Footer ----
st.markdown("---")
st.caption("© 2025 Built by Praveen Kumar | AI-Driven Expert Advisor")

