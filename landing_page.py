import streamlit as st
import datetime
import streamlit.components.v1 as components

st.set_page_config(page_title="VectorAlgoAI", layout="wide")

# ===== Header with Countdown =====
launch_date = datetime.datetime(2026, 1, 25, 0, 0, 0)
now = datetime.datetime.now()
countdown = launch_date - now

days = countdown.days
hours, remainder = divmod(countdown.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

st.markdown(f"""
<div style="background-color:#0E1117;padding:1.5rem;border-radius:10px;text-align:center;">
  <h1 style="color:#FF4B4B;font-size:3rem;margin-bottom:0;">🚀 VectorAlgoAI Launches In:</h1>
  <h2 style="color:white;font-size:2.5rem;">{days}d : {hours}h : {minutes}m : {seconds}s</h2>
</div>
""", unsafe_allow_html=True)

# ===== About & Services =====
st.markdown("### 🔍 What We Offer")
st.markdown("""
**VectorAlgoAI** is building the future of retail algorithmic trading. Here's what you'll get:

- 📊 **TradingView-style Charts** with powerful indicators
- 🤖 **Custom AI Expert Advisors (EA)** built from English instructions
- 🧠 **AI Dashboards** for live & downloadable EAs (compatible with MT5, cTrader)
- 📰 **News & Sentiment Analysis Feed**
- ✍️ **Trading Articles & Strategy Hub**
""")

# ===== Join Beta & Email Form =====
st.markdown("### 🧪 Join Beta")
st.markdown("Be the first to test our tools! Get early access to our AI dashboards and EAs.")

with st.form("email_form"):
    email = st.text_input("📧 Enter your email to join the waitlist:")
    submitted = st.form_submit_button("Join Beta")
    if submitted:
        st.success(f"Thanks, we'll notify you at {email}!")

# ===== Calendly Widget =====
st.markdown("### 📅 Book a Free Strategy Call")
components.html("""
<iframe src="https://calendly.com/yadavpraveen898/30min" width="100%" height="600" frameborder="0"></iframe>
""", height=600)

# ===== Social Media Feeds =====
st.markdown("### 📢 Follow Our Updates")
st.markdown("""
Follow us on [Twitter](https://twitter.com) or join our [Telegram](https://telegram.org) for live updates and early features!
""")

# ===== Founder Info =====
st.markdown("### 👨‍💻 About the Founder")
st.markdown("""
**Praveen Kumar** — Founder of VectorAlgoAI  
AI Researcher | Algorithmic Trading Visionary | Passionate about simplifying trading through intelligent automation.
""")

# ===== Footer =====
st.markdown("---")
st.markdown("© 2025 VectorAlgoAI. All rights reserved.")

