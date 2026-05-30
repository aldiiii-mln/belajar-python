"""
x = 10

def ubah():
    global x  # beritahu Python: x ini adalah variabel global
    x = 99


print(x)  # 99 — sekarang global x berubah
"""

def hitung_total(harga, jumlah):
    return harga * jumlah

def hitung_pajak(total, persen_pajak=11):
    return total + (total*persen_pajak/100)

def cetak_struk(nama_barang, harga, jumlah):
    print("==== STRUK BELANJA ====")
    print(f"Barang  : {nama_barang}")
    print(f"Harga   : Rp {harga}")
    print(f"Jumlah  : {jumlah}")
    total = hitung_total(harga, jumlah)
    print(f"Total   : Rp {total}")
    pajak = int(hitung_pajak(total))
    print(f"Pajak   : Rp {pajak}")
    print("=======================")

cetak_struk("Laptop", 8000000, 2)

