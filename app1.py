import streamlit as st
import requests
import matplotlib.pyplot as plt
import random


API_KEY = API_KEY = os.getenv("API_KEY", "")

API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-base"
headers = {"Authorization": f"Bearer {API_KEY}"}


# =========================
# 🤖 INTENTO DE IA
# =========================
def generar_rutina_ia(edad, objetivo):
    prompt = f"""
    Crea una rutina diaria DETALLADA para una persona de {edad} años cuyo objetivo es {objetivo}.
    Incluye ejercicios específicos, tiempos y recomendaciones.
    """

    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt}, timeout=10)

        if response.status_code != 200:
            return None

        resultado = response.json()
        return resultado[0]["generated_text"]

    except:
        return None


# =========================
# 🔥 MODO BÁSICO MEJORADO
# =========================
def generar_rutina_basica(edad, objetivo):

    rutinas = {
        "🏋️ Ganar músculo": [
            ["💪 Flexiones (3x10)", "🏋️ Sentadillas (3x12)", "🫁 Descanso 60s"],
            ["🏋️ Peso corporal", "🔥 Zancadas (3x10)", "💪 Plancha 30s"],
            ["💥 Burpees (3x8)", "🏋️ Sentadillas (3x15)", "🧱 Core"]
        ],

        "🔥 Bajar de peso": [
            ["🏃 Jumping jacks (3x30s)", "🔥 Burpees (3x10)", "🚶 Cardio"],
            ["🚴 Cardio 20 min", "💪 Abdominales", "🔥 Mountain climbers"],
            ["🏃 Saltar cuerda", "🔥 HIIT 15 min", "🚶 Caminata"]
        ],

        "🧘 Salud": [
            ["🚶 Caminata 30 min", "🧘 Estiramientos", "💧 Hidratación"],
            ["🧘 Yoga suave", "🚶 Actividad ligera", "😌 Relajación"],
            ["🚶 Paseo", "🧘 Movilidad", "💤 Buen descanso"]
        ],

        "📚 Estudio": [
            ["📚 Estudio profundo 2h", "☕ Descanso", "📝 Repaso"],
            ["📖 Lectura", "🧠 Práctica", "📚 Resumen"],
            ["📝 Ejercicios", "📚 Teoría", "☕ Break"]
        ],

        "⚡ Productividad": [
            ["⚡ Trabajo enfocado", "📚 Aprendizaje", "💪 Ejercicio"],
            ["🧠 Deep work", "📊 Organización", "🚶 Pausa"],
            ["📅 Planificación", "⚡ Ejecución", "😴 Descanso"]
        ]
    }

    seleccion = random.choice(rutinas.get(objetivo, [["Actividad básica"]]))

    return f"""
🧠 Rutina recomendada (modo básico mejorado):

👤 Edad: {edad}
🎯 Objetivo: {objetivo}

🔹 Actividades:
- {seleccion[0]}
- {seleccion[1]}
- {seleccion[2]}

💤 Dormir: {random.choice(['7 horas', '8 horas', '6-8 horas'])}
💧 Agua: {random.choice(['2 litros', '2.5 litros', '3 litros'])}
"""


# =========================
# 📊 DATOS PARA GRÁFICO
# =========================
def generar_datos_grafico(objetivo):

    if "músculo" in objetivo:
        return {"Entrenamiento": 2, "Comida": 3, "Descanso": 8, "Actividad": 2}

    elif "peso" in objetivo:
        return {"Cardio": 2, "Dieta": 3, "Descanso": 7, "Actividad": 2}

    elif "Estudio" in objetivo:
        return {"Estudio": 4, "Descanso": 8, "Ejercicio": 1, "Ocio": 2}

    else:
        return {"Trabajo": 4, "Descanso": 8, "Ejercicio": 1, "Ocio": 2}


# =========================
# 🎨 INTERFAZ
# =========================
st.title("🧠 Generador de Rutina Inteligente")

edad = st.number_input("👤 Edad", min_value=10, max_value=100)

objetivo = st.selectbox(
    "🎯 Objetivo",
    [
        "🏋️ Ganar músculo",
        "🔥 Bajar de peso",
        "🧘 Salud",
        "📚 Estudio",
        "⚡ Productividad"
    ]
)


# =========================
# ▶️ BOTÓN
# =========================
if st.button("🚀 Generar rutina"):

    rutina = generar_rutina_ia(edad, objetivo)

    if rutina:
        st.success("✅ Rutina generada con IA")
        st.write(rutina)
    else:
        st.warning("⚠️ Usando modo básico mejorado")
        rutina = generar_rutina_basica(edad, objetivo)
        st.write(rutina)

    # 📊 gráfico
    datos = generar_datos_grafico(objetivo)

    fig, ax = plt.subplots()
    ax.bar(datos.keys(), datos.values())
    ax.set_title("📊 Distribución diaria")

    st.pyplot(fig)