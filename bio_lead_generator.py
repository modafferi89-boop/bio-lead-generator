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

# Selettore di lingua principale in alto a destra
col1, col2, col3 = st.columns([2, 2, 1])
with col3:
    lingua = st.selectbox(
        "🌐", 
        ["English", "Italiano", "Español", "Français", "Deutsch", "中文", "日本語", "العربية"], 
        label_visibility="collapsed"
    )

# Dizionario delle traduzioni esteso
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
    },
    "Español": {
        "title": "Reconecta tu cuerpo con su frecuencia óptima",
        "subtitle": "Descubre la nueva frontera del Bio-Hacking y la Regeneración Energética",
        "trust": "🔒 Protocolo Seguro &nbsp;|&nbsp; 🌍 Estándar Internacional &nbsp;|&nbsp; ⚡ Acceso Inmediato",
        "social": "⭐️ Con la confianza de más de 1,400 entusiastas del bio-hacking en todo el mundo",
        "benefits_title": "Beneficios Clave",
        "b1_title": "Tecnología de Frecuencia Armónica",
        "b1_desc": "Aprovecha principios de estimulación avanzada para promover un estado de profunda relajación celular y mental.",
        "b2_title": "Optimización de la Recuperación Día y Noche",
        "b2_desc": "Ayuda a contrarrestar los efectos de la fatiga crónica y el estrés oxidativo causados por los ritmos modernos.",
        "b3_title": "Integración Perfecta en el Bienestar Diario",
        "b3_desc": "Diseñado para un uso sencillo, ofreciendo apoyo constante para tu viaje de salud holística.",
        "b4_title": "Enfoque No Invasivo",
        "b4_desc": "Una solución segura y sin efectos secundarios, ideal para quienes buscan cuidarse de forma natural y vanguardista.",
        "form_title": "Obtén Acceso Inmediato",
        "form_desc": "Introduce tu mejor dirección de correo electrónico para desbloquear acceso inmediato a la guía completa.",
        "email_placeholder": "Introduce tu correo...",
        "button": "DESBLOQUEAR ACCESO INMEDIATO",
        "success": "¡Acceso concedido! Redirigiendo a la presentación...",
        "error": "Por favor, introduce un correo electrónico válido.",
        "faq_title": "❓ Preguntas Frecuentes",
        "q1": "P: ¿Es adecuada esta presentación para principiantes?",
        "a1": "R: Sí, la guía técnica está estructurada para ser comprendida fácilmente por cualquier apasionado del bienestar.",
        "q2": "P: ¿Cómo accedo al material después de introducir mi correo?",
        "a2": "R: Serás redirigido instantáneamente a la página oficial de la presentación técnica.",
        "footer": "Basado en rigurosos principios de biofísica. Diseñado para entusiastas del bienestar global."
    },
    "Français": {
        "title": "Reconnectez votre corps à sa fréquence optimale",
        "subtitle": "Découvrez la nouvelle frontière du Bio-Hacking et de la Régénération Énergétique",
        "trust": "🔒 Protocole Sécurisé &nbsp;|&nbsp; 🌍 Standard International &nbsp;|&nbsp; ⚡ Accès Instantané",
        "social": "⭐️ Approuvé par plus de 1 400 passionnés de bio-hacking dans le monde",
        "benefits_title": "Principaux Avantages",
        "b1_title": "Technologie à Fréquence Harmonique",
        "b1_desc": "Exploite des principes de stimulation avancés pour favoriser un état de relaxation cellulaire et mentale profonde.",
        "b2_title": "Optimisation de la Récupération Jour & Nuit",
        "b2_desc": "Aide à contrer les effets de la fatigue chronique et du stress oxydatif liés aux rythmes de vie modernes.",
        "b3_title": "Intégration Quotidienne Fluide",
        "b3_desc": "Conçu pour une utilisation simple, offrant un soutien constant pour votre parcours de santé holistique.",
        "b4_title": "Approche Non Invasive",
        "b4_desc": "Une solution sûre et sans effets secondaires, idéale pour prendre soin de soi naturellement et efficacement.",
        "form_title": "Obtenez un Accès Instantané",
        "form_desc": "Entrez votre meilleure adresse e-mail ci-dessous pour débloquer un accès immédiat au guide complet.",
        "email_placeholder": "Entrez votre e-mail...",
        "button": "DÉBLOQUER L'ACCÈS MAINTENANT",
        "success": "Accès autorisé ! Redirection vers la présentation...",
        "error": "Veuillez entrer une adresse e-mail valide.",
        "faq_title": "❓ Questions Fréquentes",
        "q1": "Q : Cette présentation convient-elle aux débutants ?",
        "a1": "R : Oui, le guide technique est structuré pour être facilement compris par tous les passionnés de bien-être.",
        "q2": "Q : Comment accéder au matériel après avoir entré mon e-mail ?",
        "a2": "R : Vous serez instantanément redirigé vers la page de présentation technique officielle.",
        "footer": "Fondé sur des principes rigoureux de biophysique. Conçu pour les passionnés de bien-être."
    },
    "Deutsch": {
        "title": "Verbinden Sie Ihren Körper mit seiner optimalen Frequenz",
        "subtitle": "Entdecken Sie die nächste Grenze des Bio-Hackings und der Energieregeneration",
        "trust": "🔒 Sicheres Protokoll &nbsp;|&nbsp; 🌍 Internationaler Standard &nbsp;|&nbsp; ⚡ Sofortiger Zugriff",
        "social": "⭐️ Von über 1.400 Bio-Hacking-Enthusiasten weltweit geschätzt",
        "benefits_title": "Hauptvorteile",
        "b1_title": "Harmonische Frequenztechnologie",
        "b1_desc": "Nutzt fortgeschrittene Stimulationsprinzipien, um einen Zustand tiefer zellulärer und geistiger Entspannung zu fördern.",
        "b2_title": "Tag- & Nacht-Erholungsoptimierung",
        "b2_desc": "Hilft, den Auswirkungen von chronischer Müdigkeit und oxidativem Stress entgegenzuwirken.",
        "b3_title": "Nahtlose Integration in den Alltag",
        "b3_desc": "Für eine einfache Anwendung konzipiert und bietet ständige Unterstützung für Ihre ganzheitliche Gesundheit.",
        "b4_title": "Nicht-invasiver Ansatz",
        "b4_desc": "Eine sichere, nebenwirkungsfreie Lösung, ideal für alle, die sich auf natürliche Weise etwas Gutes tun möchten.",
        "form_title": "Sofortigen Zugriff erhalten",
        "form_desc": "Geben Sie unten Ihre beste E-Mail-Adresse ein, um den sofortigen Zugriff freizuschalten.",
        "email_placeholder": "Geben Sie Ihre E-Mail ein...",
        "button": "SOFORTIGEN ZUGRIFF FREISCHALTEN",
        "success": "Zugriff gewährt! Weiterleitung zur Präsentation...",
        "error": "Bitte geben Sie eine gültige E-Mail-Adresse ein.",
        "faq_title": "❓ Häufig gestellte Fragen",
        "q1": "F: Ist diese Präsentation für Anfänger geeignet?",
        "a1": "A: Ja, der technische Leitfaden ist so aufgebaut, dass er leicht verständlich ist.",
        "q2": "F: Wie erhalte ich nach der E-Mails-Eingabe Zugriff?",
        "a2": "A: Sie werden sofort zur offiziellen technischen Präsentationsseite weitergeleitet.",
        "footer": "Basierend auf strengen biophysikalischen Prinzipien. Für Wellness-Enthusiasten weltweit entwickelt."
    },
    "中文": {
        "title": "让您的身体重新连接最佳频率",
        "subtitle": "探索生物黑客与能量恢复的新前沿",
        "trust": "🔒 安全协议 &nbsp;|&nbsp; 🌍 国际标准 &nbsp;|&nbsp; ⚡ 即时访问",
        "social": "⭐️ 受到全球 1,400 多名生物黑客爱好者的信赖",
        "benefits_title": "核心优势",
        "b1_title": "谐振频率技术",
        "b1_desc": "利用先进的刺激原理，促进细胞和精神深层放松状态。",
        "b2_title": "昼夜恢复优化",
        "b2_desc": "帮助抵御快节奏现代生活带来的慢性疲劳和氧化应激。",
        "b3_title": "无缝融入日常健康",
        "b3_desc": "设计简单易用，为您的整体健康之旅提供持续支持。",
        "b4_title": "非侵入式方法",
        "b4_desc": "安全且无副作用的解决方案，非常适合追求自然与前沿健康的人士。",
        "form_title": "获取即时访问权限",
        "form_desc": "在下方输入您的最佳电子邮箱，即可立即解锁完整指南与技术演示。",
        "email_placeholder": "请输入您的电子邮箱...",
        "button": "立即解锁访问权限",
        "success": "访问授权成功！正在跳转至演示页面...",
        "error": "请输入有效的电子邮箱地址。",
        "faq_title": "❓ 常见问题",
        "q1": "问：本演示适合初学者吗？",
        "a1": "答：是的，技术指南结构清晰，任何对健康和生物黑客感兴趣的人都能轻松理解。",
        "q2": "问：输入邮箱后如何查看资料？",
        "a2": "答：您将被立即重定向到官方技术演示页面。",
        "footer": "基于严谨的生物物理学原理。专为全球健康爱好者设计。"
    },
    "日本語": {
        "title": "体を最適な周波数へと再接続する",
        "subtitle": "バイオハッキングとエネルギー再生の新たなフロンティアを発見",
        "trust": "🔒 セキュアプロトコル &nbsp;|&nbsp; 🌍 国際基準 &nbsp;|&nbsp; ⚡ 即時アクセス",
        "social": "⭐️ 世界中の1,400名を超えるバイオハッキング愛好者から信頼されています",
        "benefits_title": "主なメリット",
        "b1_title": "ハーモニック周波数テクノロジー",
        "b1_desc": "高度な刺激原理を活用し、細胞と精神の深いリラクゼーション状態を促進します。",
        "b2_title": "昼夜の回復最適化",
        "b2_desc": "現代の慌ただしいリズムによる慢性疲労や酸化ストレスの影響に対抗します。",
        "b3_title": "日常のウェルネスへのシームレスな統合",
        "b3_desc": "簡単に使える設計で、ホリスティックな健康への旅を継続的にサポートします。",
        "b4_title": "非侵襲的アプローチ",
        "b4_desc": "自然かつ最先端の方法でケアしたい方に最適な、安全で副作用のないソリューションです。",
        "form_title": "今すぐアクセスを取得",
        "form_desc": "以下にメールアドレスを入力して、完全なガイドと技術プレゼンテーションへの即時アクセスを解除してください。",
        "email_placeholder": "メールアドレスを入力...",
        "button": "今すぐアクセスを解除",
        "success": "アクセスが許可されました！プレゼンテーションへ転送中...",
        "error": "有効なメールアドレスを入力してください。",
        "faq_title": "❓ よくある質問",
        "q1": "Q: このプレゼンテーションは初心者でも理解できますか？",
        "a1": "A: はい、健康やバイオハッキングに関心のある方ならどなたでも簡単に理解できるように構成されています。",
        "q2": "Q: メール入力後、どのように資料にアクセスしますか？",
        "a2": "A: 公式の技術プレゼンテーションページに即座にリダイレクトされます。",
        "footer": "厳格な生物物理学の原理に基づいています。世界中のウェルネス愛好者のために設計されています。"
    },
    "العربية": {
        "title": "أعد توصيل جسمك بتردده الأمثل",
        "subtitle": "اكتشف الحدود الجديدة للقرصنة الحيوية وتجديد الطاقة",
        "trust": "🔒 بروتوكول آمن &nbsp;|&nbsp; 🌍 معيار دولي &nbsp;|&nbsp; ⚡ وصول فوري",
        "social": "⭐️ موثوق من قبل أكثر من 1,400 من عشاق القرصنة الحيوية حول العالم",
        "benefits_title": "المزايا الرئيسية",
        "b1_title": "تكنولوجيا التردد المتناسق",
        "b1_desc": "تستفيد من مبادئ التحفيز المتقدمة تعزيزا لحالة الاسترخاء الخلوي والعقلي العميق.",
        "b2_title": "تحسين الاسترداد ليلاً ونهاراً",
        "b2_desc": "يساعد في مواجهة آثار التعب المزمن والإجهاد التأكسدي الناتج عن إيقاع الحياة الحديثة السريع.",
        "b3_title": "التكامل السلس مع العافية اليومية",
        "b3_desc": "مصمم للاستخدام السهل، ويوفر دعماً مستمراً لرحلة صحتك الشاملة.",
        "b4_title": "نهج غير جراحي",
        "b4_desc": "حل آمن وخالٍ من الآثار الجانبية، مثالي لمن يرغبون في العناية بأنفسهم بطريقة طبيعية ومتطورة.",
        "form_title": "احصل على الوصول الفوري",
        "form_desc": "أدخل بريدك الإلكتروني أدناه لفتح الوصول الفوري إلى الدليل الكامل والعرض التقني.",
        "email_placeholder": "أدخل بريدك الإلكتروني...",
        "button": "فتح الوصول الفوري الآن",
        "success": "تم منح الوصول! جاري إعادة التوجيه إلى العرض التقديمي...",
        "error": "الرجاء إدخال عنوان بريد إلكتروني صالح.",
        "faq_title": "❓ الأسئلة الشائعة",
        "q1": "س: هل هذا العرض التقديمي مناسب للمبتدئين؟",
        "a1": "ج: نعم، الدليل التقني مصمم بحيث يمكن فهمه بسهولة من قبل أي شخص مهتم بالعافية.",
        "q2": "س: كيف يمكنني الوصول إلى المواد بعد إدخال بريدي الإلكتروني؟",
        "a2": "ج: سيتم توجيهك فوراً إلى صفحة العرض التقني الرسمية.",
        "footer": "مبني على مبادئ الفيزياء الحيوية الصارمة. مصمم لعشاق العافية العالمية."
    }
}

# Stile CSS ottimizzato (gestisce correttamente anche l'allineamento per l'arabo se necessario)
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
