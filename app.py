import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats

# Configuración de página
st.set_page_config(
    page_title="Estadística Básica",
    page_icon="📊",
    layout="wide"
)

# CSS personalizado simplificado y funcional
st.markdown("""
<style>
    /* Importar fuente Google */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Variables CSS */
    :root {
        --primary-color: #2E86AB;
        --secondary-color: #A23B72;
        --accent-color: #F18F01;
        --success-color: #C73E1D;
        --text-dark: #333333;
        --shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        --border-radius: 12px;
    }
    
    /* Estilos globales básicos */
    .main .block-container {
        font-family: 'Poppins', sans-serif;
        color: #333333;
    }
    
    /* Header principal */
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
        padding: 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 12px;
        color: white;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    /* Headers de sección */
    .section-header {
        font-size: 2rem;
        font-weight: 600;
        color: #2E86AB;
        margin: 2rem 0 1.5rem 0;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 12px;
        border-left: 5px solid #F18F01;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    
    /* Cajas de contenido */
    .concept-box {
        background: white;
        color: #333333;
        padding: 2rem;
        border-radius: 12px;
        border: 2px solid #e3f2fd;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        margin: 1.5rem 0;
        transition: transform 0.3s ease;
    }
    
    .concept-box:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
    }
    
    .concept-box h3 {
        color: #2E86AB;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .concept-box h4 {
        color: #A23B72;
        font-weight: 500;
        margin-bottom: 1rem;
    }
    
    .concept-box h5 {
        color: #333333;
        font-weight: 500;
        margin-bottom: 0.8rem;
    }
    
    .concept-box p, .concept-box li {
        color: #333333;
        line-height: 1.6;
    }
    
    .concept-box strong {
        color: #C73E1D;
        font-weight: 600;
    }
    
    /* Caja de fórmulas */
    .formula-box {
        background: #fff8e1;
        color: #333333;
        padding: 2rem;
        border-radius: 12px;
        border: 2px solid #ffe0b2;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        margin: 1.5rem 0;
        position: relative;
    }
    
    .formula-box::before {
        content: '📐';
        position: absolute;
        top: 15px;
        right: 20px;
        font-size: 1.5rem;
        opacity: 0.5;
    }
    
    .formula-box h3, .formula-box h4 {
        color: #F18F01;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .formula-box p, .formula-box li {
        color: #333333;
        line-height: 1.6;
    }
    
    .formula-box strong {
        color: #C73E1D;
        font-weight: 600;
    }
    
    /* Caja de ejemplos */
    .example-box {
        background: #e8f5e8;
        color: #333333;
        padding: 2rem;
        border-radius: 12px;
        border: 2px solid #c8e6c9;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        margin: 1.5rem 0;
        position: relative;
    }
    
    .example-box::before {
        content: '💡';
        position: absolute;
        top: 15px;
        right: 20px;
        font-size: 1.5rem;
    }
    
    .example-box h3, .example-box h4 {
        color: #2e7d32;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .example-box p, .example-box li {
        color: #333333;
        line-height: 1.6;
    }
    
    .example-box strong {
        color: #1b5e20;
        font-weight: 600;
    }
    
    /* Caja de advertencia */
    .warning-box {
        background: #fff3e0;
        color: #333333;
        padding: 2rem;
        border-radius: 12px;
        border: 2px solid #ffcc02;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        margin: 1.5rem 0;
        position: relative;
    }
    
    .warning-box::before {
        content: '⚠️';
        position: absolute;
        top: 15px;
        right: 20px;
        font-size: 1.5rem;
    }
    
    .warning-box h3, .warning-box h4 {
        color: #f57c00;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .warning-box p, .warning-box li {
        color: #333333;
        line-height: 1.6;
    }
    
    .warning-box strong {
        color: #e65100;
        font-weight: 600;
    }
    
    /* Botones */
    .stButton > button {
        background: linear-gradient(45deg, #2E86AB, #A23B72);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.7rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(46, 134, 171, 0.3);
    }
    
    /* Métricas */
    [data-testid="metric-container"] {
        background: white;
        border: 2px solid #e1e8ed;
        padding: 1rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    /* Tablas */
    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    /* Selectbox y inputs */
    .stSelectbox label, .stTextInput label, .stTextArea label {
        color: #333333;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="main-header">📊 Estadística Básica para Secundaria</h1>', unsafe_allow_html=True)
    
    # Sidebar para navegación
    st.sidebar.title("📚 Navegación")
    sections = [
        "🏠 Inicio",
        "📖 ¿Qué es la Estadística?",
        "👥 Conceptos Básicos",
        "📊 Tipos de Datos",
        "📋 Tablas de Frecuencia",
        "📐 Medidas de Tendencia Central",
        "📉 Otras Medidas",
        "📊 Gráficas",
        "🧮 Calculadora Estadística",
        "🎯 Ejercicios Prácticos"
    ]
    
    choice = st.sidebar.radio("Selecciona una sección:", sections)
    
    if choice == "🏠 Inicio":
        show_inicio()
    elif choice == "📖 ¿Qué es la Estadística?":
        show_que_es_estadistica()
    elif choice == "👥 Conceptos Básicos":
        show_conceptos_basicos()
    elif choice == "📊 Tipos de Datos":
        show_tipos_datos()
    elif choice == "📋 Tablas de Frecuencia":
        show_tablas_frecuencia()
    elif choice == "📐 Medidas de Tendencia Central":
        show_medidas_tendencia()
    elif choice == "📉 Otras Medidas":
        show_otras_medidas()
    elif choice == "📊 Gráficas":
        show_graficas()
    elif choice == "🧮 Calculadora Estadística":
        show_calculadora()
    elif choice == "🎯 Ejercicios Prácticos":
        show_ejercicios()

def show_inicio():
    st.markdown('<h2 class="section-header">¡Bienvenida al mundo de la Estadística! 🎉</h2>', unsafe_allow_html=True)
    
    # Mensaje de bienvenida
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="concept-box" style="text-align: center;">
        <h2 style="color: black;">🎓 ¡Hola, Dayanna y Jady!</h2>
        <p style="font-size: 1.2rem; color: black;">
        Bienvenida a tu aventura en el fascinante mundo de la estadística. 
        Aquí aprenderás de manera divertida e interactiva.
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="concept-box">
    <h3>🎯 ¿Qué vas a descubrir?</h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
        <div style="background: #e3f2fd; padding: 1rem; border-radius: 10px; text-align: center;">
            <div style="font-size: 2rem;">📊</div>
            <strong style="color: #1976d2;">Conceptos básicos</strong>
            <p>Población, muestra y datos</p>
        </div>
        <div style="background: #f3e5f5; padding: 1rem; border-radius: 10px; text-align: center;">
            <div style="font-size: 2rem;">📈</div>
            <strong style="color: #7b1fa2;">Tipos de datos</strong>
            <p>Cualitativos y cuantitativos</p>
        </div>
        <div style="background: #e8f5e8; padding: 1rem; border-radius: 10px; text-align: center;">
            <div style="font-size: 2rem;">📋</div>
            <strong style="color: #388e3c;">Tablas ordenadas</strong>
            <p>Organiza tu información</p>
        </div>
        <div style="background: #fff3e0; padding: 1rem; border-radius: 10px; text-align: center;">
            <div style="font-size: 2rem;">📐</div>
            <strong style="color: #f57c00;">Cálculos fáciles</strong>
            <p>Media, mediana y moda</p>
        </div>
        <div style="background: #fce4ec; padding: 1rem; border-radius: 10px; text-align: center;">
            <div style="font-size: 2rem;">📊</div>
            <strong style="color: #c2185b;">Gráficas bonitas</strong>
            <p>Visualiza tus datos</p>
        </div>
        <div style="background: #e1f5fe; padding: 1rem; border-radius: 10px; text-align: center;">
            <div style="font-size: 2rem;">🧮</div>
            <strong style="color: #0277bd;">Calculadora mágica</strong>
            <p>Resultados automáticos</p>
        </div>
    </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Ejemplo visual
    st.markdown('<h3 style="color: #2E86AB; text-align: center; margin: 2rem 0;">🌟 Ejemplo: YouTubers Populares</h3>', unsafe_allow_html=True)
    
    youtubers = ['MrBeast', 'ElRubius', 'TheGrefg', 'Ibai', 'AuronPlay']
    suscriptores = [180, 38, 17, 13, 14]
    
    fig = px.bar(
        x=youtubers, 
        y=suscriptores,
        title="🎬 YouTubers con más Suscriptores (Millones)",
        color=suscriptores,
        color_continuous_scale='viridis',
        text=suscriptores
    )
    fig.update_traces(texttemplate='%{text}M', textposition='outside')
    fig.update_layout(
        showlegend=False,
        xaxis_title="YouTubers",
        yaxis_title="Suscriptores (Millones)"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Datos curiosos
    st.markdown("""
    <div class="example-box">
    <h3>🤔 ¿Sabías que...?</h3>
    <ul>
    <li><strong>Netflix</strong> usa estadística para recomendarte series</li>
    <li><strong>Spotify</strong> analiza tus gustos musicales</li>
    <li><strong>Instagram</strong> decide qué posts mostrarte primero</li>
    <li><strong>Google Maps</strong> calcula rutas usando datos de tráfico</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

def show_que_es_estadistica():
    st.markdown('<h2 class="section-header">📖 ¿Qué es la Estadística?</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="concept-box">
    <h3>🔍 Definición Simple</h3>
    <p style="font-size: 1.1rem;">
    La estadística es como ser un <strong>detective de números</strong>. 
    Te ayuda a encontrar patrones, resolver misterios y tomar decisiones inteligentes.
    </p>
    
    <h4>🔄 El Proceso Estadístico:</h4>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem;">
        <div style="background: #e8f4fd; padding: 1rem; border-radius: 8px; text-align: center;">
            <div style="font-size: 2rem;">🔍</div>
            <strong style="color: #1976d2;">1. RECOGER</strong>
            <p>Buscar información</p>
        </div>
        <div style="background: #f0f7ff; padding: 1rem; border-radius: 8px; text-align: center;">
            <div style="font-size: 2rem;">📊</div>
            <strong style="color: #1976d2;">2. ORGANIZAR</strong>
            <p>Ordenar los datos</p>
        </div>
        <div style="background: #e8f4fd; padding: 1rem; border-radius: 8px; text-align: center;">
            <div style="font-size: 2rem;">🧮</div>
            <strong style="color: #1976d2;">3. ANALIZAR</strong>
            <p>Hacer cálculos</p>
        </div>
        <div style="background: #f0f7ff; padding: 1rem; border-radius: 8px; text-align: center;">
            <div style="font-size: 2rem;">💡</div>
            <strong style="color: #1976d2;">4. INTERPRETAR</strong>
            <p>Sacar conclusiones</p>
        </div>
    </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Ejemplos en la vida diaria
    st.markdown('<h3 style="color: #A23B72; margin: 2rem 0 1rem 0;">🌟 Estadística en tu Vida</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="example-box">
        <h4>📱 Redes Sociales</h4>
        <ul>
        <li><strong>TikTok:</strong> ¿Cuántos views tienes?</li>
        <li><strong>Instagram:</strong> ¿Cuándo publicar?</li>
        <li><strong>WhatsApp:</strong> ¿Quién te escribe más?</li>
        <li><strong>YouTube:</strong> ¿Qué videos ves más?</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="example-box">
        <h4>🏫 En el Colegio</h4>
        <ul>
        <li><strong>Notas:</strong> ¿Cuál es tu promedio?</li>
        <li><strong>Deportes:</strong> ¿Cuál prefiere tu curso?</li>
        <li><strong>Recreo:</strong> ¿Qué snack se vende más?</li>
        <li><strong>Transporte:</strong> ¿Cómo llegan más estudiantes?</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Ejemplo interactivo
    st.markdown('<h3 style="color: #F18F01; margin: 2rem 0 1rem 0;">🎮 Ejemplo Interactivo: Uso de Apps</h3>', unsafe_allow_html=True)
    
    apps = ['TikTok', 'Instagram', 'WhatsApp', 'YouTube', 'Spotify', 'Netflix']
    horas_dia = [2.5, 1.8, 3.2, 2.1, 1.5, 1.9]
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="concept-box">
        <h4>📊 Pregunta de Investigación:</h4>
        <p style="color: #2C3E50 !important;">
        <strong>"¿Cuánto tiempo pasan los adolescentes en cada app por día?"</strong>
        </p>
        <br>
        <h4>🔍 Proceso:</h4>
        <ol>
        <li style="color: #2C3E50 !important;"><strong>Recoger:</strong> Encuestar a 100 estudiantes</li>
        <li style="color: #2C3E50 !important;"><strong>Organizar:</strong> Crear tabla con los datos</li>
        <li style="color: #2C3E50 !important;"><strong>Analizar:</strong> Calcular promedios</li>
        <li style="color: #2C3E50 !important;"><strong>Interpretar:</strong> ¿Qué app es más popular?</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        fig = px.pie(
            values=horas_dia, 
            names=apps,
            title="⏰ Tiempo Promedio por App (Horas/Día)",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(
            font=dict(size=12),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Conclusión
    st.markdown("""
    <div class="warning-box">
    <h4>🎯 ¿Por qué es importante?</h4>
    <p style="color: #2C3E50 !important;">
    La estadística te ayuda a <strong style="color: #C73E1D !important;">tomar mejores decisiones</strong> 
    en tu vida diaria, desde elegir qué carrera estudiar hasta entender las noticias y 
    no dejarte engañar por información falsa.
    </p>
    </div>
    """, unsafe_allow_html=True)

def show_conceptos_basicos():
    st.markdown('<h2 class="section-header">👥 Conceptos Básicos</h2>', unsafe_allow_html=True)
    
    # Introducción con analogía
    st.markdown("""
    <div class="concept-box" style="text-align: center;">
    <h3>🎭 Imagina que eres un Investigador</h3>
    <p style="font-size: 1.1rem; color: #2C3E50 !important;">
    Vas a investigar algo interesante sobre tu colegio. Estos son los conceptos que necesitas conocer:
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="concept-box" style="min-height: 300px;">
        <h3>🌍 Población</h3>
        <div style="text-align: center; margin: 1rem 0;">
            <div style="font-size: 3rem;">👥</div>
        </div>
        <p style="color: #2C3E50 !important;">
        Es <strong style="color: #C73E1D !important;">TODOS</strong> los elementos que quieres estudiar.
        </p>
        <br>
        <h4 style="color: #2E86AB !important;">Ejemplos:</h4>
        <ul>
        <li style="color: #2C3E50 !important;">🏫 Todos los estudiantes del colegio</li>
        <li style="color: #2C3E50 !important;">🍕 Todas las pizzerías de tu ciudad</li>
        <li style="color: #2C3E50 !important;">🐱 Todos los gatos del barrio</li>
        <li style="color: #2C3E50 !important;">📚 Todos los libros de la biblioteca</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="concept-box" style="min-height: 300px;">
        <h3>👥 Muestra</h3>
        <div style="text-align: center; margin: 1rem 0;">
            <div style="font-size: 3rem;">👨‍👩‍👧‍👦</div>
        </div>
        <p style="color: #2C3E50 !important;">
        Es una <strong style="color: #C73E1D !important;">PARTE</strong> representativa de la población.
        </p>
        <br>
        <h4 style="color: #2E86AB !important;">Ejemplos:</h4>
        <ul>
        <li style="color: #2C3E50 !important;">👨‍🎓 30 estudiantes de tu curso</li>
        <li style="color: #2C3E50 !important;">🍕 5 pizzerías del centro</li>
        <li style="color: #2C3E50 !important;">🐱 3 gatos de tu cuadra</li>
        <li style="color: #2C3E50 !important;">📚 50 libros de ciencias</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="concept-box" style="min-height: 300px;">
        <h3>📊 Dato</h3>
        <div style="text-align: center; margin: 1rem 0;">
            <div style="font-size: 3rem;">📝</div>
        </div>
        <p style="color: #2C3E50 !important;">
        Es un <strong style="color: #C73E1D !important;">VALOR</strong> específico que observas o mides.
        </p>
        <br>
        <h4 style="color: #2E86AB !important;">Ejemplos:</h4>
        <ul>
        <li style="color: #2C3E50 !important;">🎂 Edad: 15 años</li>
        <li style="color: #2C3E50 !important;">📏 Altura: 1.65 metros</li>
        <li style="color: #2C3E50 !important;">🎨 Color favorito: Azul</li>
        <li style="color: #2C3E50 !important;">📱 Marca de celular: iPhone</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Ejemplo práctico con visualización mejorada
    st.markdown('<h3 style="color: #A23B72; margin: 2rem 0 1rem 0;">🎯 Ejemplo Práctico: Investigación en tu Colegio</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="example-box">
    <h4>🔬 Pregunta de Investigación: "¿Cuál es la edad promedio de los estudiantes?"</h4>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
        <div style="background: #e3f2fd; padding: 1rem; border-radius: 10px;">
            <h5 style="color: #1976d2 !important;">🌍 Población</h5>
            <p style="color: #2C3E50 !important;"><strong>Todos los 1,200 estudiantes</strong> del colegio Playa Rica</p>
        </div>
        <div style="background: #f3e5f5; padding: 1rem; border-radius: 10px;">
            <h5 style="color: #7b1fa2 !important;">👥 Muestra</h5>
            <p style="color: #2C3E50 !important;"><strong>60 estudiantes</strong> seleccionados al azar (5 de cada curso)</p>
        </div>
        <div style="background: #e8f5e8; padding: 1rem; border-radius: 10px;">
            <h5 style="color: #388e3c !important;">📊 Datos</h5>
            <p style="color: #2C3E50 !important;"><strong>Las edades:</strong> 14, 15, 16, 17, 18 años</p>
        </div>
    </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Simulación interactiva mejorada
    st.markdown('<h3 style="color: #F18F01; margin: 2rem 0 1rem 0;">📈 Simulación Interactiva</h3>', unsafe_allow_html=True)
    
    # Crear datos más realistas
    np.random.seed(42)
    # Población: edades de estudiantes de secundaria (13-18 años)
    poblacion = np.random.choice([13, 14, 15, 16, 17, 18], 1000, p=[0.05, 0.2, 0.25, 0.25, 0.2, 0.05])
    muestra = np.random.choice(poblacion, 50, replace=False)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="concept-box">
        <h4>📊 Datos de la Simulación:</h4>
        <ul>
        <li style="color: #2C3E50 !important;"><strong>Población:</strong> 1,000 estudiantes</li>
        <li style="color: #2C3E50 !important;"><strong>Muestra:</strong> 50 estudiantes</li>
        <li style="color: #2C3E50 !important;"><strong>Variable:</strong> Edad (años)</li>
        </ul>
        <br>
        <h4>🎯 Resultados:</h4>
        <ul>
        <li style="color: #2C3E50 !important;"><strong>Edad promedio población:</strong> {:.1f} años</li>
        <li style="color: #2C3E50 !important;"><strong>Edad promedio muestra:</strong> {:.1f} años</li>
        <li style="color: #2C3E50 !important;"><strong>Diferencia:</strong> {:.1f} años</li>
        </ul>
        </div>
        """.format(np.mean(poblacion), np.mean(muestra), abs(np.mean(poblacion) - np.mean(muestra))), unsafe_allow_html=True)
    
    with col2:
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=poblacion, name="🌍 Población (1000)", 
                                  opacity=0.7, nbinsx=12, marker_color='lightblue'))
        fig.add_trace(go.Histogram(x=muestra, name="👥 Muestra (50)", 
                                  opacity=0.8, nbinsx=12, marker_color='orange'))
        fig.update_layout(
            title="👥 Comparación: Población vs Muestra",
            xaxis_title="Edad (años)", 
            yaxis_title="Número de Estudiantes",
            barmode='overlay'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Mensaje importante
    st.markdown("""
    <div class="warning-box">
    <h4>💡 ¿Por qué usamos muestras?</h4>
    <p style="color: #2C3E50 !important;">
    Porque es más <strong style="color: #C73E1D !important;">rápido, barato y práctico</strong> estudiar una parte 
    representativa que a toda la población. ¡Imagínate preguntarle a cada persona del mundo!
    </p>
    </div>
    """, unsafe_allow_html=True)

def show_tipos_datos():
    st.markdown('<h2 class="section-header">📊 Tipos de Datos</h2>', unsafe_allow_html=True)
    
    # Introducción mejorada
    st.markdown("""
    <div class="concept-box" style="text-align: center;">
    <h3>🎯 ¿Por qué clasificar los datos?</h3>
    <p style="font-size: 1.2rem;">
    Clasificar los datos nos ayuda a saber <strong>qué tipo de análisis podemos hacer</strong> 
    y <strong>qué gráficas usar</strong>. ¡Es como organizar tu closet por tipos de ropa!
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Diagrama mejorado de tipos de datos
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="example-box">
        <div style="text-align: center; margin-bottom: 1rem;">
            <div style="font-size: 3rem;">🎨</div>
        </div>
        <h3>Datos Cualitativos</h3>
        <p><strong>Son características que NO son números</strong></p>
        <p>También llamados <em>"categóricos"</em> porque clasifican en categorías.</p>
        <br>
        <h4>🌟 Ejemplos Actuales:</h4>
        <ul>
        <li><strong>Color de ojos:</strong> Verde, Azul, Café, Negro</li>
        <li><strong>Redes sociales favoritas:</strong> TikTok, Instagram, YouTube</li>
        <li><strong>Marca de teléfono:</strong> iPhone, Samsung, Xiaomi</li>
        <li><strong>Género musical:</strong> Pop, Rock, Reggaeton, K-pop</li>
        <li><strong>Plataforma de streaming:</strong> Netflix, Disney+, Prime Video</li>
        <li><strong>Comida favorita:</strong> Pizza, Hamburguesa, Sushi</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="formula-box">
        <div style="text-align: center; margin-bottom: 1rem;">
            <div style="font-size: 3rem;">🔢</div>
        </div>
        <h3>Datos Cuantitativos</h3>
        <p><strong>Son valores que SÍ son números</strong></p>
        <p>Se pueden <em>medir</em> y hacer operaciones matemáticas.</p>
        <br>
        <h4>🎯 Discretos (números enteros):</h4>
        <ul>
        <li><strong>Número de hermanos:</strong> 0, 1, 2, 3...</li>
        <li><strong>Followers en Instagram:</strong> 150, 2K, 10K...</li>
        <li><strong>Número de videojuegos:</strong> 5, 12, 25...</li>
        <li><strong>Apps instaladas:</strong> 20, 45, 100...</li>
        </ul>
        <br>
        <h4>📏 Continuos (con decimales):</h4>
        <ul>
        <li><strong>Altura:</strong> 1.65 m, 1.78 m</li>
        <li><strong>Tiempo en TikTok:</strong> 2.5 horas, 4.2 horas</li>
        <li><strong>Peso:</strong> 55.5 kg, 62.8 kg</li>
        <li><strong>Velocidad de internet:</strong> 25.6 Mbps</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Ejemplo visual con gráficos
    st.markdown('<h3 style="color: #A23B72; margin: 2rem 0 1rem 0;">📊 Visualización de Diferencias</h3>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🎨 Datos Cualitativos", "🔢 Datos Cuantitativos"])
    
    with tab1:
        # Ejemplo de datos cualitativos
        st.markdown("### 📱 Ejemplo: Redes Sociales Favoritas")
        
        redes_sociales = ['TikTok', 'Instagram', 'YouTube', 'WhatsApp', 'Discord', 'Twitch']
        votos = [45, 38, 52, 25, 20, 15]
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Gráfico de barras
            fig_bar = px.bar(
                x=redes_sociales, 
                y=votos,
                title="📊 Gráfico de Barras - Preferencias",
                color=votos,
                color_continuous_scale='viridis',
                text=votos
            )
            fig_bar.update_traces(texttemplate='%{text}', textposition='outside')
            fig_bar.update_layout(showlegend=False, xaxis_title="Redes Sociales", yaxis_title="Votos")
            st.plotly_chart(fig_bar, use_container_width=True)
        
        with col2:
            # Gráfico circular
            fig_pie = px.pie(
                values=votos, 
                names=redes_sociales,
                title="🥧 Gráfico Circular - Proporciones",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            fig_pie.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_pie, use_container_width=True)
    
    with tab2:
        # Ejemplo de datos cuantitativos
        st.markdown("### ⏰ Ejemplo: Horas de Uso del Celular por Día")
        
        # Generar datos realistas
        np.random.seed(42)
        horas_uso = np.random.normal(5.2, 1.8, 100)  # Promedio 5.2 horas, desviación 1.8
        horas_uso = np.clip(horas_uso, 1, 12)  # Entre 1 y 12 horas
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Histograma
            fig_hist = px.histogram(
                x=horas_uso, 
                nbins=20,
                title="📈 Histograma - Distribución de Horas",
                color_discrete_sequence=['#FF6B6B']
            )
            fig_hist.update_layout(xaxis_title="Horas de Uso", yaxis_title="Número de Estudiantes")
            st.plotly_chart(fig_hist, use_container_width=True)
        
        with col2:
            # Box plot
            fig_box = px.box(
                y=horas_uso, 
                title="📦 Diagrama de Caja - Estadísticas",
                color_discrete_sequence=['#4ECDC4']
            )
            fig_box.update_layout(yaxis_title="Horas de Uso")
            st.plotly_chart(fig_box, use_container_width=True)
        
        # Estadísticas
        st.markdown(f"""
        <div class="concept-box">
        <h4>📊 Estadísticas Calculadas:</h4>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
            <div style="background: #e3f2fd; padding: 1rem; border-radius: 8px; text-align: center;">
                <strong style="color: #1976d2;">Promedio</strong><br>
                <span style="font-size: 1.5rem; color: #0d47a1;">{np.mean(horas_uso):.1f} horas</span>
            </div>
            <div style="background: #f3e5f5; padding: 1rem; border-radius: 8px; text-align: center;">
                <strong style="color: #7b1fa2;">Mediana</strong><br>
                <span style="font-size: 1.5rem; color: #4a148c;">{np.median(horas_uso):.1f} horas</span>
            </div>
            <div style="background: #e8f5e8; padding: 1rem; border-radius: 8px; text-align: center;">
                <strong style="color: #388e3c;">Mínimo</strong><br>
                <span style="font-size: 1.5rem; color: #1b5e20;">{np.min(horas_uso):.1f} horas</span>
            </div>
            <div style="background: #fff3e0; padding: 1rem; border-radius: 8px; text-align: center;">
                <strong style="color: #f57c00;">Máximo</strong><br>
                <span style="font-size: 1.5rem; color: #e65100;">{np.max(horas_uso):.1f} horas</span>
            </div>
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Juego interactivo mejorado
    st.markdown('<h3 style="color: #F18F01; margin: 2rem 0 1rem 0;">🎮 ¡Juego: Clasifica los Datos!</h3>', unsafe_allow_html=True)
    
    datos_ejemplos = [
        ("Altura de estudiantes", "Cuantitativo Continuo", "📏"),
        ("Color favorito", "Cualitativo", "🎨"),
        ("Número de hermanos", "Cuantitativo Discreto", "👨‍👩‍👧‍👦"),
        ("Peso corporal", "Cuantitativo Continuo", "⚖️"),
        ("Marca de zapatos", "Cualitativo", "👟"),
        ("Edad en años", "Cuantitativo Discreto", "🎂"),
        ("Género musical favorito", "Cualitativo", "🎵"),
        ("Tiempo de carga del celular", "Cuantitativo Continuo", "🔋"),
        ("Número de mascotas", "Cuantitativo Discreto", "🐕"),
        ("Tipo de sangre", "Cualitativo", "🩸"),
        ("Velocidad de internet", "Cuantitativo Continuo", "🌐"),
        ("Videojuego favorito", "Cualitativo", "🎮")
    ]
    
    col1, col2, col3 = st.columns([2, 1, 2])
    
    with col1:
        dato_info = st.selectbox(
            "🎯 Elige un dato para clasificar:",
            datos_ejemplos,
            format_func=lambda x: f"{x[2]} {x[0]}"
        )
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔍 Verificar Respuesta", type="primary"):
            dato_elegido, tipo_correcto, icono = dato_info
            
            if tipo_correcto == "Cualitativo":
                st.success(f"✅ ¡Correcto! **{dato_elegido}** es **CUALITATIVO**")
                st.info("💡 No son números, son categorías o características.")
            elif tipo_correcto == "Cuantitativo Discreto":
                st.success(f"✅ ¡Correcto! **{dato_elegido}** es **CUANTITATIVO DISCRETO**")
                st.info("💡 Son números enteros que se pueden contar.")
            elif tipo_correcto == "Cuantitativo Continuo":
                st.success(f"✅ ¡Correcto! **{dato_elegido}** es **CUANTITATIVO CONTINUO**")
                st.info("💡 Son números que se pueden medir con decimales.")
    
    with col3:
        # Mostrar puntaje o estadísticas del juego
        st.markdown("""
        <div class="warning-box">
        <h4>🏆 Tips para Recordar:</h4>
        <ul>
        <li><strong>¿Es un número?</strong> → Cuantitativo</li>
        <li><strong>¿Se puede contar?</strong> → Discreto</li>
        <li><strong>¿Se puede medir?</strong> → Continuo</li>
        <li><strong>¿Es una categoría?</strong> → Cualitativo</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Resumen final
    st.markdown("""
    <div class="concept-box">
    <h3>🎯 ¿Por qué es importante esto?</h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 1rem;">
        <div style="background: #e8f4fd; padding: 1.5rem; border-radius: 10px;">
            <h4 style="color: #1976d2;">📊 Para elegir gráficas</h4>
            <p><strong>Cualitativos:</strong> Barras, circular</p>
            <p><strong>Cuantitativos:</strong> Histograma, líneas, cajas</p>
        </div>
        <div style="background: #f3e5f5; padding: 1.5rem; border-radius: 10px;">
            <h4 style="color: #7b1fa2;">🧮 Para hacer cálculos</h4>
            <p><strong>Cualitativos:</strong> Contar frecuencias</p>
            <p><strong>Cuantitativos:</strong> Promedio, mediana, etc.</p>
        </div>
        <div style="background: #e8f5e8; padding: 1.5rem; border-radius: 10px;">
            <h4 style="color: #388e3c;">🔍 Para interpretar</h4>
            <p><strong>Cualitativos:</strong> ¿Cuál es más popular?</p>
            <p><strong>Cuantitativos:</strong> ¿Cuál es el valor típico?</p>
        </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

def show_tablas_frecuencia():
    st.markdown('<h2 class="section-header">📋 Tablas de Frecuencia</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="concept-box">
    <h3>🎯 ¿Para qué sirven?</h3>
    Las tablas de frecuencia nos ayudan a <b>organizar</b> y <b>contar</b> datos de manera ordenada.
    Es como hacer un inventario de lo que tenemos.
    </div>
    """, unsafe_allow_html=True)
    
    # Ejemplo práctico con datos reales
    st.subheader("📊 Ejemplo: Notas de un examen")
    
    # Datos de ejemplo
    notas = [4, 5, 4, 6, 5, 7, 4, 5, 6, 5, 4, 6, 7, 5, 4, 6, 5, 7, 6, 5]
    
    # Crear tabla de frecuencias
    df_notas = pd.DataFrame({'Nota': notas})
    tabla_freq = df_notas['Nota'].value_counts().sort_index().reset_index()
    tabla_freq.columns = ['Nota', 'Frecuencia Absoluta']
    tabla_freq['Frecuencia Acumulada'] = tabla_freq['Frecuencia Absoluta'].cumsum()
    tabla_freq['Frecuencia Relativa'] = tabla_freq['Frecuencia Absoluta'] / len(notas)
    tabla_freq['Frecuencia Relativa %'] = (tabla_freq['Frecuencia Relativa'] * 100).round(1)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📋 Tabla de Frecuencias")
        st.dataframe(tabla_freq, use_container_width=True)
        
        st.markdown("""
        <div class="formula-box">
        <h4>📝 Explicación de columnas:</h4>
        <ul>
        <li><b>Frecuencia Absoluta:</b> Cuántas veces aparece cada nota</li>
        <li><b>Frecuencia Acumulada:</b> Suma progresiva</li>
        <li><b>Frecuencia Relativa:</b> Proporción del total</li>
        <li><b>Frecuencia Relativa %:</b> En porcentaje</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Gráfico de barras
        fig = px.bar(tabla_freq, x='Nota', y='Frecuencia Absoluta',
                    title="📊 Distribución de Notas",
                    color='Frecuencia Absoluta',
                    color_continuous_scale='viridis')
        st.plotly_chart(fig, use_container_width=True)

def show_medidas_tendencia():
    st.markdown('<h2 class="section-header">📐 Medidas de Tendencia Central</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="concept-box">
    <h3>🎯 ¿Qué son?</h3>
    Son números que nos ayudan a resumir un conjunto de datos con un solo valor representativo.
    ¡Como encontrar el "centro" de todos los datos!
    </div>
    """, unsafe_allow_html=True)
    
    # Datos de ejemplo
    datos_ejemplo = [2, 4, 4, 5, 5, 5, 6, 7, 8]
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="formula-box">
        <h3>1️⃣ Media (Promedio)</h3>
        <b>Fórmula:</b><br>
        Media = (Suma de todos los valores) ÷ (Cantidad de datos)
        <br><br>
        <b>Ejemplo:</b><br>
        Datos: 2, 4, 4, 5, 5, 5, 6, 7, 8<br>
        Media = (2+4+4+5+5+5+6+7+8) ÷ 9<br>
        Media = 46 ÷ 9 = 5.11
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="formula-box">
        <h3>2️⃣ Mediana</h3>
        <b>Método:</b><br>
        1. Ordena los datos<br>
        2. Encuentra el valor del medio
        <br><br>
        <b>Ejemplo:</b><br>
        Datos ordenados: 2, 4, 4, 5, <b>5</b>, 5, 6, 7, 8<br>
        Posición central: 5<br>
        Mediana = 5
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="formula-box">
        <h3>3️⃣ Moda</h3>
        <b>Método:</b><br>
        Es el valor que más se repite
        <br><br>
        <b>Ejemplo:</b><br>
        Datos: 2, 4, 4, 5, 5, <b>5</b>, 6, 7, 8<br>
        El 5 aparece 3 veces<br>
        Moda = 5
        </div>
        """, unsafe_allow_html=True)
    
    # Calculadora interactiva
    st.subheader("🧮 Calculadora Interactiva")
    
    datos_usuario = st.text_input(
        "Ingresa tus datos separados por comas (ej: 1,2,3,4,5):",
        value="2,4,4,5,5,5,6,7,8"
    )
    
    try:
        datos = [float(x.strip()) for x in datos_usuario.split(',')]
        
        media = np.mean(datos)
        mediana = np.median(datos)
        moda = stats.mode(datos, keepdims=True)[0][0]
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📊 Media", f"{media:.2f}")
        with col2:
            st.metric("📍 Mediana", f"{mediana:.2f}")
        with col3:
            st.metric("🎯 Moda", f"{moda:.2f}")
        
        # Visualización
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=list(range(len(datos))), y=datos, 
                               mode='markers+lines', name='Datos'))
        fig.add_hline(y=media, line_dash="dash", line_color="red", 
                     annotation_text=f"Media: {media:.2f}")
        fig.add_hline(y=mediana, line_dash="dash", line_color="green", 
                     annotation_text=f"Mediana: {mediana:.2f}")
        fig.add_hline(y=moda, line_dash="dash", line_color="blue", 
                     annotation_text=f"Moda: {moda:.2f}")
        fig.update_layout(title="📈 Visualización de Medidas de Tendencia Central")
        st.plotly_chart(fig, use_container_width=True)
        
    except:
        st.error("❌ Por favor ingresa números válidos separados por comas")

def show_otras_medidas():
    st.markdown('<h2 class="section-header">📉 Otras Medidas Importantes</h2>', unsafe_allow_html=True)
    
    # Explicación del rango
    st.markdown("""
    <div class="concept-box">
    <h3>📏 Rango</h3>
    <b>Definición:</b> Es la diferencia entre el valor más grande y el más pequeño.<br>
    <b>Fórmula:</b> Rango = Valor máximo - Valor mínimo<br>
    <b>¿Para qué sirve?</b> Nos dice qué tan dispersos están los datos.
    </div>
    """, unsafe_allow_html=True)
    
    # Ejemplo práctico con temperaturas
    st.subheader("🌡️ Ejemplo: Temperaturas de la semana")
    
    temperaturas = [18, 22, 25, 20, 19, 24, 21]
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    
    df_temp = pd.DataFrame({'Día': dias, 'Temperatura (°C)': temperaturas})
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.dataframe(df_temp, use_container_width=True)
        
        rango = max(temperaturas) - min(temperaturas)
        st.markdown(f"""
        <div class="formula-box">
        <h4>📊 Cálculo del Rango:</h4>
        <b>Temperatura máxima:</b> {max(temperaturas)}°C<br>
        <b>Temperatura mínima:</b> {min(temperaturas)}°C<br>
        <b>Rango = {max(temperaturas)} - {min(temperaturas)} = {rango}°C</b>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        fig = px.line(df_temp, x='Día', y='Temperatura (°C)', 
                     title="🌡️ Temperaturas de la Semana",
                     markers=True)
        fig.add_hline(y=max(temperaturas), line_dash="dash", line_color="red",
                     annotation_text=f"Máx: {max(temperaturas)}°C")
        fig.add_hline(y=min(temperaturas), line_dash="dash", line_color="blue",
                     annotation_text=f"Mín: {min(temperaturas)}°C")
        st.plotly_chart(fig, use_container_width=True)
    
    # Ejemplo de frecuencias
    st.subheader("📊 Ejemplo completo: Número de hermanos")
    
    hermanos = [0, 1, 1, 2, 0, 1, 3, 2, 1, 0, 1, 2, 1, 0, 2]
    
    # Crear tabla completa
    df_hermanos = pd.DataFrame({'Hermanos': hermanos})
    tabla_completa = df_hermanos['Hermanos'].value_counts().sort_index().reset_index()
    tabla_completa.columns = ['Nº Hermanos', 'Frecuencia Absoluta']
    tabla_completa['Frecuencia Acumulada'] = tabla_completa['Frecuencia Absoluta'].cumsum()
    tabla_completa['Frecuencia Relativa'] = tabla_completa['Frecuencia Absoluta'] / len(hermanos)
    tabla_completa['Frecuencia Relativa %'] = (tabla_completa['Frecuencia Relativa'] * 100).round(1)
    
    st.dataframe(tabla_completa, use_container_width=True)

def show_graficas():
    st.markdown('<h2 class="section-header">📊 Representaciones Gráficas</h2>', unsafe_allow_html=True)
    
    # Datos de ejemplo
    materias = ['Matemáticas', 'Ciencias', 'Historia', 'Arte', 'Educación Física']
    votos = [15, 12, 8, 10, 20]
    
    tab1, tab2, tab3 = st.tabs(["📊 Gráfico de Barras", "📈 Histograma", "🥧 Gráfico Circular"])
    
    with tab1:
        st.subheader("📊 Gráfico de Barras")
        st.markdown("""
        <div class="concept-box">
        <b>¿Cuándo usarlo?</b> Para comparar cantidades entre diferentes categorías.
        </div>
        """, unsafe_allow_html=True)
        
        fig_bar = px.bar(x=materias, y=votos, 
                        title="📚 Materia Favorita de los Estudiantes",
                        color=votos, color_continuous_scale='viridis')
        fig_bar.update_layout(xaxis_title="Materias", yaxis_title="Número de Votos")
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with tab2:
        st.subheader("📈 Histograma")
        st.markdown("""
        <div class="concept-box">
        <b>¿Cuándo usarlo?</b> Para mostrar la distribución de datos numéricos agrupados.
        </div>
        """, unsafe_allow_html=True)
        
        # Generar datos de alturas
        np.random.seed(42)
        alturas = np.random.normal(165, 10, 100)
        
        fig_hist = px.histogram(
            x=alturas, 
            nbins=15,
            title="📏 Distribución de Alturas de Estudiantes",
            color_discrete_sequence=['skyblue']
        )
        fig_hist.update_layout(xaxis_title="Altura (cm)", yaxis_title="Frecuencia")
        st.plotly_chart(fig_hist, use_container_width=True)
    
    with tab3:
        st.subheader("🥧 Gráfico Circular (Pastel)")
        st.markdown("""
        <div class="concept-box">
        <b>¿Cuándo usarlo?</b> Para mostrar proporciones o porcentajes del total.
        </div>
        """, unsafe_allow_html=True)
        
        fig_pie = px.pie(values=votos, names=materias,
                        title="🥧 Distribución de Preferencias por Materia")
        st.plotly_chart(fig_pie, use_container_width=True)

def show_calculadora():
    st.markdown('<h2 class="section-header">🧮 Calculadora Estadística</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="concept-box">
    <h3>🎯 ¡Prueba tu propia calculadora!</h3>
    Ingresa tus datos y obtén todos los cálculos automáticamente.
    </div>
    """, unsafe_allow_html=True)
    
    # Input de datos
    datos_input = st.text_area(
        "📝 Ingresa tus datos (separados por comas o espacios):",
        value="1, 2, 2, 3, 4, 4, 4, 5, 6, 7",
        height=100
    )
    
    if st.button("🔢 Calcular"):
        try:
            # Procesar datos
            import re
            datos = re.findall(r'-?\d+\.?\d*', datos_input)
            datos = [float(x) for x in datos]
            
            if len(datos) == 0:
                st.error("❌ No se encontraron datos válidos")
                return
            
            # Cálculos
            media = np.mean(datos)
            mediana = np.median(datos)
            try:
                moda = stats.mode(datos, keepdims=True)[0][0]
            except:
                moda = "No hay moda única"
            
            rango = max(datos) - min(datos)
            desv_std = np.std(datos, ddof=1)
            
            # Mostrar resultados
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("📊 Media", f"{media:.2f}")
            with col2:
                st.metric("📍 Mediana", f"{mediana:.2f}")
            with col3:
                if isinstance(moda, (int, float)):
                    st.metric("🎯 Moda", f"{moda:.2f}")
                else:
                    st.metric("🎯 Moda", moda)
            with col4:
                st.metric("📏 Rango", f"{rango:.2f}")
            
            # Tabla de frecuencias
            st.subheader("📋 Tabla de Frecuencias")
            df_datos = pd.DataFrame({'Valor': datos})
            tabla_freq = df_datos['Valor'].value_counts().sort_index().reset_index()
            tabla_freq.columns = ['Valor', 'Frecuencia']
            tabla_freq['Frecuencia Acumulada'] = tabla_freq['Frecuencia'].cumsum()
            tabla_freq['Frecuencia Relativa'] = (tabla_freq['Frecuencia'] / len(datos)).round(4)
            tabla_freq['Frecuencia Relativa %'] = (tabla_freq['Frecuencia Relativa'] * 100).round(2)
            
            st.dataframe(tabla_freq, use_container_width=True)
            
            # Gráficos
            col1, col2 = st.columns(2)
            
            with col1:
                fig_hist = px.histogram(
                    x=datos, 
                    nbins=min(10, len(set(datos))),
                    title="📊 Histograma de los Datos"
                )
                st.plotly_chart(fig_hist, use_container_width=True)
            
            with col2:
                fig_box = px.box(
                    y=datos, 
                    title="📦 Diagrama de Caja"
                )
                st.plotly_chart(fig_box, use_container_width=True)
            
        except Exception as e:
            st.error(f"❌ Error al procesar los datos: {str(e)}")

def show_ejercicios():
    st.markdown('<h2 class="section-header">🎯 Ejercicios Prácticos</h2>', unsafe_allow_html=True)
    
    # Introducción mejorada
    st.markdown("""
    <div class="concept-box" style="text-align: center;">
    <h3>🎮 ¡Hora de Practicar!</h3>
    <p style="font-size: 1.2rem;">
    Pon a prueba tus conocimientos con estos ejercicios interactivos. 
    ¡Cada uno tiene datos reales y gráficas dinámicas!
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Selector de ejercicios mejorado
    ejercicios = {
        "📊 Ejercicio 1: Análisis de Notas del Examen": {
            "descripcion": "Analiza las calificaciones de matemáticas",
            "dificultad": "⭐⭐",
            "tipo": "Medidas de tendencia central"
        },
        "🏃 Ejercicio 2: Encuesta de Deportes Favoritos": {
            "descripcion": "Investiga las preferencias deportivas",
            "dificultad": "⭐",
            "tipo": "Datos cualitativos y frecuencias"
        },
        "🍕 Ejercicio 3: Estudio de Comidas Populares": {
            "descripcion": "Descubre los gustos gastronómicos",
            "dificultad": "⭐⭐",
            "tipo": "Tablas de frecuencia y gráficas"
        },
        "📱 Ejercicio 4: Tiempo de Pantalla Digital": {
            "descripcion": "Analiza el uso de dispositivos móviles",
            "dificultad": "⭐⭐⭐",
            "tipo": "Datos continuos y distribuciones"
        },
        "🎮 Ejercicio 5: Gaming en Estudiantes": {
            "descripcion": "Estudia los hábitos de videojuegos",
            "dificultad": "⭐⭐⭐",
            "tipo": "Análisis completo de datos"
        }
    }
    
    # Mostrar tarjetas de ejercicios
    st.markdown('<h3 style="color: #A23B72; margin: 2rem 0 1rem 0;">🎯 Selecciona tu Ejercicio</h3>', unsafe_allow_html=True)
    
    # Crear grid de ejercicios
    cols = st.columns(2)
    ejercicio_elegido = None
    
    for i, (nombre, info) in enumerate(ejercicios.items()):
        with cols[i % 2]:
            if st.button(f"{nombre}\n{info['dificultad']} | {info['tipo']}", 
                        key=f"btn_{i}", use_container_width=True):
                ejercicio_elegido = nombre
    
    # Ejercicio seleccionado por defecto
    if not ejercicio_elegido:
        ejercicio_elegido = st.selectbox(
            "O elige desde el menú:",
            list(ejercicios.keys()),
            format_func=lambda x: f"{x} - {ejercicios[x]['dificultad']}"
        )
    
    st.markdown("---")
    
    # EJERCICIO 1: Análisis de Notas
    if "Ejercicio 1" in ejercicio_elegido:
        st.markdown("""
        <div class="example-box">
        <h3>📊 Ejercicio 1: Análisis de Notas del Examen</h3>
        <p><strong>Contexto:</strong> El profesor de matemáticas quiere analizar los resultados del último examen para entender el rendimiento de la clase.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Datos del ejercicio
        notas_raw = "7, 8, 6, 9, 7, 8, 10, 6, 7, 8, 9, 7, 6, 8, 7, 5, 9, 8, 7, 6"
        notas = [7, 8, 6, 9, 7, 8, 10, 6, 7, 8, 9, 7, 6, 8, 7, 5, 9, 8, 7, 6]
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown(f"""
            <div class="concept-box">
            <h4>📝 Datos del Examen:</h4>
            <p style="font-family: monospace; background: #f0f0f0; padding: 1rem; border-radius: 8px;">
            {notas_raw}
            </p>
            <p><strong>Total de estudiantes:</strong> {len(notas)}</p>
            <p><strong>Escala:</strong> 1-10 puntos</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Pregunta interactiva
            st.markdown("### 🤔 Pregunta:")
            pregunta = st.radio(
                "¿Cuál crees que es la nota más común?",
                ["6", "7", "8", "9"],
                key="pregunta_nota"
            )
        
        with col2:
            # Mostrar gráfico inmediatamente
            fig_notas = px.histogram(
                x=notas, 
                nbins=10,
                title="📊 Distribución de Notas del Examen",
                color_discrete_sequence=['#FF6B6B'],
                text_auto=True
            )
            fig_notas.update_layout(
                xaxis_title="Notas", 
                yaxis_title="Número de Estudiantes",
                showlegend=False
            )
            fig_notas.update_traces(texttemplate='%{y}', textposition='outside')
            st.plotly_chart(fig_notas, use_container_width=True)
        
        # Botón de solución
        if st.button("🔍 Ver Análisis Completo", key="solucion1"):
            media = np.mean(notas)
            mediana = np.median(notas)
            moda = stats.mode(notas, keepdims=True)[0][0]
            rango = max(notas) - min(notas)
            
            # Verificar respuesta
            if pregunta == str(int(moda)):
                st.success(f"✅ ¡Correcto! La moda es {int(moda)}")
            else:
                st.error(f"❌ Incorrecto. La nota más común (moda) es {int(moda)}, no {pregunta}")
            
            # Mostrar métricas
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("📊 Media", f"{media:.1f}")
            with col2:
                st.metric("📍 Mediana", f"{mediana:.1f}")
            with col3:
                st.metric("🎯 Moda", f"{int(moda)}")
            with col4:
                st.metric("📏 Rango", f"{rango}")
            
            # Interpretación
            st.markdown(f"""
            <div class="warning-box">
            <h4>📝 Interpretación de Resultados:</h4>
            <ul>
            <li><strong>Rendimiento general:</strong> {'Bueno' if media >= 7 else 'Regular' if media >= 6 else 'Necesita mejorar'} (promedio: {media:.1f})</li>
            <li><strong>Nota más frecuente:</strong> {int(moda)} puntos</li>
            <li><strong>Variabilidad:</strong> {'Alta' if rango > 4 else 'Media' if rango > 2 else 'Baja'} (rango: {rango} puntos)</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    
    # EJERCICIO 2: Deportes Favoritos
    elif "Ejercicio 2" in ejercicio_elegido:
        st.markdown("""
        <div class="example-box">
        <h3>🏃 Ejercicio 2: Encuesta de Deportes Favoritos</h3>
        <p><strong>Contexto:</strong> El colegio quiere implementar nuevas actividades deportivas y necesita saber las preferencias de los estudiantes.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Datos de deportes
        deportes = ["Fútbol", "Básquetbol", "Voleibol", "Natación", "Atletismo", "Tenis"]
        votos_deportes = [45, 32, 28, 15, 20, 12]
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Crear tabla interactiva
            df_deportes = pd.DataFrame({
                'Deporte': deportes,
                'Votos': votos_deportes,
                'Porcentaje': [f"{(v/sum(votos_deportes)*100):.1f}%" for v in votos_deportes]
            })
            df_deportes = df_deportes.sort_values('Votos', ascending=False).reset_index(drop=True)
            df_deportes['Ranking'] = range(1, len(df_deportes) + 1)
            
            st.markdown("### 📋 Resultados de la Encuesta:")
            st.dataframe(df_deportes[['Ranking', 'Deporte', 'Votos', 'Porcentaje']], 
                        use_container_width=True, hide_index=True)
            
            # Pregunta interactiva
            st.markdown("### 🤔 Pregunta:")
            respuesta_deporte = st.selectbox(
                "¿Qué porcentaje de estudiantes prefiere fútbol?",
                ["25.7%", "29.4%", "32.1%", "35.8%"],
                key="pregunta_deporte"
            )
        
        with col2:
            # Gráfico de barras horizontal
            fig_deportes = px.bar(
                df_deportes, 
                x='Votos', 
                y='Deporte',
                orientation='h',
                title="🏆 Deportes Favoritos - Ranking",
                color='Votos',
                color_continuous_scale='viridis',
                text='Votos'
            )
            fig_deportes.update_traces(texttemplate='%{text}', textposition='outside')
            fig_deportes.update_layout(yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig_deportes, use_container_width=True)
        
        if st.button("🔍 Ver Análisis Deportivo", key="solucion2"):
            porcentaje_futbol = (votos_deportes[0] / sum(votos_deportes)) * 100
            
            if respuesta_deporte == f"{porcentaje_futbol:.1f}%":
                st.success(f"✅ ¡Correcto! El fútbol representa el {porcentaje_futbol:.1f}% de las preferencias")
            else:
                st.error(f"❌ Incorrecto. El fútbol representa el {porcentaje_futbol:.1f}%")
            
            # Gráfico circular
            fig_pie = px.pie(
                values=votos_deportes, 
                names=deportes,
                title="🥧 Distribución de Preferencias Deportivas",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            fig_pie.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_pie, use_container_width=True)
            
            st.markdown(f"""
            <div class="concept-box">
            <h4>🏆 Conclusiones del Estudio:</h4>
            <ul>
            <li><strong>Deporte más popular:</strong> {deportes[0]} con {votos_deportes[0]} votos</li>
            <li><strong>Los 3 primeros</strong> representan el {sum(votos_deportes[:3])/sum(votos_deportes)*100:.1f}% del total</li>
            <li><strong>Recomendación:</strong> Priorizar instalaciones para los deportes más votados</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    
    # EJERCICIO 3: Comidas Populares
    elif "Ejercicio 3" in ejercicio_elegido:
        st.markdown("""
        <div class="example-box">
        <h3>🍕 Ejercicio 3: Estudio de Comidas Populares</h3>
        <p><strong>Contexto:</strong> La cafetería del colegio quiere renovar su menú basándose en las preferencias de los estudiantes.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Datos de comidas
        comidas_data = {
            'Pizza': 85, 'Hamburguesa': 67, 'Sushi': 45, 'Tacos': 38, 
            'Pasta': 52, 'Ensaladas': 23, 'Sándwiches': 41, 'Hot Dogs': 29
        }
        
        tab1, tab2, tab3 = st.tabs(["📊 Datos", "📈 Análisis", "🎯 Ejercicio"])
        
        with tab1:
            # Mostrar datos en formato de encuesta
            st.markdown("### 📝 Resultados de la Encuesta (200 estudiantes):")
            
            df_comidas = pd.DataFrame(list(comidas_data.items()), columns=['Comida', 'Votos'])
            df_comidas['Frecuencia Relativa'] = df_comidas['Votos'] / df_comidas['Votos'].sum()
            df_comidas['Porcentaje'] = df_comidas['Frecuencia Relativa'] * 100
            df_comidas = df_comidas.sort_values('Votos', ascending=False).reset_index(drop=True)
            
            # Tabla con formato mejorado
            st.dataframe(
                df_comidas[['Comida', 'Votos', 'Porcentaje']].round(1),
                use_container_width=True,
                hide_index=True
            )
        
        with tab2:
            # Múltiples visualizaciones
            col1, col2 = st.columns(2)
            
            with col1:
                # Gráfico de barras
                fig_bar = px.bar(
                    df_comidas.head(6), 
                    x='Comida', 
                    y='Votos',
                    title="🍽️ Top 6 Comidas Favoritas",
                    color='Votos',
                    color_continuous_scale='reds',
                    text='Votos'
                )
                fig_bar.update_traces(texttemplate='%{text}', textposition='outside')
                fig_bar.update_layout(xaxis={'tickangle': 45})
                st.plotly_chart(fig_bar, use_container_width=True)
            
            with col2:
                # Gráfico de dona
                fig_donut = px.pie(
                    df_comidas, 
                    values='Votos', 
                    names='Comida',
                    title="🍩 Distribución Completa",
                    hole=0.4
                )
                fig_donut.update_traces(textposition='inside', textinfo='percent')
                st.plotly_chart(fig_donut, use_container_width=True)
            
            # Métricas adicionales
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("🥇 Más Popular", df_comidas.iloc[0]['Comida'])
            with col2:
                st.metric("📊 Total Votos", df_comidas['Votos'].sum())
            with col3:
                st.metric("🔝 Top 3", f"{df_comidas.head(3)['Votos'].sum()}")
            with col4:
                st.metric("📉 Menos Popular", df_comidas.iloc[-1]['Comida'])
        
        with tab3:
            # Ejercicio interactivo
            st.markdown("### 🧮 Calcula las Frecuencias:")
            
            comida_elegida = st.selectbox(
                "Selecciona una comida para calcular su frecuencia relativa:",
                df_comidas['Comida'].tolist()
            )
            
            respuesta_freq = st.number_input(
                f"¿Cuál es la frecuencia relativa de {comida_elegida}? (como decimal, ej: 0.425)",
                min_value=0.0, max_value=1.0, step=0.001, format="%.3f"
            )
            
            if st.button("✅ Verificar Cálculo", key="check_freq"):
                frecuencia_real = df_comidas[df_comidas['Comida'] == comida_elegida]['Frecuencia Relativa'].iloc[0]
                
                if abs(respuesta_freq - frecuencia_real) < 0.01:
                    st.success(f"✅ ¡Correcto! La frecuencia relativa es {frecuencia_real:.3f}")
                    
                    # Mostrar explicación
                    votos_comida = df_comidas[df_comidas['Comida'] == comida_elegida]['Votos'].iloc[0]
                    st.markdown(f"""
                    <div class="formula-box">
                    <h4>🧮 Cálculo paso a paso:</h4>
                    <p><strong>Frecuencia Relativa = Votos de {comida_elegida} ÷ Total de votos</strong></p>
                    <p>Frecuencia Relativa = {votos_comida} ÷ {df_comidas['Votos'].sum()} = {frecuencia_real:.3f}</p>
                    <p>En porcentaje: {frecuencia_real:.3f} × 100 = {frecuencia_real*100:.1f}%</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error(f"❌ Incorrecto. La frecuencia relativa correcta es {frecuencia_real:.3f}")
    
    # EJERCICIO 4: Tiempo de Pantalla
    elif "Ejercicio 4" in ejercicio_elegido:
        st.markdown("""
        <div class="example-box">
        <h3>📱 Ejercicio 4: Tiempo de Pantalla Digital</h3>
        <p><strong>Contexto:</strong> Un estudio sobre el tiempo que los estudiantes pasan usando dispositivos digitales diariamente.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Generar datos realistas
        np.random.seed(42)
        horas_pantalla = np.round(np.random.normal(6.5, 2.1, 50), 1)
        horas_pantalla = np.clip(horas_pantalla, 1.0, 12.0)
        
        tab1, tab2, tab3 = st.tabs(["📊 Exploración", "📈 Distribución", "🎯 Predicción"])
        
        with tab1:
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.markdown("### 📱 Datos del Estudio:")
                st.markdown(f"**Muestra:** {len(horas_pantalla)} estudiantes")
                st.markdown("**Período:** Promedio semanal")
                st.markdown("**Unidad:** Horas por día")
                
                # Estadísticas básicas
                media_h = np.mean(horas_pantalla)
                mediana_h = np.median(horas_pantalla)
                std_h = np.std(horas_pantalla)
                
                st.markdown(f"""
                <div class="concept-box">
                <h4>📊 Estadísticas Básicas:</h4>
                <ul>
                <li><strong>Media:</strong> {media_h:.1f} horas</li>
                <li><strong>Mediana:</strong> {mediana_h:.1f} horas</li>
                <li><strong>Desviación estándar:</strong> {std_h:.1f} horas</li>
                <li><strong>Mínimo:</strong> {np.min(horas_pantalla):.1f} horas</li>
                <li><strong>Máximo:</strong> {np.max(horas_pantalla):.1f} horas</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                # Box plot interactivo
                fig_box = px.box(
                    y=horas_pantalla, 
                    title="📦 Distribución del Tiempo de Pantalla",
                    labels={'y': 'Horas por día'}
                )
                fig_box.add_hline(y=media_h, line_dash="dash", line_color="red", 
                                 annotation_text=f"Media: {media_h:.1f}h")
                fig_box.add_hline(y=mediana_h, line_dash="dash", line_color="green", 
                                 annotation_text=f"Mediana: {mediana_h:.1f}h")
                st.plotly_chart(fig_box, use_container_width=True)
        
        with tab2:
            # Análisis de distribución
            st.markdown("### 📈 Análisis de la Distribución:")
            
            # Histograma
            fig_hist = px.histogram(
                x=horas_pantalla, 
                nbins=15,
                title="📊 Histograma - Distribución de Horas",
                color_discrete_sequence=['#FF6B6B']
            )
            fig_hist.update_layout(xaxis_title="Horas de Uso", yaxis_title="Número de Estudiantes")
            st.plotly_chart(fig_hist, use_container_width=True)
            
            # Gráfico de línea acumulativa
            horas_sorted = np.sort(horas_pantalla)
            percentiles = np.arange(1, len(horas_sorted) + 1) / len(horas_sorted) * 100
            
            fig_cum = px.line(
                x=horas_sorted, 
                y=percentiles,
                title="📈 Distribución Acumulativa",
                labels={'x': 'Horas por día', 'y': 'Percentil'}
            )
            st.plotly_chart(fig_cum, use_container_width=True)
            
            # Categorización
            categories = {
                'Bajo (< 4h)': np.sum(horas_pantalla < 4),
                'Moderado (4-7h)': np.sum((horas_pantalla >= 4) & (horas_pantalla <= 7)),
                'Alto (> 7h)': np.sum(horas_pantalla > 7)
            }
            
            st.markdown("### 🎯 Categorización del Uso:")
            cols = st.columns(3)
            for i, (cat, count) in enumerate(categories.items()):
                with cols[i]:
                    percentage = (count / len(horas_pantalla)) * 100
                    st.metric(cat, f"{count} estudiantes", f"{percentage:.1f}%")
        
        with tab3:
            # Ejercicio de predicción
            st.markdown("### 🔮 Ejercicio de Predicción:")
            
            st.markdown("""
            <div class="warning-box">
            <h4>📝 Pregunta:</h4>
            <p>Si elegimos un estudiante al azar, ¿cuál es la probabilidad de que use su dispositivo más de 8 horas al día?</p>
            </div>
            """, unsafe_allow_html=True)
            
            respuesta_prob = st.slider(
                "Tu respuesta (en porcentaje):",
                0, 100, 25, step=1
            )
            
            if st.button("🎯 Verificar Predicción", key="check_prediction"):
                estudiantes_mas_8h = np.sum(horas_pantalla > 8)
                probabilidad_real = (estudiantes_mas_8h / len(horas_pantalla)) * 100
                
                diferencia = abs(respuesta_prob - probabilidad_real)
                
                if diferencia <= 5:
                    st.success(f"✅ ¡Excelente! Tu respuesta ({respuesta_prob}%) está muy cerca del valor real ({probabilidad_real:.1f}%)")
                elif diferencia <= 10:
                    st.warning(f"⚠️ Cerca, pero puedes mejorar. La probabilidad real es {probabilidad_real:.1f}%")
                else:
                    st.error(f"❌ La probabilidad real es {probabilidad_real:.1f}%. ¡Sigue practicando!")
                
                # Explicación detallada
                st.markdown(f"""
                <div class="formula-box">
                <h4>🧮 Explicación del Cálculo:</h4>
                <p><strong>Estudiantes con más de 8h:</strong> {estudiantes_mas_8h} de {len(horas_pantalla)}</p>
                <p><strong>Probabilidad = {estudiantes_mas_8h}/{len(horas_pantalla)} = {probabilidad_real:.3f}</strong></p>
                <p><strong>En porcentaje:</strong> {probabilidad_real:.3f} × 100 = {probabilidad_real*100:.1f}%</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Visualizar la zona de más de 8 horas
                fig_highlight = px.histogram(
                    x=horas_pantalla, 
                    nbins=15,
                    title="📱 Estudiantes con Más de 8 Horas (Zona Roja)"
                )
                fig_highlight.add_vline(x=8, line_dash="dash", line_color="red", 
                                       annotation_text="8 horas")
                st.plotly_chart(fig_highlight, use_container_width=True)
    
    # EJERCICIO 5: Gaming
    elif "Ejercicio 5" in ejercicio_elegido:
        st.markdown("""
        <div class="example-box">
        <h3>🎮 Ejercicio 5: Gaming en Estudiantes</h3>
        <p><strong>Contexto:</strong> Análisis completo sobre los hábitos de videojuegos en estudiantes de secundaria.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Datos complejos de gaming
        gaming_data = {
            'plataformas': ['PC', 'PlayStation', 'Xbox', 'Nintendo Switch', 'Móvil'],
            'usuarios': [120, 85, 45, 60, 180],
            'horas_promedio': [4.2, 3.8, 3.5, 2.9, 2.1],
            'generos': ['Acción', 'Deportes', 'RPG', 'Estrategia', 'Casual'],
            'popularidad_generos': [35, 25, 20, 12, 8]
        }
        
        tab1, tab2, tab3, tab4 = st.tabs(["🎮 Plataformas", "⏰ Tiempo de Juego", "🎯 Géneros", "📊 Análisis Final"])
        
        with tab1:
            st.markdown("### 🎮 Análisis de Plataformas:")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Gráfico de barras de plataformas
                fig_plat = px.bar(
                    x=gaming_data['plataformas'], 
                    y=gaming_data['usuarios'],
                    title="👥 Usuarios por Plataforma",
                    color=gaming_data['usuarios'],
                    color_continuous_scale='viridis',
                    text=gaming_data['usuarios']
                )
                fig_plat.update_traces(texttemplate='%{text}', textposition='outside')
                fig_plat.update_layout(xaxis_title="Plataformas", yaxis_title="Número de Usuarios")
                st.plotly_chart(fig_plat, use_container_width=True)
            
            with col2:
                # Scatter plot: usuarios vs horas
                fig_scatter = px.scatter(
                    x=gaming_data['usuarios'], 
                    y=gaming_data['horas_promedio'],
                    text=gaming_data['plataformas'],
                    title="📊 Usuarios vs Horas Promedio",
                    labels={'x': 'Número de Usuarios', 'y': 'Horas Promedio/Día'},
                    size=gaming_data['usuarios'],
                    color=gaming_data['horas_promedio'],
                    color_continuous_scale='reds'
                )
                fig_scatter.update_traces(textposition="top center")
                st.plotly_chart(fig_scatter, use_container_width=True)
            
            # Pregunta interactiva
            st.markdown("### 🤔 Pregunta de Correlación:")
            correlacion_resp = st.radio(
                "¿Observas alguna relación entre el número de usuarios y las horas promedio?",
                ["Correlación positiva fuerte", "Correlación negativa", "No hay correlación clara"],
                key="correlacion_gaming"
            )
            
            if st.button("🔍 Analizar Correlación", key="check_correlacion"):
                # Calcular correlación real
                corr = np.corrcoef(gaming_data['usuarios'], gaming_data['horas_promedio'])[0,1]
                
                if correlacion_resp == "Correlación negativa" and corr < -0.3:
                    st.success("✅ ¡Correcto! Hay una correlación negativa: más usuarios, menos horas promedio por persona")
                else:
                    st.info(f"La correlación es {corr:.3f}, indicando una relación negativa moderada")
                
                st.markdown(f"""
                <div class="concept-box">
                <h4>📊 Interpretación:</h4>
                <p>Las plataformas más populares tienden a tener menor tiempo promedio de juego por usuario, 
                posiblemente porque atraen usuarios más casuales.</p>
                </div>
                """, unsafe_allow_html=True)
        
        with tab2:
            # Análisis de tiempo detallado
            st.markdown("### ⏰ Distribución del Tiempo de Juego:")
            
            # Generar datos individuales basados en promedios
            np.random.seed(123)
            tiempo_detallado = []
            plataforma_detallada = []
            
            for i, plat in enumerate(gaming_data['plataformas']):
                usuarios_plat = gaming_data['usuarios'][i]
                horas_prom = gaming_data['horas_promedio'][i]
                
                # Generar datos normales alrededor del promedio
                tiempos = np.random.normal(horas_prom, 1.2, usuarios_plat)
                tiempos = np.clip(tiempos, 0.5, 10)  # Límites realistas
                
                tiempo_detallado.extend(tiempos)
                plataforma_detallada.extend([plat] * usuarios_plat)
            
            # Box plot comparativo
            df_gaming = pd.DataFrame({
                'Plataforma': plataforma_detallada,
                'Horas': tiempo_detallado
            })
            
            fig_box_gaming = px.box(
                df_gaming, 
                x='Plataforma', 
                y='Horas',
                title="📦 Distribución de Horas por Plataforma"
            )
            st.plotly_chart(fig_box_gaming, use_container_width=True)
            
            # Estadísticas por plataforma
            st.markdown("### 📊 Estadísticas Detalladas:")
            stats_gaming = df_gaming.groupby('Plataforma')['Horas'].agg(['mean', 'median', 'std']).round(2)
            st.dataframe(stats_gaming, use_container_width=True)
        
        with tab3:
            # Análisis de géneros
            st.markdown("### 🎯 Popularidad de Géneros:")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Gráfico de dona para géneros
                fig_dona = px.pie(
                    values=gaming_data['popularidad_generos'], 
                    names=gaming_data['generos'],
                    title="🍩 Distribución de Géneros Preferidos",
                    hole=0.5
                )
                fig_dona.update_traces(textposition='inside', textinfo='percent')
                st.plotly_chart(fig_dona, use_container_width=True)
            
            with col2:
                # Tabla de frecuencias
                df_generos = pd.DataFrame({
                    'Género': gaming_data['generos'],
                    'Votos': gaming_data['popularidad_generos']
                })
                df_generos['Porcentaje'] = (df_generos['Votos'] / df_generos['Votos'].sum() * 100).round(1)
                df_generos['Frecuencia Acumulada'] = df_generos['Votos'].cumsum()
                
                st.markdown("### 📋 Tabla de Frecuencias:")
                st.dataframe(df_generos, use_container_width=True, hide_index=True)
            
            # Ejercicio de probabilidad
            st.markdown("### 🎲 Cálculo de Probabilidades:")
            
            evento = st.selectbox(
                "¿Cuál es la probabilidad de que un estudiante elegido al azar prefiera:",
                ["Acción", "Deportes", "RPG", "Acción O Deportes", "RPG O Estrategia"]
            )
            
            if st.button("🧮 Calcular Probabilidad", key="calc_prob_gaming"):
                total_votos = sum(gaming_data['popularidad_generos'])
                
                if evento == "Acción":
                    prob = gaming_data['popularidad_generos'][0] / total_votos
                elif evento == "Deportes":
                    prob = gaming_data['popularidad_generos'][1] / total_votos
                elif evento == "RPG":
                    prob = gaming_data['popularidad_generos'][2] / total_votos
                elif evento == "Acción O Deportes":
                    prob = (gaming_data['popularidad_generos'][0] + gaming_data['popularidad_generos'][1]) / total_votos
                elif evento == "RPG O Estrategia":
                    prob = (gaming_data['popularidad_generos'][2] + gaming_data['popularidad_generos'][3]) / total_votos
                
                st.success(f"📊 Probabilidad de {evento}: {prob:.3f} o {prob*100:.1f}%")
        
        with tab4:
            # Análisis final integrado
            st.markdown("### 📊 Análisis Final Integrado:")
            
            # Crear dashboard final
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("🎮 Total Jugadores", sum(gaming_data['usuarios']))
            with col2:
                st.metric("⏰ Promedio General", f"{np.mean(gaming_data['horas_promedio']):.1f}h")
            with col3:
                plat_popular = gaming_data['plataformas'][np.argmax(gaming_data['usuarios'])]
                st.metric("📱 Plataforma #1", plat_popular)
            with col4:
                genero_popular = gaming_data['generos'][np.argmax(gaming_data['popularidad_generos'])]
                st.metric("🎯 Género #1", genero_popular)
            
            # Conclusiones finales
            st.markdown("""
            <div class="concept-box">
            <h3>🎯 Conclusiones del Estudio Gaming:</h3>
            <ul>
            <li><strong>Plataforma dominante:</strong> Móvil (más accesible)</li>
            <li><strong>Tiempo de juego:</strong> PC tiene usuarios más dedicados</li>
            <li><strong>Género preferido:</strong> Acción es el más popular</li>
            <li><strong>Diversidad:</strong> Buenos niveles de variedad en preferencias</li>
            </ul>
            
            <h4>📈 Recomendaciones:</h4>
            <ul>
            <li>Desarrollar más juegos móviles casuales</li>
            <li>Mantener variedad en géneros</li>
            <li>Considerar el tiempo limitado de usuarios móviles</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            # Gráfico final combinado
            fig_final = go.Figure()
            
            # Barras para usuarios
            fig_final.add_trace(go.Bar(
                name='Usuarios',
                x=gaming_data['plataformas'],
                y=gaming_data['usuarios'],
                yaxis='y',
                offsetgroup=1
            ))
            
            # Línea para horas promedio
            fig_final.add_trace(go.Scatter(
                name='Horas Promedio',
                x=gaming_data['plataformas'],
                y=gaming_data['horas_promedio'],
                yaxis='y2',
                mode='lines+markers',
                line=dict(color='red', width=3)
            ))
            
            fig_final.update_layout(
                title='🎮 Usuarios vs Horas Promedio por Plataforma',
                xaxis_title='Plataforma',
                yaxis=dict(title='Número de Usuarios', side='left'),
                yaxis2=dict(title='Horas Promedio', side='right', overlaying='y'),
                legend=dict(x=0.7, y=0.9)
            )
            
            st.plotly_chart(fig_final, use_container_width=True)

if __name__ == "__main__":
    main()
