import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Contruir un histograma de año de modelo del vehiculo')

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_checkbox = st.checkbox('Construir histograma')  # crear un botón

if hist_checkbox:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma de año de modelo del vehículo con filtro por condición.')
    # mostrar un mensaje de éxito
    st.write('Los datos se han cargado correctamente.')

    # crear un histograma
    fig = px.histogram(car_data, x="model_year", color="condition")

    # mostrar un gráfico Plotly interactivo d
    st.plotly_chart(fig, use_container_width=True)

st.header(
    'Contruir un gráfico de dispersión del precio del vehículo con año de modelo')

scatt_checkbox = st.checkbox(
    'Construir gráfico de dispersión')  # crear un checkbox
if scatt_checkbox:  # al hacer clic en el checkbox
    # escribir un mensaje
    st.write(
        'Creación de un gráfico de dispersión de año de modelo del vehículo con precio.')
    # mostrar un mensaje de éxito
    st.write('Los datos se han cargado correctamente.')

    # crear un gráfico de dispersión
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="model_year", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
