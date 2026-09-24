import streamlit as st

# ==========================================
# CONFIGURACIÓN DE PÁGINA
# ==========================================
st.set_page_config(
    page_title="Sebastián Botero | Portafolio IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# ESTILOS CSS UX/UI (AZUL COBALTO & CARDS)
# ==========================================
st.markdown("""
<style>
    /* Estilos globales */
    .stApp {
        background-color: #F8FAFC;
    }
    
    /* Estilo para los contenedores/cards de Streamlit */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 14px !important;
        padding: 1.25rem !important;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03) !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease !important;
    }
    
    /* Efecto hover suave en las cards */
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-4px) !important;
        box-shadow: 0 12px 20px rgba(15, 23, 42, 0.08) !important;
        border-color: #CBD5E1 !important;
    }

    /* Botón personalizado en Azul Cobalto */
    .stLinkButton > a {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%) !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 0.6rem 1.2rem !important;
        box-shadow: 0 4px 10px rgba(37, 99, 235, 0.25) !important;
        transition: all 0.2s ease !important;
        text-align: center !important;
        display: block !important;
        width: 100% !important;
    }

    .stLinkButton > a:hover {
        background: linear-gradient(135deg, #1D4ED8 0%, #1E40AF 100%) !important;
        box-shadow: 0 6px 14px rgba(37, 99, 235, 0.35) !important;
        transform: translateY(-1px) !important;
        color: #FFFFFF !important;
    }

    /* Tag/Badge de número de app */
    .app-badge {
        display: inline-block;
        background-color: #EFF6FF;
        color: #1D4ED8;
        font-weight: 700;
        font-size: 0.8rem;
        padding: 0.2rem 0.6rem;
        border-radius: 6px;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# BARRA LATERAL
# ==========================================
with st.sidebar:
    st.markdown("## 👨‍💻 Sebastián Botero Z.")
    st.markdown("---")
    st.write(
        "Bienvenido a mi portafolio interactivo de prototipos de IA. "
        "Explora soluciones avanzadas de visión por computador, procesamiento de lenguaje natural y síntesis de voz."
    )
    st.markdown("---")
    st.caption("EAFIT | Interfaces Multimodales & Producto")

# ==========================================
# ENCABEZADO PRINCIPAL
# ==========================================
st.title("Aplicaciones de Inteligencia Artificial 🤖")
st.caption("Portafolio interactivo de herramientas web y modelos multimodales.")

st.markdown("---")

# ==========================================
# DATOS DE APPS (ORDEN EXACTO)
# ==========================================
apps = [
    {
        "num": "01",
        "title": "Mi Primera App IA",
        "icon": "🚀",
        "desc": "Primer desarrollo exploratorio e interfaz básica de interacción multimodal.",
        "url": "https://miprimeraappsebas.streamlit.app/"
    },
    {
        "num": "02",
        "title": "Convertir Texto a Audio",
        "icon": "🎧",
        "desc": "Generación de voz sintética de alta calidad a partir de entradas de texto.",
        "url": "https://interfacesmultimodalessebas.streamlit.app/"
    },
    {
        "num": "03",
        "title": "Traductor Multimodal",
        "icon": "🌐",
        "desc": "Herramienta inteligente de traducción para múltiples idiomas con voz y texto.",
        "url": "https://traductorsebastianboteroz.streamlit.app/"
    },
    {
        "num": "04",
        "title": "Digitalización OCR",
        "icon": "📄",
        "desc": "Reconocimiento óptico de caracteres para extraer texto desde imágenes físicas.",
        "url": "https://ocr-sebastianboteroz.streamlit.app/"
    },
    {
        "num": "05",
        "title": "OCR con Audio",
        "icon": "📢",
        "desc": "Digitaliza textos impresos desde imágenes y los reproduce en voz hablada.",
        "url": "https://ocr-audiosebastianboteroz.streamlit.app/"
    },
    {
        "num": "06",
        "title": "WordCloud Studio",
        "icon": "📊",
        "desc": "Generación de nubes de palabras interactivas para análisis de frecuencia textual.",
        "url": "https://wordcloudsebastianboterozz.streamlit.app/"
    },
    {
        "num": "07",
        "title": "Análisis de Sentimiento",
        "icon": "🎭",
        "desc": "Evaluación de polaridad emocional y clasificación de opiniones en español.",
        "url": "https://sentimentalsebastianboteroz.streamlit.app/"
    },
    {
        "num": "08",
        "title": "TF-IDF en Español",
        "icon": "🔤",
        "desc": "Modelado de relevancia semántica de términos y frecuencia inversa en corpus de texto.",
        "url": "https://tdfesp-sebastianboterozz.streamlit.app/"
    },
    {
        "num": "09",
        "title": "Detección de Objetos YOLOv5",
        "icon": "🎯",
        "desc": "Detección, delimitación y etiquetado de objetos en imágenes mediante YOLOv5.",
        "url": "https://yolov5sebastianboteroz.streamlit.app/"
    },
    {
        "num": "10",
        "title": "Teachable Machine",
        "icon": "🧠",
        "desc": "Clasificación de imágenes utilizando modelos entrenados en Teachable Machine.",
        "url": "https://teachablemachinesebastianboteroz.streamlit.app/"
    }
]

# ==========================================
# RENDERIZADO EN CARDS CON CONTENEDOR FÍSICO
# ==========================================
for i in range(0, len(apps), 3):
    cols = st.columns(3)
    group = apps[i:i+3]
    
    for idx, app in enumerate(group):
        with cols[idx]:
            # Contenedor nativo con borde/sombra (Card real)
            with st.container(border=True):
                st.markdown(f'<span class="app-badge">APP {app["num"]}</span>', unsafe_allow_html=True)
                st.subheader(f"{app['icon']} {app['title']}")
                st.write(app['desc'])
                st.write("") # Espaciador
                st.link_button("Abrir App 🚀", app['url'], use_container_width=True)
