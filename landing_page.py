import streamlit as st
from PIL import Image

# ---- Page Config ----
st.set_page_config(page_title="VectorAlgo AI", page_icon="📈", layout="wide")

# ---- Custom Styling ----
st.markdown(
    """
    <style>
        .main { background-color: #ffffff; padding: 0 5%; }
        h1, h2, h3, p { color: #0f172a; font-family: 'Inter', sans-serif; }
        .hero-title { font-size: 2.5rem; font-weight: 600; margin-bottom: 0; }
        .hero-tagline { font-size: 1.2rem; color: #334155; margin-top: 0.25rem; }
        .feature-title { font-size: 1.1rem; font-weight: 600; }
        .stButton button {
            background-color: #2563eb;
            color: white;
            padding: 0.6em 1.2em;
            font-size: 1rem;
            border-radius: 6px;
            border: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---- Hero Section ----
logo_col, title_col = st.columns([1, 4])
with logo_col:
    st.image("logo.png", width=120)
with title_col:
    st.markdown("<div class='hero-title'>VectorAlgo AI</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='hero-tagline'>Smarter signals and market insights for professional traders.</div>",
        unsafe_allow_html=True,
    )
    st.button("Request Early Access")

# ---- Features ----
st.markdown("### Key Features")
cols = st.columns(3)

with cols[0]:
    st.markdown("<div class='feature-title'>Market Signals</div>", unsafe_allow_html=True)
    st.write("Proprietary LSTM models highlight opportunities ahead of the crowd.")

with cols[1]:
    st.markdown("<div class='feature-title'>News Sentiment</div>", unsafe_allow_html=True)
    st.write("Language models analyse headlines to gauge potential impact.")

with cols[2]:
    st.markdown("<div class='feature-title'>Performance Dashboard</div>", unsafe_allow_html=True)
    st.write("Clean charts display open positions and historical results.")

# ---- Optional: Image / GIF ----
st.markdown("---")
st.markdown("### Preview")
st.image("logo.png", caption="Example Dashboard", use_container_width=True)

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

