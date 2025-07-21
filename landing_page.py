import streamlit as st

st.set_page_config(page_title="VectorAlgo AI - AI Trading Expert Advisor", page_icon="🤖", layout="centered")

# --- Header Section ---
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>Welcome to VectorAlgo AI 🤖</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #306998;'>Your AI-powered trading partner — intelligent, fast, and transparent.</h3>", unsafe_allow_html=True)

st.markdown("---")

# --- Trailer style intro ---
st.markdown("""
<div style='text-align:center; font-size: 18px; font-weight: 600; color: #FFD43B;'>
🎬 Coming soon to revolutionize retail trading! 🚀
</div>
""", unsafe_allow_html=True)

st.markdown("""
<ul style='max-width: 600px; margin: auto; font-size: 18px;'>
<li>⚡ Real-time AI trading signals combining LSTM & GPT-4</li>
<li>📈 Seamless integration with your favorite brokers</li>
<li>🤝 Expert insights and fundamental analysis</li>
<li>🔒 Transparent, explainable AI decisions</li>
</ul>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Founder Section ---
st.markdown("<h2 style='text-align: center; color: #4B8BBE;'>About the Founder</h2>", unsafe_allow_html=True)
st.markdown("""
<div style='max-width: 600px; margin: auto; font-size: 16px; line-height: 1.6;'>
Hi, I’m <b>Praveen Kumar</b>, founder of VectorAlgo AI. With a Master’s degree in Artificial Intelligence and years of experience in deep learning and finance, I am passionate about empowering retail traders worldwide by building cutting-edge AI trading tools that are easy to use and highly effective.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Call to Action ---
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🚀 Join Waitlist"):
        st.markdown("[Sign up here](https://forms.gle/your-google-form-link)")

with col2:
    st.markdown("[🐦 Twitter](https://twitter.com/your_twitter_handle)", unsafe_allow_html=True)
    
with col3:
    st.markdown("[💬 Telegram](https://t.me/your_telegram_channel)", unsafe_allow_html=True)

st.markdown("<div style='text-align:center; margin-top: 40px; color: grey;'>Built with ❤️ by Praveen Kumar</div>", unsafe_allow_html=True)
