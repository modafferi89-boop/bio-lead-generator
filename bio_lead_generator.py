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

# ID Google Analytics
GOOGLE_ANALYTICS_ID = "G-GHSTG893H9"

if GOOGLE_ANALYTICS_ID != "G-XXXXXXXXXX":
    st.markdown(f"""
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id={GOOGLE_ANALYTICS_ID}"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){{dataLayer.push(arguments);}}
          gtag('js', new Date());
          gtag('config', '{GOOGLE_ANALYTICS_ID}');
        </script>
    """, unsafe_allow_html=True)

# Selettore di lingua in cima alla pagina
col1, col2, col3 = st.columns([2, 2, 1])
with col3:
    lingua = st.selectbox("🌐", ["English", "Italiano"], label_visibility="collapsed")

# Dizionario delle traduzioni
t = {
    "English": {
        "title": "Reconnect Your Body to Its Optimal Frequency",
        "subtitle": "Discover the Next Frontier of Bio-Hacking and Energy Regeneration",
        "trust": "🔒 Secure Protocol &nbsp;|&nbsp; 🌍 International Standard &nbsp;|&nbsp; ⚡ Instant Access",
        "social": "⭐️ Trusted by over 1,400+ bio-hacking enthusiasts worldwide",
        "benefits_title": "Key Benefits",
        "b1_title": "Harmonic Frequency Technology",
        "b1_desc": "Leverages advanced stimulation principles to promote a state of deep cellular and mental relaxation.",
        "b2_title": "Day & Night Recovery Optimization",
        "b2_desc": "Helps counteract the effects of chronic fatigue and oxidative stress caused by fast-paced modern rhythms.",
        "b3_title": "Seamless Daily Wellness Integration",
        "b3_desc": "Designed for effortless use, offering constant support for your holistic health journey.",
        "b4_title": "Non-Invasive Approach",
        "b4_desc": "A safe, side-effect-free solution ideal for those looking to care for themselves naturally and cutting-edge.",
        "form_title": "Get Instant Access",
        "form_desc": "Enter your best email address below to unlock immediate access to the full guide and technical presentation.",
        "email_placeholder": "Enter your email...",
        "button": "UNLOCK INSTANT ACCESS NOW",
        "success": "Access granted! Redirecting to the presentation...",
        "error": "Please enter a valid email address.",
        "faq_title": "❓ Frequently Asked Questions",
        "q1": "Q: Is this presentation suitable for beginners?",
        "a1": "A: Yes, the technical guide is structured to be easily understood by anyone passionate about wellness and bio-hacking.",
        "q2": "Q: How do I access the material after entering my email?",
        "a2": "A: You will be instantly redirected to the official technical presentation page.",
        "footer": "Built on rigorous principles of biophysics. Designed for global wellness enthusiasts."
    },
    "Italiano": {
        "title": "Riconnetti il tuo corpo alla sua frequenza ottimale",
        "subtitle": "Scopri la nuova frontiera del Bio-Hacking e della Rigenerazione Energetica",
        "trust": "🔒 Protocollo Sicuro &nbsp;|&nbsp; 🌍 Standard Internazionale &nbsp;|&nbsp; ⚡ Accesso Immediato",
        "social": "⭐️ Scelto da oltre 1.400+ appassionati di bio-hacking in tutto il mondo",
        "benefits_title": "Principali Vantaggi",
        "b1_title": "Tecnologia a Frequenza Armonica",
        "b1_desc": "Sfrutta principi di stimolazione avanzata per promuovere uno stato di profondo rilassamento cellulare e mentale.",
        "b2_title": "Ottimizzazione del Recupero Giorno e Notte",
        "b2_desc": "Aiuta a contrastare gli effetti della stanchezza cronica e dello stress ossidativo causati dai ritmi moderni.",
        "b3_title": "Integrazione Perfetta nel Benessere Quotidiano",
        "b3_desc": "Progettato per un utilizzo semplice, offre un supporto costante per il tuo percorso di salute olistica.",
        "b4_title": "Approccio Non Invasivo",
        "b4_desc": "Una soluzione sicura e priva di effetti collaterali, ideale per chi desidera prendersi cura di sé in modo naturale e all'avanguardia.",
        "form_title": "Ottieni Accesso Immediato",
        "form_desc": "Inserisci il tuo miglior indirizzo email qui sotto per sbloccare l'accesso immediato alla guida e alla presentazione tecnica.",
        "email_placeholder": "Inserisci la tua email...",
        "button": "SBLOCCA SUBITO L'ACCESSO",
        "success": "Accesso consentito! Reindirizzamento alla presentazione...",
        "error": "Inserisci un indirizzo email valido.",
        "faq_title": "❓ Domande Frequenti",
        "q1": "D: Questa presentazione è adatta ai principianti?",
        "a1": "R: Sì, la guida tecnica è strutturata per essere compresa facilmente da chiunque sia appassionato di benessere e bio-hacking.",
        "q2": "D: Come posso accedere al materiale dopo aver inserito la mia email?",
        "a2": "R: Verrai reindirizzato istantaneamente alla pagina della presentazione tecnica ufficiale.",
        "footer": "Basato su rigorosi principi di biofisica. Progettato per gli amanti del benessere di tutto il mondo."
    }
}

# Stile CSS ottimizzato
st.markdown("""
    <style>
    .main {
        background-color: #f8fafc;
        color: #0f172a;
    }
    .stButton>button {
        width: 100%;
        background-color: #0ea5e9;
        color: white;
        font-weight: bold;
        border-radius: 6px;
        padding: 0.8rem;
        border: none;
        font-size: 1.1rem;
    }
    .stButton>button:hover {
        background-color: #0284c7;
        color: white;
    }
    .benefit-box {
        background-color: #ffffff;
        color: #0f172a;
        padding: 22px;
        border-radius: 8px;
        border-left: 6px solid #0ea5e9;
        margin-bottom: 18px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-top: 1px solid #e2e8f0;
        border-right: 1px solid #e2e8f0;
        border-bottom: 1px solid #e2e8f0;
    }
    .benefit-desc {
        color: #334155;
        font-size: 1.02rem;
        line-height: 1.5;
        margin-top: 6px;
    }
    .trust-badge {
        text-align: center;
        color: #0284c7;
        font-size: 0.95rem;
        font-weight: 600;
        margin-bottom: 15px;
    }
    .social-proof {
        text-align: center;
        color: #64748b;
        font-size: 0.9rem;
        margin-bottom: 25px;
        font-style: italic;
    }
    </style>
""", unsafe_allow_html=True)

# Intestazione Principale
st.markdown(f"<h1 style='text-align: center; color: #0284c7;'>{t[lingua]['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; font-style: italic; color: #475569; font-size: 1.15rem;'>{t[lingua]['subtitle']}</p>", unsafe_allow_html=True)

st.write("---")

# Badge di fiducia e Social Proof
st.markdown(f"<div class='trust-badge'>{t[lingua]['trust']}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='social-proof'>{t[lingua]['social']}</div>", unsafe_allow_html=True)

# Sezione Benefici
st.markdown(f"### {t[lingua]['benefits_title']}")

st.markdown(f"""
<div class="benefit-box">
    <strong style="color: #0284c7; font-size: 1.15rem;">{t[lingua]['b1_title']}</strong><br>
    <div class="benefit-desc">{t[lingua]['b1_desc']}</div>
</div>
<div class="benefit-box">
    <strong style="color: #0284c7; font-size: 1.15rem;">{t[lingua]['b2_title']}</strong><br>
    <div class="benefit-desc">{t[lingua]['b2_desc']}</div>
</div>
<div class="benefit-box">
    <strong style="color: #0284c7; font-size: 1.15rem;">{t[lingua]['b3_title']}</strong><br>
    <div class="benefit-desc">{t[lingua]['b3_desc']}</div>
</div>
<div class="benefit-box">
    <strong style="color: #0284c7; font-size: 1.15rem;">{t[lingua]['b4_title']}</strong><br>
    <div class="benefit-desc">{t[lingua]['b4_desc']}</div>
</div>
""", unsafe_allow_html=True)

st.write("---")

# Sezione Modulo di Raccolta Contatti (Lead Generation)
st.markdown(f"### {t[lingua]['form_title']}")
st.markdown(t[lingua]['form_desc'])

def save_lead(email):
    file_path = "leads.csv"
    new_data = pd.DataFrame([[email, datetime.now()]], columns=["Email", "Timestamp"])
    if os.path.exists(file_path):
        new_data.to_csv(file_path, mode='a', header=False, index=False)
    else:
        new_data.to_csv(file_path, mode='w', header=True, index=False)

with st.form("lead_form"):
    user_email = st.text_input("Email Address", placeholder=t[lingua]['email_placeholder'])
    submit_button = st.form_submit_button(label=t[lingua]['button'])
    
    if submit_button:
        if user_email and "@" in user_email and "." in user_email:
            save_lead(user_email)
            st.success(t[lingua]['success'])
            
            affiliate_url = "https://www.checkout-ds24.com/redir/649413/vincenzomodafferi/"
            st.markdown(f"""
                <meta http-equiv="refresh" content="1;url={affiliate_url}" />
                <script>
                    window.location.href = "{affiliate_url}";
                </script>
            """, unsafe_allow_html=True)
        else:
            st.error(t[lingua]['error'])

st.write("---")

# Sezione FAQ a scomparsa
with st.expander(t[lingua]['faq_title']):
    st.write(f"**{t[lingua]['q1']}**")
    st.write(t[lingua]['a1'])
    st.write(f"**{t[lingua]['q2']}**")
    st.write(t[lingua]['a2'])

st.markdown(f"<p style='text-align: center; font-size: 0.8rem; color: #64748b; margin-top: 25px;'>{t[lingua]['footer']}</p>", unsafe_allow_html=True)
