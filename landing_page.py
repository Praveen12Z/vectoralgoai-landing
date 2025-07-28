import streamlit as st

import datetime
import streamlit.components.v1 as components

# Refresh every 1 second
st_autorefresh(interval=1000, key="auto_refresh")

st.set_page_config(page_title="VectorAlgoAI", layout="wide")

# ====== Header & LIVE Countdown =======
launch_date = datetime.datetime(2026, 1, 25, 0, 0, 0)
now = datetime.datetime.now()
countdown = launch_date - now

days = countdown.days
hours, remainder = divmod(countdown.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

st.markdown(f"""
<div style="background-color:#0E1117;padding:1.5rem;border-radius:10px;text-align:center;">
  <h1 style="color:#FF4B4B;font-size:3rem;margin-bottom:0;">🚀 VectorAlgoAI Launch Countdown</h1>
  <h2 style="color:white;font-size:2.5rem;">{days}d : {hours}h : {minutes}m : {seconds}s</h2>
</div>
""", unsafe_allow_html=True)

# ====== About Section =======
st.markdown("## 🤖 What is VectorAlgoAI?")
st.markdown("""
VectorAlgoAI is building the **next generation of AI-powered trading infrastructure** for retail and semi-professional traders.
""")

# ====== Clear & Transparent Services =======
st.markdown("## 💼 Our Services")

st.markdown("""
### 📈 TradingView-style Web Charts  
- Interactive, fast charts with indicators and overlays  
- Full-screen mode, drawing tools, and custom timeframes  
- Integrates seamlessly with your strategies

---

### 🧠 Custom AI Expert Advisors (EAs)  
- Just **describe your strategy in English** — we convert it to code  
- Delivered as **ready-to-use EAs** compatible with **MT5, cTrader, TradingView**, and more  
- **No downloads required** — run directly on your cloud dashboard  
- Option to download for offline platforms

---

### 🗞️ Real-time News + Sentiment Analysis  
- Stay ahead with **AI-filtered financial news**  
- Market mood detection using GPT sentiment scoring  
- Filter by ticker, asset class, or region

---

### ✍️ Articles & Education  
- Short reads and explainers for all trading levels  
- Strategy insights, algorithm education, and tutorials  
- Backtested performance reports

---

### 🧪 AI Dashboard Access  
- See and manage all your custom EAs in one dashboard  
- Performance metrics, PnL tracking, strategy adjustments  
- Access from mobile, desktop, or tablet
""")

# ====== Join Beta =======
st.markdown("## 🔓 Join the Beta Access List")

with st.form("email_form"):
    email = st.text_input("📧 Enter your email to get early access:")
    submitted = st.form_submit_button("Join Beta")
    if submitted:
        st.success(f"Thanks, {email} has been added to the early access list!")

# ====== Calendar Booking =======
st.markdown("## 📅 Book a Strategy Call with Founder")

components.html("""
<iframe src="https://calendly.com/yadavpraveen898/30min" width="100%" height="600" frameborder="0" style="border-radius:10px;"></iframe>
""", height=600)

# ====== Follow Us =======
st.markdown("## 📣 Stay Connected")
st.markdown("""
📢 [Join us on Telegram](https://t.me/yourchannel)  
🐦 [Follow us on Twitter](https://twitter.com/yourhandle)  
📬 Subscribe to our weekly newsletter
""")

# ====== Founder Info =======
st.markdown("## 👨‍💻 Meet the Founder")

st.markdown("""
**Praveen Kumar**  
Founder, VectorAlgoAI  
- AI Researcher & ML Engineer  
- Experienced in deep learning, trading, and real-world deployment  
- Passionate about democratizing access to intelligent trading systems
""")

# ====== Footer =======
st.markdown("---")
st.markdown("© 2025 VectorAlgoAI. All rights reserved.")
