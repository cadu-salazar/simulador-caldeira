import streamlit as st

# Título do Simulador
st.title("Simulador de Caldeira a Biomassa")

# Entradas do usuário
vazao_biomassa = st.slider("Vazão de Biomassa (kg/s):", 0.1, 10.0, 2.0)
eficiencia = st.slider("Eficiência da Caldeira (%):", 50, 100, 85)
demanda_vapor = st.slider("Demanda de Vapor (kg/s):", 0.1, 5.0, 1.5)
pci_biomassa = st.number_input("Poder Calorífico Inferior da Biomassa (kJ/kg):", value=15000)

# Cálculos
energia_util = demanda_vapor * 2257  # kJ/s, considerando entalpia latente do vapor
consumo_biomassa = energia_util / (pci_biomassa * (eficiencia / 100))  # kg/s

# Saídas
st.write("### Resultados:")
st.write(f"Demanda de Energia Útil: {energia_util:.2f} kJ/s")
st.write(f"Consumo de Biomassa Necessário: {consumo_biomassa:.2f} kg/s")
st.write(f"Eficiência Operacional: {eficiencia:.2f} %")
