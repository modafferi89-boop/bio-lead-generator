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

# Iniezione corretta del Tag Google Analytics
if GOOGLE_ANALYTICS_ID and GOOGLE_ANALYTICS_ID != "G-XXXXXXXXXX":
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

# Selettore di lingua principale in alto a destra
col1, col2, col3 = st.columns([2, 2, 1])
with col3:
    lingua = st.selectbox(
        "🌐", 
        ["English", "Italiano", "Español", "Français", "Deutsch", "中文", "日本語", "العربية"], 
        label_visibility="collapsed"
    )

# Dizionario delle traduzioni ottimizzato per un pubblico sensibile ed etico
t = {
    "English": {
        "title": "Restore Balance and Harmony to Your Natural Energy",
        "subtitle": "A gentle, science-backed approach to modern well-being and inner vitality",
        "trust": "🔒 Safe & Transparent &nbsp;|&nbsp; 🌍 Mindful Standard &nbsp;|&nbsp; ⚡ Respectful Approach",
        "social": "⭐️ Welcomed with trust by individuals seeking conscious wellness worldwide",
        "benefits_title": "Why Choose a Harmonious Approach",
        "b1_title": "Gentle Harmonic Frequency",
        "b1_desc": "Carefully designed to support deep relaxation and help restore your natural inner rhythm without disruption.",
        "b2_title": "Mindful Recovery & Rest",
        "b2_desc": "Thoughtfully crafted to gently soothe the effects of daily stress and mental fatigue.",
        "b3_title": "Seamless & Natural Integration",
        "b3_desc": "Fits effortlessly into your lifestyle, offering quiet, reliable support for your personal wellness journey.",
        "b4_title": "Completely Non-Invasive",
        "b4_desc": "A calm, safe, and completely side-effect-free path designed to care for your body with absolute respect.",
        "form_title": "Receive the Complete Guide",
        "form_desc": "Enter your email address below to receive the detailed informational guide directly in your inbox, at your own pace.",
        "email_placeholder": "Enter your email address...",
        "button": "SEND ME THE FREE GUIDE",
        "success": "Thank you. Redirecting you to the information page...",
        "error": "Please enter a valid email address.",
        "faq_title": "❓ Frequently Asked Questions",
        "q1": "Q: Is this suitable for everyone?",
        "a1": "A: Yes, the guide has been created with care to be clear, transparent, and accessible to anyone approaching conscious wellness.",
        "q2": "Q: What happens after I enter my email?",
        "a2": "A: You will be gently guided to the complete presentation page, with no obligation or rush.",
        "footer": "Rooted in rigorous biophysical principles and mindful care. Designed for conscious living."
    },
    "Italiano": {
        "title": "Ritrova l'Armonia e l'Equilibrio della tua Energia Naturale",
        "subtitle": "Un approccio gentile e consapevole al benessere e alla vitalità di tutti i giorni",
        "trust": "🔒 Sicuro e Trasparente &nbsp;|&nbsp; 🌍 Standard Etico &nbsp;|&nbsp; ⚡ Ascolto e Rispetto",
        "social": "⭐️ Accolto con fiducia da persone attente al proprio benessere consapevole in tutto il mondo",
        "benefits_title": "Perché scegliere un percorso armonioso",
        "b1_title": "Frequenze Armoniche Delicate",
        "b1_desc": "Studiate con cura per favorire un profondo rilassamento e accompagnare il corpo verso il suo ritmo naturale.",
        "b2_title": "Rigenerazione e Riposo Consapevole",
        "b2_desc": "Un supporto pensato per alleggerire con delicatezza gli effetti dello stress quotidiano e della stanchezza mentale.",
        "b3_title": "In Armonia con la tua Quotidianità",
        "b3_desc": "Si integra in modo fluido e naturale nella tua routine, offrendo un sostegno costante e silenzioso.",
        "b4_title": "Approccio Totalmente Non Invasivo",
        "b4_desc": "Una via sicura, priva di effetti collaterali e concepita per prendersi cura di sé con il massimo rispetto.",
        "form_title": "Ricevi la Guida Approfondita",
        "form_desc": "Inserisci il tuo indirizzo email qui sotto per ricevere la presentazione tecnica completa e scoprire tutti i dettagli in libertà.",
        "email_placeholder": "Inserisci il tuo indirizzo email...",
        "button": "INVIAMI LA GUIDA GRATUITA",
        "success": "Grazie di cuore. Verrai reindirizzato alla pagina informativa...",
        "error": "Inserisci un indirizzo email valido per favore.",
        "faq_title": "❓ Domande Frequenti",
        "q1": "D: È un percorso adatto a chi si avvicina per la prima volta a questi temi?",
        "a1": "R: Assolutamente sì. La guida è pensata per essere chiara, trasparente e accessibile a chiunque desideri prendersi cura di sé.",
        "q2": "D: Cosa succede dopo aver inserito la mia email?",
        "a2": "R: Verrai accompagnato direttamente alla pagina della presentazione ufficiale, senza alcun impegno o fretta.",
        "footer": "Fondato su rigorosi principi di biofisica e rispetto della persona. Dedicato a chi vive il benessere in modo consapevole."
    },
    "Español": {
        "title": "Restaura el Equilibrio y la Armonía de tu Energía Natural",
        "subtitle": "Un enfoque consciente y respetuoso hacia el bienestar y la vitalidad",
        "trust": "🔒 Seguro y Transparente &nbsp;|&nbsp; 🌍 Enfoque Ético &nbsp;|&nbsp; ⚡ Respeto Absoluto",
        "social": "⭐️ Acogido con confianza por personas que buscan un bienestar consciente en todo el mundo",
        "benefits_title": "Por qué elegir un enfoque armonioso",
        "b1_title": "Frecuencias Armónicas Suaves",
        "b1_desc": "Diseñadas cuidadosamente para fomentar una relajación profunda y acompañar tu ritmo natural.",
        "b2_title": "Recuperación y Descanso Consciente",
        "b2_desc": "Un apoyo pensado para calmar con delicadeza los efectos del estrés diario.",
        "b3_title": "Integración Natural en tu Día a Día",
        "b3_desc": "Se adapta de forma fluida a tu estilo de vida, ofreciendo un respaldo constante.",
        "b4_title": "Enfoque Totalmente No Invasivo",
        "b4_desc": "Un camino seguro y libre de efectos secundarios, creado para cuidar de ti con respeto.",
        "form_title": "Recibe la Guía Completa",
        "form_desc": "Introduce tu correo electrónico para recibir toda la información detallada a tu propio ritmo.",
        "email_placeholder": "Introduce tu correo electrónico...",
        "button": "QUIERO RECIBIR LA GUÍA",
        "success": "Muchas gracias. Te redirigimos a la página informativa...",
        "error": "Por favor, introduce un correo electrónico válido.",
        "faq_title": "❓ Preguntas Frecuentes",
        "q1": "P: ¿Es adecuado para principiantes?",
        "a1": "R: Sí, la guía es transparente y accesible para cualquier persona interesada en el bienestar.",
        "q2": "P: ¿Qué ocurre después de introducir mi correo?",
        "a2": "R: Serás dirigido a la presentación oficial sin ningún tipo de compromiso.",
        "footer": "Basado en principios de biofísica y cuidado consciente. Para amantes del bienestar global."
    },
    "Français": {
        "title": "Retrouvez l'Harmonie et l'Équilibre de votre Énergie Naturelle",
        "subtitle": "Une approche douce, respectueuse et consciente du bien-être au quotidien",
        "trust": "🔒 Sûr et Transparent &nbsp;|&nbsp; 🌍 Standard Éthique &nbsp;|&nbsp; ⚡ Écoute et Respect",
        "social": "⭐️ Accueilli avec confiance par des personnes en quête de bien-être conscient",
        "benefits_title": "Pourquoi choisir une démarche harmonieuse",
        "b1_title": "Fréquences Harmoniques Douces",
        "b1_desc": "Conçues avec soin pour favoriser un apaisement profond et respecter votre rythme.",
        "b2_title": "Récupération et Repos Serein",
        "b2_desc": "Un soutien pensé pour adoucir les effets du stress quotidien et de la fatigue.",
        "b3_title": "Harmonie avec votre Quotidien",
        "b3_desc": "S'intègre naturellement dans votre vie pour un accompagnement discret et constant.",
        "b4_title": "Approche Totalement Non Invasive",
        "b4_desc": "Une voie sûre et sans effets secondaires, idéale pour prendre soin de soi en toute confiance.",
        "form_title": "Recevez le Guide Complet",
        "form_desc": "Indiquez votre adresse e-mail ci-dessous pour découvrir la présentation détaillée à votre rythme.",
        "email_placeholder": "Votre adresse e-mail...",
        "button": "RECEVOIR LE GUIDE GRATUIT",
        "success": "Merci beaucoup. Redirection vers la page d'information...",
        "error": "Veuillez entrer une adresse e-mail valide.",
        "faq_title": "❓ Questions Fréquentes",
        "q1": "Q : Est-ce adapté à ceux qui débutent ?",
        "a1": "R : Tout à fait, le guide est conçu pour être clair, transparent et accessible à tous.",
        "q2": "Q : Que se passe-t-il après avoir entré mon e-mail ?",
        "a2": "R : Vous accéderez directement à la présentation officielle, en toute liberté.",
        "footer": "Fondé sur des principes rigoureux et un soin attentif. Conédié au bien-être conscient."
    },
    "Deutsch": {
        "title": "Finden Sie die Harmonie und Balance Ihrer natürlichen Energie",
        "subtitle": "Ein achtsamer und sanfter Weg zu mehr Wohlbefinden und innerer Vitalität",
        "trust": "🔒 Sicher & Transparent &nbsp;|&nbsp; 🌍 Ethischer Standard &nbsp;|&nbsp; ⚡ Respektvoller Ansatz",
        "social": "⭐️ Vertrauensvoll geschätzt von Menschen, die bewusste Lebensqualität suchen",
        "benefits_title": "Warum ein harmonischer Weg der richtige ist",
        "b1_title": "Sanfte Harmonische Frequenzen",
        "b1_desc": "Sorgfältig entwickelt, um tiefe Entspannung zu fördern und den natürlichen Rhythmus zu unterstützen.",
        "b2_title": "Achtsame Erholung & Ruhe",
        "b2_desc": "Ein durchdachter Begleiter, um die Spuren des Alltagsstress sanft auszugleichen.",
        "b3_title": "Harmonisch im Alltag integriert",
        "b3_desc": "Fügt sich unaufdringlich in Ihr Leben ein und bietet verlässliche Unterstützung.",
        "b4_title": "Vollständig Nicht-Invasiv",
        "b4_desc": "Ein sicherer, nebenwirkungsfreier Ansatz für einen respektvollen Umgang mit dem eigenen Körper.",
        "form_title": "Den ausführlichen Leitfaden anfordern",
        "form_desc": "Geben Sie Ihre E-Mail-Adresse ein, um die vollständigen Informationen in Ihrem eigenen Tempo zu erhalten.",
        "email_placeholder": "Ihre E-Mail-Adresse...",
        "button": "LEITFADEN KOSTENLOS ANFORDERN",
        "success": "Vielen Dank. Sie werden zur Informationsseite weitergeleitet...",
        "error": "Bitte geben Sie eine gültige E-Mail-Adresse ein.",
        "faq_title": "❓ Häufig gestellte Fragen",
        "q1": "F: Ist dieser Ansatz auch für Einsteiger geeignet?",
        "a1": "A: Ja, der Leitfaden ist transparent und für jeden verständlich aufgebaut.",
        "q2": "F: Was geschieht nach der E-Mails-Eingabe?",
        "a2": "A: Sie gelangen völlig unverbindlich direkt zur offiziellen Präsentation.",
        "footer": "Verankert in biophysikalischen Prinzipien und bewusster Fürsorge."
    },
    "中文": {
        "title": "找回您自然能量的和谐与平衡",
        "subtitle": "一种温和、科学且注重关怀的现代健康与活力之旅",
        "trust": "🔒 安全透明 &nbsp;|&nbsp; 🌍 意识标准 &nbsp;|&nbsp; ⚡ 尊重关怀",
        "social": "⭐️ 受到全球追求意识健康人士的信任与欢迎",
        "benefits_title": "为什么选择和谐的方法",
        "b1_title": "柔和的谐振频率",
        "b1_desc": "精心设计，旨在促进深层放松，帮助恢复您的自然内在节奏。",
        "b2_title": "用心恢复与休息",
        "b2_desc": "体贴地舒缓日常快节奏带来的精神疲劳与压力。",
        "b3_title": "无缝融入日常生活",
        "b3_desc": "轻松契合您的生活方式，为您的健康之旅提供安静、可靠的支持。",
        "b4_title": "完全无创的方法",
        "b4_desc": "一条安全、无副作用、以绝对尊重呵护身体的温和途径。",
        "form_title": "获取完整指南",
        "form_desc": "在下方输入您的电子邮箱，以便按照您自己的节奏接收详细的资讯指南。",
        "email_placeholder": "请输入您的电子邮箱...",
        "button": "免费获取指南",
        "success": "非常感谢。正在引导您进入资讯页面...",
        "error": "请输入有效的电子邮箱地址。",
        "faq_title": "❓ 常见问题",
        "q1": "问：这适合初次接触的人吗？",
        "a1": "答：是的，本指南旨在保持清晰透明，适合任何注重健康的朋友。",
        "q2": "问：输入邮箱后会发生什么？",
        "a2": "答：您将被轻柔地引导至官方展示页面，没有任何压力或强制。",
        "footer": "根植于严谨的生物物理学与用心关怀。专为注重意识生活的您设计。"
    },
    "日本語": {
        "title": "自然なエネルギーの調和とバランスを取り戻す",
        "subtitle": "現代の健やかさと内なる活力に向けた、優しく寄り添うアプローチ",
        "trust": "🔒 安全と透明性 &nbsp;|&nbsp; 🌍 倫理的基準 &nbsp;|&nbsp; ⚡ 丁寧な配慮",
        "social": "⭐️ 世界中で意識的なウェルネスを求める方々から温かい信頼を寄せられています",
        "benefits_title": "調和をもたらす理由",
        "b1_title": "穏やかなハーモニック周波数",
        "b1_desc": "深いリラックスを促し、本来の健やかなリズムへ優しく導くよう設計されています。",
        "b2_title": "心休まる休息と回復",
        "b2_desc": "日々の緊張や心身の疲れをやわらげるための細やかなサポートです。",
        "b3_title": "日々の暮らしに自然と寄り添う",
        "b3_desc": "生活のリズムを崩さず、静かで確かな支えを日常にもたらします。",
        "b4_title": "完全な非侵襲的アプローチ",
        "b4_desc": "身体への負担や副作用がなく、大切にご自身をケアするための安全な方法です。",
        "form_title": "詳細ガイドを受け取る",
        "form_desc": "メールアドレスを入力して、ご自身のペースで詳しい案内資料をお受け取りください。",
        "email_placeholder": "メールアドレスを入力...",
        "button": "無料ガイドを受け取る",
        "success": "ありがとうございます。案内ページへお進みします...",
        "error": "有効なメールアドレスを入力してください。",
        "faq_title": "❓ よくある質問",
        "q1": "Q: 初めての方でも安心してご覧いただけますか？",
        "a1": "A: はい。どなたにも分かりやすく、透明性のある内容でまとめています。",
        "q2": "Q: メール入力後はどうなりますか？",
        "a2": "A: プレッシャーや義務感なく、公式のプレゼンテーションページへご案内します。",
        "footer": "生物物理学の原理と細やかな思いやりを基盤としています。"
    },
    "العربية": {
        "title": "استعد الانسجام والتوازن لطاقتك الطبيعية",
        "subtitle": "نهج لطيف وواعي نحو العافية الحديثة والحيوية الداخلية",
        "trust": "🔒 آمن وشفاف &nbsp;|&nbsp; 🌍 معيار أخلاقي &nbsp;|&nbsp; ⚡ احترام واهتمام",
        "social": "⭐️ محل ثقة الأفراد الباحثين عن العافية الواعية حول العالم",
        "benefits_title": "لماذا تختار نهجاً متناغماً",
        "b1_title": "ترددات متناسقة ولطيفة",
        "b1_desc": "مصممة بعناية لتعزيز الاسترخاء العميق ومساعدة الجسم على استعادة إيقاعه الطبيعي.",
        "b2_title": "التعافي والراحة الواعية",
        "b2_desc": "دعم مصمم لتهدئة آثار ضغوط الحياة اليومية والإرهاق بكل لطف.",
        "b3_title": "انسجام تام مع حياتك اليومية",
        "b3_desc": "تتواءم بسلاسة مع روتينك، وتوفر لك دعماً هادئاً وموثوقاً في رحلتك.",
        "b4_title": "نهج غير جراحي تماماً",
        "b4_desc": "طريقة آمنة وخالية من أي آثار جانبية، مصممة للعناية بنفسك بأقصى درجات الاحترام.",
        "form_title": "احصل على الدليل الشامل",
        "form_desc": "أدخل بريدك الإلكتروني أدناه لتلقي الدليل التوضيحي بالتفصيل وبالسرعة التي تناسبك.",
        "email_placeholder": "أدخل بريدك الإلكتروني...",
        "button": "أرسل لي الدليل المجاني",
        "success": "شكراً جزيلاً لك. جاري توجيهك إلى صفحة المعلومات...",
        "error": "الرجاء إدخال عنوان بريد إلكتروني صالح.",
        "faq_title": "❓ الأسئلة الشائعة",
        "q1": "س: هل هذا مناسب لمن يستكشف هذا المجال لأول مرة؟",
        "a1": "ج: بالتأكيد. تم إعداد الدليل ليكون واضحاً وشفيفاً ومتاحاً لكل مهتم بالعافية الواعية.",
        "q2": "س: ماذا يحدث بعد إدخال بريدي الإلكتروني؟",
        "a2": "ج: سيتم توجيهك بلطف إلى صفحة العرض الرسمي، دون أي التزام أو إزعاج.",
        "footer": "مبني على أسس الفيزياء الحيوية والرعاية الواعية. مصمم لحياة أكثر وعياً."
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
