daftar_kontak = [
    {"nama": "Aldi", "nomor": "0821", "kota": "Makassar"},
    {"nama": "Wawan", "nomor": "0812", "kota": "Bandung"},
    {"nama": "Rifqi", "nomor": "0895", "kota": "Jakarta"}
]

for kontak in daftar_kontak:
    print(f"{kontak['nama']} dengan nomor {kontak['nomor']} dan kota {kontak['kota']}")

ditemukan = False
while True:
    cari_nama = input("Kontak siapa yang anda cari: ")
    

    for kontak in daftar_kontak:
        if cari_nama == kontak['nama']:
            print(f"{kontak['nama']} dengan nomor {kontak['nomor']} dan kota {kontak['kota']}")
            ditemukan = True
            break
    

if not ditemukan:
    print("Kontak tidak ditemukan")