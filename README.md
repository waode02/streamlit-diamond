# 💎 Diamond Price Predictor

Aplikasi web untuk memprediksi harga berlian menggunakan Machine Learning.

## 📌 Deskripsi

Project ini menggunakan model **XGBoost** untuk memprediksi harga berlian berdasarkan karakteristiknya seperti carat, cut, color, clarity, serta dimensi berlian.

Aplikasi dibuat menggunakan **Streamlit** sehingga pengguna dapat memasukkan data berlian dan langsung mendapatkan estimasi harga.

## ⚙️ Teknologi yang Digunakan

* Python
* Streamlit
* XGBoost
* Scikit-learn
* Pandas
* NumPy

## 📊 Fitur Input

Pengguna dapat memasukkan beberapa informasi berlian seperti:

* Carat (berat berlian)
* Depth (%)
* Table (%)
* Dimensi berlian (x, y, z)
* Cut
* Color
* Clarity

Aplikasi kemudian akan memprediksi estimasi harga berlian.

## 📂 Struktur Project

app.py
best_diamond_model.pkl
featuresa_couloms.pkl
requirements.txt
README.md

## 🚀 Menjalankan Aplikasi

Install library:

pip install -r requirements.txt

Jalankan aplikasi:

streamlit run app.py

## 👩‍💻 Author

Project ini dibuat sebagai bagian dari pembelajaran Machine Learning dan deployment aplikasi menggunakan Streamlit.
