import streamlit as st
import pandas as pd
import numpy as np

# Título
st.title("🎮 Adivina la Tendencia (TrendGuess)")

st.write("Observa el gráfico y predice qué pasó después:")

# Generar datos simulados
np.random.seed(42)
data = np.cumsum(np.random.randn(50))

df = pd.DataFrame({
    "time": range(50),
    "value": data
})

# SLICING (ocultar última parte)
cut = int(len(df) * 0.8)
visible = df[:cut]
hidden = df[cut:]

# Mostrar gráfico incompleto
st.line_chart(visible.set_index("time"))

# Elección del usuario
choice = st.radio("¿Qué crees que pasó?", ["Subió", "Bajó", "Se mantuvo"])

# Botón
if st.button("Revelar resultado"):
    st.subheader("📊 Resultado completo")
    st.line_chart(df.set_index("time"))

    inicio = visible["value"].iloc[-1]
    final = df["value"].iloc[-1]

    if final > inicio:
        correcta = "Subió"
    elif final < inicio:
        correcta = "Bajó"
    else:
        correcta = "Se mantuvo"

    st.write(f"Respuesta correcta: {correcta}")

    if choice == correcta:
        st.success("🎉 ¡Acertaste!")
    else:
        st.error("❌ No acertaste")


