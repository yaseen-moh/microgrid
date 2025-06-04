import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.set_page_config(page_title="Microgrid Simulator", layout="centered")

st.title("🔋 Microgrid Simulation Tool")
st.write("Simulates a 24-hour microgrid with solar generation, battery storage, and home energy usage.")

# --- Sidebar toggles ---
st.sidebar.header("⚙️ Simulation Settings")

battery_capacity = st.sidebar.slider("Battery Capacity (kWh)", 0, 20, 10)
battery_efficiency = st.sidebar.slider("Battery Efficiency (%)", 70, 100, 90) / 100

# Feature toggles
enable_cost_analysis = st.sidebar.checkbox("Enable Cost Analysis", True)
enable_demand_response = st.sidebar.checkbox("Enable Demand Response", True)
enable_wind_energy = st.sidebar.checkbox("Enable Wind Energy", True)
enable_battery_degradation = st.sidebar.checkbox("Enable Battery Degradation", True)
enable_weather_variability = st.sidebar.checkbox("Enable Weather Variability", True)
enable_alerts = st.sidebar.checkbox("Enable Alerts", True)
enable_data_export = st.sidebar.checkbox("Enable Data Export", True)

# --- Base profiles ---
hours = np.arange(24)

# Solar profile (24h)
solar_profile = np.array([0]*6 + [2, 3, 4, 5, 5, 5, 4, 3, 2] + [0]*9)

# Wind profile (if enabled, else zeros)
base_wind_profile = np.array([3]*24)  # Constant wind 3 kW baseline
wind_profile = base_wind_profile if enable_wind_energy else np.zeros(24)

# Load profile (24h)
load_profile = np.array([2]*6 + [3]*4 + [4]*6 + [3]*4 + [2]*4)

# Apply demand response if enabled: reduce peak loads by 20% during hours 12-18
if enable_demand_response:
    for h in range(12, 19):
        load_profile[h] *= 0.8

# Apply weather variability (random +/- 20% fluctuations)
if enable_weather_variability:
    solar_profile = solar_profile * (1 + 0.2 * (np.random.rand(24)*2 - 1))
    wind_profile = wind_profile * (1 + 0.2 * (np.random.rand(24)*2 - 1))
    solar_profile = np.clip(solar_profile, 0, None)
    wind_profile = np.clip(wind_profile, 0, None)

battery_level = 0
battery_storage = []
grid_usage = []
alerts = []

# For battery degradation, define simple capacity fade per cycle
battery_cycles = 0
degradation_rate_per_cycle = 0.001  # 0.1% per cycle

# Cost parameters (example)
cost_grid_kwh = 0.15  # $0.15 per kWh from grid
cost_wind = 0.05      # $0.05 per kWh from wind (maintenance)
cost_solar = 0.02     # $0.02 per kWh (maintenance)

total_cost = 0

for hour in range(24):
    solar = solar_profile[hour]
    wind = wind_profile[hour]
    load = load_profile[hour]

    generation = solar + wind
    net_energy = generation - load

    # Battery degradation reduces capacity gradually
    if enable_battery_degradation and battery_cycles > 0:
        battery_capacity *= (1 - degradation_rate_per_cycle * battery_cycles)
        battery_capacity = max(battery_capacity, 0)  # Prevent negative

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

    # Count a cycle if battery charges and discharges within the hour (approximation)
    if enable_battery_degradation and net_energy < 0 and battery_level < battery_capacity:
        battery_cycles += 1

    battery_storage.append(battery_level)
    grid_usage.append(grid)

    # Cost calculation
    if enable_cost_analysis:
        # Cost from grid usage + maintenance costs from solar & wind generation
        cost_this_hour = grid * cost_grid_kwh + solar * cost_solar + wind * cost_wind
        total_cost += cost_this_hour

    # Alerts
    if enable_alerts:
        if battery_level < 0.1 * battery_capacity:
            alerts.append(f"Warning: Low battery at hour {hour}")
        if grid > 0.8 * max(load_profile):
            alerts.append(f"Alert: High grid usage at hour {hour}")

# --- Plotting ---
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(hours, solar_profile, label="☀️ Solar Generation (kW)")
if enable_wind_energy:
    ax.plot(hours, wind_profile, label="💨 Wind Generation (kW)")
ax.plot(hours, load_profile, label="🏠 Load Demand (kW)")
ax.plot(hours, battery_storage, label="🔋 Battery Level (kWh)")
ax.plot(hours, grid_usage, label="⚡ Grid Usage (kW)")

ax.set_xlabel("Hour of Day")
ax.set_ylabel("Energy / Power")
ax.set_title("Microgrid Simulation Over 24 Hours")
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Show alerts if any
if enable_alerts and alerts:
    st.warning("\n".join(set(alerts)))  # Show unique alerts only

# Show cost summary
if enable_cost_analysis:
    st.write(f"💰 **Total estimated cost:** ${total_cost:.2f}")

# Data export
if enable_data_export:
    df = pd.DataFrame({
        "Hour": hours,
        "Solar Generation (kW)": solar_profile,
        "Wind Generation (kW)": wind_profile,
        "Load Demand (kW)": load_profile,
        "Battery Level (kWh)": battery_storage,
        "Grid Usage (kW)": grid_usage,
    })
    csv = df.to_csv(index=False)
    st.download_button("📥 Download Simulation Data as CSV", csv, "microgrid_simulation.csv", "text/csv")

st.success("✅ Simulation complete!")
