

def menu():
    
    daftar_menu = [
        {"nama": "Nasi Goreng", "harga": 15000, "kategori": "Makanan"},
        {"nama": "Mie Ayam", "harga": 12000, "kategori": "Makanan"},
        {"nama": "Es Teh", "harga": 5000, "kategori": "Minuman"},
        {"nama": "Kopi", "harga": 8000, "kategori": "Minuman"}
    ]

    return daftar_menu


def tampil_menu(daftar):
    no_urut = 1
    print("==== MENU ====")
    for menuu in daftar:
        print(f"{no_urut}. {menuu['nama']} | {menuu['harga']} | {menuu['kategori']}")
        no_urut += 1

def input_pesanan(pesanan, daftar):
    
    while True:
        ditemukan = False
        inputt = input("Pesan apa? (ketik 'selesai' untuk berhenti) : ")
        if inputt == "selesai":
            break
        for menuu in daftar:
            if inputt == menuu["nama"]:
                print(f"{inputt} ditambahkan ke keranjang!")
                ditemukan = True
                pesanan.append(inputt)
            
        if not ditemukan:
            print("Menu tidak ditemukan")

def hitung_pajak(total, persen_pajak=11):
    return total + (total*persen_pajak/100)

def cetak_struk(pesanan, daftar):

    """
    pesanan = []

    input_pesanan(pesanan)

    print(pesanan)
    """
    print("==== STRUK ====")
    total = 0

    no_urut = 1
    for i in pesanan:
        for j in daftar:
            if i == j["nama"]:
                print(f"{no_urut}. {i} {j['harga']}")
                total += j['harga']
                no_urut += 1
    
    pajak = hitung_pajak(total)
    print("---------------")
    print(f"Total       : Rp {total}")
    print(f"Pajak 11%   : Rp {int(pajak)}")
    print("===============")

def jalankan():
    daftar = menu()
    tampil_menu(daftar)

    pesanan = []

    input_pesanan(pesanan, daftar)

    cetak_struk(pesanan, daftar)

jalankan()
















