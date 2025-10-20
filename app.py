import pandas as pd
import plotly.express as px
import streamlit as st

# --- Título / encabezado ---
st.title("Exploración de Datos de Vehículos")
st.write("Esta aplicación muestra ejemplos de análisis exploratorio básico usando Streamlit y Plotly.")


car_data = pd.read_csv("vehicles_us.csv")

# --- Casilla para mostrar histograma ---
if st.checkbox("Mostrar histograma del odómetro"):
    st.write("### Histograma del odómetro")
    fig_hist = px.histogram(car_data, x="odometer", nbins=50, title="Distribución del odómetro")
    st.plotly_chart(fig_hist, use_container_width=True)


# --- Casilla para mostrar gráfico de dispersión ---
if st.checkbox("Mostrar gráfico de dispersión de precio vs odómetro"):
    st.write("### Gráfico de dispersión: precio vs odómetro")
    
    # Quitar filas con NaN en 'odometer' o 'price'
    car_data_clean = car_data.dropna(subset=['odometer', 'price'])
    
    # Scatter básico
    fig_scatter = px.scatter(
        car_data_clean,
        x="odometer",
        y="price",
        title="Precio vs Odómetro"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
