def hitung_diskon(harga, diskon=10):
    diskon = diskon / 100
    total_diskon = harga * diskon
    total_harga = harga - total_diskon

    return total_harga

print(hitung_diskon(100000))
print(hitung_diskon(100000, 25))

def info_list(data):
    total = sum(data)
    rata = total / len(data)
    terbesar = max(data)
    terkecil = min(data)
    return total, rata, terbesar, terkecil

nilai = [75, 90, 60, 85, 70]
rata, total, terbesar, terkecil = info_list(nilai)
print(f"Total       : {total}")
print(f"Rata-rata   : {rata}")
print(f"Terbeesar   : {terbesar}")
print(f"Terkecil    : {terkecil}")
