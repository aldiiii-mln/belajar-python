
"""
for i in range(1, 11) :
    if i % 2 == 0:
        print(f"{i} genap")
    else:
        print(f"{i} ganjil")
"""
"""
for i in range(3, 31) :
    if i % 3 == 0:
        print(i)
"""
"""

angka = int(input("Masukkan angka (0 untuk berhenti): "))

while angka != 0:
    
    if angka == 0:
        print("Program selesai")
    elif angka % 2 == 0:
        print(f"{angka} adalah genap")
    elif angka % 2 == 1:
        print(f"{angka} adalah ganjil ")
    else:
        print("Program Selesai")
    angka = int(input("Masukkan angka (0 untuk berhenti): "))

print("Program selesai")
"""

angka = int(input("Masukkan angka (0 untuk berhenti): "))

while angka != 0:
    if angka % 2 == 0:
        print(f"{angka} adalah genap")
    else:
        print(f"{angka} adalah ganjil")
    angka = int(input("Masukkan angka (0 untuk berhenti): "))

print("Program selesai")