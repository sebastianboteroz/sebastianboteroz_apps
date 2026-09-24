import os
import platform
import traceback
import streamlit as st
from PIL import Image

# ==========================================
# CONFIGURACIÓN DE PÁGINA Y TEMÁTICA VISUAL
# ==========================================
st.set_page_config(
    page_title="Sebastián Botero | Portfolio de Inteligencia Artificial",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados para una UI/UX moderna, legible y accesible
st.markdown("""
<style>
    /* Estructura general */
    .main { padding: 1.5rem 2.5rem; }
    
    /* Header principal con degradado elegante */
    .hero-header {
        background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 50%, #4338CA 100%);
        padding: 2.5rem;
        border-radius: 16px;
        color: #FFFFFF;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.2);
    }
    
    .hero-header h1 {
        color: #FFFFFF !important;
        font-weight: 800;
        font-size: 2.4rem;
        margin-bottom: 0.5rem;
    }
    
    .hero-header p {
        color: #C7D2FE;
        font-size: 1.1rem;
        margin: 0;
    }

    /* Tarjetas de aplicaciones */
    .app-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1.25rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .app-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }

    /* Enlaces tipo botón interactivo */
    .app-link {
        display: inline-block;
        background: linear-gradient(90deg, #4F46E5 0%, #7C3AED 100%);
        color: white !important;
        font-weight: 600;
        padding: 0.5rem 1.2rem;
        border-radius: 8px;
        text-decoration: none !important;
        margin-top: 0.8rem;
        width: 100%;
        text-align: center;
        transition: opacity 0.2s ease;
    }

    .app-link:hover {
        opacity: 0.92;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Función auxiliar para renderizar imágenes de forma segura sin romper la App
def render_app_image(image_filename, fallback_url):
    try:
        image = Image.open(image_filename)
        st.image(image, use_column_width=True)
    except Exception:
        st.image(fallback_url, use_column_width=True)

# ==========================================
# BARRA LATERAL (PERFIL Y RECURSOS)
# ==========================================
with st.sidebar:
    st.markdown("## 👨‍💻 Sebastián Botero Z.")
    st.caption("Diseñador de Interfaces & Desarrollador de Soluciones con Inteligencia Artificial")
    
    st.markdown("---")
    
    st.markdown("### 📌 Sobre este Portal")
    st.write(
        "Esta plataforma centraliza un ecosistema de aplicaciones interactivas desarrolladas con "
        "modelos de Visión por Computador, Procesamiento de Lenguaje Natural (NLP), "
        "Sintetización de Voz e Interfaces Multimodales."
    )
    
    st.markdown("---")
    
    # Enlace externo
    url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
    st.markdown(f"📚 **Recursos & Guías Prácticas:**\n[Sitio Web de Aplicaciones de IA]({url_ia})")

    st.markdown("---")
    st.caption(f"Entorno: Python v{platform.python_version()} | Framework: Streamlit")

# ==========================================
# BANNER PRINCIPAL
# ==========================================
st.markdown("""
<div class="hero-header">
    <h1>Ecosistema de Aplicaciones con Inteligencia Artificial 🤖✨</h1>
    <p>Explora prototipos interactivos, herramientas multimodales y soluciones basadas en modelos de IA.</p>
</div>
""", unsafe_allow_html=True)

# Métricas rápidas del portafolio
m1, m2, m3, m4 = st.columns(4)
m1.metric(label="Apps Desarrolladas", value="10")
m2.metric(label="Procesamiento de Voz", value="3 Apps")
m3.metric(label="Análisis de Texto / NLP", value="4 Apps")
m4.metric(label="Computer Vision", value="3 Apps")

st.markdown("---")

# ==========================================
# CATEGORÍA 1: AUDIO & INTERFACES MULTIMODALES
# ==========================================
st.header("🔊 1. Audio, Voz & Traducción Multimodal")
st.caption("Herramientas para sintetización de voz, traducción en tiempo real y lectura asistida.")

c1_1, c1_2, c1_3 = st.columns(3)

with c1_1:
    st.subheader("🗣️ Texto a Audio")
    render_app_image(
        'txt_to_audio2.png', 
        "https://images.unsplash.com/photo-1590602847861-f357a9332bbc?auto=format&fit=crop&w=500&q=80"
    )
    st.write("Genera voz sintética de alta calidad a partir de entradas de texto.")
    st.markdown('<a href="https://interfacesmultimodalessebas.streamlit.app/" target="_blank" class="app-link">Probar Texto a Audio 🚀</a>', unsafe_allow_html=True)

with c1_2:
    st.subheader("🌐 Traductor Multimodal")
    render_app_image(
        'OIG8.jpg', 
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=500&q=80"
    )
    st.write("Traducción inteligente de texto y voz en múltiples idiomas.")
    st.markdown('<a href="https://traductorsebastianboteroz.streamlit.app/" target="_blank" class="app-link">Probar Traductor 🚀</a>', unsafe_allow_html=True)

with c1_3:
    st.subheader("🔊 OCR con Reproducción")
    render_app_image(
        'OIG3.jpg', 
        "https://images.unsplash.com/photo-1589254065878-42c9da997008?auto=format&fit=crop&w=500&q=80"
    )
    st.write("Extrae texto de documentos físicos e imágenes y escúchalo al instante.")
    st.markdown('<a href="https://ocr-audiosebastianboteroz.streamlit.app/" target="_blank" class="app-link">Probar OCR + Audio 🚀</a>', unsafe_allow_html=True)

st.markdown("---")

# ==========================================
# CATEGORÍA 2: PROCESAMIENTO DE TEXTO & NLP
# ==========================================
st.header("📑 2. Inteligencia de Texto, NLP & Analítica")
st.caption("Procesamiento de documentos, análisis de sentimientos, minería de texto y visualización lingüística.")

c2_1, c2_2, c2_3, c2_4 = st.columns(4)

with c2_1:
    st.subheader("📄 Extracción OCR")
    render_app_image(
        'data_analisis.png', 
        "https://images.unsplash.com/photo-1568667256549-094345857637?auto=format&fit=crop&w=500&q=80"
    )
    st.write("Reconocimiento óptico de caracteres para digitalizar texto desde imágenes.")
    st.markdown('<a href="https://ocr-sebastianboteroz.streamlit.app/" target="_blank" class="app-link">Probar OCR 🚀</a>', unsafe_allow_html=True)

with c2_2:
    st.subheader("📊 WordCloud Studio")
    render_app_image(
        'OIG5.jpg', 
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=500&q=80"
    )
    st.write("Generación de nubes de palabras interactivas para análisis de frecuencia.")
    st.markdown('<a href="https://wordcloudsebastianboterozz.streamlit.app/" target="_blank" class="app-link">Probar WordCloud 🚀</a>', unsafe_allow_html=True)

with c2_3:
    st.subheader("🎭 Análisis de Sentimiento")
    render_app_image(
        'OIG6.jpg', 
        "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?auto=format&fit=crop&w=500&q=80"
    )
    st.write("Evaluación de polaridad y emociones en textos en español.")
    st.markdown('<a href="https://sentimentalsebastianboteroz.streamlit.app/" target="_blank" class="app-link">Probar Sentimiento 🚀</a>', unsafe_allow_html=True)

with c2_4:
    st.subheader("🔤 TF-IDF en Español")
    render_app_image(
        'Chat_pdf.png', 
        "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?auto=format&fit=crop&w=500&q=80"
    )
    st.write("Modelado de relevancia de términos e importancia conceptual en corpus de texto.")
    st.markdown('<a href="https://tdfesp-sebastianboterozz.streamlit.app/" target="_blank" class="app-link">Probar TF-IDF 🚀</a>', unsafe_allow_html=True)

st.markdown("---")

# ==========================================
# CATEGORÍA 3: COMPUTER VISION & DEMOS
# ==========================================
st.header("👁️ 3. Visión por Computador & Prototipos")
st.caption("Detección de objetos, clasificación de imágenes y modelos entrenados personalizados.")

c3_1, c3_2, c3_3 = st.columns(3)

with c3_1:
    st.subheader("🎯 Detección YOLOv5")
    render_app_image(
        'txt_to_audio.png', 
        "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=500&q=80"
    )
    st.write("Detección y delimitación de objetos en imágenes usando el modelo YOLOv5.")
    st.markdown('<a href="https://yolov5sebastianboteroz.streamlit.app/" target="_blank" class="app-link">Probar YOLOv5 🚀</a>', unsafe_allow_html=True)

with c3_2:
    st.subheader("🧠 Teachable Machine")
    render_app_image(
        'OIG4.jpg', 
        "https://images.unsplash.com/photo-1507146426996-ef05306b995a?auto=format&fit=crop&w=500&q=80"
    )
    st.write("Clasificación de imágenes mediante modelos customizados entrenados en Teachable Machine.")
    st.markdown('<a href="https://teachablemachinesebastianboteroz.streamlit.app/" target="_blank" class="app-link">Probar Teachable 🚀</a>', unsafe_allow_html=True)

with c3_3:
    st.subheader("⚡ Mi Primera App IA")
    render_app_image(
        'OIG5.jpg', 
        "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=500&q=80"
    )
    st.write("Primer desarrollo exploratorio e interfaz básica de interacción.")
    st.markdown('<a href="https://miprimeraappsebas.streamlit.app/" target="_blank" class="app-link">Probar Primera App 🚀</a>', unsafe_allow_html=True)
