print("latihan 1")
angka = int(input("masukan angka:"))
if angka > 10:
    print("angka yang Anda masukkan lebih besar dari 10")
else:
    print("angka yang Anda masukkan 10 atau kurang")

print("latihan 2")
angka = int(input("masukan angka:"))
if angka < 0:
    print("bilangan negatif")
elif angka > 0:
    print("bilangan positif")
else:
    print("bilangan nol")

print("latihan 3")
total_pembelanjaan = int(input("masukan total pembelajaan: "))
if total_pembelanjaan >= 100000:
    print("anda mendapatkan diskon 10%")
    diskon = total_pembelanjaan * 0.10
    harga_diskon = total_pembelanjaan - diskon
    print("total pembayaran: ", harga_diskon)
else: 
    print("anda tidak mendapatkan diskon")

print("latihan 4")
print("masukanlah angka 0-100")
nilai = int(input("masukan grade :"))
if nilai > 100:
    print("nilai tidak boleh lebih dari 100")
elif nilai >= 90:
    print("grade A")
elif nilai >= 80:
    print("grade B")
elif nilai >= 70:
    print("grade C")
elif nilai >= 60:
    print("grade D")
elif nilai < 0:
    print("masukan nilai dengan benar")
else :
    print("grade E")

tahun_lahir = int(input("masukan tahun lahir anda"))
tahun_sekarang = 2023
umur = tahun_sekarang - tahun_lahir
print("umur anda",umur)
if umur < 18:
    print("anda belum bisa membuat KTP")
else :
    print("anda sudah bisa membuat KTP")

tahun_lahir = int(input("masukan tahun lahir anda"))
tahun_sekarang = 2023
umur = tahun_sekarang - tahun_lahir
print("umur anda", umur)
if umur < 18:
    print("kamu masih dibawah umur")
else :
    print("anda sudah bisa membuat sim")
