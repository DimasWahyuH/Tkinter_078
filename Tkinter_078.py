import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menghitung rata-rata dan memberikan hasil prediksi prodi
def hasil_prediksi():
    try:
        # Mengambil nilai dari setiap input dan menghitung rata-rata
        total = 0
        for entry in inputs:
            nilai = entry.get()
            
            # Pengecekan apakah input kosong
            if not nilai.strip():
                raise ValueError("Semua nilai harus diisi.")
            
            # Pengecekan apakah input berupa angka
            if not nilai.isdigit():
                raise ValueError("Nilai harus berupa angka.")
            
            # Menjumlahkan nilai yang diinputkan
            total += int(nilai)
        
        # Menghitung rata-rata nilai
        rata_rata = total / len(inputs)
        
        # Menentukan prodi berdasarkan rata-rata nilai
        if rata_rata >= 80:
            prodi = "Teknologi Informasi"
            penjelasan = "Selamat! Anda cocok untuk masuk ke prodi Teknologi Informasi."
        else:
            prodi = "Tidak ada prodi yang cocok"
            penjelasan = "Maaf, Anda belum memenuhi syarat untuk prodi Teknologi Informasi."
        
        # Menampilkan hasil prediksi pada label hasil
        label_hasil.config(text=f"Prodi Pilihan: {prodi}\n{penjelasan}")

    except ValueError as e:
        # Menampilkan pesan kesalahan jika terjadi ValueError
        messagebox.showerror("Input Error", str(e))

# Membuat window utama
window = tk.Tk()
window.title("Aplikasi Prediksi Prodi Pilihan")
window.geometry("600x800")

# Label judul aplikasi
judul = tk.Label(window, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"))
judul.pack(pady=20)

# Membuat daftar label dan input untuk 10 mata pelajaran
inputs = []
for i in range(1, 11):
    label = tk.Label(window, text=f"Nilai Mata Pelajaran {i}:", anchor="w")
    label.pack(fill="x", padx=20)
    
    entry = tk.Entry(window)
    entry.pack(padx=20, pady=5)
    inputs.append(entry)

# Tombol untuk memproses prediksi
button_prediksi = tk.Button(window, text="Hasil Prediksi", command=hasil_prediksi)
button_prediksi.pack(pady=20)

# Label untuk menampilkan hasil prediksi
label_hasil = tk.Label(window, text="", font=("Arial", 14), fg="blue")
label_hasil.pack(pady=20)

