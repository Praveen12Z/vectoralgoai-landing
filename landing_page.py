import streamlit as st
from datetime import datetime, timedelta
import time

# --- Page config ---
st.set_page_config(page_title="VectorAlgoAI", layout="wide")

# --- Custom CSS styling ---
st.markdown("""
    <style>
        html, body {
            background-color: #0f1117;
            color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
        }
        .hero {
            text-align: center;
            padding: 3rem 1rem;
            background-color: #141722;
            border-radius: 12px;
        }
        .hero h1 {
            font-size: 3.5rem;
            color: #00FFAD;
        }
        .hero p {
            font-size: 1.2rem;
            color: #ccc;
            margin-top: 1rem;
        }
        .countdown {
            font-size: 2rem;
            color: #FFD700;
            font-weight: bold;
            text-align: center;
            margin-bottom: 2rem;
        }
        .services, .timeline, .founder {
            background-color: #1b1e2b;
            padding: 2rem;
            margin-top: 2rem;
            border-radius: 12px;
        }
        h2 {
            color: #00FFAD;
            margin-bottom: 1rem;
        }
        ul {
            line-height: 1.8;
            font-size: 1.1rem;
            color: #ddd;
        }
        .footer {
            text-align: center;
            margin-top: 4rem;
            color: #666;
        }
    </style>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("""
    <div class="hero">
        <h1>VectorAlgoAI</h1>
        <p>AI-Powered Trading Tools, Custom Bots, News & Sentiment Analysis – Built for Traders by Traders.</p>
    </div>
""", unsafe_allow_html=True)

# --- Countdown Timer ---
launch_date = datetime(2026, 1, 25)
now = datetime.now()
remaining = launch_date - now

days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds // 60) % 60
seconds = remaining.seconds % 60

st.markdown(f"""
    <div class="countdown">
        ⏳ Launching In: <br>
        {days} days, {hours} hours, {minutes} minutes, {seconds} seconds
    </div>
""", unsafe_allow_html=True)

# --- Services Section ---
st.markdown("""
    <div class="services">
        <h2>📊 What We Offer</h2>
        <ul>
            <li>Real-time TradingView-style Chart Dashboards</li>
            <li>Custom AI Algorithm Development from Natural Language</li>
            <li>Compatible with MT5, cTrader, and all major platforms</li>
            <li>Web-based EA Dashboards – no downloads needed</li>
            <li>Downloadable expert advisors for desktop traders</li>
            <li>Live News Feed & Market Sentiment Analysis</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# --- Timeline Section ---
st.markdown("""
    <div class="timeline">
        <h2>🗓️ Roadmap to Launch</h2>
        <ul>
            <li><strong>Q3 2025</strong>: Alpha Version Testing with Internal Traders</li>
            <li><strong>Q4 2025</strong>: Public Beta with Core Services</li>
            <li><strong>25 Jan 2026</strong>: 🎉 Official Launch Day!</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# --- Founder Section ---
st.markdown("""
    <div class="founder">
        <h2>👨‍💻 Meet the Founder</h2>
        <p><strong>Praveen Kumar</strong> — AI Engineer & Quantitative Trading Strategist with a Master's in AI from JKU Linz and a background in automobile engineering. 
        Praveen brings years of experience in deep learning, LLMs, and trading system development.</p>

        <p>Driven by passion for democratizing algorithmic trading, he created VectorAlgoAI to empower traders with AI tools that require zero code and deliver professional-grade performance.</p>
        
        <p>📍 Based in Europe | 🚀 Building the future of AI + Trading | 🧠 Fluent in tech, strategy & execution</p>
    </div>
""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
    <div class="footer">
        Built with ❤️ by Praveen Kumar | © 2025 VectorAlgoAI
    </div>
""", unsafe_allow_html=True)
