

list_belanja = []

for i in range(5) :
    nama_barang = input("nama barang? ")

    list_belanja.append(nama_barang)
    
for i in range(len(list_belanja)) :
    print(f"{i+1}. {list_belanja[i]}")



while True:
    hapus_barang = input("Mau Hapus Barang apa? ")
    if hapus_barang in list_belanja:
        list_belanja.remove(hapus_barang)
        break
    else:
        print("barang yang ingin kamu hapus tidak ada dalam daftar")

for i in range(len(list_belanja)):
    print(f"{i+1}. {list_belanja[i]}, ", end="")

print(f"\ntotal barang tersisa : {len(list_belanja)}")




"""
list_belanja.insert(0, nama_barang)

print(list_belanja)

buah = ["apel", "mangga", "jeruk"]
item_dihapus = buah.pop(1)
print(item_dihapus)
print(buah)


"""
