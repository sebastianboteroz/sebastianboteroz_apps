import streamlit as st

# ==========================================
# CONFIGURACIÓN DE PÁGINA
# ==========================================
st.set_page_config(
    page_title="Sebastián Botero | Portafolio IA",
    page_icon="🚀",
    layout="wide"
)

# Estilos CSS limpios y nativos para ajustar los botones y contenedores
st.markdown("""
<style>
    /* Estilo para los botones principales de la app */
    .stButton > button {
        background-color: #2563EB !important;
        color: white !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        border: none !important;
        width: 100% !important;
        padding: 0.5rem 1rem !important;
        transition: background-color 0.2s ease !important;
    }
    .stButton > button:hover {
        background-color: #1D4ED8 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# BARRA LATERAL
# ==========================================
with st.sidebar:
    st.markdown("## 👨‍💻 Sebastián Botero Z.")
    st.caption("Diseñador de Interfaces & Desarrollador de Inteligencia Artificial")
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
st.write("Portafolio interactivo de herramientas web y modelos multimodales.")

st.markdown("---")

# ==========================================
# LISTA DE DATOS DE APPS EN ORDEN EXACTO
# ==========================================
apps = [
    {
        "title": "1. Mi Primera App IA",
        "icon": "🚀",
        "desc": "Primer desarrollo exploratorio e interfaz básica de interacción multimodal.",
        "url": "https://miprimeraappsebas.streamlit.app/"
    },
    {
        "title": "2. Convertir Texto a Audio",
        "icon": "🎧",
        "desc": "Generación de voz sintética de alta calidad a partir de entradas de texto.",
        "url": "https://interfacesmultimodalessebas.streamlit.app/"
    },
    {
        "title": "3. Traductor Multimodal",
        "icon": "🌐",
        "desc": "Herramienta inteligente de traducción para múltiples idiomas con voz y texto.",
        "url": "https://traductorsebastianboteroz.streamlit.app/"
    },
    {
        "title": "4. Digitalización OCR",
        "icon": "📄",
        "desc": "Reconocimiento óptico de caracteres para extraer texto desde imágenes físicas.",
        "url": "https://ocr-sebastianboteroz.streamlit.app/"
    },
    {
        "title": "5. OCR con Audio",
        "icon": "📢",
        "desc": "Digitaliza textos impresos desde imágenes y los reproduce en voz hablada.",
        "url": "https://ocr-audiosebastianboteroz.streamlit.app/"
    },
    {
        "title": "6. WordCloud Studio",
        "icon": "📊",
        "desc": "Generación de nubes de palabras interactivas para análisis de frecuencia textual.",
        "url": "https://wordcloudsebastianboterozz.streamlit.app/"
    },
    {
        "title": "7. Análisis de Sentimiento",
        "icon": "🎭",
        "desc": "Evaluación de polaridad emocional y clasificación de opiniones en español.",
        "url": "https://sentimentalsebastianboteroz.streamlit.app/"
    },
    {
        "title": "8. TF-IDF en Español",
        "icon": "🔤",
        "desc": "Modelado de relevancia semántica de términos y frecuencia inversa en corpus de texto.",
        "url": "https://tdfesp-sebastianboterozz.streamlit.app/"
    },
    {
        "title": "9. Detección de Objetos YOLOv5",
        "icon": "🎯",
        "desc": "Detección, delimitación y etiquetado de objetos en imágenes mediante YOLOv5.",
        "url": "https://yolov5sebastianboteroz.streamlit.app/"
    },
    {
        "title": "10. Teachable Machine",
        "icon": "🧠",
        "desc": "Clasificación de imágenes utilizando modelos entrenados en Teachable Machine.",
        "url": "https://teachablemachinesebastianboteroz.streamlit.app/"
    }
]

# ==========================================
# RENDERIZADO EN FILAS DE 3 COLUMNAS
# ==========================================

# Dividir las 10 apps en grupos de 3 para armar filas
for i in range(0, len(apps), 3):
    cols = st.columns(3)
    group = apps[i:i+3]
    
    for idx, app in enumerate(group):
        with cols[idx]:
            # Contenedor nativo tipo card
            with st.container():
                st.subheader(f"{app['icon']} {app['title']}")
                st.write(app['desc'])
                # Enlace directo formateado como botón limpio
                st.link_button("Abrir App 🚀", app['url'], use_container_width=True)
                st.markdown("<br>", unsafe_allow_html=True)
