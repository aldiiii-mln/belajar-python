umur = int(input("Berapa Umurmu? "))
saldo_cukup = input("Saldo Cukup? (ya/tidak) ")
punya_kartu = input("Punya Kartu? (ya/tidak) ")

if umur >= 18 and (saldo_cukup == "ya" or punya_kartu == "ya") :
    print ("user bisa checkout")



