import streamlit as st
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np
import pycountry

st.set_page_config(page_title="Quantum Farming & Bio-Economy", layout="wide")

st.title("🌾 Quantum Farming and Bio-Economy Simulator")
st.markdown("An interactive platform blending quantum simulations with real-time agri-policy visualizations")

# Global synthetic time axis
years = np.arange(2020, 2051)

# Sample synthetic annotations
annotations = [
    dict(x=2030, y=2 + 0.05*(2030-2020), text='Policy Overhaul', showarrow=True, arrowhead=2),
    dict(x=2040, y=2 + 0.05*(2040-2020), text='Global Market Shock', showarrow=True, arrowhead=2)
]

# Sample survey processing
def process_farmer_surveys(surveys):
    sentiment_scores = [np.random.uniform(0.8, 1.2) for _ in surveys]
    return np.mean(sentiment_scores)

sample_surveys = [
    "Subsidy cuts are hurting our production.",
    "Dairy yields are steady, but weather remains unpredictable.",
    "We need more support for sustainable practices.",
    "Market conditions are volatile."
]

survey_sentiment_index = process_farmer_surveys(sample_surveys)
st.metric("Farmer Sentiment Index", f"{survey_sentiment_index:.2f}", delta=None)

# Simulate a quantum-influenced agricultural growth curve
base_growth = 2 + 0.05 * (years - 2020) * np.random.normal(1, 0.05, len(years))
fig = go.Figure()
fig.add_trace(go.Scatter(x=years, y=base_growth, mode='lines+markers', name='Simulated Yield'))
fig.update_layout(title="Projected Agri-Yield under Quantum Simulation",
                  xaxis_title="Year",
                  yaxis_title="Yield Index",
                  annotations=annotations)

st.plotly_chart(fig, use_container_width=True)

# Country dropdown (Europe only)
european_countries = [c.alpha_2 for c in pycountry.countries if c.alpha_2 in [
    'AT','BE','BG','HR','CY','CZ','DK','EE','FI','FR','DE','GR','HU','IE','IT','LV','LT','LU','MT','NL','PL','PT','RO','SK','SI','ES','SE'
]]

selected_country = st.sidebar.selectbox("Select Country for Policy Intervention", european_countries)
st.sidebar.write(f"Selected: {selected_country}")

# Upload your CSV (optional real dataset)
uploaded_file = st.sidebar.file_uploader("Upload your agri-data CSV", type=["csv", "xlsx"])
if uploaded_file:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
    st.subheader("📂 Uploaded Dataset Preview")
    st.dataframe(df.head())

# Summary
st.success("Simulation Complete. Customize this app to integrate with real-time farm data, remote sensors, or policy triggers.")
