import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache
def load_data(path):
    data = pd.read_csv(path, sep=";")
    return data

def barPlot():
    a4_dims = (14, 8.27)
    fig, ax = plt.subplots(figsize=a4_dims)
    sns.set(font_scale=0.7)
    sns.barplot(x = "Tahun", y = "Real Estate", hue = "Keterangan", data = df, ax=ax).set(ylabel='Real Estate(%)')
    st.pyplot(fig)

def linePlot(y):
    a4_dims = (14, 8.27)
    fig, ax = plt.subplots(figsize=a4_dims)
    sns.set(font_scale=0.7)
    sns.lineplot(x = "Tahun", y = y, data=df_line, hue="KETERANGAN", ax=ax).set(ylabel='Presentase(%)')
    st.pyplot(fig)

st.markdown("<h3 style='text-align: center; color: grey;'>Capstone Project TETRIS PROA</h3>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: blue;'>Potensi Lapangan Usaha Real Estate di Indonesia\n</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: grey;'></h3>", unsafe_allow_html=True)

st.markdown("<h6 style='text-align: justify;'>Real estat adalah properti berupa tanah secara fisik dan bangunan yang ada di atasnya. Usaha Real Estat menurut Klasifikasi Baku Lapangan Usaha Indonesia (KBLI) 2020 mencakup kegiatan orang yang menyewakan, agen dan atau broker/perantara dalam penjualan atau pembelian real estat, penyewaan real estat dan penyediaan jasa real estat lainnya, seperti jasa penaksir real estat atau bertindak sebagai agen pemegang wasiat real estat. Kegiatan dalam kategori ini bisa dilakukan atas milik sendiri atau milik orang lain yang disewa dan bisa dilakukan atas dasar balas jasa atau kontrak. Menurut data dari BPS yang ditunjukkan pada chart di bawah ini, distribusi dan laju pertumbuhan dari usaha real estat berbanding lurus dari tahun ke tahun. (Kalo bisa jelasin pake angka juga)</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: justify;'>Berdasarkan data dari BPS yang ditampilkan dalam bentuk chart di bawah ini, terjadi ketimpangan antara jumlah distribusi dengan laju pertumbuhan dari sektor real estat. Laju pertumbuhan mencapai 7,68% pada tahun 2011 dan menurun di tahun-tahun berikutnya hingga sempat mencapai 3,48% di tahun 2018. Namun pada tahun 2019, laju pertumbuhan real estat ini sempat naik mencapai 5,76% dan kembali turun di tahun 2020. Setelah mengalami kenaikan dari tahun sebelumnya di tahun 2021, alangkah baiknya memanfaatkan kesempatan ini untuk terus meningkatkan laju pertumbuhan dari sektor real estate. Hal tersebut dikarenakan jika dilihat baik dari distribusi maupun laju pertumbuhannya, sektor real estate ini masih tergolong rendah dengan presentase dibawah 10% dari seluruh sektor yang ada. Selain itu, seiring dengan bertambahnya penduduk, kebutuhan akan real estat juga meningkat. Maka dari itu, sektor real estat ini sangat berpotensi untuk menjadi lapangan usaha yang produktif.</h6>", unsafe_allow_html=True)

RE_data = load_data('source/Distribusi dan Laju Pertumbuhan Real Estate.csv')
df = pd.DataFrame(RE_data)
barPlot()

st.markdown("<h5 style='text-align: justify; color: green;'>Kemudian dari banyaknya provinsi di Indonesia, kira-kira pulau manakah yang berpotensi tinggi untuk meningkatkan sektor real estat ini?</h5>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: justify;'>Berdasarkan perbandingan distribusi dan laju pertumbuhan dari provinsi-provinsi di Indonesia, dapat dilihat bahwa terdapat beberapa provinsi yang memiliki laju pertumbuhan lebih sedikit dibandingkan dengan jumlah distribusi seperti Riau, Jawa Barat, Jawa Tengah, Jawa Timur, dan Kalimantan Timur. Provinsi-provinsi tersebut meiliki potensi untuk dapat dikembangkan lagi agar laju pertumbuhannya semakin meningkat.</h3>", unsafe_allow_html=True)

Prov_data = load_data('source/distribusi_dan_laju_provinsi.csv')
df_line = pd.DataFrame(Prov_data)
option = st.selectbox('Pilih provinsi yang akan di cek distribusi dan laju pertumbuhannya:', ("ACEH", "SUMATERA UTARA", "SUMATERA BARAT", "RIAU", "JAMBI", "SUMATERA SELATAN", "BENGKULU", "LAMPUNG", "KEP. BANGKA BELITUNG", "KEP. RIAU", "DKI JAKARTA","JAWA BARAT", "JAWA TENGAH", "DI YOGYAKARTA", "JAWA TIMUR", "BANTEN", "BALI", "NUSA TENGGARA BARAT", "NUSA TENGGARA TIMUR", "KALIMANTAN BARAT", "KALIMANTAN TENGAH", "KALIMANTAN SELATAN", "KALIMANTAN TIMUR", "KALIMANTAN UTARA", "SULAWESI UTARA", "SULAWESI TENGAH", "SULAWESI SELATAN", "SULAWESI TENGGARA", "GORONTALO", "SULAWESI BARAT", "MALUKU", "MALUKU UTARA", "PAPUA BARAT", "PAPUA"))
linePlot(option)

st.markdown("<h6 style='text-align: justify;'>Berdasarkan data-data yang telah disebutkan sebelumnya, dapat disimpulkan bahwa sektor lapangan usaha real estat memiliki potensi yang besar untuk dapat dikembangkan lagi terutama di beberapa provinsi yang masih memiliki laju pertumbuhan lebih sedikir dibandingkan dengan jumlah distribusinya. Saran untuk masyarakat Indonesia yang masih mencari lapangan kerja dapat mencoba mempelajari sektor usaha real estat karena sektor ini memiliki potensi yang besar untuk dikembangkan kedepannya.</h3>", unsafe_allow_html=True)

bps = "https://www.bps.go.id/"
kbli = "https://oss.go.id/informasi/kbli-kode?kode=L"
ojk = "https://www.ojk.go.id/id/kanal/pasar-modal/regulasi/peraturan-ojk/Documents/Pages/POJK-Nomor-18.POJK.04.2016/SAL%20-%20POJK%20DIRE.pdf"

# st.markdown("<h6 style='text-align: justify;'>Referensi [link]</h6>")
# st.markdown("<h6 style='text-align: justify;'>1. [BPS](%s)</h6>" % bps, unsafe_allow_html=True)
# st.markdown("<h6 style='text-align: justify;'>1. [KBLI](%s)</h6>" % kbli, unsafe_allow_html=True)
# st.markdown("<h6 style='text-align: justify;'>1. [OJK](%s)</h6>" % ojk, unsafe_allow_html=True)

st.markdown("<h6 style='text-align: justify;'>\nReferensi:</h6>", unsafe_allow_html=True)
st.write("1. [BPS](%s)\n" % bps , "2. [KBLI](%s)\n" % kbli, "3. [OJK](%s)\n" % ojk)
