print("selamat datang  di dufan")
nama = input ("masukan nama :")
umur = input ("masukan umur :")
print("halo", nama, "selamat menikmati wahana  di dufan")

daftar_wahana = {"1. Biang Lala RP. 13.000", "2. Istana Boneka RP. 10.000", "3. Rumah Kaca RP. 15.000", "4. Roller Coaster RP. 20.000"}
harga = 0
for wahana in daftar_wahana :
    print (wahana)
pilihan = input ("masukan pilihanmu :")
if pilihan == "1":
    print("tiket RP. 13.000")
    harga += 13000
elif pilihan == "2":
    print("tiket RP. 10.000")
    harga += 10000
elif pilihan == "3":
    print("tiket RP. 15.000")
    harga += 15000
elif pilihan == "4":
    print("tiket RP. 20.000")
    harga += 20000
else:
    print("pilihlah wahana yang ada di dalam daftar")

pajak = int(2000)
total = (harga + pajak)
print("total keseluruhan yang harus anda bayar adalah", total)
     
