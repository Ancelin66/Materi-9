import re

# Teks input
teks = """
Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan
nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki
Hajar Dewantara (1889-05-02).
"""

# Fungsi bantu: cek apakah tahun kabisat
def is_kabisat(tahun):
    return tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0)

# Fungsi bantu: hitung jumlah hari dari 0000-01-01 sampai tahun-bulan-hari tertentu
def hitung_total_hari(tahun, bulan, hari):
    # Jumlah hari tiap bulan (biasa)
    hari_per_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    total_hari = 0

    # Tambah hari dari tahun-tahun penuh
    for t in range(0, tahun):
        total_hari += 366 if is_kabisat(t) else 365

    # Tambah hari dari bulan-bulan penuh di tahun ini
    for b in range(1, bulan):
        if b == 2 and is_kabisat(tahun):
            total_hari += 29
        else:
            total_hari += hari_per_bulan[b-1]
    
    # Tambah hari berjalan di bulan ini
    total_hari += hari

    return total_hari

tahun_sekarang = 2025
bulan_sekarang = 4
hari_sekarang = 28

total_hari_sekarang = hitung_total_hari(tahun_sekarang, bulan_sekarang, hari_sekarang)

tanggal_ditemukan = re.findall(r'\d{4}-\d{2}-\d{2}', teks)

# Proses setiap tanggal
for tgl in tanggal_ditemukan:
    tahun, bulan, hari = map(int, tgl.split('-'))

    total_hari_tanggal = hitung_total_hari(tahun, bulan, hari)
    selisih = total_hari_sekarang - total_hari_tanggal

    # Format DD-MM-YYYY
    tgl_format_baru = f"{hari:02d}-{bulan:02d}-{tahun}"

    print(f"{tgl_format_baru} {tahun}-{bulan:02d}-{hari:02d} 00:00:00 selisih {selisih} hari")
