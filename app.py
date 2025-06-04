import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Microgrid Simulator", layout="centered")

st.title("🔋 Microgrid Simulation Tool")
st.write("Simulates a 24-hour microgrid with solar generation, battery storage, and home energy usage.")

# --- Input sliders ---
st.sidebar.header("⚙️ Simulation Settings")

battery_capacity = st.sidebar.slider("Battery Capacity (kWh)", 0, 20, 10)
battery_efficiency = st.sidebar.slider("Battery Efficiency (%)", 70, 100, 90) / 100

# --- Generate profiles ---
hours = np.arange(24)
solar_profile = np.array([0]*6 + [2, 3, 4, 5, 5, 5, 4, 3, 2] + [0]*5)
load_profile = np.array([2]*6 + [3]*4 + [4]*6 + [3]*4 + [2]*4)

battery_level = 0
battery_storage = []
grid_usage = []

# --- Simulation logic ---
for hour in range(24):
    solar = solar_profile[hour]
    load = load_profile[hour]
    net_energy = solar - load

    if net_energy >= 0:
        # Surplus: charge battery
        charge_amount = net_energy * battery_efficiency
        battery_level = min(battery_level + charge_amount, battery_capacity)
        grid = 0
    else:
        # Deficit: use battery first
        required = -net_energy
        if battery_level >= required:
            battery_level -= required / battery_efficiency
            grid = 0
        else:
            grid = required - battery_level
            battery_level = 0

    battery_storage.append(battery_level)
    grid_usage.append(grid)

# --- Plotting ---
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(hours, solar_profile, label="☀️ Solar Generation (kW)")
ax.plot(hours, load_profile, label="🏠 Load Demand (kW)")
ax.plot(hours, battery_storage, label="🔋 Battery Level (kWh)")
ax.plot(hours, grid_usage, label="⚡ Grid Usage (kW)")
ax.set_xlabel("Hour of Day")
ax.set_ylabel("Energy / Power")
ax.set_title("Microgrid Simulation Over 24 Hours")
ax.legend()
ax.grid(True)

st.pyplot(fig)
st.success("✅ Simulation complete!")
