import re
import time

# Teks input
teks = """
Berikut adalah daftar email dan nama pengguna dari mailing list:
anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi anwari
slamet@getnada.com dimiliki oleh slamet slumut
matahari@tokopedia.com dimiliki oleh toko matahari
"""

# Daftar huruf kecil, huruf besar, dan angka
karakter = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

# Fungsi buat password random 8 karakter
def generate_password(length=8):
    password = ''
    t = int(time.time() * 1000)  # Ambil waktu sekarang dalam milidetik
    for i in range(length):
        index = (t + i * 17) % len(karakter)  # Modulo jumlah karakter
        password += karakter[index]
    return password

# Cari semua email
email_list = re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', teks)

# Proses tiap email
for email in email_list:
    username = email.split('@')[0]
    password = generate_password()
    print(f"{email} username: {username} , password: {password}")
