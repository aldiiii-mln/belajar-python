nilai_ujian = int(input("Berapa Nilai Ujianmu? (0-100) "))

if nilai_ujian < 0 or nilai_ujian > 100:
    print("Nilai tidak valid!")
elif nilai_ujian >= 90:
    print("Grade A - Luar Biasa!")
elif nilai_ujian >= 75:
    print("Grade B - Bagus!")
elif nilai_ujian >=60:
    print("Grade C - Cukup")
else:
    print("Grade D - Perlu belajar lebih giat")
    
