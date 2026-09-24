import streamlit as st

# ==========================================
# CONFIGURACIÓN DE PÁGINA
# ==========================================
st.set_page_config(
    page_title="Sebastián Botero | Portafolio de Aplicaciones IA",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# ESTILOS CSS PERSONALIZADOS (UI/UX)
# ==========================================
st.markdown("""
<style>
    /* Fondo limpio de la aplicación */
    .stApp {
        background-color: #F8FAFC;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    .main {
        padding: 2rem 3rem;
    }

    /* Encabezado Principal */
    .portfolio-header {
        text-align: center;
        margin-bottom: 2.5rem;
    }

    .portfolio-header h1 {
        color: #0F172A !important;
        font-weight: 800;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }

    .portfolio-header p {
        color: #64748B;
        font-size: 1.15rem;
        max-width: 700px;
        margin: 0 auto;
    }

    /* Grilla Responsive para las Cards */
    .cards-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.8rem;
        width: 100%;
        margin-top: 1.5rem;
    }

    /* Estilo de las Cards (Inspirado en la referencia visual) */
    .ui-card {
        background: #FFFFFF;
        border-radius: 14px;
        padding: 1.8rem 1.5rem 1.5rem 1.5rem;
        position: relative;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        border: 1px solid #E2E8F0;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        overflow: hidden;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }

    /* Efecto Hover con Animación Sutil */
    .ui-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 25px rgba(15, 23, 42, 0.12);
        border-color: #CBD5E1;
    }

    /* Barra superior decorativa de color en cada card */
    .card-accent {
        position: absolute;
        top: 0;
        right: 1.5rem;
        width: 45px;
        height: 5px;
        border-bottom-left-radius: 4px;
        border-bottom-right-radius: 4px;
    }

    /* Número de índice estilizado en marca de agua */
    .card-number {
        position: absolute;
        top: 0.8rem;
        left: 1.2rem;
        font-size: 2.5rem;
        font-weight: 900;
        color: #F1F5F9;
        z-index: 1;
        user-select: none;
    }

    /* Contenedor del ícono */
    .card-icon-wrapper {
        position: relative;
        z-index: 2;
        margin-top: 1rem;
        margin-bottom: 1.2rem;
        display: flex;
        align-items: center;
        justify-content: flex-start;
    }

    .card-icon {
        width: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 10px;
        background-color: #F8FAFC;
    }

    /* Contenido de la Card */
    .card-body {
        position: relative;
        z-index: 2;
        flex-grow: 1;
    }

    .card-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 0.6rem;
    }

    .card-description {
        font-size: 0.92rem;
        color: #64748B;
        line-height: 1.5;
        margin-bottom: 1.5rem;
    }

    /* Botón con alto contraste */
    .card-btn {
        display: block;
        width: 100%;
        padding: 0.75rem 1rem;
        background-color: #2563EB; /* Azul de alto contraste */
        color: #FFFFFF !important;
        font-weight: 600;
        font-size: 0.95rem;
        text-align: center;
        text-decoration: none !important;
        border-radius: 8px;
        transition: background-color 0.2s ease, transform 0.1s ease;
        box-shadow: 0 2px 4px rgba(37, 99, 235, 0.2);
    }

    .card-btn:hover {
        background-color: #1D4ED8;
        transform: translateY(-1px);
        color: #FFFFFF !important;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# BARRA LATERAL (DATOS DEL AUTOR)
# ==========================================
with st.sidebar:
    st.markdown("## 👨‍💻 Sebastián Botero Z.")
    st.caption("Diseñador de Interfaces & Desarrollador de Inteligencia Artificial")
    st.markdown("---")
    st.write(
        "Bienvenido a mi ecosistema de prototipos interactivos de IA. "
        "Aquí puedes explorar soluciones avanzadas de visión por computador, procesamiento de lenguaje natural y síntesis de voz."
    )
    st.markdown("---")
    st.caption("EAFIT | Interfaces Multimodales & Producto")

# ==========================================
# ENCABEZADO
# ==========================================
st.markdown("""
<div class="portfolio-header">
    <h1>Aplicaciones de Inteligencia Artificial 🤖</h1>
    <p>Portafolio interactivo de herramientas web y modelos multimodales</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# LISTA DE DATOS DE APPS (ORDEN EXACTO PEDIDO)
# ==========================================
apps_data = [
    {
        "num": "01",
        "title": "Mi Primera App IA",
        "description": "Primer desarrollo exploratorio e interfaz básica de interacción multimodal.",
        "url": "https://miprimeraappsebas.streamlit.app/",
        "color": "#EC4899", # Rosa
        "icon": "🚀"
    },
    {
        "num": "02",
        "title": "Conversión de Texto a Audio",
        "description": "Generación de voz sintética de alta calidad a partir de entradas de texto.",
        "url": "https://interfacesmultimodalessebas.streamlit.app/",
        "color": "#06B6D4", # Cian
        "icon": "🎧"
    },
    {
        "num": "03",
        "title": "Traductor Multimodal",
        "description": "Herramienta inteligente de traducción para múltiples idiomas con voz y texto.",
        "url": "https://traductorsebastianboteroz.streamlit.app/",
        "color": "#EAB308", # Amarillo
        "icon": "🌐"
    },
    {
        "num": "04",
        "title": "Digitalización OCR",
        "description": "Reconocimiento óptico de caracteres para extraer texto desde imágenes físicas.",
        "url": "https://ocr-sebastianboteroz.streamlit.app/",
        "color": "#22C55E", # Verde
        "icon": "📄"
    },
    {
        "num": "05",
        "title": "OCR con Reproducción de Audio",
        "description": "Digitaliza textos impresos desde imágenes y los reproduce en voz hablada.",
        "url": "https://ocr-audiosebastianboteroz.streamlit.app/",
        "color": "#A855F7", # Morado
        "icon": "📢"
    },
    {
        "num": "06",
        "title": "WordCloud Studio",
        "description": "Generación de nubes de palabras interactivas para análisis de frecuencia textual.",
        "url": "https://wordcloudsebastianboterozz.streamlit.app/",
        "color": "#EF4444", # Rojo
        "icon": "📊"
    },
    {
        "num": "07",
        "title": "Análisis de Sentimiento",
        "description": "Evaluación de polaridad emocional y clasificación de opiniones en español.",
        "url": "https://sentimentalsebastianboteroz.streamlit.app/",
        "color": "#3B82F6", # Azul
        "icon": "🎭"
    },
    {
        "num": "08",
        "title": "TF-IDF en Español",
        "description": "Modelado de relevancia semántica de términos y frecuencia inversa en corpus de texto.",
        "url": "https://tdfesp-sebastianboterozz.streamlit.app/",
        "color": "#6366F1", # Índigo
        "icon": "🔤"
    },
    {
        "num": "09",
        "title": "Detección de Objetos YOLOv5",
        "description": "Detección, delimitación y etiquetado de objetos en imágenes mediante YOLOv5.",
        "url": "https://yolov5sebastianboteroz.streamlit.app/",
        "color": "#14B8A6", # Teal
        "icon": "🎯"
    },
    {
        "num": "10",
        "title": "Reconocimiento Teachable Machine",
        "description": "Clasificación de imágenes utilizando modelos entrenados en Teachable Machine.",
        "url": "https://teachablemachinesebastianboteroz.streamlit.app/",
        "color": "#F97316", # Naranja
        "icon": "🧠"
    }
]

# ==========================================
# RENDERIZADO DE LAS CARDS EN GRID RESPONSIVE
# ==========================================
cards_html = '<div class="cards-grid">'

for app in apps_data:
    cards_html += f"""
    <div class="ui-card">
        <div class="card-accent" style="background-color: {app['color']};"></div>
        <div class="card-number">{app['num']}</div>
        <div class="card-icon-wrapper">
            <div class="card-icon" style="font-size: 1.5rem;">
                {app['icon']}
            </div>
        </div>
        <div class="card-body">
            <div class="card-title">{app['title']}</div>
            <div class="card-description">{app['description']}</div>
        </div>
        <a href="{app['url']}" target="_blank" class="card-btn">Abrir App 🚀</a>
    </div>
    """

cards_html += '</div>'

# Despliegue en Streamlit
st.markdown(cards_html, unsafe_allow_html=True)
