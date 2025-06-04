# 🔋 Microgrid Simulator Web App

A smart, browser-based microgrid simulation tool that models solar generation, battery storage, home energy usage, and grid demand across a 24-hour period.

Built with **Python**, **Streamlit**, and **Matplotlib**, this app helps users understand energy flow in a modern home or small-scale microgrid environment.

---

## 🌟 Features

- 🧠 Simulates a full 24-hour energy cycle
- ☀️ Solar generation modeled by time of day
- 🔋 Battery with customizable capacity & efficiency
- ⚡ Grid usage shown when demand exceeds generation
- 📊 Visual output with interactive graphs
- 🛠 Optional toggles: EV charging, smart appliances, and more (coming soon)

---

## 🖥 Try the App

👉 [Click here to launch the live demo](https://YOUR_STREAMLIT_APP_URL_HERE)

> *Note: Limited free usage for demo purposes only. Reach out for custom access or API integrations.*

---

## ⚙️ How It Works

The app runs an hourly simulation:
- Compares solar production vs. home energy load
- Charges or discharges the battery based on surplus/deficit
- Pulls from the grid only if battery is empty

Energy trends are plotted for clarity and decision-making.

---

## 🚀 Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Matplotlib](https://matplotlib.org/)
- [NumPy](https://numpy.org/)

---

## 📦 Installation (For Developers)

```bash
git clone https://github.com/yourusername/microgrid-sim.git
cd microgrid-sim
pip install -r requirements.txt
streamlit run app.py
