import streamlit as st

# --- Page config ---
st.set_page_config(page_title="VectorAlgoAI", page_icon="📈", layout="centered")

# --- Main Header ---
st.title("🚀 VectorAlgoAI")
st.subheader("AI-Powered Trading Signals. Built with LSTM, GPT & Real-Time Market Insight.")

# --- Banner ---
st.markdown("""
### 📢 **Coming Soon!**
We're building the future of AI-driven trading — smarter, faster, and adaptive to markets in real time.

Join the waitlist and be the first to access our private beta!
""")

# --- Join Waitlist ---
with st.form("waitlist_form"):
    email = st.text_input("📧 Enter your email to join waitlist")
    submitted = st.form_submit_button("Join Waitlist")
    if submitted:
        st.success(f"Thanks for joining! We'll notify you at {email} once we launch.")

# --- Product Highlights ---
st.markdown("---")
st.markdown("### ⚙️ What We Offer:")
st.markdown("""
- 📊 LSTM-powered trade signal generation  
- 🧠 GPT-powered news sentiment interpretation  
- 📈 Real-time market analysis + technical indicators  
- 📤 Telegram alerts for trading signals  
- 🧪 Backtested strategies with hybrid AI models  
""")

# --- Contact Info ---
st.markdown("---")
st.markdown("### 📬 Contact Us")
st.markdown("""
- Email: [vectoralgoai@gmail.com](mailto:vectoralgoai@gmail.com)  
- Telegram: [t.me/VectorAlgoAI](https://t.me/VectorAlgoAI)  
- Twitter: [@VectorAlgoAI](https://twitter.com/VectorAlgoAI)  
- LinkedIn: [VectorAlgoAI](https://linkedin.com/company/vectoralgoai)  
""")

st.markdown("---")
st.markdown("Made with ❤️ by Praveen Kumar")
