import streamlit as st
import pandas as pd
import numpy as np

st.title("Calculadora de Valor Presente Neto (VPN)")

# Inputs iniciales
tasa_descuento = st.number_input("Tasa de descuento (%)", min_value=0.0, value=10.0, step=0.1)
duracion = st.number_input("Duración del proyecto (años)", min_value=1, step=1, value=5)

# Crear una tabla para los cashflows
st.subheader("Ingresa los flujos de caja anuales")

años = list(range(1, int(duracion)+1))
cashflows = [0.0] * len(años)

# Crear inputs dinámicos para cada año
for i in range(len(años)):
    cashflows[i] = st.number_input(f"Flujo de caja año {años[i]}", key=f"cf_{i}")

# Calcular VPN
tasa_decimal = tasa_descuento / 100
vpn = sum(cf / (1 + tasa_decimal) ** i for i, cf in enumerate(cashflows, start=1))

# Resultado
st.markdown("---")
st.subheader(f"Valor Presente Neto (VPN): ${vpn:,.2f}")