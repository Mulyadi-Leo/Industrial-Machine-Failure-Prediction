import streamlit as st
import pandas as pd
import joblib

# --- Load model dan encoder ---
@st.cache_resource
def load_model():
    model = joblib.load("model.joblib")
    encoder = joblib.load("encoder_machine_type.pkl")
    return model, encoder

model, encoder = load_model()

# --- Judul aplikasi ---
st.title("Prediksi Kegagalan Mesin dalam 7 Hari")

st.write("""
Masukkan nilai untuk 6 fitur berikut, kemudian klik **Prediksi**  
(Model Random Forest versi 4)
""")

# --- Input pengguna ---
# 1. Machine_Type (kategori)
machine_types = encoder.classes_.tolist()  # daftar kategori hasil fitting encoder
machine_input = st.selectbox("1. Tipe Mesin (Machine_Type)", machine_types)

# 2. Installation_Year
year_input = st.number_input("2. Tahun Instalasi (Installation_Year)",
                             min_value=1900, max_value=2100, value=2020, step=1)

# 3. Oil Level (%) -- ganti nama sesuai pada model Anda
oil_input = st.number_input("3. Level Oli (%)",
                            min_value=0.0, max_value=100.0, value=50.0, step=0.1)

coolant_input = st.number_input("3. Level Coolant (%)",
                            min_value=0.0, max_value=100.0, value=50.0, step=0.1)

# 4. Power Consumption (kW)
power_input = st.number_input("4. Konsumsi Daya (kW)",
                              min_value=0.0, value=10.0, step=0.1)

# 5. Last Maintenance (hari lalu)
maint_input = st.number_input("5. Hari Sejak Perawatan Terakhir",
                              min_value=0, value=30, step=1)

# --- Prediksi ---
if st.button("Prediksi"):
    # Buat DataFrame 1 baris dengan urutan kolom sesuai feature_4
    df = pd.DataFrame({
        "Machine_Type": [machine_input],
        "Installation_Year": [year_input],
        "Oil_Level_pct": [oil_input],
        "Coolant_Level_pct": [coolant_input],
        "Power_Consumption_kW": [power_input],
        "Last_Maintenance_Days_Ago": [maint_input],
    })

    # Encode kolom kategori
    df["Machine_Type"] = encoder.transform(df["Machine_Type"])

    # Pastikan urutan kolom sesuai yang dipakai model
    X = df[["Machine_Type",
            "Installation_Year",
            "Oil_Level_pct",
            "Coolant_Level_pct",
            "Power_Consumption_kW",
            "Last_Maintenance_Days_Ago",
           ]]

    # Lakukan prediksi
    y_pred = model.predict(X)[0]
    proba = model.predict_proba(X)[0]

    label = "Gagal" if y_pred == 1 else "Sukses"

    st.write(f"### Hasil Prediksi: **{label}**")
