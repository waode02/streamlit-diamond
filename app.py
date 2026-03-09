import streamlit as st
import pickle
import numpy as np
import joblib
import pandas as pd

st.set_page_config(page_title="💎 Diamond Price Predictor", layout="centered")

st.title("💎 Diamond Price Predictor")
st.caption("Prediksi harga berlian menggunakan model XGBoost")
st.divider()

# Load model
@st.cache_resource
def load_model():
    with open("best_diamond_model.pkl", "rb") as f:
        return pickle.load(f)

# Load feature columns
@st.cache_resource
def load_features():
    return joblib.load("feature_columns.pkl")

model = load_model()
feature_columns = load_features()

# Encoding
CUT_MAP     = {"Fair": 0, "Good": 1, "Very Good": 2, "Premium": 3, "Ideal": 4}
COLOR_MAP   = {"J": 0, "I": 1, "H": 2, "G": 3, "F": 4, "E": 5, "D": 6}
CLARITY_MAP = {"I1": 0, "SI2": 1, "SI1": 2, "VS2": 3, "VS1": 4, "VVS2": 5, "VVS1": 6, "IF": 7}

# Input
st.subheader("⚖️ Berat & Dimensi")
col1, col2, col3 = st.columns(3)
carat = col1.number_input("Carat", 0.1, 6.0, 1.0, 0.01)
depth = col2.number_input("Depth (%)", 40.0, 80.0, 61.5, 0.1)
table = col3.number_input("Table (%)", 40.0, 100.0, 57.0, 0.5)

col4, col5, col6 = st.columns(3)
x = col4.number_input("X - Panjang (mm)", 0.1, 15.0, 6.4, 0.01)
y = col5.number_input("Y - Lebar (mm)", 0.1, 15.0, 6.4, 0.01)
z = col6.number_input("Z - Tinggi (mm)", 0.1, 10.0, 4.0, 0.01)

st.subheader("🏅 Grading 4C")
col7, col8, col9 = st.columns(3)
cut     = col7.selectbox("Cut", list(CUT_MAP.keys()), index=4)
color   = col8.selectbox("Color", list(COLOR_MAP.keys()), index=3)
clarity = col9.selectbox("Clarity", list(CLARITY_MAP.keys()), index=3)

st.divider()

st.markdown("""
<style>
div.stButton > button { background-color: #1a73e8 !important; color: white !important; border: none; }
div.stButton > button:hover { background-color: #1558b0 !important; }
</style>
""", unsafe_allow_html=True)

# Predict
if st.button("🔍 Prediksi Harga", use_container_width=True):

    input_data = {
        "carat": carat,
        "cut": CUT_MAP[cut],
        "color": COLOR_MAP[color],
        "clarity": CLARITY_MAP[clarity],
        "depth": depth,
        "table": table,
        "x": x,
        "y": y,
        "z": z
    }

    df = pd.DataFrame([input_data])

    # samakan urutan kolom dengan training
    df = df.reindex(columns=feature_columns, fill_value=0)

    price = model.predict(df)[0]

    st.markdown(f"### 💰 Estimasi Harga: **${price:,.0f}**")
    st.caption(f"{carat}ct · {cut} · Color {color} · {clarity} · {x}×{y}×{z} mm")