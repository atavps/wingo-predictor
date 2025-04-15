
import pandas as pd
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.plot import Plot
from rich.rule import Rule
import sys
import os
import time

console = Console()
PASSFILE = "password.txt"

def read_password():
    if os.path.exists(PASSFILE):
        with open(PASSFILE, "r") as f:
            return f.read().strip()
    else:
        return "wingo123"

def save_password(new_pass):
    with open(PASSFILE, "w") as f:
        f.write(new_pass)

def ganti_password():
    new_pass = input("Masukkan password baru: ")
    save_password(new_pass)
    console.print("[green]Password berhasil diganti![/green]\n")

def lihat_panduan():
    console.print(Panel("""
Panduan Penggunaan:

1. Pilih 'Mulai Prediksi'.
2. Masukkan password terlebih dahulu.
3. Masukkan data warna & angka terakhir.
4. Hasil prediksi dan grafik tren akan ditampilkan.
5. Gunakan menu 'Ganti Password' untuk mengubah sandi login.
""", title="Panduan Penggunaan", border_style="cyan"))
    input("Tekan Enter untuk kembali ke menu...")

def login_prediksi():
    pw = read_password()
    user_input = input("Masukkan password: ")
    if user_input != pw:
        console.print("\n[red]Password salah! Akses ditolak.[/red]")
        sys.exit()
    console.print("\n[green]Login berhasil![/green]\n")
    console.print(Panel("""
Jika mengalami kesulitan atau butuh bantuan:
📞 WA   : 0812-3456-7890
📧 Email: support@wingotools.com
""", title="Kontak Bantuan", border_style="magenta"))

def prediksi():
    login_prediksi()
    history = []
    for i in range(5):
        console.print(f"[magenta]Input Data #{i+1}:[/magenta]")
        warna = input("  Warna (Merah/Hijau/Ungu): ").capitalize()
        angka = int(input("  Angka (0-9)              : "))
        history.append({"Warna": warna, "Angka": angka})

    df = pd.DataFrame(history)
    last_colors = df["Warna"].value_counts()
    avg_number = df["Angka"].mean()
    predicted_color = last_colors.idxmin()
    predicted_number = "kecil (0-4)" if avg_number > 5 else "besar (5-9)"

    table = Table(title="Analisis Warna (5 Input)", show_lines=True, style="black on yellow")
    table.add_column("Warna", justify="center", style="red")
    table.add_column("Jumlah", justify="center", style="blue")
    for color, count in last_colors.items():
        table.add_row(color, str(count))
    console.print(table)

    panel = Panel.fit(f"""\nWarna      : {predicted_color}\nAngka      : {predicted_number}\nRata-rata  : {round(avg_number, 2)}\n""", title="Hasil Prediksi", border_style="black")
    console.print(panel)

    console.print(Rule("GRAFIK TREND ANGKA"))
    plot = Plot(width=40, height=10)
    plot.add_series("Angka", df["Angka"].tolist())
    console.print(plot)
    input("\nTekan Enter untuk kembali ke menu...")

# === MENU UTAMA ===
while True:
    console.print(Panel.fit("""
=== MENU UTAMA ===
1. Mulai Prediksi
2. Ganti Password
3. Lihat Panduan
4. Keluar
""", title="Selamat Datang", border_style="green"))
    pilihan = input("Pilihan Anda (1/2/3/4): ")

    if pilihan == "1":
        prediksi()
    elif pilihan == "2":
        ganti_password()
    elif pilihan == "3":
        lihat_panduan()
    elif pilihan == "4":
        console.print("\n[yellow]Terima kasih telah menggunakan aplikasi prediksi Wingo![/yellow]")
        time.sleep(1)
        break
    else:
        console.print("[red]Pilihan tidak valid![/red]\n")
