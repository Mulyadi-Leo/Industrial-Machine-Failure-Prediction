import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns

def visualisasi_project():
    # --- 1. Load dataset ---
    # Ganti 'your_dataset.csv' dengan path file lokalmu
    df = pd.read_csv('dataset.csv')

    # --- 2. Ambil kolom yang dibutuhkan ---
    # Ganti nama kolom sesuai dengan nama di dataset asli
    required_columns = ['Billing Amount', 'Insurance Provider', 'Medical Condition']
    data = df[required_columns].copy()

    # Optional: Bersihkan missing value jika ada
    data.dropna(subset=required_columns, inplace=True)

    # # --- 3. Sidebar Filter ---
    # # st.sidebar.title("🔍 Filter")
    # selected_condition = st.sidebar.selectbox("Pilih Jenis Penyakit:", data['Medical Condition'].unique())

    # # --- 4. Filter data sesuai pilihan ---
    # filtered_data = data[data['Medical Condition'] == selected_condition]

    # # --- 5. Hitung rata-rata biaya berdasarkan asuransi ---
    # grouped_data = filtered_data.groupby('Insurance Provider')['Billing Amount'].mean().reset_index()

    # # --- 6. Tampilkan visualisasi ---
    # st.title("📊 Rata-rata Biaya Berdasarkan Asuransi dan Jenis Penyakit")
    # st.subheader(f"Jenis Penyakit: {selected_condition}")

    # chart = alt.Chart(grouped_data).mark_bar().encode(
    #     x='Insurance Provider',
    #     y='Billing Amount',
    #     # y=alt.Y('Billing Amount', scale=alt.Scale(domain=(20000, grouped_data['Billing Amount'].max()))),
    #     tooltip=['Insurance Provider', 'Billing Amount']
    # ).properties(
    #     width=600,
    #     height=400
    # )

    # st.altair_chart(chart, use_container_width=True)
    
    # Sidebar filter
    # st.sidebar.title("🔎 Filter Data")
    # selected_condition = st.sidebar.selectbox(
    #     "Pilih Jenis Penyakit (Medical Condition):",
    #     options=sorted(data['Medical Condition'].unique())
    # )

    # # Filter data berdasarkan kondisi yang dipilih
    # filtered_data = data[data['Medical Condition'] == selected_condition]

    # # Hitung rata-rata Billing Amount per Insurance Provider
    # grouped_data = (
    #     filtered_data.groupby('Insurance Provider')['Billing Amount']
    #     .mean()
    #     .reset_index()
    #     .sort_values(by='Billing Amount', ascending=False)
    # )

    # # Visualisasi
    # chart = alt.Chart(grouped_data).mark_bar().encode(
    #     x=alt.X('Insurance Provider', sort='-y'),
    #     y=alt.Y('Billing Amount',
    #         title='Rata-rata Biaya Ditanggung',
    #         scale=alt.Scale(domain=[25000, 26000])),
    #     # y=alt.Y('Billing Amount', title='Rata-rata Biaya Ditanggung'),
    #     tooltip=['Insurance Provider', 'Billing Amount']
    # ).properties(
    #     title=f"Rata-rata Biaya Ditanggung per Asuransi untuk Penyakit '{selected_condition}'",
    #     width=700,
    #     height=400
    # )

    # # Tampilkan di Streamlit
    # st.title("📊 Visualisasi Biaya Ditanggung Asuransi")
    # st.altair_chart(chart, use_container_width=True)

    medical_condition = st.selectbox(
        'Pilih Kondisi Medis:',
        sorted(data['Medical Condition'].unique().tolist())
    )

    # Filter data berdasarkan kondisi medis
    data_filtered = data[data['Medical Condition'] == medical_condition]

    # 5. Hitung frekuensi masing-masing jenis asuransi berdasarkan kondisi medis yang dipilih
    insurance_counts = data_filtered['Insurance Provider'].value_counts()

    # if insurance_counts.empty:
    #     st.write("Tidak ada data yang sesuai dengan kondisi medis yang dipilih.")
    # else:
    #     # 6. Visualisasi: Grafik batang (bar chart)
    #     plt.figure(figsize=(10, 6))
    #     sns.barplot(x=insurance_counts.index, y=insurance_counts.values, palette='viridis')

    #     plt.ylim(bottom=1700)

    #     # Menambahkan label dan judul
    #     plt.title(f'Frekuensi Penggunaan Asuransi untuk Kondisi Medis: {medical_condition}', fontsize=16)
    #     plt.xlabel('Provider Asuransi', fontsize=12)
    #     plt.ylabel('Jumlah Penggunaan', fontsize=12)

    #     # Putar label pada sumbu X agar lebih mudah dibaca
    #     plt.xticks(rotation=45, ha='right')

    #     # Tampilkan grafik
    #     st.pyplot(plt)

    if insurance_counts.empty:
        st.write("Tidak ada data yang sesuai dengan kondisi medis yang dipilih.")
    else:
        # Tampilkan nama asuransi yang paling sering digunakan
        top_insurance = insurance_counts.idxmax()
        top_count = insurance_counts.max()
        st.success(f"🔎 Provider asuransi yang paling sering digunakan untuk kondisi **{medical_condition}** adalah **{top_insurance}** sebanyak **{top_count}** kali.")

        # Visualisasi: Grafik batang (bar chart)
        plt.figure(figsize=(10, 6))
        ax = sns.barplot(x=insurance_counts.index, y=insurance_counts.values, palette='viridis')

        # Menambahkan label jumlah di atas tiap batang
        for i, v in enumerate(insurance_counts.values):
            ax.text(i, v + 50, str(v), color='black', ha='center', fontweight='bold')

        # Hilangkan sumbu Y
        ax.get_yaxis().set_visible(False)

        plt.ylim(bottom=1700)

        # Menambahkan label dan judul
        plt.title(f'Frekuensi Penggunaan Asuransi untuk Kondisi Medis: {medical_condition}', fontsize=16)
        plt.xlabel('Provider Asuransi', fontsize=12)
        plt.ylabel('')
        plt.xticks(rotation=45, ha='right')

        # Tampilkan grafik
        st.pyplot(plt)