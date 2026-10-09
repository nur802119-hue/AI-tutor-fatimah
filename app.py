import streamlit as st
import os
import re
import base64
from datetime import datetime
from collections import Counter

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================
st.set_page_config(
    page_title="Bahasa Indonesia Kelas IX",
    page_icon="📚",
    layout="wide"
)


# =========================================================
# ANIMASI DAN ELEMEN BERGERAK
# =========================================================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(-45deg, #EAF7FF, #FFF7E8, #EEFCEB, #F6EEFF);
    background-size: 400% 400%;
    animation: backgroundMove 14s ease infinite;
}
@keyframes backgroundMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.animated-card {
    animation: floatCard 4s ease-in-out infinite;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.animated-card:hover {
    transform: translateY(-7px) scale(1.02);
}
@keyframes floatCard {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-6px); }
}
.floating-emoji {
    display: inline-block;
    font-size: 42px;
    animation: floatEmoji 3s ease-in-out infinite;
}
.floating-emoji.delay1 { animation-delay: 0.7s; }
.floating-emoji.delay2 { animation-delay: 1.4s; }
@keyframes floatEmoji {
    0%, 100% { transform: translateY(0) rotate(-3deg); }
    50% { transform: translateY(-13px) rotate(3deg); }
}
.hero-title {
    animation: titleIn 1s ease-out;
}
@keyframes titleIn {
    from { opacity: 0; transform: translateY(-18px); }
    to { opacity: 1; transform: translateY(0); }
}
.stButton > button {
    transition: all 0.25s ease;
}
.stButton > button:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 8px 18px rgba(0,0,0,0.12);
}
section[data-testid="stSidebar"] .stRadio label {
    transition: transform 0.2s ease;
}
section[data-testid="stSidebar"] .stRadio label:hover {
    transform: translateX(5px);
}
.school-hero {
    background: linear-gradient(135deg, rgba(255,255,255,.96), rgba(232,247,255,.94));
    border: 1px solid rgba(70,130,180,.18);
    border-radius: 24px;
    padding: 22px;
    margin: 10px 0 22px 0;
    box-shadow: 0 12px 30px rgba(50,90,120,.10);
    animation: titleIn .8s ease-out;
}
.visual-card {
    border-radius: 20px;
    padding: 12px;
    background: rgba(255,255,255,.86);
    border: 1px solid rgba(100,120,150,.15);
    box-shadow: 0 8px 22px rgba(50,70,100,.08);
    transition: transform .25s ease, box-shadow .25s ease;
}
.visual-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 14px 28px rgba(50,70,100,.14);
}
.level-card {
    border-radius: 18px;
    padding: 16px;
    margin: 8px 0;
    background: rgba(255,255,255,.88);
    border: 1px solid rgba(70,100,140,.15);
    box-shadow: 0 7px 18px rgba(50,70,100,.07);
}
.material-card {
    border-radius: 18px;
    padding: 16px;
    background: rgba(255,255,255,.90);
    border: 1px solid rgba(70,100,140,.14);
    margin-bottom: 12px;
    transition: transform .25s ease, box-shadow .25s ease;
}
.material-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 25px rgba(50,70,100,.12);
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# TEMA VISUAL CERIA UNTUK SISWA SMP KELAS 9
# =========================================================

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 6% 9%, rgba(255, 213, 128, .58) 0 5%, transparent 17%),
        radial-gradient(circle at 94% 14%, rgba(151, 219, 255, .60) 0 6%, transparent 19%),
        radial-gradient(circle at 12% 88%, rgba(210, 181, 255, .42) 0 7%, transparent 21%),
        radial-gradient(circle at 88% 83%, rgba(164, 243, 208, .42) 0 6%, transparent 20%),
        linear-gradient(-45deg, #f8fbff 0%, #fff5e9 35%, #f1f7ff 68%, #f7efff 100%);
    background-size: 150% 150%;
    animation: backgroundMove 18s ease-in-out infinite;
}
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #fff7d6 0%, #eef8ff 55%, #f5edff 100%);
    border-right: 2px solid rgba(99, 102, 241, .12);
}
h1 { color: #4338ca !important; font-weight: 800 !important; letter-spacing: -.5px; }
h2, h3 { color: #334155 !important; }
p, label, .stMarkdown { color: #334155; }
div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 20px !important;
    border: 1px solid rgba(99, 102, 241, .12) !important;
    box-shadow: 0 8px 24px rgba(30, 41, 59, .07) !important;
    background: rgba(255,255,255,.82) !important;
}
.stButton > button {
    border-radius: 14px !important; border: 0 !important; min-height: 46px;
    font-weight: 750 !important; background: linear-gradient(90deg, #6366f1, #8b5cf6) !important;
    color: white !important; box-shadow: 0 7px 16px rgba(99,102,241,.24);
}
.stButton > button:hover { transform: translateY(-2px); box-shadow: 0 10px 20px rgba(99,102,241,.32); }
div[data-baseweb="select"] > div, textarea, input { border-radius: 13px !important; }
textarea { background: rgba(255,255,255,.9) !important; }
div[role="radiogroup"] { background: rgba(255,255,255,.55); border-radius: 14px; padding: 8px 12px; }
.study-banner {
    padding: 22px 26px; border-radius: 24px; margin: 4px 0 20px 0;
    background: linear-gradient(110deg, rgba(255,255,255,.94), rgba(239,246,255,.94));
    border: 2px solid rgba(99,102,241,.10); box-shadow: 0 10px 30px rgba(30,41,59,.08);
}
.study-banner .title { font-size: 1.75rem; font-weight: 850; color: #4338ca; }
.study-banner .subtitle { margin-top: 5px; color: #475569; }
.edu-icons { font-size: 1.55rem; letter-spacing: 9px; margin-bottom: 5px; }
div[data-testid="stAlert"] { border-radius: 14px !important; }
.home-hero {
    position: relative; overflow: hidden; padding: 30px 30px 26px;
    border-radius: 30px; margin: 6px 0 20px;
    background: linear-gradient(125deg, rgba(255,255,255,.97), rgba(237,246,255,.94) 48%, rgba(255,242,221,.96));
    border: 2px solid rgba(255,255,255,.95);
    box-shadow: 0 18px 42px rgba(79,70,229,.13);
    animation: titleIn .8s ease-out;
}
.home-hero:after { content:"✦"; position:absolute; right:25px; top:12px; color:#fbbf24; font-size:50px; transform:rotate(12deg); }
.home-kicker { display:inline-block; background:#ede9fe; color:#5b21b6; padding:7px 13px; border-radius:999px; font-size:.82rem; font-weight:800; }
.home-title { color:#312e81; font-size:clamp(2rem, 4vw, 3.2rem); line-height:1.12; font-weight:900; margin-top:14px; }
.home-subtitle { color:#475569; font-size:1.08rem; margin-top:10px; line-height:1.6; }
.sticker-row { display:flex; flex-wrap:wrap; gap:12px; justify-content:center; margin:15px 0 22px; }
.sticker { display:inline-flex; align-items:center; gap:7px; padding:11px 15px; border-radius:18px; background:rgba(255,255,255,.88); border:2px solid white; box-shadow:0 7px 17px rgba(60,70,120,.10); font-weight:800; color:#475569; animation:floatEmoji 3.8s ease-in-out infinite; }
.sticker:nth-child(2n) { animation-delay:.6s; }
.sticker:nth-child(3n) { animation-delay:1.1s; }
.home-card { height:100%; min-height:145px; padding:20px; border-radius:23px; border:2px solid rgba(255,255,255,.95); box-shadow:0 10px 25px rgba(30,41,59,.08); transition:transform .25s ease, box-shadow .25s ease; }
.home-card:hover { transform:translateY(-6px) rotate(-.5deg); box-shadow:0 16px 30px rgba(30,41,59,.13); }
.home-card .emoji { font-size:2.1rem; }
.home-card h3 { margin:.35rem 0; color:#312e81; }
.home-card p { margin:0; color:#475569; line-height:1.5; }
.home-note { border-radius:20px; padding:16px 20px; background:linear-gradient(90deg,#dcfce7,#dbeafe,#f3e8ff); border:1px solid rgba(255,255,255,.9); color:#334155; font-weight:650; }

.student-hero { display:flex; align-items:center; justify-content:space-between; gap:18px; padding:20px 26px 10px; margin:0 0 20px; border-radius:26px; background:linear-gradient(105deg,#eef2ff 0%,#fff7ed 52%,#ecfeff 100%); border:2px solid rgba(99,102,241,.10); box-shadow:0 12px 30px rgba(30,41,59,.08); overflow:hidden; }
.student-copy { flex:1; min-width:300px; padding:8px 0 16px 4px; }
.mini-badge { display:inline-block; padding:6px 11px; border-radius:999px; background:#ffffff; color:#4f46e5; font-size:.78rem; font-weight:800; box-shadow:0 4px 12px rgba(79,70,229,.10); }
.student-title { margin-top:10px; font-size:1.65rem; font-weight:850; color:#312e81; }
.student-text { margin-top:6px; color:#475569; max-width:560px; line-height:1.55; }
.student-chips { display:flex; gap:8px; flex-wrap:wrap; margin-top:12px; }
.student-chips span { background:rgba(255,255,255,.88); border:1px solid rgba(99,102,241,.10); border-radius:999px; padding:6px 10px; font-weight:700; color:#475569; }
.student-art { width:48%; min-width:430px; }
.student-art svg { width:100%; height:auto; display:block; }
@media (max-width: 900px) { .student-hero { flex-direction:column; align-items:stretch; } .student-art { width:100%; min-width:0; } }
/* Tampilan konsisten untuk seluruh menu pembelajaran */
section[data-testid="stSidebar"] { box-shadow: 8px 0 25px rgba(99,102,241,.07); }
section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3 { color:#5145b8 !important; }
div[data-testid="stTabs"] button[role="tab"] { border-radius:14px 14px 8px 8px; padding:10px 16px; font-weight:750; }
div[data-testid="stTabs"] button[aria-selected="true"] { background:linear-gradient(100deg,#e9e7ff,#e0f2fe); color:#4338ca; }
div[data-testid="stExpander"] { background:rgba(255,255,255,.84); border:1px solid rgba(129,140,248,.22); border-radius:17px; overflow:hidden; }
div[data-testid="stForm"] { background:rgba(255,255,255,.70); border:1px solid rgba(129,140,248,.20); border-radius:22px; padding:18px; }
div[data-testid="stMetric"] { background:linear-gradient(145deg,rgba(255,255,255,.96),rgba(237,242,255,.90)); padding:16px; border:1px solid rgba(129,140,248,.18); border-radius:18px; box-shadow:0 7px 18px rgba(79,70,229,.08); }
div[data-testid="stDataFrame"] { background:rgba(255,255,255,.9); padding:8px; border:1px solid rgba(129,140,248,.18); border-radius:16px; }
.stTextInput input, .stNumberInput input, .stTextArea textarea { background:rgba(255,255,255,.92)!important; border:1px solid #d9d6fe!important; }
.stSelectbox [data-baseweb="select"] > div { background:rgba(255,255,255,.92); }
.stRadio > div, .stCheckbox > label { gap:8px; }
.page-ribbon { position:relative; overflow:hidden; padding:18px 22px; margin:0 0 20px; border-radius:23px; background:linear-gradient(110deg,rgba(255,255,255,.94),rgba(224,242,254,.94) 48%,rgba(243,232,255,.94)); border:2px solid rgba(255,255,255,.96); box-shadow:0 12px 28px rgba(79,70,229,.10); animation:titleIn .65s ease-out; }
.page-ribbon:after { content:'✦  ✧  ✦'; position:absolute; right:18px; top:8px; color:#f4b942; font-size:25px; letter-spacing:5px; }
.page-ribbon-title { font-size:1.42rem; font-weight:900; color:#4338ca; margin-bottom:4px; }
.page-ribbon-text { color:#475569; line-height:1.55; }
.page-stickers { display:flex; gap:8px; flex-wrap:wrap; margin:0 0 18px; }
.page-stickers span { padding:7px 11px; border-radius:14px; background:rgba(255,255,255,.83); border:1px solid rgba(255,255,255,.98); box-shadow:0 4px 12px rgba(71,85,105,.07); font-size:.92rem; animation:floatEmoji 4s ease-in-out infinite; }
.page-stickers span:nth-child(2n) { animation-delay:.5s; }
.page-stickers span:nth-child(3n) { animation-delay:1s; }
.stMarkdown h2, .stMarkdown h3 { letter-spacing:-.2px; }
@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation:none!important; transition:none!important; } }
</style>
""", unsafe_allow_html=True)

# =========================================================
# DESAIN MODERN: NAVY TO CYAN
# =========================================================
st.markdown("""
<style>
:root {
    --navy: #0B1F3A;
    --navy-2: #12345A;
    --blue: #176B9A;
    --cyan: #20C4D8;
    --cyan-soft: #DDF8FC;
    --paper: #F3F8FC;
    --ink: #203247;
    --muted: #60758A;
    --line: #D9E6EF;
}
.stApp {
    background:
        radial-gradient(circle at 90% 0%, rgba(32,196,216,.13), transparent 27%),
        linear-gradient(135deg, #F5F9FC 0%, #EAF3F9 55%, #F7FBFD 100%) !important;
    color: var(--ink);
    background-attachment: fixed;
}
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0B1F3A 0%, #12345A 68%, #14516D 100%) !important;
    border-right: 1px solid rgba(32,196,216,.25) !important;
}
section[data-testid="stSidebar"] * { color: #EAF7FF; }
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #C5D8E8 !important;
}
section[data-testid="stSidebar"] div[role="radiogroup"] {
    background: rgba(255,255,255,.055) !important;
    border: 1px solid rgba(255,255,255,.10);
    border-radius: 16px;
    padding: 8px;
}
section[data-testid="stSidebar"] div[role="radiogroup"] label {
    border-radius: 10px;
    padding: 7px 9px;
    transition: background .2s ease, transform .2s ease;
}
section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background: rgba(32,196,216,.14);
    transform: translateX(3px);
}
h1, h2, h3, h4 { color: var(--navy) !important; letter-spacing: -.025em; }
p, label, .stMarkdown { color: var(--ink); }
.stCaption, [data-testid="stCaptionContainer"] { color: var(--muted) !important; }
.stButton > button, div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(105deg, #12345A, #176B9A 62%, #20AFC8) !important;
    color: white !important;
    border: 1px solid rgba(32,196,216,.25) !important;
    border-radius: 12px !important;
    min-height: 44px;
    font-weight: 700 !important;
    box-shadow: 0 7px 18px rgba(11,31,58,.14);
    transition: transform .2s ease, box-shadow .2s ease, filter .2s ease;
}
.stButton > button:hover, div[data-testid="stFormSubmitButton"] button:hover {
    transform: translateY(-2px);
    filter: brightness(1.06);
    box-shadow: 0 11px 24px rgba(11,31,58,.22);
}
.stButton > button:focus, div[data-testid="stFormSubmitButton"] button:focus {
    outline: 2px solid var(--cyan) !important;
    outline-offset: 2px;
}
div[data-baseweb="select"] > div,
.stTextInput input, .stNumberInput input, .stTextArea textarea,
textarea, input {
    border-radius: 11px !important;
    border-color: #C9DCE8 !important;
    background: rgba(255,255,255,.94) !important;
    color: var(--ink) !important;
}
div[data-baseweb="select"] > div:focus-within,
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: var(--cyan) !important;
    box-shadow: 0 0 0 2px rgba(32,196,216,.14) !important;
}
div[data-testid="stVerticalBlockBorderWrapper"],
div[data-testid="stForm"],
div[data-testid="stExpander"],
div[data-testid="stDataFrame"] {
    border: 1px solid var(--line) !important;
    border-radius: 17px !important;
    background: rgba(255,255,255,.88) !important;
    box-shadow: 0 8px 24px rgba(11,31,58,.055) !important;
}
div[data-testid="stMetric"] {
    background: linear-gradient(145deg, #FFFFFF, #EAF8FC) !important;
    border: 1px solid #D5EAF1 !important;
    border-radius: 16px !important;
    padding: 16px;
    box-shadow: 0 7px 18px rgba(11,31,58,.06);
}
div[data-testid="stMetric"] label { color: var(--muted) !important; }
div[data-testid="stMetric"] [data-testid="stMetricValue"] { color: var(--navy) !important; }
div[data-testid="stTabs"] button[role="tab"] {
    border-radius: 10px 10px 5px 5px;
    font-weight: 700;
}
div[data-testid="stTabs"] button[aria-selected="true"] {
    background: var(--cyan-soft) !important;
    color: var(--navy) !important;
    border-bottom: 3px solid var(--cyan) !important;
}
div[data-testid="stAlert"] { border-radius: 13px !important; }
hr { border-color: var(--line) !important; }

/* Hero dan kartu: bersih, modern, tetap responsif */
.home-hero, .student-hero, .study-banner, .page-ribbon, .school-hero {
    background: linear-gradient(120deg, #0B1F3A 0%, #123D64 58%, #087E9A 100%) !important;
    border: 1px solid rgba(32,196,216,.28) !important;
    border-radius: 22px !important;
    box-shadow: 0 16px 34px rgba(11,31,58,.14) !important;
    color: #F4FBFF !important;
    animation: none !important;
}
.home-hero .home-kicker, .mini-badge {
    background: rgba(32,196,216,.16) !important;
    border: 1px solid rgba(32,196,216,.35);
    color: #BDF7FF !important;
}
.home-hero .home-title, .study-banner .title, .page-ribbon-title,
.student-title {
    color: #FFFFFF !important;
}
.home-hero .home-subtitle, .study-banner .subtitle,
.page-ribbon-text, .student-text {
    color: #D5E9F5 !important;
}
.home-hero:after, .page-ribbon:after { color: #7CEAF5 !important; }
.home-card, .visual-card, .level-card, .material-card {
    background: rgba(255,255,255,.94) !important;
    border: 1px solid #D9E7EF !important;
    border-radius: 17px !important;
    box-shadow: 0 8px 22px rgba(11,31,58,.06) !important;
    transition: transform .22s ease, box-shadow .22s ease, border-color .22s ease;
    animation: none !important;
}
.home-card:hover, .visual-card:hover, .material-card:hover {
    transform: translateY(-3px) !important;
    border-color: rgba(32,196,216,.65) !important;
    box-shadow: 0 13px 27px rgba(11,31,58,.11) !important;
}
.home-card h3, .material-card h3, .visual-card h4 { color: var(--navy) !important; }
.home-card p, .material-card p, .visual-card p { color: var(--muted) !important; }
.home-note {
    background: linear-gradient(100deg, #DDF8FC, #EAF3F9) !important;
    border: 1px solid #C8EAF0 !important;
    color: var(--navy) !important;
    border-radius: 15px !important;
}
.sticker-row, .page-stickers { gap: 8px !important; }
.sticker, .page-stickers span {
    background: #FFFFFF !important;
    border: 1px solid var(--line) !important;
    color: #34516A !important;
    border-radius: 10px !important;
    box-shadow: none !important;
    animation: none !important;
}
.floating-emoji { animation: none !important; }
@media (max-width: 760px) {
    .home-hero { padding: 22px !important; }
    .home-hero .home-title { font-size: 2rem !important; }
    .home-card { min-height: 0 !important; }
}
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { animation: none !important; transition: none !important; }
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# KONFIGURASI DATABASE
# =========================================================

FOLDER_DATABASE = "database"


# =========================================================
# FUNGSI MEMBACA DATABASE TXT
# =========================================================

def baca_database():

    data = []

    if not os.path.exists(FOLDER_DATABASE):
        os.makedirs(FOLDER_DATABASE)

    daftar_file = os.listdir(FOLDER_DATABASE)

    for nama_file in daftar_file:

        if nama_file.lower().endswith(".txt"):

            lokasi_file = os.path.join(
                FOLDER_DATABASE,
                nama_file
            )

            try:

                with open(
                    lokasi_file,
                    "r",
                    encoding="utf-8"
                ) as file:

                    isi = file.read()

                data.append({
                    "nama_file": nama_file,
                    "isi": isi
                })

            except Exception as error:

                st.error(
                    f"Gagal membaca {nama_file}: {error}"
                )

    return data


# =========================================================
# MEMBERSIHKAN TEKS
# =========================================================

def bersihkan_teks(teks):

    teks = teks.lower()

    teks = re.sub(
        r"[^a-zA-ZÀ-ÿ0-9\s]",
        " ",
        teks
    )

    teks = re.sub(
        r"\s+",
        " ",
        teks
    )

    return teks.strip()


# =========================================================
# STOPWORDS SEDERHANA
# =========================================================

STOPWORDS = {
    "yang",
    "dan",
    "di",
    "ke",
    "dari",
    "pada",
    "dengan",
    "untuk",
    "dalam",
    "adalah",
    "itu",
    "ini",
    "atau",
    "apa",
    "bagaimana",
    "mengapa",
    "sebutkan",
    "jelaskan",
    "jelaskanlah",
    "tentang",
    "suatu",
    "sebuah",
    "secara",
    "merupakan",
    "dapat",
    "akan",
    "sebagai",
    "oleh",
    "lebih",
    "juga",
    "tidak",
    "tersebut"
}


# =========================================================
# MENGAMBIL KATA KUNCI
# =========================================================

def ambil_kata_kunci(pertanyaan):

    teks = bersihkan_teks(pertanyaan)

    kata = teks.split()

    kata_kunci = []

    for item in kata:

        if len(item) > 2 and item not in STOPWORDS:

            kata_kunci.append(item)

    return kata_kunci


# =========================================================
# SISTEM PENILAIAN RELEVANSI
# =========================================================

def hitung_relevansi(pertanyaan, isi):

    kata_kunci = ambil_kata_kunci(pertanyaan)

    if len(kata_kunci) == 0:
        return 0

    teks_database = bersihkan_teks(isi)

    kata_database = teks_database.split()

    frekuensi = Counter(kata_database)

    skor = 0

    for kata in kata_kunci:

        if kata in frekuensi:

            jumlah = frekuensi[kata]

            if jumlah > 10:
                jumlah = 10

            skor += jumlah

    # Bonus jika frasa pertanyaan muncul
    pertanyaan_bersih = bersihkan_teks(
        pertanyaan
    )

    if pertanyaan_bersih in teks_database:

        skor += 20

    # Bonus jika kata kunci utama terdapat di judul
    baris_awal = teks_database[:500]

    for kata in kata_kunci:

        if kata in baris_awal:

            skor += 5

    return skor


# =========================================================
# MENCARI MATERI
# =========================================================

def cari_materi(pertanyaan, database):

    hasil = []

    for data in database:

        skor = hitung_relevansi(
            pertanyaan,
            data["isi"]
        )

        if skor > 0:

            hasil.append({
                "nama_file": data["nama_file"],
                "isi": data["isi"],
                "skor": skor
            })

    hasil.sort(
        key=lambda x: x["skor"],
        reverse=True
    )

    return hasil


# =========================================================
# MEMBUAT POTONGAN MATERI
# =========================================================

def ambil_potongan_relevan(
    pertanyaan,
    isi,
    jumlah_maksimal=1200
):

    kata_kunci = ambil_kata_kunci(
        pertanyaan
    )

    paragraf = re.split(
        r"\n\s*\n|\r\n",
        isi
    )

    paragraf_relevan = []

    for p in paragraf:

        p_bersih = bersihkan_teks(p)

        skor = 0

        for kata in kata_kunci:

            if kata in p_bersih:

                skor += 1

        if skor > 0:

            paragraf_relevan.append(
                (skor, p.strip())
            )

    paragraf_relevan.sort(
        key=lambda x: x[0],
        reverse=True
    )

    hasil = ""

    for skor, p in paragraf_relevan:

        if len(hasil) + len(p) <= jumlah_maksimal:

            hasil += p + "\n\n"

    if hasil.strip() == "":

        hasil = isi[:jumlah_maksimal]

    return hasil.strip()


# =========================================================
# LOAD DATABASE
# =========================================================

database = baca_database()

# Menyimpan riwayat nilai selama aplikasi berjalan
st.session_state.setdefault("riwayat_nilai", [])


# =========================================================
# HEADER APLIKASI
# =========================================================

# =========================================================
# FUNGSI VISUAL APLIKASI
# =========================================================

def kartu_visual(judul, deskripsi, svg):
    st.markdown(
        f"""
        <div class="visual-card">
            {svg}
            <h4 style="margin:8px 0 4px 0;">{judul}</h4>
            <p style="margin:0;color:#52606d;">{deskripsi}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


SVG_SEKOLAH = """
<svg viewBox="0 0 320 150" width="100%" height="150" xmlns="http://www.w3.org/2000/svg">
  <rect width="320" height="150" rx="18" fill="#eaf7ff"/>
  <circle cx="270" cy="32" r="19" fill="#ffd166"/>
  <rect x="78" y="50" width="165" height="72" rx="5" fill="#ffffff" stroke="#8bb8d8" stroke-width="3"/>
  <path d="M65 52 L160 20 L255 52 Z" fill="#7bb7d9"/>
  <rect x="145" y="83" width="30" height="39" fill="#8bb8d8"/>
  <g fill="#dff3ff" stroke="#8bb8d8" stroke-width="2">
    <rect x="92" y="68" width="25" height="20"/><rect x="128" y="68" width="25" height="20"/>
    <rect x="183" y="68" width="25" height="20"/><rect x="219" y="68" width="12" height="20"/>
  </g>
  <text x="160" y="141" text-anchor="middle" font-size="14" fill="#456">SEKOLAH</text>
</svg>
"""

SVG_SISWA = """
<svg viewBox="0 0 320 150" width="100%" height="150" xmlns="http://www.w3.org/2000/svg">
  <rect width="320" height="150" rx="18" fill="#fff7e8"/>
  <circle cx="105" cy="55" r="24" fill="#f4c7a1"/>
  <path d="M82 49 Q105 18 128 49 Q119 36 91 38 Z" fill="#5b4636"/>
  <path d="M75 124 Q105 83 135 124 Z" fill="#7bb7d9"/>
  <circle cx="215" cy="55" r="24" fill="#f1c19a"/>
  <path d="M191 47 Q215 16 239 47 Q228 32 201 36 Z" fill="#49382f"/>
  <path d="M185 124 Q215 83 245 124 Z" fill="#9bcf8f"/>
  <text x="160" y="143" text-anchor="middle" font-size="14" fill="#6b5b4d">SISWA BELAJAR</text>
</svg>
"""

SVG_TAMAN = """
<svg viewBox="0 0 320 150" width="100%" height="150" xmlns="http://www.w3.org/2000/svg">
  <rect width="320" height="150" rx="18" fill="#eefceb"/>
  <circle cx="260" cy="32" r="18" fill="#ffd166"/>
  <path d="M0 115 Q80 82 160 115 T320 110 V150 H0 Z" fill="#9bcf8f"/>
  <rect x="70" y="70" width="12" height="50" fill="#8b5e3c"/>
  <circle cx="76" cy="60" r="30" fill="#66b96b"/>
  <circle cx="53" cy="72" r="22" fill="#79c879"/>
  <circle cx="100" cy="72" r="22" fill="#79c879"/>
  <path d="M145 125 Q180 105 220 125" fill="none" stroke="#d5a253" stroke-width="10" stroke-linecap="round"/>
  <circle cx="160" cy="88" r="7" fill="#ff8fab"/>
  <circle cx="187" cy="75" r="7" fill="#ffd166"/>
  <circle cx="214" cy="92" r="7" fill="#9b8cff"/>
  <text x="160" y="143" text-anchor="middle" font-size="14" fill="#49644b">TAMAN SEKOLAH</text>
</svg>
"""


# =========================================================
# SIDEBAR / MENU
# =========================================================

with st.sidebar:

    st.header("🎒 Menu Belajar")

    menu = st.radio(
        "Pilih Menu",
        [
            "🏠 Beranda",
            "📝 Presensi",
            "📚 Daftar Materi",
            "🔎 Cari Materi",
            "📖 Belajar Materi",
            "🎬 Media Ajar",
            "📝 Latihan Soal",
            "🎮 Game Edukasi",
            "🧊 Ice Breaking",
            "🏆 Nilai"
        ]
    )

    st.divider()

    st.subheader("🗂️ Knowledge Base")
    st.write("Database dibaca otomatis dari folder:")
    st.code("database/")
    st.write(f"Jumlah file database: **{len(database)}**")


# =========================================================
# BANK SOAL - MATERI TEKS DESKRIPSI
# =========================================================
# Soal berikut dibuat berdasarkan materi "Teks Deskripsi"
# yang kamu masukkan.

SOAL = [
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Apa yang dimaksud dengan teks deskripsi?",
        "pilihan": [
            "Teks yang menceritakan rangkaian peristiwa",
            "Teks yang menggambarkan suatu objek secara terperinci",
            "Teks yang memberikan langkah-langkah melakukan sesuatu",
            "Teks yang mengajak pembaca melakukan sesuatu"
        ],
        "jawaban": "Teks yang menggambarkan suatu objek secara terperinci",
        "pembahasan": (
            "Teks deskripsi menggambarkan suatu objek secara terperinci "
            "sehingga pembaca memperoleh gambaran yang jelas tentang objek tersebut."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Apa tujuan utama teks deskripsi?",
        "pilihan": [
            "Memberikan gambaran yang jelas dan terperinci mengenai suatu objek",
            "Memberikan langkah-langkah melakukan sesuatu",
            "Menceritakan konflik antartokoh",
            "Membujuk pembaca agar mengikuti pendapat penulis"
        ],
        "jawaban": "Memberikan gambaran yang jelas dan terperinci mengenai suatu objek",
        "pembahasan": (
            "Tujuan utama teks deskripsi adalah memberikan gambaran yang jelas "
            "dan terperinci agar pembaca dapat membayangkan objek yang dijelaskan."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Berikut yang termasuk objek yang dapat dideskripsikan adalah ...",
        "pilihan": [
            "Manusia, hewan, tumbuhan, benda, tempat, dan peristiwa",
            "Hanya manusia dan hewan",
            "Hanya tempat dan peristiwa",
            "Hanya benda dan tumbuhan"
        ],
        "jawaban": "Manusia, hewan, tumbuhan, benda, tempat, dan peristiwa",
        "pembahasan": (
            "Materi menyebutkan manusia, hewan, tumbuhan, benda, tempat dan "
            "lingkungan, serta peristiwa sebagai objek yang dapat dideskripsikan."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Salah satu ciri teks deskripsi adalah ...",
        "pilihan": [
            "Melibatkan pancaindra",
            "Selalu menggunakan kalimat perintah",
            "Selalu menceritakan tokoh dan alur",
            "Berisi langkah-langkah secara berurutan"
        ],
        "jawaban": "Melibatkan pancaindra",
        "pembahasan": (
            "Teks deskripsi melibatkan pancaindra, yaitu penglihatan, "
            "pendengaran, penciuman, perabaan, dan pengecapan."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Struktur teks deskripsi yang berisi pengenalan objek secara umum disebut ...",
        "pilihan": [
            "Deskripsi bagian",
            "Penutup",
            "Deskripsi umum atau identifikasi",
            "Kesimpulan"
        ],
        "jawaban": "Deskripsi umum atau identifikasi",
        "pembahasan": (
            "Deskripsi umum atau identifikasi merupakan bagian yang "
            "memperkenalkan objek secara umum, seperti nama atau lokasi."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Bagian struktur teks deskripsi yang menggambarkan bagian-bagian objek secara terperinci disebut ...",
        "pilihan": [
            "Deskripsi umum",
            "Deskripsi bagian",
            "Orientasi",
            "Penutup"
        ],
        "jawaban": "Deskripsi bagian",
        "pembahasan": (
            "Deskripsi bagian berisi penggambaran terperinci mengenai "
            "bagian-bagian objek, seperti bentuk, warna, ukuran, sifat, dan suasana."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Kata seperti 'kemerahan', 'mungil', 'rimbun', dan 'sejuk' termasuk ...",
        "pilihan": [
            "Kata sifat",
            "Kata rujukan",
            "Kata hubung",
            "Kata kerja"
        ],
        "jawaban": "Kata sifat",
        "pembahasan": (
            "Kata-kata tersebut menjelaskan warna, ukuran, keadaan, atau "
            "suasana sehingga termasuk kata sifat atau adjektiva."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Manakah penulisan kata baku yang tepat?",
        "pilihan": [
            "Aktifitas",
            "Resiko",
            "Obyek",
            "Aktivitas"
        ],
        "jawaban": "Aktivitas",
        "pembahasan": (
            "Bentuk baku yang terdapat dalam materi adalah aktivitas, "
            "sedangkan aktifitas merupakan bentuk yang tidak baku."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Kata 'di pantai' ditulis terpisah karena 'di' berfungsi sebagai ...",
        "pilihan": [
            "Imbuhan",
            "Kata depan yang menunjukkan tempat",
            "Kata kerja",
            "Kata sifat"
        ],
        "jawaban": "Kata depan yang menunjukkan tempat",
        "pembahasan": (
            "Kata depan di ditulis terpisah jika menunjukkan tempat, "
            "misalnya di pantai, di hutan, dan di rumah."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Kalimat 'Air terjun itu bagaikan tirai putih raksasa' menggunakan majas ...",
        "pilihan": [
            "Metafora",
            "Personifikasi",
            "Hiperbola",
            "Perumpamaan atau simile"
        ],
        "jawaban": "Perumpamaan atau simile",
        "pembahasan": (
            "Kalimat tersebut menggunakan kata 'bagaikan' untuk membandingkan "
            "air terjun dengan tirai putih raksasa sehingga termasuk perumpamaan."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Teks deskripsi yang menggambarkan objek berdasarkan keadaan sebenarnya tanpa terlalu memasukkan kesan pribadi disebut ...",
        "pilihan": [
            "Deskripsi subjektif",
            "Deskripsi objektif",
            "Deskripsi spasial",
            "Deskripsi impresionistis"
        ],
        "jawaban": "Deskripsi objektif",
        "pembahasan": (
            "Deskripsi objektif menggambarkan objek berdasarkan fakta hasil "
            "pengamatan secara jelas dan apa adanya."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Deskripsi subjektif dipengaruhi oleh ...",
        "pilihan": [
            "Pengalaman dan sudut pandang penulis",
            "Urutan langkah kerja",
            "Data statistik saja",
            "Pendapat pembaca"
        ],
        "jawaban": "Pengalaman dan sudut pandang penulis",
        "pembahasan": (
            "Deskripsi subjektif berdasarkan penafsiran, kesan, pandangan, "
            "atau perasaan penulis."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Pola pengembangan yang disusun menurut letak, seperti depan ke belakang atau luar ke dalam, disebut pola ...",
        "pilihan": [
            "Waktu",
            "Kesan",
            "Spasial",
            "Khusus ke umum"
        ],
        "jawaban": "Spasial",
        "pembahasan": (
            "Pola spasial disusun berdasarkan ruang atau letak, misalnya "
            "depan ke belakang, atas ke bawah, atau luar ke dalam."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Langkah pertama dalam membuat teks deskripsi adalah ...",
        "pilihan": [
            "Menyunting teks",
            "Menentukan tema atau topik",
            "Mengembangkan kerangka",
            "Menetapkan pola pengembangan"
        ],
        "jawaban": "Menentukan tema atau topik",
        "pembahasan": (
            "Langkah pertama adalah menentukan tema atau topik yang menjadi "
            "dasar penggambaran."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Dalam menulis teks deskripsi, kata 'bagus' atau 'indah' sebaiknya ...",
        "pilihan": [
            "Digunakan sebanyak mungkin",
            "Diganti dengan kata yang lebih spesifik dan disertai penjelasan",
            "Dihilangkan semua",
            "Diganti dengan kata asing"
        ],
        "jawaban": "Diganti dengan kata yang lebih spesifik dan disertai penjelasan",
        "pembahasan": (
            "Materi menyarankan penggunaan kata yang spesifik, bukan kata umum "
            "seperti bagus atau indah tanpa penjelasan."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Teks yang menggambarkan ruang atau tempat dari berbagai sisi disebut ...",
        "pilihan": [
            "Deskripsi spasial",
            "Deskripsi objektif",
            "Deskripsi subjektif",
            "Narasi"
        ],
        "jawaban": "Deskripsi spasial",
        "pembahasan": (
            "Deskripsi spasial menggambarkan ruang atau tempat berdasarkan "
            "letak dan posisi bagian-bagiannya."
        )
    }
]

# =========================================================
# BANK SOAL ESAI - MATERI TEKS DESKRIPSI
# =========================================================
SOAL_ESAI = [
    {"nomor": 1, "pertanyaan": "Jelaskan pengertian teks deskripsi dengan menggunakan bahasa Anda sendiri!"},
    {"nomor": 2, "pertanyaan": "Sebutkan dan jelaskan minimal empat ciri-ciri teks deskripsi!"},
    {"nomor": 3, "pertanyaan": "Jelaskan perbedaan antara teks deskripsi spasial, objektif, dan subjektif!"},
    {"nomor": 4, "pertanyaan": "Jelaskan secara berurutan langkah-langkah yang harus dilakukan dalam membuat teks deskripsi!"},
    {"nomor": 5, "pertanyaan": "Buatlah sebuah teks deskripsi singkat mengenai salah satu objek yang ada di lingkungan sekolah, rumah, atau tempat tinggal Anda. Gunakan penggambaran yang jelas dan terperinci!"}
]


# =========================================================
# 8 MATERI TEKS DESKRIPSI
# =========================================================

MATERI_DESKRIPSI = [
    {
        "judul": "Pengertian Teks Deskripsi",
        "ikon": "1️⃣",
        "ringkas": "Mengenal pengertian dan fungsi teks deskripsi.",
        "isi": """
Teks deskripsi adalah teks yang menggambarkan suatu objek secara terperinci
sehingga pembaca seolah-olah dapat melihat, mendengar, merasakan, atau
membayangkan objek yang dideskripsikan.

Objek dapat berupa orang, tempat, benda, hewan, suasana, atau lingkungan.
Penggambaran dibuat dengan memilih detail yang jelas dan sesuai dengan objek.
"""
    },
    {
        "judul": "Tujuan dan Ciri-Ciri Teks Deskripsi",
        "ikon": "2️⃣",
        "ringkas": "Memahami tujuan dan karakteristik teks deskripsi.",
        "isi": """
Tujuan utama teks deskripsi adalah memberikan gambaran yang jelas dan terperinci
kepada pembaca mengenai suatu objek.

Ciri-cirinya antara lain:
• Menggambarkan objek secara khusus dan terperinci.
• Menggunakan kata-kata yang dapat merangsang pancaindra.
• Menjelaskan bagian, bentuk, warna, ukuran, suasana, atau karakteristik objek.
• Menggunakan kata sifat untuk memperjelas gambaran.
• Membuat pembaca seolah-olah dapat mengalami objek yang dideskripsikan.
"""
    },
    {
        "judul": "Struktur Teks Deskripsi",
        "ikon": "3️⃣",
        "ringkas": "Mengenal bagian-bagian penyusun teks deskripsi.",
        "isi": """
Struktur umum teks deskripsi terdiri atas:

1. Identifikasi
   Memperkenalkan objek yang akan dideskripsikan.

2. Deskripsi bagian
   Menjelaskan bagian-bagian objek secara lebih rinci, misalnya bentuk,
   warna, ukuran, suasana, atau karakteristik khusus.

3. Penutup/kesan
   Berisi simpulan atau kesan penulis terhadap objek yang dideskripsikan.
"""
    },
    {
        "judul": "Kaidah Kebahasaan Teks Deskripsi",
        "ikon": "4️⃣",
        "ringkas": "Mengenal bahasa yang digunakan dalam teks deskripsi.",
        "isi": """
Kaidah kebahasaan yang sering digunakan antara lain:
• Kata sifat: indah, luas, bersih, sejuk, ramai.
• Kata khusus yang membuat gambaran lebih tepat.
• Kata yang berkaitan dengan pancaindra.
• Kalimat yang menggambarkan keadaan atau ciri objek.
• Kata depan dan keterangan tempat untuk menjelaskan posisi objek.
• Ungkapan atau majas tertentu jika diperlukan untuk memperkuat gambaran.
"""
    },
    {
        "judul": "Pancaindra dalam Teks Deskripsi",
        "ikon": "5️⃣",
        "ringkas": "Menggunakan penglihatan, pendengaran, penciuman, peraba, dan pengecap.",
        "isi": """
Penggambaran melalui pancaindra membuat teks deskripsi terasa hidup.

👁️ Penglihatan: warna, bentuk, ukuran, cahaya.
👂 Pendengaran: suara, bunyi, riuh, hening.
👃 Penciuman: aroma, harum, wangi, bau.
✋ Peraba: halus, kasar, dingin, hangat.
👅 Pengecap: manis, asin, asam, pahit.

Pilih kata yang sesuai dengan objek agar pembaca mendapatkan gambaran yang kuat.
"""
    },
    {
        "judul": "Contoh dan Analisis Teks Deskripsi",
        "ikon": "6️⃣",
        "ringkas": "Membaca contoh lalu menemukan bagian dan ciri kebahasaannya.",
        "isi": """
Contoh singkat:

“Halaman sekolahku tampak asri pada pagi hari. Rumput hijau tumbuh rapi di
sekeliling taman. Bunga-bunga berwarna cerah bermekaran di dekat jalan setapak.
Udara terasa sejuk dan suara burung terdengar dari pepohonan.”

Analisis:
• Objek: halaman sekolah.
• Detail visual: rumput hijau, bunga berwarna cerah.
• Indra pendengaran: suara burung.
• Indra peraba: udara terasa sejuk.
• Tujuan: memberikan gambaran halaman sekolah secara jelas.
"""
    },
    {
        "judul": "Memahami dan Menganalisis Teks Deskripsi",
        "ikon": "7️⃣",
        "ringkas": "Melatih kemampuan menemukan objek, struktur, detail, dan bahasa.",
        "isi": """
Saat menganalisis teks deskripsi, perhatikan:
1. Apa objek yang dideskripsikan?
2. Bagaimana objek diperkenalkan?
3. Detail apa saja yang diberikan?
4. Pancaindra apa yang digunakan?
5. Kata sifat apa yang digunakan?
6. Bagaimana struktur teksnya?
7. Kesan apa yang ingin dibangun penulis?

Gunakan pertanyaan tersebut sebagai panduan agar analisis lebih terarah.
"""
    },
    {
        "judul": "Langkah-Langkah Menulis Teks Deskripsi",
        "ikon": "8️⃣",
        "ringkas": "Panduan dari memilih objek sampai menyunting tulisan.",
        "isi": """
Langkah-langkah menulis teks deskripsi:
1. Menentukan objek yang akan dideskripsikan.
2. Mengamati objek secara langsung atau melalui sumber yang sesuai.
3. Mencatat detail penting berdasarkan pancaindra.
4. Menentukan tujuan dan sudut pandang penulisan.
5. Menyusun kerangka berdasarkan struktur teks deskripsi.
6. Mengembangkan kerangka menjadi paragraf yang runtut.
7. Memilih kata yang konkret, khusus, dan menarik.
8. Memeriksa kembali ejaan, tanda baca, pilihan kata, dan kelengkapan isi.
"""
    },
]


# =========================================================
# VISUAL APLIKASI
# =========================================================

def kartu_visual(judul, deskripsi, svg):
    st.markdown(
        f"""
        <div class="visual-card">
            {svg}
            <h4 style="margin:8px 0 4px 0;">{judul}</h4>
            <p style="margin:0;color:#52606d;">{deskripsi}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


SVG_SEKOLAH = """
<svg viewBox="0 0 320 150" width="100%" height="150" xmlns="http://www.w3.org/2000/svg">
  <rect width="320" height="150" rx="18" fill="#eaf7ff"/>
  <circle cx="270" cy="32" r="19" fill="#ffd166"/>
  <rect x="78" y="50" width="165" height="72" rx="5" fill="#ffffff" stroke="#8bb8d8" stroke-width="3"/>
  <path d="M65 52 L160 20 L255 52 Z" fill="#7bb7d9"/>
  <rect x="145" y="83" width="30" height="39" fill="#8bb8d8"/>
  <g fill="#dff3ff" stroke="#8bb8d8" stroke-width="2">
    <rect x="92" y="68" width="25" height="20"/><rect x="128" y="68" width="25" height="20"/>
    <rect x="183" y="68" width="25" height="20"/><rect x="219" y="68" width="12" height="20"/>
  </g>
  <text x="160" y="141" text-anchor="middle" font-size="14" fill="#456">SEKOLAH</text>
</svg>
"""

SVG_SISWA = """
<svg viewBox="0 0 320 150" width="100%" height="150" xmlns="http://www.w3.org/2000/svg">
  <rect width="320" height="150" rx="18" fill="#fff7e8"/>
  <circle cx="105" cy="55" r="24" fill="#f4c7a1"/>
  <path d="M82 49 Q105 18 128 49 Q119 36 91 38 Z" fill="#5b4636"/>
  <path d="M75 124 Q105 83 135 124 Z" fill="#7bb7d9"/>
  <circle cx="215" cy="55" r="24" fill="#f1c19a"/>
  <path d="M191 47 Q215 16 239 47 Q228 32 201 36 Z" fill="#49382f"/>
  <path d="M185 124 Q215 83 245 124 Z" fill="#9bcf8f"/>
  <text x="160" y="143" text-anchor="middle" font-size="14" fill="#6b5b4d">SISWA BELAJAR</text>
</svg>
"""

SVG_TAMAN = """
<svg viewBox="0 0 320 150" width="100%" height="150" xmlns="http://www.w3.org/2000/svg">
  <rect width="320" height="150" rx="18" fill="#eefceb"/>
  <circle cx="260" cy="32" r="18" fill="#ffd166"/>
  <path d="M0 115 Q80 82 160 115 T320 110 V150 H0 Z" fill="#9bcf8f"/>
  <rect x="70" y="70" width="12" height="50" fill="#8b5e3c"/>
  <circle cx="76" cy="60" r="30" fill="#66b96b"/>
  <circle cx="53" cy="72" r="22" fill="#79c879"/>
  <circle cx="100" cy="72" r="22" fill="#79c879"/>
  <path d="M145 125 Q180 105 220 125" fill="none" stroke="#d5a253" stroke-width="10" stroke-linecap="round"/>
  <circle cx="160" cy="88" r="7" fill="#ff8fab"/><circle cx="187" cy="75" r="7" fill="#ffd166"/>
  <circle cx="214" cy="92" r="7" fill="#9b8cff"/>
  <text x="160" y="143" text-anchor="middle" font-size="14" fill="#49644b">TAMAN SEKOLAH</text>
</svg>
"""

# =========================================================
# HEADER VISUAL UNTUK SEMUA MENU
# =========================================================

if menu != "🏠 Beranda":
    deskripsi_menu = {
        "📝 Presensi": "Catat kehadiranmu dengan rapi dan mulai kegiatan belajar dengan semangat.",
        "📚 Daftar Materi": "Pilih materi, temukan informasi penting, dan jelajahi teks deskripsi.",
        "🔎 Cari Materi": "Masukkan kata kunci untuk menemukan informasi yang kamu butuhkan.",
        "📖 Belajar Materi": "Baca, pahami, dan amati contoh agar makin mahir mendeskripsikan objek.",
        "🎬 Media Ajar": "Belajar melalui video, gambar, dan pengalaman visual yang menyenangkan.",
        "📝 Latihan Soal": "Asah pemahamanmu melalui latihan pilihan berganda dan soal esai.",
        "🎮 Game Edukasi": "Uji pengetahuan sambil bermain dan kumpulkan skor terbaikmu.",
        "🧊 Ice Breaking": "Segarkan pikiran sejenak agar siap belajar kembali dengan ceria.",
        "🏆 Nilai": "Lihat hasil latihan dan gunakan indikator untuk menilai teks deskripsi."
    }
    st.markdown(f"""
    <div class="page-ribbon">
      <div class="page-ribbon-title">Ruang Belajar Digital · Kelas IX</div>
      <div class="page-ribbon-text"><b>{menu}</b><br>{deskripsi_menu.get(menu, 'Jelajahi kegiatan belajar Bahasa Indonesia dengan cara yang menyenangkan.')}</div>
    </div>
    <div class="page-stickers">
      <span>📚 Yuk belajar!</span><span>✏️ Kreatif</span><span>🌼 Amati detail</span>
      <span>💡 Temukan ide</span><span>⭐ Semangat</span><span>🦋 Belajar seru</span>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# MENU PRESENSI
# =========================================================

if menu == "🏠 Beranda":

    st.markdown("""
    <div class="home-hero">
        <div class="home-kicker">RUANG BELAJAR DIGITAL • KELAS IX</div>
        <div class="home-title">📚 Materi Teks Deskripsi</div>
        <div class="home-subtitle">Pembelajaran Bahasa Indonesia Kelas IX<br>
        Yuk, amati hal-hal di sekitar, temukan kata-kata menarik, lalu ceritakan objek dengan jelas dan kreatif! ✨</div>
    </div>
    <div class="sticker-row">
        <span class="sticker">📖 Siap Membaca</span>
        <span class="sticker">✏️ Ayo Menulis</span>
        <span class="sticker">🔎 Amati Detail</span>
        <span class="sticker">💡 Ide Kreatif</span>
        <span class="sticker">🌟 Belajar Seru</span>
        <span class="sticker">🎨 Imajinasi</span>
        <span class="sticker">🦋 Semangat!</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Ruang eksplorasi belajar")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class="home-card" style="background:linear-gradient(145deg,#fff1f2,#ffe4e6);">
        <div class="emoji">🌷📷</div><h3>Amati Objek</h3><p>Gunakan pancaindra untuk menemukan ciri khas objek yang akan dideskripsikan.</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="home-card" style="background:linear-gradient(145deg,#eff6ff,#dbeafe);">
        <div class="emoji">📝🖍️</div><h3>Susun Kata</h3><p>Pilih kata yang tepat agar gambaran objek terasa jelas dan hidup.</p></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="home-card" style="background:linear-gradient(145deg,#f0fdf4,#dcfce7);">
        <div class="emoji">🏆🎉</div><h3>Uji Pemahaman</h3><p>Kerjakan latihan dan permainan untuk menguji pemahamanmu.</p></div>""", unsafe_allow_html=True)

    st.markdown("### 🧭 Pilih kegiatan yang ingin kamu mulai")
    st.info("Gunakan menu **di sebelah kiri** untuk membuka materi, mencari informasi, mengerjakan latihan soal, bermain game edukasi, atau melihat nilai. 🚀")
    st.markdown("""<div class="home-note">💖 Ingat: setiap tempat punya cerita. Perhatikan detail kecil, pilih kata yang menarik, dan berani menuangkan idemu!</div>""", unsafe_allow_html=True)
    st.markdown("<div class='sticker-row'><span class='floating-emoji'>🌼</span><span class='floating-emoji delay1'>🧸</span><span class='floating-emoji delay2'>🌈</span><span class='floating-emoji'>⭐</span><span class='floating-emoji delay1'>🍀</span><span class='floating-emoji delay2'>🦄</span><span class='floating-emoji'>🪄</span></div>", unsafe_allow_html=True)

elif menu == "📝 Presensi":

    st.header("📝 Presensi Siswa")
    st.caption("Isi presensi dengan lengkap. Data presensi disimpan selama sesi aplikasi berjalan. 🏫")

    st.info(
        "📅 Tanggal dan waktu dicatat otomatis saat presensi dikirim."
    )

    with st.form("form_presensi"):
        nama = st.text_input("👤 Nama Siswa", placeholder="Masukkan nama lengkap")
        kelas = st.text_input("🏫 Kelas", placeholder="Contoh: IX-A")
        nomor_absen = st.number_input("🔢 Nomor Absen", min_value=1, max_value=60, step=1)
        status = st.selectbox(
            "📌 Status Kehadiran",
            ["Hadir", "Izin", "Sakit", "Alpa"]
        )
        kirim = st.form_submit_button("✅ SIMPAN PRESENSI", use_container_width=True)

    st.session_state.setdefault("data_presensi", [])

    if kirim:
        if not nama.strip() or not kelas.strip():
            st.warning("Nama dan kelas wajib diisi.")
        else:
            waktu = datetime.now()
            data_baru = {
                "Nama": nama.strip(),
                "Kelas": kelas.strip(),
                "No. Absen": int(nomor_absen),
                "Status": status,
                "Tanggal": waktu.strftime("%d-%m-%Y"),
                "Waktu": waktu.strftime("%H:%M:%S"),
            }

            sudah_ada = any(
                x["Nama"].lower() == data_baru["Nama"].lower()
                and x["Kelas"].lower() == data_baru["Kelas"].lower()
                and x["Tanggal"] == data_baru["Tanggal"]
                for x in st.session_state["data_presensi"]
            )

            if sudah_ada:
                st.warning("Presensi untuk nama dan kelas tersebut hari ini sudah tercatat.")
            else:
                st.session_state["data_presensi"].append(data_baru)
                st.success("🎉 Presensi berhasil disimpan!")

    if st.session_state["data_presensi"]:
        st.subheader("📋 Data Presensi")
        st.dataframe(
            st.session_state["data_presensi"],
            use_container_width=True,
            hide_index=True
        )


# =========================================================
# MENU DAFTAR MATERI
# =========================================================

elif menu == "📚 Daftar Materi":

    st.header("📚 Daftar Materi — Teks Deskripsi")
    st.caption("Delapan materi dari pengertian hingga langkah menulis. Pilih kartu untuk belajar. 🌟")

    for i in range(0, len(MATERI_DESKRIPSI), 2):
        c1, c2 = st.columns(2)
        for col, materi in zip((c1, c2), MATERI_DESKRIPSI[i:i+2]):
            with col:
                st.markdown(
                    f"""
                    <div class="material-card">
                        <div style="font-size:30px;">{materi['ikon']}</div>
                        <h3 style="margin:4px 0;">{materi['judul']}</h3>
                        <p style="color:#52606d;">{materi['ringkas']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                with st.expander("📖 Pelajari Materi"):
                    st.write(materi["isi"])

# =========================================================
# MENU CARI MATERI
# =========================================================

elif menu == "🔎 Cari Materi":

    st.header("🔎 Cari Materi")
    st.caption("Tanyakan materi dengan kata kunci yang kamu pahami. 💡")

    pertanyaan = st.text_area(
        "Masukkan pertanyaan Anda:",
        placeholder=(
            "Contoh: Apa yang dimaksud dengan kalimat efektif?"
        ),
        height=120
    )

    tombol = st.button(
        "🔍 TANYAKAN",
        use_container_width=True
    )

    if tombol:

        if pertanyaan.strip() == "":

            st.warning(
                "Silakan masukkan pertanyaan terlebih dahulu."
            )

        elif len(database) == 0:

            st.error(
                "Database TXT belum ditemukan."
            )

        else:

            with st.spinner(
                "Sedang mencari materi..."
            ):

                hasil = cari_materi(
                    pertanyaan,
                    database
                )

            if len(hasil) > 0:

                hasil_utama = hasil[0]

                st.success(
                    "Materi yang paling relevan ditemukan."
                )

                st.subheader("💡 Jawaban")

                jawaban = ambil_potongan_relevan(
                    pertanyaan,
                    hasil_utama["isi"]
                )

                st.info(jawaban)

                st.subheader("📚 Sumber Materi")

                st.write(
                    f"**{hasil_utama['nama_file']}**"
                )

                if len(hasil) > 1:

                    st.subheader("📑 Materi Terkait")

                    for item in hasil[1:4]:

                        with st.expander(
                            item["nama_file"]
                        ):

                            potongan = ambil_potongan_relevan(
                                pertanyaan,
                                item["isi"],
                                800
                            )

                            st.write(potongan)

            else:

                st.warning(
                    "Maaf, materi yang Anda tanyakan "
                    "belum ditemukan dalam database."
                )

                st.write(
                    "Coba gunakan kata kunci yang lebih spesifik."
                )


# =========================================================
# MENU BELAJAR MATERI
# =========================================================

elif menu == "📖 Belajar Materi":

    st.header("📖 Belajar Materi")
    st.caption("Baca perlahan, tandai ide penting, dan pahami contohnya. ✏️")

    if len(database) == 0:
        st.info("Knowledge Base TXT belum tersedia. Gunakan 8 materi Teks Deskripsi di bawah ini.")
        pilihan_judul = st.selectbox(
            "Pilih materi yang ingin dipelajari:",
            [m["judul"] for m in MATERI_DESKRIPSI]
        )
        materi = next(m for m in MATERI_DESKRIPSI if m["judul"] == pilihan_judul)
        st.subheader(materi["judul"])
        st.write(materi["isi"])
    else:
        pilihan_file = st.selectbox(
            "Pilih materi yang ingin dipelajari:",
            [data["nama_file"] for data in database]
        )

        data_terpilih = next(
            (data for data in database if data["nama_file"] == pilihan_file),
            None
        )

        if data_terpilih:
            st.subheader(
                pilihan_file.replace(".txt", "").replace("_", " ").title()
            )
            st.write(data_terpilih["isi"])

        st.divider()
        st.subheader("📚 8 Materi Teks Deskripsi")
        pilihan_ringkas = st.selectbox(
            "Atau pilih salah satu materi utama:",
            [m["judul"] for m in MATERI_DESKRIPSI],
            key="pilih_materi_utama_belajar"
        )
        materi_utama = next(
            m for m in MATERI_DESKRIPSI if m["judul"] == pilihan_ringkas
        )
        with st.expander("📖 Buka materi lengkap", expanded=True):
            st.write(materi_utama["isi"])


# =========================================================
# MENU MEDIA AJAR
# =========================================================

elif menu == "🎬 Media Ajar":

    st.header("🎬 Media Ajar Teks Deskripsi")
    st.caption(
        "Pelajari materi melalui video dan presentasi PowerPoint."
    )

    st.markdown(
        """
        <div class="home-note">
            📚 <b>Ruang Media Ajar</b><br>
            Pilih video untuk pengantar materi atau buka presentasi PowerPoint
            untuk mempelajari teks deskripsi secara lebih terstruktur.
        </div>
        """,
        unsafe_allow_html=True
    )

    tab_video, tab_ppt = st.tabs([
        "🎥 Video Pembelajaran",
        "📊 PowerPoint"
    ])

    with tab_video:
        st.subheader("🎥 Video Pembelajaran Teks Deskripsi")
        st.write(
            "Simak penjelasan mengenai pengertian, ciri-ciri, dan struktur "
            "teks deskripsi. Catat poin penting sebelum mengerjakan latihan."
        )
        st.video("https://youtu.be/5PlX5FxrVVg?si=MpI1oGteKAVzJdy1")
        st.info(
            "Tips belajar: perhatikan pengertian, tujuan, ciri-ciri, jenis, "
            "langkah menulis, dan contoh teks deskripsi."
        )

    with tab_ppt:
        st.subheader("📊 Presentasi Materi Teks Deskripsi")
        st.write(
            "Presentasi ini membahas pengertian, tujuan, ciri-ciri, jenis "
            "teks deskripsi, langkah menulis, contoh, dan evaluasi."
        )

        # Simpan file PPTX di repository pada folder media/
        # dengan nama: teks_deskripsi_kelas_ix.pptx
        lokasi_ppt = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "media",
            "teks_deskripsi_kelas_ix.pptx"
        )

        if os.path.exists(lokasi_ppt):
            with open(lokasi_ppt, "rb") as file_ppt:
                data_ppt = file_ppt.read()

            st.success("File PowerPoint tersedia dan siap dibuka.")
            st.download_button(
                label="⬇️ Unduh PowerPoint Teks Deskripsi",
                data=data_ppt,
                file_name="Materi_Teks_Deskripsi_Kelas_IX.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                use_container_width=True
            )
            st.caption(
                "Setelah diunduh, buka file menggunakan Microsoft PowerPoint "
                "atau aplikasi presentasi yang kompatibel."
            )
        else:
            st.warning(
                "File PowerPoint belum ditemukan di folder media/. "
                "Tambahkan file PPTX ke repository dengan nama "
                "'teks_deskripsi_kelas_ix.pptx' agar tombol unduh muncul."
            )
            st.code(
                "media/teks_deskripsi_kelas_ix.pptx",
                language="text"
            )
            st.markdown(
                "Jika folder `media` belum ada, buat folder tersebut di "
                "repository GitHub, lalu unggah file PowerPoint ke dalamnya."
            )


# =========================================================
# MENU LATIHAN SOAL INTERAKTIF
# =========================================================

elif menu == "📝 Latihan Soal":

    st.header("📝 Latihan Soal Interaktif")
    st.caption("Uji pemahamanmu dan jadikan hasilnya sebagai bahan belajar berikutnya. 🚀")

    jenis_latihan = st.radio(
        "Pilih jenis soal:",
        ["A. Pilihan Berganda", "B. Esai"],
        horizontal=True
    )

    # =====================================================
    # PILIHAN BERGANDA
    # =====================================================

    if jenis_latihan == "A. Pilihan Berganda":

        st.write("Pilihlah jawaban yang paling tepat!")

        daftar_materi_soal = sorted(
            set(soal["materi"] for soal in SOAL)
        )

        materi_dipilih = st.selectbox(
            "📚 Pilih materi:",
            ["Semua Materi"] + daftar_materi_soal
        )

        if materi_dipilih == "Semua Materi":

            soal_aktif = SOAL

        else:

            soal_aktif = [
                soal
                for soal in SOAL
                if soal["materi"] == materi_dipilih
            ]

        jumlah_maksimal = len(soal_aktif)

        jumlah_soal = st.slider(
            "🔢 Jumlah soal:",
            min_value=1,
            max_value=jumlah_maksimal,
            value=min(5, jumlah_maksimal)
        )

        soal_aktif = soal_aktif[:jumlah_soal]

        st.divider()

        jawaban_pengguna = {}

        for nomor, soal in enumerate(soal_aktif, 1):

            st.markdown(f"### Soal {nomor}")

            st.write(soal["pertanyaan"])

            jawaban_pengguna[nomor] = st.radio(
                "Pilih jawaban:",
                soal["pilihan"],
                key=f"jawaban_{materi_dipilih}_{nomor}"
            )

        st.divider()

        if st.button(
            "✅ PERIKSA JAWABAN",
            use_container_width=True
        ):

            skor = 0

            st.subheader("📊 Hasil Latihan")

            for nomor, soal in enumerate(soal_aktif, 1):

                jawaban = jawaban_pengguna[nomor]

                if jawaban == soal["jawaban"]:

                    skor += 1

                    st.success(
                        f"Soal {nomor}: ✅ Benar"
                    )

                else:

                    st.error(
                        f"Soal {nomor}: ❌ Salah"
                    )

                    st.write(
                        f"Jawaban yang benar: **{soal['jawaban']}**"
                    )

                with st.expander(
                    f"💡 Pembahasan soal {nomor}"
                ):

                    st.write(
                        soal["pembahasan"]
                    )

            nilai = round(
                (skor / len(soal_aktif)) * 100
            )

            st.session_state["riwayat_nilai"].append({
                "jenis": "Pilihan Berganda",
                "nilai": nilai,
                "benar": skor,
                "jumlah": len(soal_aktif)
            })

            st.divider()

            st.metric(
                "🎯 Nilai Anda",
                f"{nilai}"
            )

            st.write(
                f"Jawaban benar: **{skor} dari {len(soal_aktif)} soal**"
            )

            if nilai >= 80:

                st.success(
                    "🎉 Sangat baik! Kamu sudah memahami materi."
                )

                st.balloons()

            elif nilai >= 60:

                st.warning(
                    "👍 Cukup baik. Pelajari kembali materi yang masih kurang."
                )

            else:

                st.error(
                    "📚 Jangan menyerah. Pelajari materi kembali dan coba lagi."
                )

    # =====================================================
    # ESAI
    # =====================================================

    else:

        st.subheader("B. ESAI")
        st.write("Jawablah pertanyaan berikut dengan jelas dan lengkap!")

        jawaban_esai = {}

        for soal in SOAL_ESAI:
            st.markdown(f"### {soal['nomor']}. {soal['pertanyaan']}")
            jawaban_esai[soal["nomor"]] = st.text_area(
                f"Jawaban soal {soal['nomor']}:",
                height=140,
                key=f"esai_{soal['nomor']}",
                placeholder="Tuliskan jawaban Anda di sini..."
            )

        st.divider()

        if st.button("💾 SIMPAN JAWABAN ESAI", use_container_width=True):
            jumlah_terisi = sum(
                1 for jawaban in jawaban_esai.values()
                if jawaban.strip()
            )
            if jumlah_terisi == 0:
                st.warning("Silakan isi jawaban terlebih dahulu.")
            else:
                st.success(
                    f"Jawaban berhasil dicatat. "
                    f"{jumlah_terisi} dari {len(SOAL_ESAI)} soal telah diisi."
                )
                st.info(
                    "Jawaban esai belum diberi nilai otomatis. "
                    "Penilaian dapat dilakukan oleh guru."
                )



# =========================================================
# MENU GAME EDUKASI
# =========================================================

elif menu == "🎮 Game Edukasi":

    st.header("🎮 Game Edukasi Teks Deskripsi")
    st.caption("Belajar sambil bermain! Mulai dari Wordwall sampai tantangan mini. 🕹️")

    tab1, tab2, tab3, tab4 = st.tabs([
        "🟢 Wordwall",
        "🔵 Tebak Istilah",
        "🟣 Susun Struktur",
        "🟠 Tantangan Pancaindra"
    ])

    with tab1:
        st.subheader("🟢 Wordwall — Teks Deskripsi")
        st.write("Mainkan game Wordwall berikut untuk menguji pemahamanmu.")
        st.components.v1.html(
            """
            <iframe style="max-width:100%"
                src="https://wordwall.net/embed/play/120681/271/203"
                width="500" height="380" frameborder="0"
                allowfullscreen>
            </iframe>
            """,
            height=410,
            scrolling=False
        )

        st.markdown(
            """
            <div class="level-card">
                <b>🏅 Level Permainan</b><br>
                🟢 Pemula → 🟡 Dasar → 🟠 Menengah → 🔵 Lanjutan → 🔴 HIGH / MASTER
            </div>
            """,
            unsafe_allow_html=True
        )

    with tab2:
        st.subheader("🔵 Tebak Istilah")
        st.write("Pilih jawaban yang paling tepat.")

        teka = [
            ("Teks yang menggambarkan objek secara terperinci adalah ...",
             ["Teks deskripsi", "Teks prosedur", "Teks berita", "Teks persuasi"], "Teks deskripsi"),
            ("Bagian yang memperkenalkan objek disebut ...",
             ["Deskripsi bagian", "Identifikasi", "Argumentasi", "Orientasi"], "Identifikasi"),
            ("Kata seperti 'sejuk', 'indah', dan 'luas' termasuk ...",
             ["Kata sifat", "Kata bilangan", "Kata tanya", "Kata hubung"], "Kata sifat"),
        ]

        skor_game = 0
        for n, (q, pilihan, jawaban) in enumerate(teka, 1):
            pilihan_user = st.radio(q, pilihan, key=f"tebak_{n}")
            if pilihan_user == jawaban:
                skor_game += 1

        if st.button("🎯 CEK SKOR TEBAK ISTILAH", use_container_width=True):
            st.success(f"Skor kamu: {skor_game}/{len(teka)}")
            if skor_game == len(teka):
                st.balloons()
                st.success("🏆 Sempurna! Kamu menguasai istilah dasar Teks Deskripsi.")

    with tab3:
        st.subheader("🟣 Susun Struktur")
        st.write("Tentukan urutan struktur yang paling tepat.")

        urutan = st.select_slider(
            "Urutan struktur Teks Deskripsi:",
            options=[
                "Deskripsi bagian → Identifikasi → Kesan",
                "Identifikasi → Deskripsi bagian → Penutup/Kesan",
                "Penutup/Kesan → Identifikasi → Deskripsi bagian"
            ]
        )

        if st.button("✅ PERIKSA URUTAN", use_container_width=True):
            if urutan == "Identifikasi → Deskripsi bagian → Penutup/Kesan":
                st.success("Benar! 🎉")
            else:
                st.error("Belum tepat. Coba ingat kembali struktur Teks Deskripsi.")

    with tab4:
        st.subheader("🟠 Tantangan Pancaindra")
        st.write("Pasangkan kata dengan pancaindra yang paling sesuai.")

        soal_indra = {
            "Wangi bunga": "👃 Penciuman",
            "Suara burung": "👂 Pendengaran",
            "Rumput hijau": "👁️ Penglihatan",
            "Permukaan batu kasar": "✋ Peraba",
            "Rasa buah manis": "👅 Pengecap",
        }

        benar = 0
        for i, (contoh, jawaban_benar) in enumerate(soal_indra.items(), 1):
            pilihan = st.selectbox(
                contoh,
                ["👁️ Penglihatan", "👂 Pendengaran", "👃 Penciuman", "✋ Peraba", "👅 Pengecap"],
                key=f"indra_{i}"
            )
            if pilihan == jawaban_benar:
                benar += 1

        if st.button("🌟 CEK TANTANGAN", use_container_width=True):
            st.success(f"Hasil: {benar}/{len(soal_indra)} benar.")
            if benar == len(soal_indra):
                st.balloons()

# =========================================================
# MENU ICE BREAKING
# =========================================================

elif menu == "🧊 Ice Breaking":

    st.header("🧊 Ice Breaking")
    st.caption("Pilih aktivitas singkat untuk menyegarkan suasana belajar.")

    tab_youtube, tab_wordwall, tab_educaplay = st.tabs([
        "▶️ YouTube",
        "🟢 Wordwall",
        "🟣 Educaplay"
    ])

    with tab_youtube:
        st.subheader("▶️ Ice Breaking melalui YouTube")
        st.write(
            "Putar video berikut dan ikuti aktivitasnya bersama teman-teman."
        )
        st.video("https://youtu.be/mWpFwlH3338?si=S6F1IpMQ8T1FA6Fa")
        st.caption("Jika video tidak dapat diputar, buka tautannya langsung di YouTube.")
        st.link_button(
            "Buka video di YouTube",
            "https://youtu.be/mWpFwlH3338?si=S6F1IpMQ8T1FA6Fa",
            use_container_width=True
        )

    with tab_wordwall:
        st.subheader("🟢 Permainan Wordwall")
        st.write(
            "Mainkan aktivitas Wordwall berikut. Gunakan mode layar penuh "
            "jika tersedia agar permainan lebih nyaman."
        )
        st.components.v1.html(
            """
            <iframe
                style="width:100%; max-width:100%; border:0; border-radius:12px;"
                src="https://wordwall.net/id/embed/dbd3402baa874d61b9c18481e42ab1a2?themeId=65&templateId=30&fontStackId=0"
                width="800"
                height="500"
                allowfullscreen>
            </iframe>
            """,
            height=520,
            scrolling=True
        )
        st.link_button(
            "Buka Wordwall di tab baru",
            "https://wordwall.net/id/embed/dbd3402baa874d61b9c18481e42ab1a2?themeId=65&templateId=30&fontStackId=0",
            use_container_width=True
        )

    with tab_educaplay:
        st.subheader("🟣 Permainan Educaplay: Kata Benda Baku")
        st.write(
            "Kerjakan permainan untuk berlatih mengenali kata benda baku."
        )
        st.components.v1.html(
            """
            <iframe
                style="width:100%; max-width:100%; border:0; border-radius:12px;"
                src="https://www.educaplay.com/game/30979760-kata_benda_baku.html"
                width="800"
                height="600"
                allow="fullscreen; autoplay; allow-top-navigation-by-user-activation"
                allowfullscreen>
            </iframe>
            """,
            height=620,
            scrolling=True
        )
        st.link_button(
            "Buka Educaplay di tab baru",
            "https://www.educaplay.com/game/30979760-kata_benda_baku.html",
            use_container_width=True
        )


# =========================================================
# MENU NILAI
# =========================================================

elif menu == "🏆 Nilai":

    st.header("🏆 Nilai Saya")
    st.write("Lihat hasil latihan pilihan berganda yang sudah kamu kerjakan.")

    riwayat = st.session_state.get("riwayat_nilai", [])

    if len(riwayat) == 0:
        st.info("Belum ada nilai. Yuk kerjakan Latihan Soal terlebih dahulu! 📝")
    else:
        nilai_terakhir = riwayat[-1]
        st.metric("🎯 Nilai Terakhir", nilai_terakhir["nilai"])

        st.write(
            f"Jawaban benar: **{nilai_terakhir['benar']} dari "
            f"{nilai_terakhir['jumlah']} soal**"
        )

        if nilai_terakhir["nilai"] >= 80:
            st.success("🎉 Hebat! Hasil belajarmu sangat baik.")
        elif nilai_terakhir["nilai"] >= 60:
            st.warning("👍 Cukup baik. Yuk belajar lagi agar nilainya lebih tinggi.")
        else:
            st.error("💪 Jangan menyerah. Pelajari kembali materinya dan coba lagi!")

        st.subheader("📊 Riwayat Nilai")

        for nomor, hasil in enumerate(reversed(riwayat), 1):
            st.write(
                f"**Latihan {len(riwayat) - nomor + 1}** — "
                f"{hasil['jenis']} — **{hasil['nilai']}** "
                f"({hasil['benar']}/{hasil['jumlah']} benar)"
            )

        if st.button("🗑️ Hapus Riwayat Nilai"):
            st.session_state["riwayat_nilai"] = []
            st.rerun()

    st.divider()
    st.header("📝 Indikator Penilaian Esai Teks Deskripsi")
    st.write("Gunakan indikator berikut untuk menilai jawaban esai siswa secara manual berdasarkan dokumen indikator penilaian.")

    with st.expander("📌 Kisi-kisi indikator penilaian", expanded=True):
        st.markdown("**1. Judul**")
        st.markdown("- Judul menggambarkan objek khusus yang dideskripsikan.\n- Ditulis sebagai frasa/konstruksi yang sesuai, bukan kalimat lengkap.\n- Penggunaan huruf kapital tepat.\n- Tidak diakhiri tanda titik.")
        st.markdown("**2. Identifikasi**")
        st.markdown("- Memperkenalkan atau menyebutkan objek yang dideskripsikan.\n- Memuat informasi umum mengenai objek.\n- Struktur kalimat tepat dan mudah dipahami.\n- Tanda baca digunakan secara tepat.")
        st.markdown("**3. Deskripsi Bagian**")
        st.markdown("- Menggambarkan objek secara terperinci.\n- Menjelaskan bagian, ciri, keadaan, atau karakteristik objek secara jelas.\n- Struktur kalimat tepat.\n- Kosakata sesuai dan bervariasi.\n- Tanda baca digunakan secara tepat.")
        st.markdown("**4. Penutup**")
        st.markdown("- Memuat simpulan atau tanggapan terhadap objek.\n- Memuat kesan terhadap objek yang dideskripsikan.\n- Kosakata sesuai dan bervariasi.\n- Tanda baca digunakan secara tepat.")

    st.subheader("🧮 Lembar Penskoran Esai")
    st.caption("Pilih skor 1–4 pada setiap aspek. Skor maksimal 16; nilai akhir = (skor diperoleh / 16) × 100.")
    nama_siswa = st.text_input("Nama siswa", key="nama_siswa_penilaian_esai", placeholder="Masukkan nama siswa")
    skor_judul = st.select_slider("Judul — skor (1–4)", options=[1, 2, 3, 4], value=1, key="skor_esai_judul", help="Skor 4: memenuhi 4 indikator; 3: memenuhi 3; 2: memenuhi 2; 1: memenuhi 1.")
    skor_identifikasi = st.select_slider("Identifikasi — skor (1–4)", options=[1, 2, 3, 4], value=1, key="skor_esai_identifikasi", help="Skor 4: memenuhi 4 indikator; 3: memenuhi 3; 2: memenuhi 2; 1: memenuhi 1.")
    skor_deskripsi = st.select_slider("Deskripsi Bagian — skor (1–4)", options=[1, 2, 3, 4], value=1, key="skor_esai_deskripsi", help="Sesuai dokumen: skor 4 memenuhi 5 indikator; skor 3 memenuhi 4; skor 2 memenuhi 2–3; skor 1 memenuhi 1.")
    skor_penutup = st.select_slider("Penutup — skor (1–4)", options=[1, 2, 3, 4], value=1, key="skor_esai_penutup", help="Skor 4: memenuhi 4 indikator; 3: memenuhi 3; 2: memenuhi 2; 1: memenuhi 1.")
    total_skor = skor_judul + skor_identifikasi + skor_deskripsi + skor_penutup
    nilai_esai = round((total_skor / 16) * 100, 2)
    col_skor1, col_skor2 = st.columns(2)
    col_skor1.metric("Total Skor", f"{total_skor} / 16")
    col_skor2.metric("Nilai Esai", nilai_esai)
    if st.button("💾 Simpan Hasil Penilaian Esai", use_container_width=True):
        if not nama_siswa.strip():
            st.warning("Isi nama siswa terlebih dahulu sebelum menyimpan penilaian.")
        else:
            if "riwayat_nilai_esai" not in st.session_state:
                st.session_state["riwayat_nilai_esai"] = []
            st.session_state["riwayat_nilai_esai"].append({
                "nama": nama_siswa.strip(),
                "skor_judul": skor_judul,
                "skor_identifikasi": skor_identifikasi,
                "skor_deskripsi": skor_deskripsi,
                "skor_penutup": skor_penutup,
                "total_skor": total_skor,
                "nilai": nilai_esai,
            })
            st.success(f"Penilaian esai untuk {nama_siswa.strip()} berhasil disimpan.")

    riwayat_esai = st.session_state.get("riwayat_nilai_esai", [])
    if riwayat_esai:
        st.subheader("📋 Riwayat Penilaian Esai")
        st.dataframe(
            [{
                "Nama Siswa": item["nama"],
                "Judul": item["skor_judul"],
                "Identifikasi": item["skor_identifikasi"],
                "Deskripsi Bagian": item["skor_deskripsi"],
                "Penutup": item["skor_penutup"],
                "Total Skor": f"{item['total_skor']}/16",
                "Nilai": item["nilai"],
            } for item in riwayat_esai],
            use_container_width=True,
            hide_index=True
        )

    with st.expander("📚 Sumber indikator penilaian"):
        st.write("Direktorat Sekolah Menengah Pertama, Kementerian Pendidikan dan Kebudayaan. (2020). Modul pembelajaran jarak jauh Bahasa Indonesia SMP/MTs.")
        st.markdown("[Buka sumber di Repositori Kemendikdasmen](https://repositori.kemendikdasmen.go.id/23387/1/Modul%20PJJ%20Bahasa%20Indonesia%202020.pdf)")


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Bahasa Indonesia Kelas IX | "
    "Python + Streamlit + TXT Knowledge Base"
)
