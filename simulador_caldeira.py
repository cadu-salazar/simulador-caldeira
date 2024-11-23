import streamlit as st
import random
import time

# Título
st.title("Simulador SCADA de Caldeira a Biomassa")

# Controles do Operador
st.sidebar.header("Controles do Operador")
vazao_biomassa = st.sidebar.slider("Vazão de Biomassa (kg/s):", 0.1, 10.0, 2.0, step=0.1)
vazao_ar = st.sidebar.slider("Vazão de Ar Primário (kg/s):", 0.1, 10.0, 3.0, step=0.1)
eficiencia = st.sidebar.slider("Eficiência da Caldeira (%):", 50, 100, 85, step=1)

# Simulações Dinâmicas
st.subheader("Monitoramento em Tempo Real")

# Inicialização de variáveis simuladas
pressao_vapor = random.uniform(8, 12)
temperatura_vapor = random.uniform(180, 220)
nivel_agua = random.uniform(50, 80)
emissoes_co = random.uniform(50, 100)

# Simular comportamento
pressao_vapor = 8 + 0.5 * vazao_biomassa + random.uniform(-0.5, 0.5)
temperatura_vapor = 200 + 2 * vazao_ar + random.uniform(-5, 5)
nivel_agua = 70 + random.uniform(-5, 5)
emissoes_co = 100 - 0.5 * eficiencia + random.uniform(-10, 10)

# Exibição de Métricas
col1, col2, col3, col4 = st.columns(4)

col1.metric("Pressão do Vapor (bar)", f"{pressao_vapor:.2f}")
col2.metric("Temperatura do Vapor (°C)", f"{temperatura_vapor:.1f}")
col3.metric("Nível de Água (%)", f"{nivel_agua:.1f}")
col4.metric("Emissões de CO (ppm)", f"{emissoes_co:.1f}")

# Gráficos de Tendência
st.subheader("Tendência de Variáveis")
placeholder = st.empty()

# Histórico para gráficos
historico_pressao = []
historico_temperatura = []
historico_nivel_agua = []

# Simulação de Tendência
for i in range(20):
    pressao_vapor = 8 + 0.5 * vazao_biomassa + random.uniform(-0.5, 0.5)
    temperatura_vapor = 200 + 2 * vazao_ar + random.uniform(-5, 5)
    nivel_agua = 70 + random.uniform(-5, 5)

    historico_pressao.append(pressao_vapor)
    historico_temperatura.append(temperatura_vapor)
    historico_nivel_agua.append(nivel_agua)

    with placeholder.container():
        st.line_chart({
            "Pressão do Vapor (bar)": historico_pressao,
            "Temperatura do Vapor (°C)": historico_temperatura,
            "Nível de Água (%)": historico_nivel_agua
        })

    time.sleep(0.5)

