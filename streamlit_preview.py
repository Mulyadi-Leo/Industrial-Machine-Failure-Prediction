import streamlit as st
from PIL import Image

# Sidebar untuk navigasi
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman:", ["Introduction", "Project", "Contact"])

# Halaman Awal
if page == "Introduction":
    

    col_kiri, col_kanan = st.columns([2, 3])  # 40% dan 60%

    # === Kolom Kiri ===
    with col_kiri:
        st.image("gambar/mul.png",caption="Data Scientist", use_container_width=True)
       

    # === Kolom Kanan ===
    with col_kanan:
        col_atas, col_bawah = st.columns([1, 0.25])  # Trik layout agar terlihat vertikal proporsional

        # Perkenalan diri (bagian atas)
        with st.container():
            st.markdown("### Call me Mulyadi")
            st.write("""
        I’m a <span style="color: #FF5733; font-weight: bold;">Data Scientist</span> with expertise in data accuracy, validation, and exploratory data analysis (EDA). 
        I specialize in managing large datasets, creating data visualizations, and building dashboards to drive business insights. 
        Check out my <span style="color: #FF5733; font-weight: bold;">projects</span> in the navigation to see how I deliver data-driven solutions using tools like Google Colab, PostgreSQL, and Power BI.
        """, unsafe_allow_html=True)

        st.markdown("---") 

        # Baris bawah (3 gambar kecil)
        col1, col2, col3 = st.columns(3)

        # Buka dan resize gambar
        img1 = Image.open("gambar/colab.png").resize((150, 150))
        img2 = Image.open("gambar/postgre.png").resize((150, 150))
        img3 = Image.open("gambar/powerbi.png").resize((150, 150))

        with col1:
            st.image(img1, use_container_width=True)
        with col2:
            st.image(img2, use_container_width=True)
        with col3:
            st.image(img3, use_container_width=True)

# Halaman List Barang
elif page == "Project":

    # Bagian atas (gambar banner + caption)
    with st.container():
        st.markdown('<div class="top-container">', unsafe_allow_html=True)
        # Menampilkan gambar banner
        img = Image.open("gambar/machine.png")
        img_resized = img.resize((1000, 400))  # Resize to width=1000, height=300

        st.image(img_resized)
        st.markdown('</div>', unsafe_allow_html=True)

        st.header("Industrial Machine Failure Prediction")
        st.write("A machine learning project to predict industrial machine failures, aiming to prevent downtime, reduce maintenance costs, and improve efficiency. " \
        "Includes data balancing, cross-validation, feature importance analysis, and model evaluation")

    # Bagian bawah (dinamis)
    with st.container():
        import project
        project . visualisasi_project()

# Halaman Alamat
elif page == "Alamat":
    st.title("Alamat Toko")
    st.write("Toko Elektronik Cerdas")
    st.write("Jl. Teknologi No. 123, Jakarta Selatan")
    st.write("Email: info@tokocerdas.com")
    st.write("Telepon: (021) 123-4567")