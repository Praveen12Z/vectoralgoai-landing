import streamlit as st
import time

st.set_page_config(page_title="VectorAlgo AI - AI Trading Bots", layout="wide")

# Custom CSS for styles
st.markdown(
    """
    <style>
    /* Gradient text */
    .gradient-text {
        background: linear-gradient(90deg, #ff7e5f, #feb47b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 4rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin-bottom: 0;
    }
    /* Subheadline */
    .subheadline {
        font-size: 1.5rem;
        color: #666;
        margin-top: 0;
        margin-bottom: 2rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* CTA button */
    .cta-button {
        background: #ff7e5f;
        color: white;
        padding: 1rem 2rem;
        border-radius: 40px;
        font-weight: 700;
        font-size: 1.3rem;
        text-decoration: none;
        transition: background 0.3s ease;
        display: inline-block;
        margin-bottom: 3rem;
    }
    .cta-button:hover {
        background: #feb47b;
        color: #fff;
        cursor: pointer;
    }
    /* Feature blocks */
    .feature {
        text-align: center;
        padding: 1rem 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 20px rgba(255, 126, 95, 0.2);
        background: #fff7f4;
        margin: 1rem;
    }
    .feature h3 {
        font-size: 1.6rem;
        margin-bottom: 0.5rem;
    }
    .feature p {
        color: #666;
        font-size: 1rem;
    }
    /* Founder block */
    .founder {
        background: #ffefd5;
        border-left: 8px solid #ff7e5f;
        padding: 1.5rem 2rem;
        font-style: italic;
        font-size: 1.1rem;
        margin: 3rem 0;
    }
    /* Footer */
    footer {
        font-size: 0.9rem;
        color: #999;
        margin-top: 3rem;
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    a.social-link {
        margin: 0 0.7rem;
        color: #ff7e5f;
        text-decoration: none;
        font-weight: 700;
    }
    a.social-link:hover {
        text-decoration: underline;
        color: #feb47b;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Hero Section
st.markdown('<h1 class="gradient-text">Build AI Trading Bots <br> Without Coding</h1>', unsafe_allow_html=True)
st.markdown('<p class="subheadline">Describe your strategy in simple English — get a fully deployable trading bot instantly.</p>', unsafe_allow_html=True)

# CTA Button
if st.button("Join the Waitlist"):
    st.success("Thanks for joining! We will notify you with updates.")

# Features
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(
        """
        <div class="feature">
        <h3>🚀 Instant Bot Creation</h3>
        <p>Generate live trading bots from plain English strategy descriptions.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        """
        <div class="feature">
        <h3>🧠 AI-Powered NLP</h3>
        <p>Advanced AI translates your words into clean, ready-to-run code.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col3:
    st.markdown(
        """
        <div class="feature">
        <h3>📈 Backtest & Optimize</h3>
        <p>Instantly test strategies and see performance before you trade.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col4:
    st.markdown(
        """
        <div class="feature">
        <h3>🔒 Secure & Easy Deployment</h3>
        <p>Deploy bots safely to your preferred trading platform.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Founder Note
st.markdown(
    """
    <div class="founder">
    “VectorAlgo AI is built by Praveen Kumar — passionate AI researcher and trader. Our mission: democratize algo trading so anyone can automate strategies with zero coding.”
    </div>
    """,
    unsafe_allow_html=True,
)

# Footer with social links
st.markdown(
    """
    <footer>
    Contact us: contact@vectoralgoai.com |  
    <a href="https://t.me/VectorAlgoAI" class="social-link" target="_blank">Telegram</a> |  
    <a href="https://twitter.com/VectorAlgoAI" class="social-link" target="_blank">Twitter</a> |  
    <a href="https://linkedin.com/company/vectoralgoai" class="social-link" target="_blank">LinkedIn</a>
    </footer>
    """,
    unsafe_allow_html=True,
)
