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
# ESTILOS CSS UX/UI (BANNER, PESTAÑAS Y CARDS)
# ==========================================
st.markdown("""
<style>
    /* Estilos globales */
    .stApp {
        background-color: #F8FAFC;
    }

    /* Banner Superior Estilizado en Azul Cobalto */
    .hero-banner {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 50%, #1D4ED8 100%);
        padding: 2.5rem 2rem;
        border-radius: 18px;
        color: #FFFFFF;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.3);
    }

    .hero-banner h1 {
        color: #FFFFFF !important;
        font-weight: 800;
        font-size: 2.3rem;
        margin-bottom: 0.4rem;
        border: none !important;
        padding: 0 !important;
    }

    .hero-banner p {
        color: #DBEAFE;
        font-size: 1.05rem;
        margin: 0;
    }
    
    /* Estilo para las Pestañas (st.tabs) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        margin-bottom: 1.5rem;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: #E2E8F0 !important;
        border-radius: 10px 10px 0 0 !important;
        padding: 0.6rem 1.5rem !important;
        font-weight: 700 !important;
        color: #475569 !important;
        border: none !important;
    }

    .stTabs [aria-selected="true"] {
        background-color: #2563EB !important;
        color: #FFFFFF !important;
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
        "Navega entre las pestañas superiores para explorar los desarrollos de cada entrega."
    )
    st.markdown("---")
    st.caption("EAFIT | Interfaces Multimodales & Producto")

# ==========================================
# BANNER PRINCIPAL
# ==========================================
st.markdown("""
<div class="hero-banner">
    <h1>Mis Aplicaciones de Inteligencia Artificial ✨</h1>
    <p>Repositorio interactivo de proyectos e interfaces organizadas cronológicamente por entregas.</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# DATOS DE APPS: ENTREGA 1
# ==========================================
apps_entrega_1 = [
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
# DATOS DE APPS: ENTREGA 2
# ==========================================
apps_entrega_2 = [
    {
        "num": "01",
        "title": "BrandIntel AI (RAG)",
        "icon": "📈",
        "desc": "Análisis estratégico de reportes de marca, competencia y briefs en PDF.",
        "url": "https://chatpdfsebastianboterozz.streamlit.app/"
    },
    {
        "num": "02",
        "title": "BrandVision AI (Vision)",
        "icon": "👁️‍🗨️",
        "desc": "Auditoría visio-estratégica de piezas publicitarias e identidad de marca con GPT-4o.",
        "url": "https://visionappsebastianboterozz.streamlit.app/"
    },
    {
        "num": "03",
        "title": "Lienzo de Princesas",
        "icon": "👑",
        "desc": "Tablero de dibujo interactivo con generación automática de cuentos de hadas.",
        "url": "#"  # Agrega la URL desplegada de esta app si la tienes
    },
    {
        "num": "04",
        "title": "AuraHome Control por Voz",
        "icon": "🎙️",
        "desc": "Interfaz multimodal de voz para control de dispositivos Smart Home mediante MQTT.",
        "url": "#"  # Agrega la URL desplegada de esta app si la tienes
    },
    {
        "num": "05",
        "title": "AuraIoT Command Center",
        "icon": "⚡",
        "desc": "Panel de telemetría e Internet de las Cosas (IoT) para control digital y analógico.",
        "url": "#"  # Agrega la URL desplegada de esta app si la tienes
    }
]

# Función auxiliar para renderizar la grilla de cards dentro de cualquier pestaña
def render_app_grid(apps_list):
    for i in range(0, len(apps_list), 3):
        cols = st.columns(3)
        group = apps_list[i:i+3]
        
        for idx, app in enumerate(group):
            with cols[idx]:
                with st.container(border=True):
                    st.markdown(f'<span class="app-badge">APP {app["num"]}</span>', unsafe_allow_html=True)
                    st.subheader(f"{app['icon']} {app['title']}")
                    st.write(app['desc'])
                    st.write("")
                    st.link_button("Abrir App 🚀", app['url'], use_container_width=True)

# ==========================================
# NAVEGACIÓN POR PESTAÑAS (ST.TABS)
# ==========================================
tab1, tab2 = st.tabs(["📦 Entrega 1: Fundamentos & Multimodalidad", "🚀 Entrega 2: RAG, Vision, IoT & Canvas"])

with tab1:
    st.caption("Proyectos desarrollados durante la primera etapa del curso.")
    st.write("")
    render_app_grid(apps_entrega_1)

with tab2:
    st.caption("Soluciones avanzadas de RAG, Visión Computacional, IoT y lienzos generativos.")
    st.write("")
    render_app_grid(apps_entrega_2)
