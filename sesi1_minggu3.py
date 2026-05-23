""" List """

buah = ["apel", "mangga", "jeruk", "pisang", "anggur"]

print(buah[0])
print(buah[-1])

for i in range(len(buah)):
    print(f"{i+1}. {buah[i]}, ", end="")

buah[2] = "semangka"

print("")

for i in buah:
    print(i)

angka = [8, 4, 7, 3, 6, 1]

for i in angka:
    print(f"{i+1}. {angka[3]}")