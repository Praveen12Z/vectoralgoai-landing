import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(page_title="VectorAlgoAI", layout="centered")

# Custom styles
st.markdown("""
<style>
h1, h2, h3 {
    color: #4B8BBE;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.service-icon {
    font-size: 40px;
    color: #F39C12;
    margin-right: 15px;
}
.service-item {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}
.countdown {
    font-size: 48px;
    font-weight: bold;
    color: #E74C3C;
    margin-top: 10px;
}
.timeline {
    border-left: 4px solid #4B8BBE;
    margin-left: 20px;
    padding-left: 20px;
}
.timeline-item {
    margin-bottom: 30px;
}
.timeline-date {
    color: #2980B9;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Header and logo
st.title("🚀 VectorAlgoAI")
st.image("logo.png", width=120)  # Replace with your actual logo filename

# Services section
st.subheader("What We Offer")
services = [
    ("📈", "Interactive Trading Charts", "Analyze markets with intuitive, real-time charts—no downloads needed."),
    ("🤖", "Custom AI Expert Advisors", "Describe your trading strategy in plain English and get a personalized AI-powered Expert Advisor compatible with MT5, cTrader, and more."),
    ("📊", "Unified Dashboard", "Manage strategies, monitor open positions, and receive signals — all in one easy-to-use platform."),
    ("📰", "News & Sentiment Analysis", "Stay updated with curated financial news and AI-powered sentiment insights to make smarter decisions."),
]

for icon, title, desc in services:
    st.markdown(f"""
    <div class="service-item">
        <div class="service-icon">{icon}</div>
        <div>
            <strong>{title}</strong><br>
            <small>{desc}</small>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Roadmap with timeline style
st.subheader("Our Roadmap")
roadmap = [
    ("Nov 2025", "MVP", "Basic charts + Strategy input form + Sample signals + News & Sentiment feed"),
    ("Jan 2026", "Beta Launch", "AI-driven EA generation + Backtesting dashboard"),
    ("Mar 2026", "Full Launch", "Multi-platform EA downloads + Real-time data + Advanced analytics"),
]

st.markdown('<div class="timeline">', unsafe_allow_html=True)
for date, phase, desc in roadmap:
    st.markdown(f"""
    <div class="timeline-item">
        <div class="timeline-date">{date}</div>
        <strong>{phase}</strong><br>
        <small>{desc}</small>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="VectorAlgoAI Live Timer Demo", layout="centered")

launch_date = datetime(2026, 1, 25, 0, 0, 0)

st.title("🚀 Countdown to Launch")

# Create an empty placeholder for the timer
timer_placeholder = st.empty()

def format_time_left(timedelta):
    days = timedelta.days
    hours, remainder = divmod(timedelta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days:02}d : {hours:02}h : {minutes:02}m : {seconds:02}s"

while True:
    now = datetime.now()
    time_left = launch_date - now
    if time_left.total_seconds() <= 0:
        timer_placeholder.markdown("<h2 style='color:green; text-align:center;'>🎉 We have launched! Welcome to VectorAlgoAI.</h2>", unsafe_allow_html=True)
        break
    
    # Display timer with custom styling and monospace font for digital feel
    timer_placeholder.markdown(f"""
        <div style="
            font-family: 'Courier New', Courier, monospace;
            font-size: 64px;
            font-weight: bold;
            color: #E74C3C;
            text-align: center;
            background: #1e1e1e;
            border-radius: 12px;
            padding: 20px;
            width: fit-content;
            margin: auto;
            box-shadow: 0 0 20px #E74C3C;">
            {format_time_left(time_left)}
        </div>
    """, unsafe_allow_html=True)
    
    time.sleep(1)
