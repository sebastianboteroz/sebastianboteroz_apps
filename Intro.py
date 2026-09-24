import streamlit as st
from PIL import Image

# Configuración básica de la página
st.set_page_config(page_title="Aplicaciones de Inteligencia Artificial", layout="wide")

st.title("Aplicaciones de Inteligencia Artificial 🤖")

# Barra lateral con tu información de perfil
with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial")
    parrafo = (
        "Esta plataforma reúne un portafolio de aplicaciones interactivas desarrolladas con "
        "modelos de Visión por Computador, Procesamiento de Lenguaje Natural (NLP), "
        "Sintetización de Voz e Interfaces Multimodales."
    )
    st.write(parrafo)

# Función auxiliar para cargar imágenes sin romper la aplicación si no se encuentra el archivo local
def cargar_imagen(nombre_archivo, url_respaldo):
    try:
        img = Image.open(nombre_archivo)
        st.image(img, width=200)
    except Exception:
        st.image(url_respaldo, width=200)

# Distribución original en 3 columnas principales
col1, col2, col3 = st.columns(3)

# ==================== FILA 1 ====================
with col1:
    st.subheader("Conversión de texto a voz")
    cargar_imagen('txt_to_audio2.png', "https://images.unsplash.com/photo-1590602847861-f357a9332bbc?auto=format&fit=crop&w=400&q=80")
    st.write("Sintetiza voz de alta calidad a partir de entradas de texto.") 
    st.write("Texto a voz: [Probar App](https://interfacesmultimodalessebas.streamlit.app/)")

with col2: 
    st.subheader("Traductor Multimodal")
    cargar_imagen('OIG8.jpg', "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=400&q=80")
    st.write("Traducción inteligente e interactiva de texto y voz.") 
    st.write("Traductor: [Probar App](https://traductorsebastianboteroz.streamlit.app/)")

with col3: 
    st.subheader("Lectura OCR")
    cargar_imagen('data_analisis.png', "https://images.unsplash.com/photo-1568667256549-094345857637?auto=format&fit=crop&w=400&q=80")
    st.write("Digitalización y extracción de texto desde imágenes mediante OCR.") 
    st.write("OCR: [Probar App](https://ocr-sebastianboteroz.streamlit.app/)")

st.markdown("---")

# ==================== FILA 2 ====================
col4, col5, col6 = st.columns(3)

with col4:
    st.subheader("Lectura OCR con Audio")
    cargar_imagen('OIG3.jpg', "https://images.unsplash.com/photo-1589254065878-42c9da997008?auto=format&fit=crop&w=400&q=80")
    st.write("Extrae texto impreso de imágenes y lo reproduce en voz.") 
    st.write("OCR + Audio: [Probar App](https://ocr-audiosebastianboteroz.streamlit.app/)")

with col5:
    st.subheader("WordCloud Studio")
    cargar_imagen('Chat_pdf.png', "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=400&q=80")
    st.write("Visualización y nubes de palabras interactivas para análisis de frecuencia.") 
    st.write("WordCloud: [Probar App](https://wordcloudsebastianboterozz.streamlit.app/)")

with col6:
    st.subheader("Análisis de Sentimiento")
    cargar_imagen('OIG4.jpg', "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?auto=format&fit=crop&w=400&q=80")
    st.write("Evaluación de polaridad y emociones expresadas en texto.") 
    st.write("Sentimiento: [Probar App](https://sentimentalsebastianboteroz.streamlit.app/)")

st.markdown("---")

# ==================== FILA 3 ====================
col7, col8, col9 = st.columns(3)

with col7:
    st.subheader("TF-IDF en Español")
    cargar_imagen('OIG6.jpg', "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?auto=format&fit=crop&w=400&q=80")
    st.write("Modelado de relevancia de términos y frecuencia inversa en español.") 
    st.write("TF-IDF: [Probar App](https://tdfesp-sebastianboterozz.streamlit.app/)")

with col8:
    st.subheader("Detección de Objetos")
    cargar_imagen('txt_to_audio.png', "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=400&q=80")
    st.write("Identificación y delimitación de objetos con YOLOv5.") 
    st.write("YOLOv5: [Probar App](https://yolov5sebastianboteroz.streamlit.app/)")

with col9:
    st.subheader("Reconocimiento Teachable")
    cargar_imagen('OIG5.jpg', "https://images.unsplash.com/photo-1507146426996-ef05306b995a?auto=format&fit=crop&w=400&q=80")
    st.write("Clasificación de imágenes con modelos entrenados en Teachable Machine.") 
    st.write("Teachable Machine: [Probar App](https://teachablemachinesebastianboteroz.streamlit.app/)")

st.markdown("---")

# ==================== FILA 4 ====================
col10, col11, col12 = st.columns(3)

with col10:
    st.subheader("Mi Primera App IA")
    cargar_imagen('OIG5.jpg', "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=400&q=80")
    st.write("Primer desarrollo exploratorio e interfaz básica de interacción.") 
    st.write("Mi Primera App: [Probar App](https://miprimeraappsebas.streamlit.app/)")
