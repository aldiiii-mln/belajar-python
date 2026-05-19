nama = input("Siapa Namamu? ")
umur = int(input("Berapa Umurmu? "))
tinggi_badan = int(input("Berapa Tinggi Badanmu(cm)? "))
berat_badan = int(input("Berapa Berat Badanmu(kg)? "))

print("""==== PROFIL KAMU ====
LIST BERIKUT
""")
print(f"Nama        :  {nama}")
print(f"Umur        :  {umur} tahun")
print(f"Tinggi      :  {tinggi_badan} cm")
print(f"Berat       :  {berat_badan} kg")

tinggi_meter = tinggi_badan / 100
bmi = berat_badan / (tinggi_meter ** 2)

print(f"BMI kamu    :  {bmi:.3f}")

if bmi < 18.5:
    kategori = "Kurus"
elif bmi < 25:
    kategori = "Normal"
else:
    kategori = "Gemuk"

print(f"Kategori    :  {kategori}")