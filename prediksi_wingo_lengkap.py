
import time
from datetime import datetime, timedelta

password_default = "wingo123"
riwayat_prediksi = []
user_password = password_default

def login():
    print("=== LOGIN APLIKASI PREDIKSI WINGO ===")
    print("[!] Trial mode tersedia selama 3 menit.")
    pw = input("Masukkan password (Enter untuk trial): ")
    if pw == "":
        print(">>> Login sebagai trial. Anda punya waktu 3 menit.")
        return datetime.now() + timedelta(minutes=3)
    elif pw == user_password:
        print(">>> Login berhasil.")
        return None
    else:
        print("Password salah.")
        return login()

def menu_utama():
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Mulai Prediksi")
        print("2. Tentang Aplikasi")
        print("3. Kontak Kami")
        print("4. Ganti Password")
        print("5. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        if pilihan == "1":
            mulai_prediksi()
        elif pilihan == "2":
            tentang_aplikasi()
        elif pilihan == "3":
            kontak_kami()
        elif pilihan == "4":
            ganti_password()
        elif pilihan == "5":
            break

def mulai_prediksi():
    global riwayat_prediksi
    waktu_akhir = login()
    while True:
        if waktu_akhir and datetime.now() > waktu_akhir:
            print(">>> Waktu trial habis. Silakan login ulang.")
            break
        print("\n=== MULAI PREDIKSI ===")
        periode = input("Masukkan Periode: ")
        warna = input("Masukkan Warna (Merah/Hijau/Ungu): ")
        angka = int(input("Masukkan Angka (0-9): "))
        kategori = input("Masukkan Kategori (Besar/Kecil): ")

        print("\n=== PILIH MODE PREDIKSI ===")
        print("1. Countdown 30 Detik")
        print("2. Countdown 1 Menit")
        mode = input("Pilihan Anda: ")
        if mode == "1":
            countdown(30)
        elif mode == "2":
            countdown(60)

        warna_pred = warna
        angka_pred = "besar (0-4 kecil, 5-9 besar)" if angka >= 5 else "kecil (0-4 kecil, 5-9 besar)"
        kategori_pred = kategori
        waktu_pred = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("\n=== HASIL PREDIKSI ===")
        print(f"Periode Selanjutnya : {periode}")
        print(f"Prediksi Warna      : {warna_pred}")
        print(f"Prediksi Angka      : {angka_pred}")
        print(f"Prediksi Kategori   : {kategori_pred}")
        print(f"Waktu Prediksi      : {waktu_pred}")

        riwayat_prediksi.append(f"[{waktu_pred}] Warna: {warna} | Angka: {angka} | Kategori: {kategori}")
        print("\n=== RIWAYAT PREDIKSI ===")
        for i, r in enumerate(reversed(riwayat_prediksi[-5:]), 1):
            print(f"{i}. {r}")
        break

def countdown(waktu):
    print(f"\nCountdown dimulai: {waktu} detik")
    for i in range(waktu, 0, -1):
        print(f"  {i} detik", end="\r")
        time.sleep(1)
    print("Waktu selesai!")

def tentang_aplikasi():
    print("\n=== TENTANG APLIKASI ===")
    print("Aplikasi ini membantu memprediksi warna, angka, dan kategori")
    print("berdasarkan data input dari permainan Wingo secara manual.")

def kontak_kami():
    print("\n=== KONTAK KAMI ===")
    print("Jika mengalami kendala atau butuh bantuan:")
    print("WhatsApp : wa.me/6281234567890")
    print("Telegram : t.me/wingosupport")

def ganti_password():
    global user_password
    print("\n=== GANTI PASSWORD ===")
    current = input("Masukkan password lama: ")
    if current == user_password:
        new_pw = input("Masukkan password baru: ")
        user_password = new_pw
        print("Password berhasil diubah!")
    else:
        print("Password lama salah.")
