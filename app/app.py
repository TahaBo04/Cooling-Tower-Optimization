import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Cooling Tower Optimization", page_icon="🧊", layout="wide")

st.title("Cooling Tower Optimization Dashboard")
st.markdown("""
This interactive dashboard lets you explore how PID parameters affect the **cooling tower efficiency**.
Adjust the sliders below to see predicted performance indicators based on your control inputs.
""")

# Sidebar inputs
st.sidebar.header("🔧 Control Parameters")
kp = st.sidebar.slider("Kp (Proportional Gain)", 1.0, 1.5, 1.29, 0.01)
ki = st.sidebar.slider("Ki (Integral Gain)", 0.4, 0.7, 0.56, 0.01)
kd = st.sidebar.slider("Kd (Derivative Gain)", 0.2, 0.5, 0.38, 0.01)
air_velocity = st.sidebar.slider("Air Velocity (m/s)", 1.5, 3.0, 2.56, 0.01)
water_flow = st.sidebar.slider("Water Flow Rate (L/s)", 40.0, 60.0, 54.7, 0.1)

st.sidebar.markdown("---")
st.sidebar.info("Optimized setpoint found using Random Forest model for maximum efficiency and minimum CO₂.")

# Simple demo model (replace with your trained one if available)
def predict_efficiency(kp, ki, kd, air_velocity, water_flow):
    # Approximation based on your optimization results
    base_eff = 80.1
    eff = base_eff + 1.8 * np.exp(-((kp - 1.29)**2 + (ki - 0.56)**2 + (kd - 0.38)**2)*15)
    eff += 0.01 * (air_velocity - 2.5) + 0.005 * (water_flow - 50)
    energy = 120 + (82 - eff) * 0.5
    co2 = 5 + (energy - 120) * 0.02
    water = 150 - (eff - 80) * 0.4
    return eff, energy, co2, water

# Predictions
eff, energy, co2, water = predict_efficiency(kp, ki, kd, air_velocity, water_flow)

# Results display
col1, col2, col3, col4 = st.columns(4)
col1.metric("Efficiency (%)", f"{eff:.2f}")
col2.metric("Energy (kWh)", f"{energy:.2f}")
col3.metric("CO₂ Emissions (kg)", f"{co2:.3f}")
col4.metric("Water Use (L)", f"{water:.2f}")

# Chart visualization
st.markdown("### Efficiency Trend Simulation")
x = np.linspace(1.0, 1.5, 50)
y = [predict_efficiency(i, ki, kd, air_velocity, water_flow)[0] for i in x]
st.line_chart(pd.DataFrame({"Kp": x, "Efficiency": y}).set_index("Kp"))

st.success("Dashboard ready — experiment with the sliders to see how control tuning affects performance.")


