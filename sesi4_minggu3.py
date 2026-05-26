mahasiswa = [
    {"nama": "Aldi", "nilai": 80, "kota": "Makassar"},
    {"nama": "Wawan", "nilai": 40, "kota": "Makassar"},
    {"nama": "Rifqi", "nilai": 95, "kota": "Makassar"},
    {"nama": "Halimah", "nilai": 65, "kota": "Manado"}
    
]

print("==== DATA MAHASISWA ====")

no_urut = 1
for mhs in mahasiswa:
    
    if mhs['nilai'] >= 90:
        print(f"{no_urut}.      {mhs['nama']} | Nilai: {mhs['nilai']} | Grade: A")
    elif mhs['nilai'] >= 75:
        print(f"{no_urut}.      {mhs['nama']} | Nilai: {mhs['nilai']} | Grade: B")
    elif mhs['nilai'] >= 60:
        print(f"{no_urut}.      {mhs['nama']} | Nilai: {mhs['nilai']} | Grade: C")
    else:
        print(f"{no_urut}.      {mhs['nama']} | Nilai: {mhs['nilai']} | Grade: D")
    no_urut += 1


nilai_total = 0
for mhs in mahasiswa:
    nilai_total += mhs['nilai']

print(f"\nRata-rata kelas : {nilai_total / len(mahasiswa)}")

nilai = []


for mhs in mahasiswa:
    nilai.append(mhs['nilai'])

nilai_tertinggi = max(nilai)

for mhs in mahasiswa:
    if nilai_tertinggi == mhs['nilai']:
        print(f"Nilai tertinggi : {mhs['nama']} ({nilai_tertinggi})")

cari_mahasiswa = input("Cari mahasiswa dari kota: ")

ditemukan = False
for mhs in mahasiswa:
    if cari_mahasiswa == mhs['kota']:
        print(f"- {mhs['nama']}")
        ditemukan = True
    

if not ditemukan:
    print("Tidak ada mahasiswa dari kota tersebut")

for i in nilai:
    print(i)
