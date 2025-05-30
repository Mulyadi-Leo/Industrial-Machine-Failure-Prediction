import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# —————— Load model & encoder ——————
# Jika kamu punya pipeline lengkap, cukup:
# pipeline = joblib.load('pipeline.pkl')

# Atau load model + encoder terpisah:
model = joblib.load('model.joblib')
encoder = joblib.load('encoder.pkl')  
# encoder.classes_ berisi daftar semua machine_type

# # —————— UI ——————
# st.title("Industrial Machine Failure Prediction")

# st.markdown(
#     """
#     Masukkan detail mesin untuk memprediksi kemungkinan **Gagal** atau **Tidak**.
#     """
# )

# Dinamis: ambil daftar machine_type dari encoder
df = pd.read_csv('dataset.csv')

machine_types = list(encoder.classes_)
machine_type = st.selectbox("Machine Type", machine_types)

installation_year     = st.number_input("Installation Year", min_value=2000, max_value=2025, step=1)
oil_level             = st.slider("Oil Level", 0.0, 1.0, step=0.01)
coolant_level         = st.slider("Coolant Level", 0.0, 1.0, step=0.01)
power_consumption     = st.number_input("Power Consumption (kW)", value=500.0)
last_maintenance_days = st.number_input("Days Since Last Maintenance", min_value=0)

if st.button("Predict Failure"):
    # —————— Siapkan DataFrame input ——————
    input_df = pd.DataFrame([{
        'installation_year': installation_year,
        'oil_level': oil_level,
        'coolant_level': coolant_level,
        'power_consumption': power_consumption,
        'last_maintenance_days': last_maintenance_days,
    }])

    # —————— Encode machine_type ——————
    # Jika pakai LabelEncoder:
    encoded = encoder.transform([machine_type])  
    input_df['machine_type'] = encoded

    # Jika pakai pipeline:
    # input_df['machine_type'] = machine_type
    # preds = pipeline.predict(input_df)

    # —————— Predict & Tampilkan ——————
    pred = model.predict(input_df)[0]
    label = "Gagal" if pred == 1 else "Tidak Gagal"
    st.success(f"Hasil Prediksi: **{label}**")