import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

uiApp = tk.Tk()

uiApp.configure(background='dodgerblue')
uiApp.geometry("700x700")
uiApp.resizable(False, False)
uiApp.title("Nilai Tabel Siswa")

inputFrame = ttk.Frame(uiApp)
inputFrame.pack(padx=10, fill="x", expand=True)

# Membuat Variabel nama dan inputnya
inputLabel = tk.Label(inputFrame, text="Nilai Tabel Siswa")
inputLabel.pack(padx=10, pady=10, fill="x", expand=True)

# Membuat Variabel nama dan inputnya
nama_Siswa = ttk.Label(inputFrame, text="Masukkan nama siswa : ")
nama_Siswa.pack(padx=10, pady=0, fill="x", expand=True)

entrynama_Siswa = ttk.Entry(inputFrame)
entrynama_Siswa.pack(padx=10, pady=0, fill="x", expand=True)

# Membuat Variabel nilai biologi dan inputnya
nilai_biologi = ttk.Label(inputFrame, text="Masukkan nilai biologi : ")
nilai_biologi.pack(padx=10, pady=0, fill="x", expand=True)

entrynilai_biologi = ttk.Entry(inputFrame)
entrynilai_biologi.pack(padx=10, pady=0, fill="x", expand=True)

# Membuat Variabel nilai fisika dan inputnya
nilai_fisika = ttk.Label(inputFrame, text="Masukkan nilai fisika : ")
nilai_fisika.pack(padx=10, pady=0, fill="x", expand=True)

entrynilai_fisika = ttk.Entry(inputFrame)
entrynilai_fisika.pack(padx=10, pady=0, fill="x", expand=True)

# Membuat Variabel nilai biggris dan inputnya
nilai_binggris = ttk.Label(inputFrame, text="Masukkan nilai bahasa inggris : ")
nilai_binggris.pack(padx=10, pady=0, fill="x", expand=True)

entrynilai_binggris = ttk.Entry(inputFrame)
entrynilai_binggris.pack(padx=10, pady=0, fill="x", expand=True)

# Membuat Variabel prediksi fakultas
labelPrediksiFakultas = ttk.Label(inputFrame, text="Prediksi")
labelPrediksiFakultas.pack(padx=10, pady=5, fill="x", expand=True)

def klikButton():
    namasiswa = entrynama_Siswa.get()
    biologi = int(entrynilai_biologi.get())
    fisika = int(entrynilai_fisika.get())
    inggris = int(entrynilai_binggris.get())

    if biologi > fisika and biologi > inggris:
        prediksi_fakultas = "Kedokteran"
    elif fisika > biologi and fisika > inggris:
        prediksi_fakultas = "Teknik"
    elif inggris > biologi and inggris > fisika:
        prediksi_fakultas = "Bahasa"
    else:
        prediksi_fakultas = "Tidak dapat diprediksi"

    messagebox.showinfo("Hasil prediksi", f"\nHasil Prediksi Prodi {prediksi_fakultas}!")
    
    simpan_data_ke_sqlite(biologi, fisika, inggris, prediksi_fakultas, namasiswa)

def simpan_data_ke_sqlite(nilai_biologi, nilai_fisika, nilai_inggris, prodi_terpilih, namasiswa):
    conn = sqlite3.connect("prodidb.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      nama_siswa TEXT,
                      biologi INTEGER, 
                      fisika INTEGER,
                      inggris INTEGER,
                      prediksi_fakultas TEXT)''')
    cursor.execute("INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas) VALUES (?, ?, ?, ?, ?)",
                   (namasiswa, nilai_biologi, nilai_fisika, nilai_inggris, prodi_terpilih))
    conn.commit()
    conn.close()

tombolSubmit = ttk.Button(inputFrame, text="Hasil Prediksi", command=klikButton)
tombolSubmit.pack(pady=10)

uiApp.mainloop()
