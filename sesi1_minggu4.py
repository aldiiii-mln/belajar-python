def salam():
    return "Selamat datang!"

def luas_persegi(sisi):
    return sisi * sisi

def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return "genap"
    else:
        return "ganjil"

print(salam())
print(luas_persegi(5))
print(cek_ganjil_genap(7))
print(cek_ganjil_genap(4))