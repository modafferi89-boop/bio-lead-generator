import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Configurazione della pagina
st.set_page_config(
    page_title="Bio-Hacking & Energy Regeneration",
    page_icon="⚡",
    layout="centered"
)

# Stile CSS avanzato per correggere le debolezze di leggibilità e spaziatura
st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
        color: #f8fafc;
    }
    .stButton>button {
        width: 100%;
        background-color: #0ea5e9;
        color: white;
        font-weight: bold;
        border-radius: 6px;
        padding: 0.75rem;
        border: none;
        font-size: 1.05rem;
    }
    .stButton>button:hover {
        background-color: #0284c7;
        color: white;
    }
    .benefit-box {
        background-color: #ffffff;
        color: #0f172a;
        padding: 20px;
        border-radius: 8px;
        border-left: 6px solid #0ea5e9;
        margin-bottom: 18px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.15);
    }
    .benefit-desc {
        color: #334155;
        font-size: 1rem;
        line-height: 1.5;
        margin-top: 6px;
    }
    .trust-badge {
        text-align: center;
        color: #38bdf8;
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Intestazione Principale con contrasto migliorato per il sottotitolo
st.markdown("<h1 style='text-align: center; color: #38bdf8;'>Reconnect Your Body to Its Optimal Frequency</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; color: #e2e8f0; font-size: 1.1rem;'>Discover the Next Frontier of Bio-Hacking and Energy Regeneration</p>", unsafe_allow_html=True)

st.write("---")

# Badge di fiducia / Trust signals
st.markdown("<div class='trust-badge'>🔒 Secure & Verified Protocol &nbsp;|&nbsp; 🌍 International Standard &nbsp;|&nbsp; ⚡ Instant Access</div>", unsafe_allow_html=True)

# Sezione Benefici con spaziatura e font migliorati
st.markdown("### Key Benefits")

st.markdown("""
<div class="benefit-box">
    <strong style="color: #0284c7; font-size: 1.15rem;">Harmonic Frequency Technology</strong><br>
    <div class="benefit-desc">Leverages advanced stimulation principles to promote a state of deep cellular and mental relaxation.</div>
</div>
<div class="benefit-box">
    <strong style="color: #0284c7; font-size: 1.15rem;">Day & Night Recovery Optimization</strong><br>
    <div class="benefit-desc">Helps counteract the effects of chronic fatigue and oxidative stress caused by fast-paced modern rhythms.</div>
</div>
<div class="benefit-box">
    <strong style="color: #0284c7; font-size: 1.15rem;">Seamless Daily Wellness Integration</strong><br>
    <div class="benefit-desc">Designed for effortless use, offering constant support for your holistic health journey.</div>
</div>
<div class="benefit-box">
    <strong style="color: #0284c7; font-size: 1.15rem;">Non-Invasive Approach</strong><br>
    <div class="benefit-desc">A safe, side-effect-free solution ideal for those looking to care for themselves naturally and cutting-edge.</div>
</div>
""", unsafe_allow_html=True)

st.write("---")

# Sezione Modulo di Raccolta Contatti (Lead Generation)
st.markdown("### Get Instant Access")
st.markdown("Enter your best email address below to unlock immediate access to the full guide and technical presentation.")

def save_lead(email):
    file_path = "leads.csv"
    new_data = pd.DataFrame([[email, datetime.now()]], columns=["Email", "Timestamp"])
    if os.path.exists(file_path):
        new_data.to_csv(file_path, mode='a', header=False, index=False)
    else:
        new_data.to_csv(file_path, mode='index', index=False)

with st.form("lead_form"):
    user_email = st.text_input("Email Address", placeholder="Enter your email...")
    submit_button = st.form_submit_button(label="VIEW THE FULL PRESENTATION")
    
    if submit_button:
        if user_email and "@" in user_email and "." in user_email:
            save_lead(user_email)
            st.success("Access granted! Redirecting to the presentation...")
            
            affiliate_url = "https://www.checkout-ds24.com/redir/649413/vincenzomodafferi/"
            st.markdown(f"""
                <meta http-equiv="refresh" content="1;url={affiliate_url}" />
                <script>
                    window.location.href = "{affiliate_url}";
                </script>
            """, unsafe_allow_html=True)
        else:
            st.error("Please enter a valid email address.")

st.write("---")

# Mini sezione FAQ / Garanzia per aumentare le conversioni
with st.expander("❓ Frequently Asked Questions"):
    st.write("**Q: Is this presentation suitable for beginners?**")
    st.write("A: Yes, the technical guide is structured to be easily understood by anyone passionate about wellness and bio-hacking.")
    st.write("**Q: How do I access the material after entering my email?**")
    st.write("A: You will be instantly redirected to the official technical presentation page.")

st.markdown("<p style='text-align: center; font-size: 0.8rem; color: #64748b; margin-top: 20px;'>Built on rigorous principles of biophysics. Designed for global wellness enthusiasts.</p>", unsafe_allow_html=True)
