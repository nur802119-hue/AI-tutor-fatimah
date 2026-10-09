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
# KONFIGURASI DAN FUNGSI PENCARIAN MATERI
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FOLDER_DATABASE = os.path.join(BASE_DIR, "database")


def baca_database():
    """Membaca semua file TXT di folder aplikasi dan subfoldernya."""
    data = []
    folder_yang_diabaikan = {".git", ".venv", "venv", "__pycache__", ".streamlit"}

    for folder, subfolder, daftar_file in os.walk(BASE_DIR):
        subfolder[:] = [nama for nama in subfolder if nama not in folder_yang_diabaikan]
        for nama_file in daftar_file:
            if not nama_file.lower().endswith(".txt"):
                continue
            lokasi_file = os.path.join(folder, nama_file)
            try:
                with open(lokasi_file, "r", encoding="utf-8-sig") as file:
                    isi = file.read().strip()
                if isi:
                    data.append({"nama_file": nama_file, "isi": isi})
            except (OSError, UnicodeError) as error:
                st.warning(f"File {nama_file} tidak dapat dibaca: {error}")

    # Hilangkan kemungkinan file dengan nama dan isi yang sama terindeks berulang.
    unik = []
    sudah_ada = set()
    for item in data:
        identitas = (item["nama_file"].lower(), item["isi"][:300])
        if identitas not in sudah_ada:
            sudah_ada.add(identitas)
            unik.append(item)
    return unik


STOPWORDS = {
    "yang", "dan", "di", "ke", "dari", "pada", "dengan", "untuk", "dalam",
    "adalah", "itu", "ini", "atau", "apa", "bagaimana", "mengapa", "sebutkan",
    "jelaskan", "jelaskanlah", "tentang", "suatu", "sebuah", "secara", "merupakan",
    "dapat", "akan", "sebagai", "oleh", "lebih", "juga", "tidak", "tersebut",
    "kah", "dong", "sih", "ya", "jadi", "tolong", "coba", "maksud", "dimaksud",
    "pengertian", "jelaskan", "jelasin", "dong", "apa", "saja", "contoh", "berikan"
}

# Bentuk kata/ungkapan yang sering dipakai siswa untuk menanyakan konsep yang sama.
SINONIM = {
    "definisi": {"pengertian", "arti", "makna"},
    "pengertian": {"definisi", "arti", "makna"},
    "ciri": {"karakteristik", "tanda", "ciri-ciri"},
    "karakteristik": {"ciri", "tanda"},
    "tujuan": {"fungsi", "manfaat", "kegunaan"},
    "fungsi": {"tujuan", "manfaat", "kegunaan"},
    "manfaat": {"fungsi", "tujuan", "kegunaan"},
    "struktur": {"bagian", "susunan", "struktur teks"},
    "bagian": {"struktur", "susunan"},
    "langkah": {"cara", "tahapan", "proses"},
    "cara": {"langkah", "tahapan"},
    "contoh": {"misalnya", "contohnya"},
    "teks": {"tulisan", "bacaan"},
    "deskripsi": {"menggambarkan", "gambaran", "pemaparan"},
}


def bersihkan_teks(teks):
    teks = str(teks).lower()
    teks = re.sub(r"[^a-zA-ZÀ-ÿ0-9\s]", " ", teks)
    return re.sub(r"\s+", " ", teks).strip()


def normalisasi_kata(kata):
    """Normalisasi ringan agar variasi imbuhan sederhana lebih mudah cocok."""
    kata = kata.lower()
    # Tidak melakukan stemming agresif; hanya menambahkan bentuk dasar yang aman.
    variasi = {kata}
    for awalan in ("meng", "meny", "men", "mem", "me", "ber", "ter", "di", "ke", "pe", "pen", "pem", "peng"):
        if kata.startswith(awalan) and len(kata) > len(awalan) + 3:
            variasi.add(kata[len(awalan):])
    for akhiran in ("nya", "kan", "an", "i"):
        for bentuk in list(variasi):
            if bentuk.endswith(akhiran) and len(bentuk) > len(akhiran) + 3:
                variasi.add(bentuk[:-len(akhiran)])
    return variasi


def ambil_kata_kunci(pertanyaan):
    kata_kunci = []
    for kata in bersihkan_teks(pertanyaan).split():
        if len(kata) <= 2 or kata in STOPWORDS:
            continue
        kata_kunci.append(kata)
        kata_kunci.extend(SINONIM.get(kata, set()))
        kata_kunci.extend(normalisasi_kata(kata))
    # Urutan dipertahankan, kata duplikat dihapus.
    return list(dict.fromkeys(kata_kunci))


def hitung_relevansi(pertanyaan, isi, nama_file=""):
    kata_kunci = ambil_kata_kunci(pertanyaan)
    if not kata_kunci:
        return 0

    teks_bersih = bersihkan_teks(isi)
    kata_dokumen = set(teks_bersih.split())
    skor = 0
    kata_asli = [k for k in bersihkan_teks(pertanyaan).split() if k not in STOPWORDS and len(k) > 2]

    for kata in kata_kunci:
        if kata in kata_dokumen:
            # Kata asli lebih berbobot daripada sinonim/variasi.
            skor += 3 if kata in kata_asli else 1

    pertanyaan_bersih = bersihkan_teks(pertanyaan)
    if len(pertanyaan_bersih) > 5 and pertanyaan_bersih in teks_bersih:
        skor += 8

    # Judul/nama file memberi petunjuk topik, tetapi tidak mendominasi isi.
    judul_bersih = bersihkan_teks(nama_file)
    for kata in kata_asli:
        if kata in judul_bersih:
            skor += 3
    return skor


def cari_materi(pertanyaan, daftar_materi):
    hasil = []
    for item in daftar_materi:
        skor = hitung_relevansi(pertanyaan, item.get("isi", ""), item.get("nama_file", ""))
        if skor > 0:
            hasil.append({**item, "skor": skor})
    hasil.sort(key=lambda item: item["skor"], reverse=True)
    return hasil


def ambil_potongan_relevan(pertanyaan, isi, jumlah_maksimal=1800):
    """Mengambil paragraf yang paling sesuai, dengan urutan asli bila skornya sama."""
    kata_kunci = set(ambil_kata_kunci(pertanyaan))
    paragraf = [p.strip() for p in re.split(r"\n\s*\n|\r\n", isi) if p.strip()]
    if not paragraf:
        return ""

    daftar_skor = []
    for indeks, p in enumerate(paragraf):
        kata_paragraf = set(bersihkan_teks(p).split())
        skor = sum(2 if kata in bersihkan_teks(pertanyaan).split() else 1 for kata in kata_kunci if kata in kata_paragraf)
        if skor > 0:
            daftar_skor.append((skor, indeks, p))

    if not daftar_skor:
        return ""

    daftar_skor.sort(key=lambda x: (-x[0], x[1]))
    terpilih = []
    panjang = 0
    for _, _, paragraf_teks in daftar_skor:
        tambahan = len(paragraf_teks) + 2
        if panjang + tambahan <= jumlah_maksimal:
            terpilih.append(paragraf_teks)
            panjang += tambahan
    if not terpilih:
        terpilih = [daftar_skor[0][2][:jumlah_maksimal]]
    return "\n\n".join(terpilih)


# Database TXT dibaca saat aplikasi dimulai.
database = baca_database()
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
# PENILAIAN OTOMATIS ESAI TANPA AI TAMBAHAN
# Catatan: penilaian berbasis indikator/kata kunci, bukan pemahaman semantik penuh.
# Setiap soal bernilai maksimal 20; total maksimal 100.
# =========================================================

def normalisasi_jawaban(teks):
    teks = (teks or "").lower()
    teks = re.sub(r"[^a-zA-ZÀ-ÿ0-9\s]", " ", teks)
    return re.sub(r"\s+", " ", teks).strip()


def cocok_salah_satu(teks, pilihan):
    return any(normalisasi_jawaban(kata) in normalisasi_jawaban(teks) for kata in pilihan)


def nilai_esai(nomor, jawaban):
    teks = normalisasi_jawaban(jawaban)
    kata = set(teks.split())
    rincian = []
    skor = 0

    if not teks:
        return {"skor": 0, "maksimal": 20, "rincian": ["Jawaban belum diisi."],
                "umpan_balik": "Isi jawaban terlebih dahulu."}

    if nomor == 1:
        indikator = [
            ("Menjelaskan bahwa teks menggambarkan/memaparkan objek",
             ["menggambarkan", "menggambarkan", "memaparkan", "melukiskan", "menjelaskan objek"]),
            ("Menyebutkan objek secara jelas atau khusus",
             ["objek", "orang", "tempat", "benda", "hewan", "tumbuhan", "lingkungan"]),
            ("Menjelaskan bahwa gambaran disampaikan terperinci",
             ["terperinci", "rinci", "detail", "ciri ciri", "bagian bagian"]),
            ("Menjelaskan efek kepada pembaca atau penggunaan pancaindra",
             ["membayangkan", "seolah olah", "melihat", "merasakan", "pancaindra", "mendengar"])
        ]
        for label, kata_kunci in indikator:
            ok = cocok_salah_satu(teks, kata_kunci)
            skor += 5 if ok else 0
            rincian.append(f"{'✓' if ok else '•'} {label}: {5 if ok else 0}/5")

    elif nomor == 2:
        kelompok_ciri = [
            ("Menggambarkan objek tertentu", ["objek", "menggambarkan", "menguraikan"]),
            ("Menjelaskan objek secara terperinci", ["terperinci", "rinci", "detail", "bagian"]),
            ("Menggunakan detail pancaindra", ["pancaindra", "melihat", "mendengar", "mencium", "menyentuh", "merasakan", "aroma", "suara", "tekstur"]),
            ("Menggunakan kata sifat atau kata khusus", ["kata sifat", "adjektiva", "warna", "bentuk", "ukuran", "sejuk", "indah", "luas"]),
            ("Membuat pembaca seolah mengalami/membayangkan objek", ["pembaca", "membayangkan", "seolah olah", "merasakan", "melihat"])
        ]
        jumlah = sum(1 for _, kunci in kelompok_ciri if cocok_salah_satu(teks, kunci))
        skor = min(20, jumlah * 4)
        for label, kunci in kelompok_ciri:
            ok = cocok_salah_satu(teks, kunci)
            rincian.append(f"{'✓' if ok else '•'} {label}: {'terdeteksi' if ok else 'belum terdeteksi'}")
        rincian.append(f"Indikator yang terdeteksi: {jumlah} dari 5.")

    elif nomor == 3:
        kelompok_jenis = [
            ("Deskripsi spasial: ruang/tempat, posisi atau letak", ["spasial", "ruang", "tempat", "posisi", "letak", "arah"]),
            ("Deskripsi objektif: keadaan sebenarnya/fakta, apa adanya", ["objektif", "fakta", "sebenarnya", "apa adanya", "hasil pengamatan"]),
            ("Deskripsi subjektif: kesan/pandangan/perasaan penulis", ["subjektif", "kesan", "pandangan", "perasaan", "pendapat penulis", "sudut pandang"])
        ]
        for label, kunci in kelompok_jenis:
            ok = cocok_salah_satu(teks, kunci)
            skor += 6 if ok else 0
            rincian.append(f"{'✓' if ok else '•'} {label}: {6 if ok else 0}/6")
        ada_pembeda = any(x in teks for x in ["sedangkan", "berbeda", "sementara", "perbedaannya", "dibandingkan"])
        skor += 2 if ada_pembeda else 0
        rincian.append(f"{'✓' if ada_pembeda else '•'} Menunjukkan perbedaan antarjenis: {2 if ada_pembeda else 0}/2")

    elif nomor == 4:
        langkah = [
            ("Menentukan tema/topik/objek", ["menentukan topik", "menentukan tema", "memilih objek", "menentukan objek"]),
            ("Mengamati objek dan mengumpulkan/mencatat data", ["mengamati", "observasi", "mengumpulkan data", "mencatat", "pancaindra"]),
            ("Menentukan pola dan/atau menyusun kerangka", ["pola pengembangan", "menentukan pola", "kerangka", "menyusun kerangka"]),
            ("Mengembangkan kerangka menjadi teks/paragraf", ["mengembangkan", "mengembangkan kerangka", "menulis paragraf", "menyusun paragraf"]),
            ("Menyunting/memeriksa teks", ["menyunting", "memeriksa", "ejaan", "tanda baca", "memperbaiki"])
        ]
        jumlah = 0
        for label, kunci in langkah:
            ok = cocok_salah_satu(teks, kunci)
            jumlah += 1 if ok else 0
            rincian.append(f"{'✓' if ok else '•'} {label}: {'terdeteksi' if ok else 'belum terdeteksi'}")
        skor = jumlah * 4
        urutan_penanda = any(x in teks for x in ["pertama", "kemudian", "selanjutnya", "setelah itu", "terakhir", "lalu"])
        if urutan_penanda:
            skor = min(20, skor + (2 if skor <= 18 else 0))
            # Batasi agar skor maksimal 20; indikator urutan hanya membantu, bukan menggandakan nilai.
        rincian.append(f"Indikator langkah terdeteksi: {jumlah} dari 5.")
        if not urutan_penanda:
            rincian.append("Urutan langkah belum ditandai secara jelas (misalnya pertama, selanjutnya, terakhir).")

    elif nomor == 5:
        # Mengacu pada dokumen indikator penilaian teks deskripsi:
        # Judul (4 indikator), Identifikasi (4), Deskripsi Bagian (5), Penutup (4).
        # Deteksi otomatis hanya perkiraan awal; guru tetap dapat memeriksa/mengoreksi.
        teks_asli = (jawaban or "").strip()
        baris = [b.strip() for b in teks_asli.splitlines() if b.strip()]
        kalimat = [bagian.strip() for bagian in re.split(r"(?<=[.!?])\\s+|\\n+", teks_asli) if bagian.strip()]
        kata_list = re.findall(r"\\b[\\wÀ-ÿ'-]+\\b", teks, flags=re.UNICODE)
        jumlah_kata = len(kata_list)

        # Aspek 1: Judul
        judul = baris[0] if baris else ""
        judul_kata = re.findall(r"\\b[\\wÀ-ÿ'-]+\\b", judul, flags=re.UNICODE)
        judul_frasa = bool(judul) and len(judul_kata) <= 10 and not re.search(r"[.!?]$", judul)
        judul_objek = bool(judul) and any(k in normalisasi_jawaban(judul) for k in [
            "sekolah", "rumah", "kelas", "perpustakaan", "taman", "pantai",
            "pasar", "masjid", "kucing", "ibu", "ayah", "sahabat", "lingkungan"
        ])
        judul_kapital = bool(judul) and (judul[0].isupper() or judul.isupper())
        judul_tanpa_titik = bool(judul) and not judul.endswith(".")
        indikator_judul = [judul_objek or len(judul_kata) >= 1, judul_frasa, judul_kapital, judul_tanpa_titik]
        skor_judul = max(1, sum(indikator_judul)) if judul else 1
        rincian.append(f"Judul: terdeteksi {sum(indikator_judul)}/4 indikator (perkiraan skor aspek {skor_judul}/4).")

        # Aspek 2: Identifikasi
        awal = " ".join(kalimat[:2]).lower()
        objek_dikenalkan = bool(awal) and any(k in awal for k in [
            "adalah", "merupakan", "bernama", "terletak", "berada", "yaitu",
            "saya", "kami", "di ", "sebuah", "seorang", "tempat"
        ])
        info_umum = bool(awal) and len(awal.split()) >= 8
        kalimat_awal_memadai = bool(awal) and any(x in awal for x in ["adalah", "merupakan", "memiliki", "terletak", "berada", "yang"])
        tanda_baca_awal = bool(awal) and bool(re.search(r"[.!?,]", " ".join(kalimat[:2])))
        indikator_identifikasi = [objek_dikenalkan, info_umum, kalimat_awal_memadai, tanda_baca_awal]
        skor_identifikasi = max(1, sum(indikator_identifikasi))
        rincian.append(f"Identifikasi: terdeteksi {sum(indikator_identifikasi)}/4 indikator (perkiraan skor aspek {skor_identifikasi}/4).")

        # Aspek 3: Deskripsi Bagian
        kata_detail = [
            "warna", "berwarna", "bentuk", "ukuran", "tinggi", "rendah", "luas",
            "sempit", "besar", "kecil", "panjang", "pendek", "bersih", "kotor",
            "rapi", "indah", "ramai", "sepi", "tenang", "nyaman", "asri",
            "gelap", "terang", "cerah", "lembut", "kasar", "halus", "dingin",
            "hangat", "sejuk", "harum", "aroma", "suara", "terdengar", "terlihat",
            "tampak", "terasa", "memiliki", "terdapat", "di sebelah", "di depan",
            "di belakang", "di dalam", "di luar", "berdiri", "tumbuh", "tersusun",
            "dipenuhi", "berjejer", "berderet", "berkilau", "nyaman", "indah"
        ]
        jumlah_detail = sum(1 for istilah in set(kata_detail) if istilah in teks)
        detail_terperinci = jumlah_kata >= 35 and jumlah_detail >= 3
        bagian_ciri = jumlah_detail >= 2
        kalimat_beragam = len(kalimat) >= 3
        kosakata_bervariasi = len(set(kata_list)) >= min(20, max(8, jumlah_kata * 0.45))
        tanda_baca = bool(re.search(r"[.!?]", teks_asli))
        indikator_deskripsi = [detail_terperinci, bagian_ciri, kalimat_beragam, kosakata_bervariasi, tanda_baca]
        # Dokumen sumber memberi skor 2 untuk 2–3 indikator; terapkan aturan itu secara eksplisit.
        jumlah_deskripsi = sum(indikator_deskripsi)
        skor_deskripsi = 4 if jumlah_deskripsi == 5 else 3 if jumlah_deskripsi == 4 else 2 if jumlah_deskripsi in (2, 3) else 1
        rincian.append(f"Deskripsi Bagian: terdeteksi {jumlah_deskripsi}/5 indikator (perkiraan skor aspek {skor_deskripsi}/4).")
        rincian.append(f"Petunjuk detail deskriptif yang terdeteksi: {jumlah_detail}.")

        # Aspek 4: Penutup
        akhir = " ".join(kalimat[-2:]).lower()
        simpulan_tanggapan = bool(akhir) and any(k in akhir for k in [
            "kesimpulan", "jadi", "menurut saya", "bagi saya", "saya menilai",
            "saya berpendapat", "dapat disimpulkan", "secara keseluruhan"
        ])
        kesan = bool(akhir) and any(k in akhir for k in [
            "suka", "menyukai", "senang", "nyaman", "indah", "menarik",
            "mengesankan", "menyenangkan", "menurut saya", "bagi saya",
            "membuat saya", "saya merasa", "favorit"
        ])
        penutup_kosakata = bool(akhir) and len(set(akhir.split())) >= 6
        penutup_tanda_baca = bool(akhir) and bool(re.search(r"[.!?]$", akhir.strip()))
        indikator_penutup = [simpulan_tanggapan, kesan, penutup_kosakata, penutup_tanda_baca]
        skor_penutup = max(1, sum(indikator_penutup))
        rincian.append(f"Penutup: terdeteksi {sum(indikator_penutup)}/4 indikator (perkiraan skor aspek {skor_penutup}/4).")

        # Rubrik asli maksimum 16; dikonversi proporsional ke skala 20 agar konsisten
        # dengan empat soal esai lainnya di aplikasi.
        total_rubrik_16 = skor_judul + skor_identifikasi + skor_deskripsi + skor_penutup
        skor = round(total_rubrik_16 / 16 * 20)
        rincian.append(f"Total rubrik dokumen: {total_rubrik_16}/16; dikonversi menjadi {skor}/20.")
        rincian.append(
            "Catatan: sistem hanya memperkirakan indikator dari pola kata dan tanda baca. "
            "Skor akhir sebaiknya diperiksa guru karena aplikasi tanpa AI semantik tidak dapat "
            "memastikan makna, ketepatan struktur, atau kualitas bahasa secara menyeluruh."
        )
    else:
        return {"skor": 0, "maksimal": 20, "rincian": ["Nomor soal tidak dikenali."],
                "umpan_balik": "Periksa nomor soal."}

    skor = max(0, min(20, int(skor)))
    if skor == 20:
        umpan_balik = "Sangat baik! Jawaban memenuhi seluruh indikator rubrik otomatis. Periksa kembali isi dan ejaan untuk memastikan ketepatannya."
    elif skor >= 16:
        umpan_balik = "Baik. Jawaban sudah memuat sebagian besar indikator rubrik."
    elif skor >= 10:
        umpan_balik = "Cukup. Periksa indikator yang belum terdeteksi dan lengkapi jawaban."
    else:
        umpan_balik = "Jawaban masih perlu dikembangkan. Baca kembali pertanyaan dan tuliskan unsur pentingnya."
    return {"skor": skor, "maksimal": 20, "rincian": rincian, "umpan_balik": umpan_balik}


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
    st.caption("Tanyakan dengan bahasa sehari-hari. Jawaban diambil dari materi yang tersedia, tanpa API berbayar. 💡")

    pertanyaan = st.text_area(
        "Apa yang ingin kamu ketahui?",
        placeholder="Contoh: teks deskripsi itu apa? / Apa ciri-cirinya? / Bagaimana cara membuatnya?",
        height=110,
        key="pertanyaan_cari_materi"
    )

    tombol = st.button("🔍 CARI JAWABAN", use_container_width=True)

    if tombol:
        if not pertanyaan.strip():
            st.warning("Tulis pertanyaan terlebih dahulu, ya.")
        else:
            # Gabungkan file TXT dan delapan materi bawaan pada aplikasi.
            sumber_pencarian = list(database)
            for materi in MATERI_DESKRIPSI:
                sumber_pencarian.append({
                    "nama_file": f"Materi bawaan - {materi['judul']}",
                    "isi": f"{materi['judul']}\n{materi.get('ringkas', '')}\n{materi.get('isi', '')}"
                })

            with st.spinner("Mencari bagian materi yang paling sesuai..."):
                hasil = cari_materi(pertanyaan, sumber_pencarian)

            if not hasil or hasil[0]["skor"] < 2:
                st.warning("Aku belum menemukan jawaban yang cukup sesuai di materi yang tersedia.")
                st.write("Coba tanyakan dengan kata kunci lain, misalnya nama jenis teks, ciri-ciri, struktur, tujuan, atau langkah-langkah.")
            else:
                hasil_utama = hasil[0]
                jawaban = ambil_potongan_relevan(pertanyaan, hasil_utama["isi"], 2200)

                if jawaban:
                    st.subheader("💡 Jawaban dari materi")
                    st.markdown(jawaban)
                    st.caption("Jawaban disusun dari bagian materi yang paling cocok dengan pertanyaan. Sistem ini tidak menggunakan API berbayar.")
                    st.subheader("📚 Sumber")
                    st.write(hasil_utama["nama_file"])
                else:
                    st.warning("Topik yang mirip ditemukan, tetapi bagian jawaban yang tepat belum dapat diambil. Coba gunakan pertanyaan yang lebih spesifik.")

                materi_lain = [item for item in hasil[1:4] if item["skor"] >= 2]
                if materi_lain:
                    st.subheader("📑 Materi terkait")
                    for item in materi_lain:
                        with st.expander(item["nama_file"]):
                            potongan = ambil_potongan_relevan(pertanyaan, item["isi"], 900)
                            st.write(potongan if potongan else item["isi"][:900])


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
    # ESAI - PENILAIAN OTOMATIS BERBASIS RUBRIK
    # =====================================================

    else:

        st.subheader("B. ESAI")
        st.write("Jawablah kelima pertanyaan dengan jelas dan lengkap.")
        st.caption("Untuk soal nomor 5, tulis judul pada baris pertama, lalu lanjutkan dengan bagian identifikasi, deskripsi bagian, dan penutup.")
        st.info(
            "Soal 1–4 dinilai dengan kata kunci materi. Khusus soal 5, penilaian "
            "mengadaptasi empat aspek dalam dokumen indikator: judul, identifikasi, "
            "deskripsi bagian, dan penutup. Nilai otomatis adalah perkiraan awal; "
            "guru perlu memeriksa jawaban untuk hasil yang adil."
        )

        nama_siswa_esai = st.text_input(
            "Nama siswa (opsional)",
            key="nama_siswa_esai",
            placeholder="Masukkan nama untuk hasil penilaian"
        )
        jawaban_esai = {}

        with st.form("form_penilaian_esai"):
            for soal in SOAL_ESAI:
                st.markdown(f"### {soal['nomor']}. {soal['pertanyaan']}")
                jawaban_esai[soal["nomor"]] = st.text_area(
                    f"Jawaban soal {soal['nomor']}:",
                    height=140,
                    key=f"esai_{soal['nomor']}",
                    placeholder="Tuliskan jawaban Anda di sini. Untuk soal 5, tulis judul pada baris pertama, kemudian identifikasi, deskripsi bagian, dan penutup..."
                )
            nilai_otomatis = st.form_submit_button(
                "🧮 NILAIKAN JAWABAN ESAI",
                use_container_width=True
            )

        if nilai_otomatis:
            jumlah_terisi = sum(1 for jawaban in jawaban_esai.values() if jawaban.strip())
            if jumlah_terisi < len(SOAL_ESAI):
                st.warning(
                    f"Baru {jumlah_terisi} dari {len(SOAL_ESAI)} jawaban terisi. "
                    "Lengkapi semua jawaban sebelum menghitung nilai."
                )
            else:
                hasil_esai = []
                for soal in SOAL_ESAI:
                    hasil = nilai_esai(soal["nomor"], jawaban_esai[soal["nomor"]])
                    hasil_esai.append({
                        "nomor": soal["nomor"],
                        "pertanyaan": soal["pertanyaan"],
                        "jawaban": jawaban_esai[soal["nomor"]],
                        "skor": hasil["skor"],
                        "maksimal": hasil["maksimal"],
                        "rincian": hasil["rincian"],
                        "umpan_balik": hasil["umpan_balik"]
                    })

                total_skor_esai = sum(item["skor"] for item in hasil_esai)
                nilai_akhir_esai = round(total_skor_esai / (len(SOAL_ESAI) * 20) * 100)

                st.session_state["hasil_esai_terakhir"] = {
                    "nama": nama_siswa_esai.strip() or "Siswa",
                    "hasil": hasil_esai,
                    "total": total_skor_esai,
                    "nilai": nilai_akhir_esai
                }

        hasil_terakhir = st.session_state.get("hasil_esai_terakhir")
        if hasil_terakhir:
            st.divider()
            st.subheader("📊 Hasil Penilaian Esai")
            col1, col2, col3 = st.columns(3)
            col1.metric("Nama", hasil_terakhir["nama"])
            col2.metric("Total skor", f"{hasil_terakhir['total']}/100")
            col3.metric("Nilai akhir", hasil_terakhir["nilai"])

            for item in hasil_terakhir["hasil"]:
                with st.expander(
                    f"Soal {item['nomor']} — Skor {item['skor']}/{item['maksimal']}",
                    expanded=(item["skor"] < 16)
                ):
                    st.markdown("**Jawaban siswa**")
                    st.write(item["jawaban"])
                    st.markdown("**Indikator rubrik**")
                    for baris in item["rincian"]:
                        st.write(baris)
                    st.info(item["umpan_balik"])

            st.caption(
                "Nilai ini dihitung dengan rubrik berbasis indikator/kata kunci, "
                "bukan penilaian semantik AI. Gunakan penilaian guru sebagai pemeriksaan "
                "akhir untuk keputusan nilai resmi."
            )

            # Koreksi guru khusus soal 5 mengikuti rubrik sumber (skala 1–4 per aspek).
            item5 = next((item for item in hasil_terakhir["hasil"] if item["nomor"] == 5), None)
            if item5:
                with st.expander("👩‍🏫 Koreksi Guru untuk Soal 5 (opsional)", expanded=False):
                    st.write(
                        "Periksa hasil otomatis dengan rubrik indikator. Pilih skor berdasarkan "
                        "indikator yang benar-benar terpenuhi pada tulisan siswa."
                    )
                    with st.form("form_koreksi_guru_soal5"):
                        st.caption("Skala sumber: 1–4 per aspek; skor maksimal 16, dikonversi ke skala 20.")
                        c1, c2 = st.columns(2)
                        with c1:
                            koreksi_judul = st.select_slider("Judul", options=[1, 2, 3, 4], value=1, key="koreksi_q5_judul")
                            koreksi_identifikasi = st.select_slider("Identifikasi", options=[1, 2, 3, 4], value=1, key="koreksi_q5_identifikasi")
                        with c2:
                            koreksi_deskripsi = st.select_slider("Deskripsi Bagian", options=[1, 2, 3, 4], value=1, key="koreksi_q5_deskripsi")
                            koreksi_penutup = st.select_slider("Penutup", options=[1, 2, 3, 4], value=1, key="koreksi_q5_penutup")
                        simpan_koreksi = st.form_submit_button("Simpan Koreksi Guru", use_container_width=True)
                    if simpan_koreksi:
                        total_koreksi_16 = koreksi_judul + koreksi_identifikasi + koreksi_deskripsi + koreksi_penutup
                        skor_koreksi_20 = round(total_koreksi_16 / 16 * 20)
                        hasil_baru = dict(hasil_terakhir)
                        hasil_baru["hasil"] = [dict(x) for x in hasil_terakhir["hasil"]]
                        for x in hasil_baru["hasil"]:
                            if x["nomor"] == 5:
                                x["skor_otomatis"] = x["skor"]
                                x["skor"] = skor_koreksi_20
                                x["rincian"].append(
                                    f"Koreksi guru: Judul {koreksi_judul}/4; Identifikasi {koreksi_identifikasi}/4; "
                                    f"Deskripsi Bagian {koreksi_deskripsi}/4; Penutup {koreksi_penutup}/4 "
                                    f"= {total_koreksi_16}/16, dikonversi menjadi {skor_koreksi_20}/20."
                                )
                                x["umpan_balik"] = "Skor soal 5 telah disesuaikan berdasarkan pemeriksaan guru."
                        hasil_baru["total"] = sum(x["skor"] for x in hasil_baru["hasil"])
                        hasil_baru["nilai"] = round(hasil_baru["total"] / (len(SOAL_ESAI) * 20) * 100)
                        st.session_state["hasil_esai_terakhir"] = hasil_baru
                        st.success("Koreksi guru tersimpan. Hasil penilaian diperbarui.")
                        st.rerun()

            csv_header = "Nama,Nomor Soal,Skor,Maksimal,Jawaban,Umpan Balik\n"
            csv_rows = []
            for item in hasil_terakhir["hasil"]:
                fields = [
                    hasil_terakhir["nama"],
                    str(item["nomor"]),
                    str(item["skor"]),
                    str(item["maksimal"]),
                    item["jawaban"].replace('"', '""'),
                    item["umpan_balik"].replace('"', '""')
                ]
                csv_rows.append(",".join(f'"{field}"' for field in fields))
            csv_data = csv_header + "\n".join(csv_rows)
            st.download_button(
                "⬇️ Unduh hasil penilaian (CSV)",
                data=csv_data.encode("utf-8-sig"),
                file_name="hasil_penilaian_esai.csv",
                mime="text/csv",
                use_container_width=True
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