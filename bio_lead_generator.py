from datetime import datetime
import os
import pandas as pd
import streamlit as st

# Configurazione della pagina
st.set_page_config(
    page_title="Bio-Hacking & Energy Regeneration", page_icon="⚡", layout="centered"
)

# ID Google Analytics
GOOGLE_ANALYTICS_ID = "G-GHSTG893H9"

# Iniezione corretta del Tag Google Analytics
if GOOGLE_ANALYTICS_ID and GOOGLE_ANALYTICS_ID != "G-XXXXXXXXXX":
  st.markdown(
      f"""
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id={GOOGLE_ANALYTICS_ID}"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){{dataLayer.push(arguments);}}
          gtag('js', new Date());
          gtag('config', '{GOOGLE_ANALYTICS_ID}');
        </script>
    """,
      unsafe_allow_html=True,
  )

# Inizializzazione dello stato della sessione per la vetrina
if "lead_registrato" not in st.session_state:
  st.session_state.lead_registrato = False

# Selettore di lingua principale in alto a destra
col1, col2, col3 = st.columns([2, 2, 1])
with col3:
  lingua = st.selectbox(
      "🌐",
      [
          "English",
          "Italiano",
          "Español",
          "Français",
          "Deutsch",
          "中文",
          "日本語",
          "العربية",
      ],
      label_visibility="collapsed",
  )

# Dizionario delle traduzioni
t = {
    "English": {
        "title": "Restore Balance and Harmony to Your Natural Energy",
        "subtitle": (
            "A gentle, science-backed approach to modern well-being and inner"
            " vitality"
        ),
        "trust": (
            "🔒 Safe & Transparent &nbsp;|&nbsp; 🌍 Mindful Standard"
            " &nbsp;|&nbsp; ⚡ Respectful Approach"
        ),
        "social": (
            "⭐️ Welcomed with trust by individuals seeking conscious wellness"
            " worldwide"
        ),
        "benefits_title": "Why Choose a Harmonious Approach",
        "b1_title": "Gentle Harmonic Frequency",
        "b1_desc": (
            "Carefully designed to support deep relaxation and help restore your"
            " natural inner rhythm without disruption."
        ),
        "b2_title": "Mindful Recovery & Rest",
        "b2_desc": (
            "Thoughtfully crafted to gently soothe the effects of daily stress"
            " and mental fatigue."
        ),
        "b3_title": "Seamless & Natural Integration",
        "b3_desc": (
            "Fits effortlessly into your lifestyle, offering quiet, reliable"
            " support for your personal wellness journey."
        ),
        "b4_title": "Completely Non-Invasive",
        "b4_desc": (
            "A calm, safe, and completely side-effect-free path designed to"
            " care for your body with absolute respect."
        ),
        "form_title": "Receive the Complete Guide",
        "form_desc": (
            "Enter your email address below to unlock instant access to the"
            " recommended resources showcase."
        ),
        "email_placeholder": "Enter your email address...",
        "button": "UNLOCK THE RESOURCE SHOWCASE",
        "success": (
            "Thank you! Your email has been registered. Here is your showcase:"
        ),
        "error": "Please enter a valid email address.",
        "showcase_title": "🌟 Your Exclusive Resource Showcase",
        "showcase_subtitle": (
            "Explore our carefully selected tools and solutions designed to"
            " support your well-being journey."
        ),
        "btn_access": "Access Resource",
        "faq_title": "❓ Frequently Asked Questions",
        "q1": "Q: Is this suitable for everyone?",
        "a1": (
            "A: Yes, the guide has been created with care to be clear,"
            " transparent, and accessible to anyone approaching conscious"
            " wellness."
        ),
        "q2": "Q: What happens after I enter my email?",
        "a2": (
            "A: You will instantly unlock the showcase page containing all"
            " recommended solutions."
        ),
        "footer": (
            "Rooted in rigorous biophysical principles and mindful care."
            " Designed for conscious living."
        ),
    },
    "Italiano": {
        "title": "Ritrova l'Armonia e l'Equilibrio della tua Energia Naturale",
        "subtitle": (
            "Un approccio gentile e consapevole al benessere e alla vitalità di"
            " tutti i giorni"
        ),
        "trust": (
            "🔒 Sicuro e Trasparente &nbsp;|&nbsp; 🌍 Standard Etico &nbsp;|&nbsp;"
            " ⚡ Ascolto e Rispetto"
        ),
        "social": (
            "⭐️ Accolto con fiducia da persone attente al proprio benessere"
            " consapevole in tutto il mondo"
        ),
        "benefits_title": "Perché scegliere un percorso armonioso",
        "b1_title": "Frequenze Armoniche Delicate",
        "b1_desc": (
            "Studiate con cura per favorire un profondo rilassamento e"
            " accompagnare il corpo verso il suo ritmo naturale."
        ),
        "b2_title": "Rigenerazione e Riposo Consapevole",
        "b2_desc": (
            "Un supporto pensato per alleggerire con delicatezza gli effetti"
            " dello stress quotidiano e della stanchezza mentale."
        ),
        "b3_title": "In Armonia con la tua Quotidianità",
        "b3_desc": (
            "Si integra in modo fluido e naturale nella tua routine, offrendo un"
            " sostegno costante e silenzioso."
        ),
        "b4_title": "Approccio Totalmente Non Invasivo",
        "b4_desc": (
            "Una via sicura, priva di effetti collaterali e concepita per"
            " prendersi cura di sé con il massimo rispetto."
        ),
        "form_title": "Ricevi la Guida Approfondita",
        "form_desc": (
            "Inserisci il tuo indirizzo email qui sotto per sbloccare"
            " immediatamente la vetrina delle risorse consigliate."
        ),
        "email_placeholder": "Inserisci il tuo indirizzo email...",
        "button": "SBLOCA LA VETRINA RISORSE",
        "success": (
            "Grazie di cuore! Registrazione completata. Ecco la tua vetrina"
            " dedicata:"
        ),
        "error": "Inserisci un indirizzo email valido per favore.",
        "showcase_title": "🌟 La tua Vetrina Risorse Esclusive",
        "showcase_subtitle": (
            "Esplora le soluzioni selezionate con cura per accompagnarti nel"
            " tuo percorso di benessere."
        ),
        "btn_access": "Accedi alla Risorsa",
        "faq_title": "❓ Domande Frequenti",
        "q1": (
            "D: È un percorso adatto a chi si avvicina per la prima volta a"
            " questi temi?"
        ),
        "a1": (
            "R: Assolutamente sì. La guida è pensata per essere chiara,"
            " trasparente e accessibile a chiunque desideri prendersi cura di"
            " sé."
        ),
        "q2": "D: Cosa succede dopo aver inserito la mia email?",
        "a2": (
            "R: Avrai accesso immediato alla pagina della vetrina con tutti i"
            " prodotti e link consigliati."
        ),
        "footer": (
            "Fondato su rigorosi principi di biofisica e rispetto della"
            " persona. Dedicato a chi vive il benessere in modo consapevole."
        ),
    },
    "Español": {
        "title": "Restaura el Equilibrio y la Armonía de tu Energía Natural",
        "subtitle": (
            "Un enfoque consciente y respetuoso hacia el bienestar y la"
            " vitalidad"
        ),
        "trust": (
            "🔒 Seguro y Transparente &nbsp;|&nbsp; 🌍 Enfoque Ético &nbsp;|&nbsp;"
            " ⚡ Respeto Absoluto"
        ),
        "social": (
            "⭐️ Acogido con confianza por personas que buscan un bienestar"
            " consciente en todo el mundo"
        ),
        "benefits_title": "Por qué elegir un enfoque armonioso",
        "b1_title": "Frecuencias Armónicas Suaves",
        "b1_desc": (
            "Diseñadas cuidadosamente para fomentar una relajación profunda y"
            " acompañar tu ritmo natural."
        ),
        "b2_title": "Recuperación y Descanso Consciente",
        "b2_desc": (
            "Un apoyo pensado para calmar con delicadeza los efectos del estrés"
            " diario."
        ),
        "b3_title": "Integración Natural en tu Día a Día",
        "b3_desc": (
            "Se adapta de forma fluida a tu estilo de vida, ofreciendo un"
            " respaldo constante."
        ),
        "b4_title": "Enfoque Totalmente No Invasivo",
        "b4_desc": (
            "Un camino seguro y libre de efectos secundarios, creado para"
            " cuidar de ti con respeto."
        ),
        "form_title": "Recibe la Guía Completa",
        "form_desc": (
            "Introduce tu correo electrónico para desbloquear la selección de"
            " recursos recomendados."
        ),
        "email_placeholder": "Introduce tu correo electrónico...",
        "button": "DESBLOQUEAR LA VITRINA",
        "success": "¡Muchas gracias! Aquí tienes tu escaparate de recursos:",
        "error": "Por favor, introduce un correo electrónico válido.",
        "showcase_title": "🌟 Tu Vitrina de Recursos Exclusivos",
        "showcase_subtitle": (
            "Explora las soluciones seleccionadas para tu bienestar."
        ),
        "btn_access": "Acceder al Recurso",
        "faq_title": "❓ Preguntas Frecuentes",
        "q1": "P: ¿Es adecuado para principiantes?",
        "a1": (
            "R: Sí, la guía es transparente y accesible para cualquier persona"
            " interesada en el bienestar."
        ),
        "q2": "P: ¿Qué ocurre después de introducir mi correo?",
        "a2": "R: Desbloquearás de inmediato el acceso a la vitrina de productos.",
        "footer": "Basado en principios de biofísica y cuidado consciente.",
    },
    "Français": {
        "title": (
            "Retrouvez l'Harmonie et l'Équilibre de votre Énergie Naturelle"
        ),
        "subtitle": (
            "Une approche douce, respectueuse et consciente du bien-être au"
            " quotidien"
        ),
        "trust": (
            "🔒 Sûr et Transparent &nbsp;|&nbsp; 🌍 Standard Éthique &nbsp;|&nbsp;"
            " ⚡ Écoute et Respect"
        ),
        "social": (
            "⭐️ Accueilli avec confiance par des personnes en quête de"
            " bien-être conscient"
        ),
        "benefits_title": "Pourquoi choisir une démarche harmonieuse",
        "b1_title": "Fréquences Harmoniques Douces",
        "b1_desc": (
            "Conçues avec soin pour favoriser un apaisement profond et"
            " respecter votre rythme."
        ),
        "b2_title": "Récupération et Repos Serein",
        "b2_desc": (
            "Un soutien pensé pour adoucir les effets du stress quotidien et de"
            " la fatigue."
        ),
        "b3_title": "Harmonie avec votre Quotidien",
        "b3_desc": (
            "S'intègre naturellement dans votre vie pour un accompagnement"
            " discret et constant."
        ),
        "b4_title": "Approche Totalement Non Invasive",
        "b4_desc": (
            "Une voie sûre et sans effets secondaires, idéale pour prendre"
            " soin de soi en toute confiance."
        ),
        "form_title": "Recevez le Guide Complet",
        "form_desc": (
            "Indiquez votre adresse e-mail pour débloquer l'accès à la vitrine"
            " des ressources recommandées."
        ),
        "email_placeholder": "Votre adresse e-mail...",
        "button": "DÉBLOQUER LA VITRINE",
        "success": "Merci beaucoup ! Voici votre vitrine de ressources :",
        "error": "Veuillez entrer une adresse e-mail valide.",
        "showcase_title": "🌟 Votre Vitrine de Ressources Exclusives",
        "showcase_subtitle": (
            "Découvrez nos solutions sélectionnées pour votre bien-être."
        ),
        "btn_access": "Accéder à la ressource",
        "faq_title": "❓ Questions Fréquentes",
        "q1": "Q : Est-ce adapté à ceux qui débutent ?",
        "a1": (
            "R : Tout à fait, le guide est conçu pour être clair, transparent"
            " et accessible à tous."
        ),
        "q2": "Q : Que se passe-t-il après avoir entré mon e-mail ?",
        "a2": "R : Vous accédez instantanément à la vitrine de produits.",
        "footer": "Fondé sur des principes rigoureux et un soin attentif.",
    },
    "Deutsch": {
        "title": "Finden Sie die Harmonie und Balance Ihrer natürlichen Energie",
        "subtitle": (
            "Ein achtsamer und sanfter Weg zu mehr Wohlbefinden und innerer"
            " Vitalität"
        ),
        "trust": (
            "🔒 Sicher & Transparent &nbsp;|&nbsp; 🌍 Ethischer Standard"
            " &nbsp;|&nbsp; ⚡ Respektvoller Ansatz"
        ),
        "social": (
            "⭐️ Vertrauensvoll geschätzt von Menschen, die bewusste"
            " Lebensqualität suchen"
        ),
        "benefits_title": "Warum ein harmonischer Weg der richtige ist",
        "b1_title": "Sanfte Harmonische Frequenzen",
        "b1_desc": (
            "Sorgfältig entwickelt, um tiefe Entspannung zu fördern und den"
            " natürlichen Rhythmus zu unterstützen."
        ),
        "b2_title": "Achtsame Erholung & Ruhe",
        "b2_desc": (
            "Ein durchdachter Begleiter, um die Spuren des Alltagsstress sanft"
            " auszugleichen."
        ),
        "b3_title": "Harmonisch im Alltag integriert",
        "b3_desc": (
            "Fügt sich unaufdringlich in Ihr Leben ein und bietet verlässliche"
            " Unterstützung."
        ),
        "b4_title": "Vollständig Nicht-Invasiv",
        "b4_desc": (
            "Ein sicherer, nebenwirkungsfreier Ansatz für einen respektvollen"
            " Umgang mit dem eigenen Körper."
        ),
        "form_title": "Den ausführlichen Leitfaden anfordern",
        "form_desc": (
            "Geben Sie Ihre E-Mail ein, um die exklusive Produktvitrine"
            " freizuschalten."
        ),
        "email_placeholder": "Ihre E-Mail-Adresse...",
        "button": "VITRINE FREISCHALTEN",
        "success": (
            "Vielen Dank! Ihre E-Mail wurde gespeichert. Hier ist Ihre Vitrine:"
        ),
        "error": "Bitte geben Sie eine gültige E-Mail-Adresse ein.",
        "showcase_title": "🌟 Ihre exklusive Ressourcen-Vitrine",
        "showcase_subtitle": (
            "Entdecken Sie sorgfältig ausgewählte Lösungen für Ihr"
            " Wohlbefinden."
        ),
        "btn_access": "Zur Ressource",
        "faq_title": "❓ Häufig gestellte Fragen",
        "q1": "F: Ist dieser Ansatz auch für Einsteiger geeignet?",
        "a1": "A: Ja, transparent und für jeden verständlich.",
        "q2": "F: Was geschieht nach der E-Mails-Eingabe?",
        "a2": "A: Sie erhalten sofortigen Zugriff auf die Produktvitrine.",
        "footer": "Verankert in biophysikalischen Prinzipien und bewusster Fürsorge.",
    },
    "中文": {
        "title": "找回您自然能量的和谐与平衡",
        "subtitle": "一种温和、科学且注重关怀的现代健康与活力之旅",
        "trust": "🔒 安全透明 &nbsp;|&nbsp; 意识标准 &nbsp;|&nbsp; ⚡ 尊重关怀",
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
        "form_desc": "在下方输入您的电子邮箱以立即解锁推荐资源展示窗口。",
        "email_placeholder": "请输入您的电子邮箱...",
        "button": "立即解锁资源展示",
        "success": "非常感谢！您的邮箱已记录，以下是为您准备的资源展示：",
        "error": "请输入有效的电子邮箱地址。",
        "showcase_title": "🌟 您的专属资源展示",
        "showcase_subtitle": "探索专为您的健康之旅精心挑选的工具与解决方案。",
        "btn_access": "访问资源",
        "faq_title": "❓ 常见问题",
        "q1": "问：这适合初次接触的人吗？",
        "a1": "答：是的，内容清晰透明。",
        "q2": "问：输入邮箱后会发生什么？",
        "a2": "答：您将立即解锁包含所有推荐方案的展示页面。",
        "footer": "根植于严谨的生物物理学与用心关怀。",
    },
    "日本語": {
        "title": "自然なエネルギーの調和とバランスを取り戻す",
        "subtitle": (
            "現代の健やかさと内なる活力に向けた、優しく寄り添うアプローチ"
        ),
        "trust": (
            "🔒 安全と透明性 &nbsp;|&nbsp; 倫理的基準 &nbsp;|&nbsp; ⚡"
            " 丁寧な配慮"
        ),
        "social": (
            "⭐️"
            " 世界中で意識的なウェルネスを求める方々から温かい信頼を寄せられています"
        ),
        "benefits_title": "調和をもたらす理由",
        "b1_title": "穏やかなハーモニック周波数",
        "b1_desc": (
            "深いリラックスを促し、本来の健やかなリズムへ優しく導くよう設計されています。"
        ),
        "b2_title": "心休まる休息と回復",
        "b2_desc": (
            "日々の緊張や心身の疲れをやわらげるための細やかなサポートです。"
        ),
        "b3_title": "日々の暮らしに自然と寄り添う",
        "b3_desc": (
            "生活のリズムを崩さず、静かで確かな支えを日常にもたらします。"
        ),
        "b4_title": "完全な非侵襲的アプローチ",
        "b4_desc": (
            "身体への負担や副作用がなく、大切にご自身をケアするための安全な方法です。"
        ),
        "form_title": "詳細ガイドを受け取る",
        "form_desc": "メールアドレスを入力して、おすすめリソースの特設ページをアンロック。",
        "email_placeholder": "メールアドレスを入力...",
        "button": "リソース特設ページを見る",
        "success": (
            "ありがとうございます！登録が完了しました。おすすめの特設ページはこちらです："
        ),
        "error": "有効なメールアドレスを入力してください。",
        "showcase_title": "🌟 おすすめリソース・特設セレクション",
        "showcase_subtitle": (
            "あなたのウェルネスの旅を支える厳選されたツールをご覧ください。"
        ),
        "btn_access": "リソースにアクセス",
        "faq_title": "❓ よくある質問",
        "q1": "Q: 初めての方でも安心してご覧いただけますか？",
        "a1": "A: はい。分かりやすく透明性のある内容です。",
        "q2": "Q: メール入力後はどうなりますか？",
        "a2": "A: おすすめリソースの特設ページがすぐに表示されます。",
        "footer": "生物物理学の原理と細やかな思いやりを基盤としています。",
    },
    "العربية": {
        "title": "استعد الانسجام والتوازن لطاقتك الطبيعية",
        "subtitle": "نهج لطيف وواعي نحو العافية الحديثة والحيوية الداخلية",
        "trust": "🔒 آمن وشفاف &nbsp;|&nbsp; 🌍 معيار أخلاقي &nbsp;|&nbsp; ⚡ احترام واهتمام",
        "social": "⭐️ محل ثقة الأفراد الباحثين عن العافية الواعية حول العالم",
        "benefits_title": "لماذا تختار نهجاً متناغماً",
        "b1_title": "ترددات متناسقة ولطيفة",
        "b1_desc": (
            "مصممة بعناية لتعزيز الاسترخاء العميق ومساعدة الجسم على استعادة إيقاعه"
            " الطبيعي."
        ),
        "b2_title": "التعافي والراحة الواعية",
        "b2_desc": "دعم مصمم لتهدئة آثار ضغوط الحياة اليومية والإرهاق بكل لطف.",
        "b3_title": "انسجام تام مع حياتك اليومية",
        "b3_desc": (
            "تتواءم بسلاسة مع روتينك، وتوفر لك دعماً هادئاً وموثوقاً في رحلتك."
        ),
        "b4_title": "نهج غير جراحي تماماً",
        "b4_desc": (
            "طريقة آمنة وخالية من أي آثار جانبية، مصممة للعناية بنفسك بأقصى درجات"
            " الاحترام."
        ),
        "form_title": "احصل على الدليل الشامل",
        "form_desc": "أدخل بريدك الإلكتروني أدناه لفتح واجهة عرض الموارد الموصى بها فوراً.",
        "email_placeholder": "أدخل بريدك الإلكتروني...",
        "button": "فتح واجهة الموارد",
        "success": "شكراً لك! تم تسجيل بريدك بنجاح. إليك نافذة الموارد المخصصة:",
        "error": "الرجاء إدخال عنوان بريد إلكتروني صالح.",
        "showcase_title": "🌟 نافذة الموارد الحصرية الخاصة بك",
        "showcase_subtitle": (
            "استكشف الحلول المختارة بعناية لدعم رحلتك نحو العافية."
        ),
        "btn_access": "الوصول إلى المورد",
        "faq_title": "❓ الأسئلة الشائعة",
        "q1": "س: هل هذا مناسب لمن يستكشف هذا المجال لأول مرة؟",
        "a1": "ج: بالتأكيد، الدليل واضح وشفاف.",
        "q2": "س: ماذا يحدث بعد إدخال بريدي الإلكتروني؟",
        "a2": "ج: سيتم فتح صفحة العرض التي تضم كافة الموارد والروابط الموصى بها.",
        "footer": "مبني على أسس الفيزياء الحيوية والرعاية الواعية.",
    },
}

# Stile CSS ottimizzato
st.markdown(
    """
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
    .product-card {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 10px;
        border: 1px solid #cbd5e1;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.04);
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
""",
    unsafe_allow_html=True,
)


def save_lead(email):
  file_path = "leads.csv"
  new_data = pd.DataFrame([[email, datetime.now()]], columns=["Email", "Timestamp"])
  if os.path.exists(file_path):
    new_data.to_csv(file_path, mode="a", header=False, index=False)
  else:
    new_data.to_csv(file_path, mode="w", header=True, index=False)


# ==========================================
# GESTIONE SCHERMATA: SE IL LEAD NON SI È ISCRITTO
# ==========================================
if not st.session_state.lead_registrato:
  # Intestazione Principale
  st.markdown(
      f"<h1 style='text-align: center; color: #0284c7;'>{t[lingua]['title']}</h1>",
      unsafe_allow_html=True,
  )
  st.markdown(
      f"<p style='text-align: center; font-style: italic; color: #475569;"
      f" font-size: 1.15rem;'>{t[lingua]['subtitle']}</p>",
      unsafe_allow_html=True,
  )

  st.write("---")

  # Badge di fiducia e Social Proof
  st.markdown(
      f"<div class='trust-badge'>{t[lingua]['trust']}</div>",
      unsafe_allow_html=True,
  )
  st.markdown(
      f"<div class='social-proof'>{t[lingua]['social']}</div>",
      unsafe_allow_html=True,
  )

  # Sezione Benefici
  st.markdown(f"### {t[lingua]['benefits_title']}")
  st.markdown(
      f"""
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
    """,
      unsafe_allow_html=True,
  )

  st.write("---")

  # Sezione Modulo di Raccolta Contatti (Lead Generation)
  st.markdown(f"### {t[lingua]['form_title']}")
  st.markdown(t[lingua]["form_desc"])

  with st.form("lead_form"):
    user_email = st.text_input(
        "Email Address", placeholder=t[lingua]["email_placeholder"]
    )
    submit_button = st.form_submit_button(label=t[lingua]["button"])

    if submit_button:
      if user_email and "@" in user_email and "." in user_email:
        save_lead(user_email)
        st.session_state.lead_registrato = True
        st.rerun()
      else:
        st.error(t[lingua]["error"])

  st.write("---")

  # Sezione FAQ a scomparsa
  with st.expander(t[lingua]["faq_title"]):
    st.write(f"**{t[lingua]['q1']}**")
    st.write(t[lingua]["a1"])
    st.write(f"**{t[lingua]['q2']}**")
    st.write(t[lingua]["a2"])

# ==========================================
# GESTIONE SCHERMATA: VETRINA PRODOTTI (DOPO L'ISCRIZIONE)
# ==========================================
else:
  st.success(t[lingua]["success"])
  st.markdown(
      f"<h2 style='color: #0284c7; text-align: center; margin-top: 10px;'>"
      f"{t[lingua]['showcase_title']}</h2>",
      unsafe_allow_html=True,
  )
  st.markdown(
      f"<p style='text-align: center; color: #475569; font-size: 1.1rem;'>"
      f"{t[lingua]['showcase_subtitle']}</p>",
      unsafe_allow_html=True,
  )

  st.write("---")

  # --- CONFIGURAZIONE DELLA TUA VETRINA PRODOTTI (LINK SPECIFICI) ---
  prodotti_vetrina = [
      {
          "titolo": "⚡ Sistema Principale di Armonizzazione Energetica",
          "descrizione": (
              "La guida avanzata e il protocollo completo per il ripristino"
              " del benessere quotidiano attraverso frequenze mirate."
          ),
          "url": "https://www.checkout-ds24.com/redir/649413/vincenzomodafferi/",
      },
      {
          "titolo": "🌿 Kit Integrativo per il Riposo Profondo",
          "descrizione": (
              "Soluzioni e frequenze acustiche studiate specificamente per"
              " favorire un sonno rigenerante e ridurre l'affaticamento"
              " mentale."
          ),
          "url": "https://www.digistore24.com/redir/58827/vincenzomodafferi/",
      },
      {
          "titolo": "💧 Guida alla Biofisica della Vitalità Quotidiana",
          "descrizione": (
              "Un manuale pratico per comprendere l'importanza dell'idratazione"
              " e dei campi energetici naturali."
          ),
          "url": "https://pilatesandfriends.com/abo#aff=vincenzomodafferi",
      },
      {
          "titolo": "🧘‍♀️ Percorso Avanzato di Benessere e Mobilità",
          "descrizione": (
              "Un programma completo dedicato alla cura del corpo e"
              " all'equilibrio fisico per la tua routine quotidiana."
          ),
          "url": "https://www.digistore24.com/redir/90385/vincenzomodafferi/",
      },
      {
          "titolo": "🌱 Edizione Speciale Riattivazione e Vitalità",
          "descrizione": (
              "Risorse mirate e contenuti approfonditi per sostenere l'energia"
              " e il benessere generale."
          ),
          "url": (
              "https://andreas-goldemann.mykajabi.com/magen-darm-edition-e#aff=vincenzomodafferi"
          ),
      },
  ]

  # Visualizzazione dinamica dei prodotti della vetrina con i rispettivi link unici
  for prod in prodotti_vetrina:
    st.markdown(
        f"""
        <div class="product-card">
            <h3 style="color: #0284c7; margin-top: 0;">{prod['titolo']}</h3>
            <p style="color: #334155; font-size: 1.05rem; line-height: 1.5;">{prod['descrizione']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.link_button(
        f"🔗 {t[lingua]['btn_access']} — {prod['titolo']}",
        prod["url"],
        use_container_width=True,
    )
    st.write("")  # Spaziatura

  st.write("---")
  if st.button("🔄 Torna alla Home / Inserisci un'altra email"):
    st.session_state.lead_registrato = False
    st.rerun()

# --- PANNELLO ADMIN / DASHBOARD ANALITICA INTEGRATA ---
st.write("---")
with st.expander("🔐 Area Riservata / Admin Dashboard"):
  st.subheader("📊 Analisi e Monitoraggio Lead in Tempo Reale")

  admin_password = st.text_input(
      "Inserisci la password di accesso:", type="password", key="admin_pwd"
  )

  PASSWORD_SEGRETA = "vincenzo_admin_2026"

  if admin_password == PASSWORD_SEGRETA:
    st.success("Accesso effettuato con successo!")

    file_path = "leads.csv"
    if os.path.exists(file_path):
      try:
        df_leads = pd.read_csv(file_path)

        if not df_leads.empty and "Timestamp" in df_leads.columns:
          df_leads["Timestamp"] = pd.to_datetime(df_leads["Timestamp"])

          col_m1, col_m2, col_m3 = st.columns(3)
          with col_m1:
            st.metric("Totale Lead", len(df_leads))
          with col_m2:
            ultimo_contatto = (
                df_leads["Timestamp"].max().strftime("%d/%m/%Y %H:%M")
            )
            st.metric("Ultimo Contatto", ultimo_contatto)
          with col_m3:
            giorni_attivo = (
                df_leads["Timestamp"].max() - df_leads["Timestamp"].min()
            ).days + 1
            st.metric("Giorni di Attività", giorni_attivo)

          st.write("---")

          st.markdown("#### 📈 Trend Iscrizioni Giornaliere")
          df_leads["Data"] = df_leads["Timestamp"].dt.date
          trend_giornaliero = (
              df_leads.groupby("Data").size().reset_index(name="Iscrizioni")
          )
          st.bar_chart(trend_giornaliero.set_index("Data"))

          st.markdown("#### 📋 Lista Completa Contatti")

          csv_data = df_leads.to_csv(index=False).encode("utf-8")
          st.download_button(
              label="📥 Scarica Database Lead (CSV)",
              data=csv_data,
              file_name="leads_esportati.csv",
              mime="text/csv",
          )

          st.dataframe(
              df_leads.sort_values(by="Timestamp", ascending=False),
              use_container_width=True,
          )

        else:
          st.warning(
              "Il file 'leads.csv' è vuoto o non formattato correttamente."
          )
      except Exception as e:
        st.error(f"Errore durante la lettura del file dei lead: {e}")
    else:
      st.info(
          "Nessun lead registrato finora. Il file 'leads.csv' verrà creato"
          " automaticamente alla prima iscrizione."
      )
  elif admin_password != "":
    st.error("Password errata. Riprova.")

st.markdown(
    f"<p style='text-align: center; font-size: 0.8rem; color: #64748b;"
    f" margin-top: 25px;'>{t[lingua]['footer']}</p>",
    unsafe_allow_html=True,
)
